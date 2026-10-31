import { describe, expect, it } from "vitest";
import { Transport } from "../_internal/transport.js";
import { AxonPush } from "../client.js";
import { resolveSettings } from "../config.js";
import { APIConnectionError, ServerError } from "../errors.js";
import { BackgroundPublisher } from "../integrations/_publisher.js";
import { redactTelemetry } from "../redaction.js";
import { configureTelemetry } from "../telemetry/index.js";

const settings = () =>
  resolveSettings({
    apiKey: "ak_synthetic",
    baseUrl: "https://example.invalid",
    failOpen: false,
    maxRetries: 0,
    timeout: 20,
  });
describe("infrastructure regression guards", () => {
  it("validates finite bounds", () => {
    for (const maxRetries of [-1, 0.5, Infinity])
      expect(() => resolveSettings({ maxRetries })).toThrow();
    expect(() => resolveSettings({ timeout: 0 })).toThrow();
  });
  it("does not mutate a frozen caller bag", async () => {
    const t = new Transport(settings());
    expect(await t.invoke(async () => ({ data: "ok" }), Object.freeze({}))).toBe("ok");
  });
  it("cancels a stalled body within the invocation budget", async () => {
    const t = new Transport(settings());
    await expect(
      t.invoke(async (args) =>
        args.client.get({
          url: "/test",
          signal: args.signal,
          fetch: async (request: Request) =>
            new Response(
              new ReadableStream({
                start(controller) {
                  request.signal.addEventListener(
                    "abort",
                    () => controller.error(request.signal.reason),
                    { once: true },
                  );
                },
              }),
              { headers: { "content-type": "application/json" } },
            ),
        }),
      ),
    ).rejects.toBeInstanceOf(APIConnectionError);
  });
  it("never swallows caller cancellation", async () => {
    const c = new AbortController();
    c.abort(new Error("caller stopped"));
    const t = new Transport({ ...settings(), failOpen: true });
    await expect(
      t.invoke(async () => ({ data: "unreachable" }), { signal: c.signal }),
    ).rejects.toThrow("caller stopped");
  });
  it("does not retry a non-idempotent creation after a lost response", async () => {
    const t = new Transport({ ...settings(), timeout: 1000, maxRetries: 3 });
    let attempts = 0;
    await expect(
      t.invoke(
        async (args) =>
          args.client.post({
            ...args,
            url: "/apps",
            fetch: async () => {
              attempts++;
              throw new TypeError("lost response");
            },
          }),
        { body: { name: "synthetic" } },
      ),
    ).rejects.toBeInstanceOf(APIConnectionError);
    expect(attempts).toBe(1);
  });
  it("keeps retry identity stable", async () => {
    const c = new AxonPush({ ...settings(), timeout: 1000, maxRetries: 1 });
    const bodies: any[] = [];
    await c.invoke(
      async (args) => {
        await args.requestValidator?.({ method: "POST", url: "/event", body: args.body });
        bodies.push(args.body);
        if (bodies.length === 1) throw new ServerError("retry");
        return { data: "ok" };
      },
      { body: { dedupKey: "same" } },
    );
    expect(bodies[0]).toEqual(bodies[1]);
  });
  it("previews256 Unicode codepoints and independently removes secrets", () => {
    const result = redactTelemetry(
      { prompt: "😀".repeat(300), apiKey: "synthetic" },
      resolveSettings({ contentCaptureMode: "redacted" }),
    );
    expect(result.prompt).toBe(`${"😀".repeat(256)}…[REDACTED_PREVIEW]`);
    expect(result.apiKey).toBe("[REDACTED]");
  });
  it("bounds admission waiters and resolves them on close", async () => {
    const pub = new BackgroundPublisher(
      { events: { publish: () => new Promise(() => {}) } } as any,
      { queueSize: 1, overflowPolicy: "block" },
    );
    const params = { identifier: "test", channelId: "test", payload: {} };
    pub.submit(params);
    pub.submit(params);
    const waiter = pub.submitAsync(params);
    expect(await pub.submitAsync(params)).toBe(false);
    await pub.close(0);
    expect(await waiter).toBe(false);
  });
  it("registers processors per provider and shares actual handles", async () => {
    const counts = [0, 0];
    const providers = counts.map((_, i) => ({
      getTracer: () => ({}),
      addSpanProcessor: () => {
        counts[i] = (counts[i] ?? 0) + 1;
      },
    }));
    const opts = { baseUrl: "https://example.invalid", apiKey: "synthetic" };
    const first = await configureTelemetry({ ...opts, tracerProvider: providers[0] as any });
    const shared = await configureTelemetry({ ...opts, tracerProvider: providers[0] as any });
    const second = await configureTelemetry({ ...opts, tracerProvider: providers[1] as any });
    expect(counts).toEqual([1, 1]);
    await expect(
      configureTelemetry({ ...opts, apiKey: "other", tracerProvider: providers[0] as any }),
    ).rejects.toThrow("different credentials");
    await first.shutdown();
    await shared.shutdown();
    const renewed = await configureTelemetry({ ...opts, tracerProvider: providers[0] as any });
    expect(counts).toEqual([2, 1]);
    await renewed.shutdown();
    await second.shutdown();
  });
});
