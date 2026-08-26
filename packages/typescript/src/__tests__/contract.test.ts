import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";
import { resolveSettings } from "../config.js";
import { buildPublishTopic, buildSubscribeTopic, sanitiseSegment } from "../realtime/topics.js";

/**
 * Replays contract/fixtures/*.json, which the server generates by calling its
 * own functions. The MQTT grammar and the AXONPUSH_* surface used to be
 * transcribed into each SDK by hand, which is how the timeout unit and the
 * fail-open default ended up disagreeing across languages.
 */
const FIXTURES = join(
  dirname(fileURLToPath(import.meta.url)),
  "..",
  "..",
  "..",
  "..",
  "contract",
  "fixtures",
);
const read = (name: string) => JSON.parse(readFileSync(join(FIXTURES, name), "utf-8"));

interface PublishCase {
  input: {
    orgId: string;
    envSlug?: string | null;
    appId: string;
    channelId: string;
    eventType: string;
    agentId?: string | null;
  };
  topic: string;
}

interface SubscribeCase {
  input: {
    orgId: string;
    envSlug?: string | null;
    appId?: string | null;
    channelId?: string | null;
    eventType?: string | null;
    agentId?: string | null;
  };
  topic: string;
}

describe("contract: topics", () => {
  const fixture = read("topics.json");

  it.each(fixture.sanitiseCases as { input: string; output: string }[])(
    "sanitises %j",
    ({ input, output }) => {
      expect(sanitiseSegment(input)).toBe(output);
    },
  );

  it.each(fixture.publishCases as PublishCase[])("publishes to $topic", ({ input, topic }) => {
    expect(buildPublishTopic(input)).toBe(topic);
  });

  it.each(fixture.subscribeCases as SubscribeCase[])("subscribes to $topic", ({ input, topic }) => {
    expect(buildSubscribeTopic(input)).toBe(topic);
  });

  it("agrees with the server on segment order and fallbacks", () => {
    expect(fixture.segments).toEqual([
      "prefix",
      "orgId",
      "envSlug",
      "appId",
      "channelId",
      "eventType",
      "agentId",
    ]);
    expect(fixture.publishFallback).toBe("_");
    expect(fixture.subscribeWildcard).toBe("+");
  });
});

describe("contract: environment", () => {
  const fixture = read("env.json");
  const vars = fixture.variables as Record<
    string,
    { default: unknown; unit?: string; aliases?: string[] } | undefined
  >;
  const v = (name: string) => {
    const entry = vars[name];
    if (!entry) throw new Error(`env.json is missing ${name}`);
    return entry;
  };

  const withEnv = <T>(env: Record<string, string | undefined>, fn: () => T): T => {
    const saved: Record<string, string | undefined> = {};
    for (const [k, v] of Object.entries(env)) {
      saved[k] = process.env[k];
      if (v === undefined) delete process.env[k];
      else process.env[k] = v;
    }
    try {
      return fn();
    } finally {
      for (const [k, v] of Object.entries(saved)) {
        if (v === undefined) delete process.env[k];
        else process.env[k] = v;
      }
    }
  };

  const cleared = Object.fromEntries(Object.keys(vars).map((k) => [k, undefined]));

  it("uses the documented defaults", () => {
    const settings = withEnv(cleared, () => resolveSettings({}));
    expect(settings.baseUrl).toBe(v("AXONPUSH_BASE_URL").default);
    expect(settings.maxRetries).toBe(v("AXONPUSH_MAX_RETRIES").default);
    expect(settings.failOpen).toBe(v("AXONPUSH_FAIL_OPEN").default);
    expect(settings.contentCaptureMode).toBe(v("AXONPUSH_CONTENT_CAPTURE").default);
    expect(settings.maxContentLength).toBe(v("AXONPUSH_MAX_CONTENT_LENGTH").default);
  });

  it("reads AXONPUSH_TIMEOUT in the unit the contract states", () => {
    expect(v("AXONPUSH_TIMEOUT").unit).toBe("seconds");
    const settings = withEnv({ ...cleared, AXONPUSH_TIMEOUT: "5" }, () => resolveSettings({}));
    // stored in milliseconds internally, but the variable is seconds on the wire
    expect(settings.timeout).toBe(5_000);
  });

  it("defaults the timeout to the documented number of seconds", () => {
    const settings = withEnv(cleared, () => resolveSettings({}));
    expect(settings.timeout).toBe((v("AXONPUSH_TIMEOUT").default as number) * 1000);
  });

  it("honours AXONPUSH_TENANT_ID and its documented alias", () => {
    expect(v("AXONPUSH_TENANT_ID").aliases).toContain("AXONPUSH_ORG_ID");
    const viaAlias = withEnv({ ...cleared, AXONPUSH_ORG_ID: "org_1" }, () => resolveSettings({}));
    expect(viaAlias.tenantId).toBe("org_1");
  });
});

describe("contract: retry", () => {
  const fixture = read("env.json");

  it("uses the documented backoff ladder", async () => {
    const transport = await import("../_internal/transport.js");
    expect(transport.RETRY_BACKOFF_MS).toEqual(fixture.retry.backoffMs);
  });
});
