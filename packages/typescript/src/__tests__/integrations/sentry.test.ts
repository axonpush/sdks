import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { buildDsn, installSentry, sentryProjectId } from "../../integrations/sentry.js";

const ENV_KEYS = ["AXONPUSH_PUBLIC_TOKEN", "AXONPUSH_CHANNEL_ID", "AXONPUSH_HOST"] as const;
let saved: Record<string, string | undefined> = {};

beforeEach(() => {
  saved = {};
  for (const k of ENV_KEYS) {
    saved[k] = process.env[k];
    delete process.env[k];
  }
});

afterEach(() => {
  for (const k of ENV_KEYS) {
    if (saved[k] === undefined) delete process.env[k];
    else process.env[k] = saved[k];
  }
});

describe("sentryProjectId", () => {
  it("derives an integer from the leading hex of the channel id", () => {
    expect(sentryProjectId("0a1b2c3d-4e5f-6789-abcd-ef0123456789")).toBe(0x0a1b2c3d);
  });

  it("falls back to 1", () => {
    expect(sentryProjectId(undefined)).toBe(1);
    expect(sentryProjectId("zzz")).toBe(1);
    expect(sentryProjectId("00000000-0000")).toBe(1);
  });
});

describe("buildDsn", () => {
  it("uses https for production hosts and an integer project id", () => {
    expect(buildDsn("pt_tok", "0a1b2c3d-0000", "api.axonpush.xyz")).toBe(
      `https://pt_tok@api.axonpush.xyz/${0x0a1b2c3d}`,
    );
  });

  it("uses http for localhost", () => {
    expect(buildDsn("pt_tok", undefined, "localhost:3000")).toBe("http://pt_tok@localhost:3000/1");
  });

  it("rejects API keys", () => {
    expect(() => buildDsn("ak_key", "ch", "api.axonpush.xyz")).toThrow(/public ingest token/);
  });
});

describe("installSentry", () => {
  it("forwards a built dsn to sentry.init", () => {
    const sentry = { init: vi.fn() };
    installSentry(sentry, {
      publicToken: "pt_tok",
      channelId: "0a1b2c3d-0000",
      host: "api.axonpush.xyz",
      environment: "test",
      release: "v1",
    });
    expect(sentry.init).toHaveBeenCalledTimes(1);
    const opts = sentry.init.mock.calls[0]?.[0] as Record<string, unknown>;
    expect(opts.dsn).toBe(`https://pt_tok@api.axonpush.xyz/${0x0a1b2c3d}`);
    expect(opts.environment).toBe("test");
    expect(opts.release).toBe("v1");
    expect(opts.publicToken).toBeUndefined();
  });

  it("reads the public token from the environment", () => {
    process.env.AXONPUSH_PUBLIC_TOKEN = "pt_env";
    const sentry = { init: vi.fn() };
    installSentry(sentry, { environment: "test" });
    expect((sentry.init.mock.calls[0]?.[0] as Record<string, unknown>).dsn).toBe(
      "https://pt_env@api.axonpush.xyz/1",
    );
  });

  it("throws when neither dsn nor publicToken is supplied", () => {
    const sentry = { init: vi.fn() };
    expect(() => installSentry(sentry)).toThrow(/publicToken/);
  });

  it("refuses apiKey", () => {
    const sentry = { init: vi.fn() };
    expect(() => installSentry(sentry, { apiKey: "ak_x", channelId: "ch" })).toThrow(/apiKey/);
    expect(sentry.init).not.toHaveBeenCalled();
  });

  it("respects an explicit dsn override", () => {
    const sentry = { init: vi.fn() };
    installSentry(sentry, { dsn: "https://x@host/9" });
    expect(sentry.init).toHaveBeenCalledTimes(1);
    expect((sentry.init.mock.calls[0]?.[0] as Record<string, unknown>).dsn).toBe(
      "https://x@host/9",
    );
  });
});
