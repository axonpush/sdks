import { runInNewContext } from "node:vm";
import { describe, expect, it } from "vitest";
import type { AxonPush } from "../../client.js";
import {
  boundedExceptionContext,
  exceptionAttributes,
  isNativeError,
  MAX_EXCEPTION_MESSAGE_LENGTH,
  MAX_EXCEPTION_STACK_LENGTH,
} from "../../integrations/_exceptions.js";
import { AxonPushCallbackHandler } from "../../integrations/langchain.js";
import type { PublishParams } from "../../resources/events.js";

describe("bounded exception diagnostics", () => {
  it("copies serialized error context without invoking prototype setters", () => {
    const err = JSON.parse(
      '{"type":"Error","message":"fixture","stack":"Error: fixture","__proto__":{"injected":true}}',
    );
    const context = boundedExceptionContext({ err });
    const copy = context.err as Record<string, unknown>;
    expect(Object.getPrototypeOf(copy)).toBe(Object.prototype);
    expect(Object.hasOwn(copy, "__proto__")).toBe(true);
    expect(copy.injected).toBeUndefined();
  });

  it("does not mistake an arbitrary business stack property for an exception", () => {
    expect(exceptionAttributes({ stack: "worker-tier", pending: 3 })).toEqual({});
    expect(isNativeError({ name: "Error", message: "record", stack: "Error: record" })).toBe(false);
  });

  it("recognizes a native error from another realm", () => {
    const error = runInNewContext("new TypeError('cross-realm fixture')");
    expect(error instanceof Error).toBe(false);
    expect(isNativeError(error)).toBe(true);
    expect(exceptionAttributes(error)).toMatchObject({
      "exception.type": "TypeError",
      "exception.message": "cross-realm fixture",
    });
  });

  it("publishes framework failure metadata when a native stack getter throws", async () => {
    const published: PublishParams[] = [];
    const client = {
      events: {
        async publish(params: PublishParams) {
          published.push(params);
        },
      },
    } as unknown as AxonPush;
    const handler = new AxonPushCallbackHandler({ client, channelId: "synthetic" });
    const error = new TypeError("actual application failure");
    Object.defineProperty(error, "stack", {
      get() {
        throw new Error("formatter unavailable");
      },
    });
    expect(() => handler.handleChainError(error, "synthetic-run")).not.toThrow();
    await Promise.resolve();
    expect(published).toHaveLength(1);
    const payload = published[0]!.payload as Record<string, unknown>;
    expect(payload.error).toBe("actual application failure");
    expect(payload.attributes).toEqual({
      "exception.type": "TypeError",
      "exception.message": "actual application failure",
    });
  });

  it("bounds two-megabyte stacks and duplicate serialized fields without mutating input", () => {
    const stack = `Error: fixture\n    at run (/app/worker.ts:42:9)\n${"x".repeat(2 * 1024 * 1024)}`;
    const message = "m".repeat(8192);
    const error = Object.assign(new Error(message), { stack });
    const attributes = exceptionAttributes(error);
    expect(attributes["exception.stacktrace"]!.length).toBeLessThanOrEqual(
      MAX_EXCEPTION_STACK_LENGTH,
    );
    expect(attributes["exception.stacktrace"]).toContain("diagnostic truncated");
    expect(attributes["exception.stacktrace"]).toContain("/app/worker.ts:42:9");
    expect(attributes["exception.message"]!.length).toBeLessThanOrEqual(
      MAX_EXCEPTION_MESSAGE_LENGTH,
    );
    const cause = { type: "Error", message, stack };
    const serialized = { type: "Error", message, stack, custom: "preserved", cause };
    const bounded = boundedExceptionContext({ err: serialized, "exception.stacktrace": stack });
    expect((bounded.err as Record<string, string>).stack!.length).toBeLessThanOrEqual(
      MAX_EXCEPTION_STACK_LENGTH,
    );
    expect((bounded.err as Record<string, string>).message!.length).toBeLessThanOrEqual(
      MAX_EXCEPTION_MESSAGE_LENGTH,
    );
    expect((bounded.err as Record<string, string>).custom).toBe("preserved");
    expect(
      ((bounded.err as Record<string, unknown>).cause as Record<string, string>).stack!.length,
    ).toBeLessThanOrEqual(MAX_EXCEPTION_STACK_LENGTH);
    expect((bounded["exception.stacktrace"] as string).length).toBeLessThanOrEqual(
      MAX_EXCEPTION_STACK_LENGTH,
    );
    expect(serialized.stack).toBe(stack);
    expect(serialized.message).toBe(message);
  });
});
