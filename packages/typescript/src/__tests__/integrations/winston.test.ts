import { describe, expect, it } from "vitest";
import type { AxonPush } from "../../client.js";
import { createAxonPushWinstonTransport } from "../../integrations/winston.js";
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

interface AxonPushTransport {
  log(info: Record<string, unknown>, cb: () => void): void;
  flushAxonPush(timeoutMs?: number): Promise<void>;
  close(): void;
}

describe("winston transport", () => {
  it("keeps non-enumerable native Error diagnostics", async () => {
    const { client, published } = makeFakeClient();
    const transport = (await createAxonPushWinstonTransport({
      client,
      channelId: "ch-1",
    })) as AxonPushTransport;
    const error = Object.assign(new TypeError("diagnostic failure"), { level: "error" });
    error.stack = "TypeError: diagnostic failure\n    at run (/app/worker.ts:42:9)";
    await new Promise<void>((resolve) =>
      transport.log(error as unknown as Record<string, unknown>, resolve),
    );
    await transport.flushAxonPush(2000);
    transport.close();
    const payload = published[0]!.payload as Record<string, unknown>;
    expect(payload.body).toBe("diagnostic failure");
    expect(payload.attributes).toMatchObject({
      "exception.type": "TypeError",
      "exception.message": "diagnostic failure",
      "exception.stacktrace": error.stack,
    });
  });

  it("logs a record and publishes an app.log event", async () => {
    const { client, published } = makeFakeClient();
    const transport = (await createAxonPushWinstonTransport({
      client,
      channelId: "ch-1",
      serviceName: "winston-svc",
    })) as AxonPushTransport;

    await new Promise<void>((resolve) => {
      transport.log({ level: "error", message: "db down", tenant: "acme" }, resolve);
    });
    await transport.flushAxonPush(2000);

    expect(published).toHaveLength(1);
    const event = published[0]!;
    expect(event.channelId).toBe("ch-1");
    expect(event.eventType).toBe("app.log");
    expect(event.identifier).toBe("winston");
    const payload = event.payload as Record<string, unknown>;
    expect(payload.severityText).toBe("ERROR");
    expect(payload.severityNumber).toBe(17);
    expect(payload.body).toBe("db down");
    const attrs = payload.attributes as Record<string, unknown>;
    expect(attrs.tenant).toBe("acme");
    const resource = payload.resource as Record<string, unknown>;
    expect(resource["service.name"]).toBe("winston-svc");

    transport.close();
  });

  it("maps winston level names to OTel severity", async () => {
    const { client, published } = makeFakeClient();
    const transport = (await createAxonPushWinstonTransport({
      client,
      channelId: "ch-1",
    })) as AxonPushTransport;

    const cases: Array<[string, number, string]> = [
      ["debug", 5, "DEBUG"],
      ["info", 9, "INFO"],
      ["warn", 13, "WARN"],
      ["error", 17, "ERROR"],
      ["fatal", 21, "FATAL"],
    ];
    for (const [level] of cases) {
      await new Promise<void>((resolve) => {
        transport.log({ level, message: `msg_${level}` }, resolve);
      });
    }
    await transport.flushAxonPush(2000);

    expect(published).toHaveLength(cases.length);
    cases.forEach(([, expectedNum, expectedText], i) => {
      const p = published[i]!.payload as Record<string, unknown>;
      expect(p.severityNumber).toBe(expectedNum);
      expect(p.severityText).toBe(expectedText);
    });

    transport.close();
  });
});
