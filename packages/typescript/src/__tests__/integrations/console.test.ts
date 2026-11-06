import { afterEach, describe, expect, it, vi } from "vitest";
import type { AxonPush } from "../../client.js";
import { MAX_EXCEPTION_STACK_LENGTH } from "../../integrations/_exceptions.js";
import { setupConsoleCapture } from "../../integrations/console.js";
import type { PublishParams } from "../../resources/events.js";

function makeFakeClient() {
  const published: PublishParams[] = [];
  const client = {
    events: {
      async publish(p: PublishParams) {
        published.push(p);
        return undefined;
      },
    },
  } as unknown as AxonPush;
  return { client, published };
}

describe("console capture", () => {
  it("bounds a large native Error before the publisher receives it", async () => {
    const { client, published } = makeFakeClient();
    console.error = vi.fn();
    const error = new Error("fixture");
    error.stack = `Error: fixture\n    at run (/app/worker.ts:42:9)\n${"x".repeat(2 * 1024 * 1024)}`;
    const handle = setupConsoleCapture({ client, channelId: "ch-1", maxBodyLength: 16 });
    try {
      console.error(error);
      await handle.flush(2000);
    } finally {
      await handle.close();
    }
    const payload = published[0]!.payload as Record<string, unknown>;
    const attributes = payload.attributes as Record<string, string>;
    expect(attributes["exception.stacktrace"]!.length).toBeLessThanOrEqual(
      MAX_EXCEPTION_STACK_LENGTH,
    );
    expect(attributes["exception.stacktrace"]).toContain("diagnostic truncated");
    expect(payload.body).toBe("Error: fixture");
  });

  it("preserves ordinary JSON bodies even when they have stack or error-like fields", async () => {
    const { client, published } = makeFakeClient();
    console.error = vi.fn();
    const records = [
      { stack: "worker-tier", pending: 3 },
      {
        name: "TypeError",
        message: "a structured record",
        stack: "TypeError: a structured record\n    at run (/app/worker.ts:42:9)",
        pending: 3,
      },
    ];
    const handle = setupConsoleCapture({ client, channelId: "ch-1" });
    try {
      for (const record of records) console.error(record);
      await handle.flush(2000);
    } finally {
      await handle.close();
    }
    expect(published).toHaveLength(2);
    for (let index = 0; index < records.length; index++) {
      expect(
        JSON.parse((published[index]!.payload as Record<string, unknown>).body as string),
      ).toEqual(records[index]);
    }
    expect((published[0]!.payload as Record<string, unknown>).attributes).not.toHaveProperty(
      "exception.stacktrace",
    );
  });

  it("preserves an Error's diagnostic stack instead of serializing it as an empty object", async () => {
    const { client, published } = makeFakeClient();
    console.error = vi.fn();
    const error = new TypeError("diagnostic failure");
    error.stack = "TypeError: diagnostic failure\n    at failedOperation (/app/worker.ts:42:9)";
    const handle = setupConsoleCapture({ client, channelId: "ch-1" });
    try {
      console.error("operation failed", error);
      await handle.flush(2000);
    } finally {
      await handle.close();
    }
    const payload = published[0]!.payload as Record<string, unknown>;
    expect(payload.body).toBe("operation failed TypeError: diagnostic failure");
    expect(payload.attributes).toMatchObject({
      "exception.type": "TypeError",
      "exception.message": "diagnostic failure",
      "exception.stacktrace": error.stack,
    });
  });

  const origLog = console.log;
  const origInfo = console.info;
  const origWarn = console.warn;
  const origError = console.error;
  const origDebug = console.debug;

  afterEach(() => {
    console.log = origLog;
    console.info = origInfo;
    console.warn = origWarn;
    console.error = origError;
    console.debug = origDebug;
  });

  it("captures console.log calls as agent.log events", async () => {
    const { client, published } = makeFakeClient();
    console.log = vi.fn();
    const handle = setupConsoleCapture({ client, channelId: "ch-1" });
    try {
      console.log("agent starting");
      console.log("step 1: loaded tools");
      await handle.flush(2000);
    } finally {
      handle.unpatch();
      await handle.close();
    }

    expect(published).toHaveLength(2);
    expect(published[0]?.eventType).toBe("agent.log");
    expect(published[0]?.channelId).toBe("ch-1");
    const p0 = published[0]?.payload as Record<string, unknown>;
    expect(p0.body).toBe("agent starting");
    expect(p0.severityText).toBe("INFO");
  });

  it("maps severity by console method", async () => {
    const { client, published } = makeFakeClient();
    console.log = vi.fn();
    console.warn = vi.fn();
    console.error = vi.fn();
    console.debug = vi.fn();
    const handle = setupConsoleCapture({ client, channelId: "ch-1" });
    try {
      console.debug("d");
      console.log("l");
      console.warn("w");
      console.error("e");
      await handle.flush(2000);
    } finally {
      handle.unpatch();
      await handle.close();
    }

    const severities = published.map((p) => (p.payload as Record<string, unknown>).severityText);
    expect(severities).toEqual(["DEBUG", "INFO", "WARN", "ERROR"]);
  });

  it("uses app.log when source is 'app'", async () => {
    const { client, published } = makeFakeClient();
    console.log = vi.fn();
    const handle = setupConsoleCapture({ client, channelId: "ch-1", source: "app" });
    try {
      console.log("hello");
      await handle.flush(2000);
    } finally {
      handle.unpatch();
      await handle.close();
    }
    expect(published).toHaveLength(1);
    expect(published[0]?.eventType).toBe("app.log");
  });

  it("unpatch restores the original console methods", () => {
    const { client } = makeFakeClient();
    const origSpy = vi.fn();
    console.log = origSpy;
    const handle = setupConsoleCapture({ client, channelId: "ch-1" });
    expect(console.log).not.toBe(origSpy);
    handle.unpatch();
    expect(console.log).toBe(origSpy);
    void handle.close();
  });

  it("numeric channelId is coerced to string with a deprecation warning", async () => {
    const { client, published } = makeFakeClient();
    console.log = vi.fn();
    const warnSpy = vi.spyOn(console, "warn");
    const handle = setupConsoleCapture({ client, channelId: 7 });
    try {
      console.log("hello");
      await handle.flush(2000);
    } finally {
      handle.unpatch();
      await handle.close();
    }
    expect(published[0]?.channelId).toBe("7");
    expect(warnSpy.mock.calls.some((c) => String(c[0]).includes("deprecated"))).toBe(true);
    warnSpy.mockRestore();
  });

  it("does not loop console.warn calls produced inside the publisher path", async () => {
    const failingClient = {
      events: {
        async publish() {
          // simulate a failure to provoke an internal sdkLogger.warn → console
          throw new Error("simulated");
        },
      },
    } as unknown as AxonPush;

    console.log = vi.fn();
    console.warn = vi.fn();
    const handle = setupConsoleCapture({ client: failingClient, channelId: "ch-1" });
    try {
      console.log("trigger");
      await handle.flush(2000);
    } finally {
      handle.unpatch();
      await handle.close();
    }
    // The test asserts no infinite loop / no crash; the absence of a hang
    // is the contract.
    expect(true).toBe(true);
  });
});
