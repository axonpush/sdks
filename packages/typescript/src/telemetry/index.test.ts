import http from "node:http";
import type { AddressInfo } from "node:net";
import zlib from "node:zlib";
import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";
import { afterEach, describe, expect, it } from "vitest";
import {
  configureTelemetry,
  genaiSpan,
  recordGenaiContent,
  recordGenaiResponse,
  type TracerProvider,
} from "./index.js";

// A tiny HTTP server standing in for the AxonPush OTLP collector. Captures
// the request headers + (gunzipped) body for every POST to /v1/traces, mirror
// of the Python tests/test_telemetry.py fixture.
interface Capture {
  headers: http.IncomingHttpHeaders;
  body: Buffer;
}

interface MockCollector {
  baseUrl: string;
  requests: Capture[];
  close(): Promise<void>;
}

async function startCollector(): Promise<MockCollector> {
  const requests: Capture[] = [];
  const server = http.createServer((req, res) => {
    const chunks: Buffer[] = [];
    req.on("data", (c) => chunks.push(c as Buffer));
    req.on("end", () => {
      let body = Buffer.concat(chunks);
      if ((req.headers["content-encoding"] ?? "").includes("gzip") && body.length > 0) {
        body = zlib.gunzipSync(body);
      }
      if ((req.url ?? "").replace(/\/+$/, "").endsWith("/v1/traces")) {
        requests.push({ headers: req.headers, body });
        res.writeHead(200, { "Content-Type": "application/x-protobuf" });
        res.end();
      } else {
        res.writeHead(404);
        res.end();
      }
    });
  });
  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  const { port } = server.address() as AddressInfo;
  return {
    baseUrl: `http://127.0.0.1:${port}`,
    requests,
    close: () => new Promise<void>((resolve) => server.close(() => resolve())),
  };
}

// Normalise an OTLP ExportTraceServiceRequest into a flat span list. The
// exporter sends JSON; a protobuf fallback keeps the decoder honest if a
// future exporter version switches encodings.
interface DecodedSpan {
  name: string;
  attributes: Record<string, unknown>;
  events: Array<{ name: string; attributes: Record<string, unknown> }>;
}

function anyValue(v: Record<string, unknown>): unknown {
  for (const k of ["stringValue", "boolValue", "intValue", "doubleValue"]) {
    if (k in v) return v[k];
  }
  const arr = v.arrayValue as { values?: Record<string, unknown>[] } | undefined;
  if (arr?.values) return arr.values.map((x) => anyValue(x));
  return v;
}

function kvMap(
  kvs: Array<{ key: string; value: Record<string, unknown> }> = [],
): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  for (const { key, value } of kvs) out[key] = anyValue(value);
  return out;
}

function decodeSpans(bodies: Buffer[]): DecodedSpan[] {
  const spans: DecodedSpan[] = [];
  for (const body of bodies) {
    if (body.length === 0) continue;
    const text = body.toString("utf8").trimStart();
    if (text[0] !== "{" && text[0] !== "[") continue; // non-JSON encoding: skip
    const doc = JSON.parse(text) as {
      resourceSpans?: Array<{
        scopeSpans?: Array<{
          spans?: Array<{
            name?: string;
            attributes?: Array<{ key: string; value: Record<string, unknown> }>;
            events?: Array<{
              name?: string;
              attributes?: Array<{ key: string; value: Record<string, unknown> }>;
            }>;
          }>;
        }>;
      }>;
    };
    for (const rs of doc.resourceSpans ?? []) {
      for (const ss of rs.scopeSpans ?? []) {
        for (const sp of ss.spans ?? []) {
          spans.push({
            name: sp.name ?? "",
            attributes: kvMap(sp.attributes),
            events: (sp.events ?? []).map((ev) => ({
              name: ev.name ?? "",
              attributes: kvMap(ev.attributes),
            })),
          });
        }
      }
    }
  }
  return spans;
}

interface EmitOptions {
  contentCapture?: "metadata_only" | "redacted" | "full";
  prompt?: string;
  completion?: string;
}

async function emitOneSpan(baseUrl: string, opts: EmitOptions = {}): Promise<void> {
  const handle = await configureTelemetry({
    baseUrl,
    apiKey: "ak_test",
    channelId: "ch_test",
    serviceName: "test-svc",
    contentCapture: opts.contentCapture ?? "metadata_only",
    tracerProvider: freshProvider(),
  });
  try {
    const tracer = handle.tracer("axonpush-test");
    const span = genaiSpan(tracer, {
      operation: "chat",
      requestModel: "gpt-4o",
      system: "openai",
    });
    recordGenaiResponse(span, {
      responseModel: "gpt-4o-2024",
      finishReasons: ["stop"],
      inputTokens: 11,
      outputTokens: 3,
      reasoningTokens: 2,
      cacheReadTokens: 5,
      cacheWriteTokens: 7,
    });
    if (opts.prompt !== undefined || opts.completion !== undefined) {
      recordGenaiContent(span, {
        prompt: opts.prompt,
        completion: opts.completion,
        contentCapture: opts.contentCapture ?? "metadata_only",
      });
    }
    span.end();
    expect(await handle.flush(5000)).toBe(true);
  } finally {
    await handle.shutdown();
  }
}

// Each test passes an explicit provider so it never touches the process-wide
// global (mirrors the Python fixture that hands a fresh TracerProvider).
function freshProvider(): TracerProvider {
  return new NodeTracerProvider() as unknown as TracerProvider;
}

describe("configureTelemetry (OTLP export)", () => {
  let collector: MockCollector | undefined;

  afterEach(async () => {
    if (collector) await collector.close();
    collector = undefined;
  });

  it("exports a GenAI span with semconv attrs and auth/channel headers", async () => {
    collector = await startCollector();
    await emitOneSpan(collector.baseUrl);

    expect(collector.requests.length).toBeGreaterThan(0);
    for (const { headers } of collector.requests) {
      expect(headers["x-api-key"]).toBe("ak_test");
      expect(headers["x-axonpush-channel"]).toBe("ch_test");
    }

    const spans = decodeSpans(collector.requests.map((r) => r.body));
    expect(spans).toHaveLength(1);
    const attrs = spans[0]!.attributes;
    expect(attrs["gen_ai.operation.name"]).toBe("chat");
    expect(attrs["gen_ai.request.model"]).toBe("gpt-4o");
    expect(Number(attrs["gen_ai.usage.input_tokens"])).toBe(11);
    expect(Number(attrs["gen_ai.usage.output_tokens"])).toBe(3);
    expect(Number(attrs["gen_ai.usage.cache_write_input_tokens"])).toBe(7);
  });

  it("metadata_only does not leak prompt text", async () => {
    collector = await startCollector();
    await emitOneSpan(collector.baseUrl, {
      contentCapture: "metadata_only",
      prompt: "secret-ish prompt text",
    });

    for (const { body } of collector.requests) {
      expect(body.toString("utf8")).not.toContain("secret-ish prompt text");
    }
  });

  it("full capture includes the prompt text", async () => {
    collector = await startCollector();
    await emitOneSpan(collector.baseUrl, {
      contentCapture: "full",
      prompt: "secret-ish prompt text",
    });

    const joined = collector.requests.map((r) => r.body.toString("utf8")).join("");
    expect(joined).toContain("secret-ish prompt text");
  });

  it("posts to the /v1/traces endpoint with gzip encoding", async () => {
    collector = await startCollector();
    await emitOneSpan(collector.baseUrl);
    for (const { headers } of collector.requests) {
      expect((headers["content-encoding"] ?? "").includes("gzip")).toBe(true);
    }
  });

  it("is idempotent for the same endpoint/channel", async () => {
    collector = await startCollector();
    const provider = freshProvider();

    const h1 = await configureTelemetry({
      baseUrl: collector.baseUrl,
      apiKey: "ak_test",
      channelId: "ch_test",
      serviceName: "test-svc",
      tracerProvider: provider,
    });
    const h2 = await configureTelemetry({
      baseUrl: collector.baseUrl,
      apiKey: "ak_test",
      channelId: "ch_test",
      serviceName: "test-svc",
      tracerProvider: provider,
    });
    let spans: DecodedSpan[];
    try {
      const span = genaiSpan(h2.tracer("axonpush-test"), {
        operation: "chat",
        requestModel: "gpt-idem",
      });
      span.end();
      expect(await h2.flush(5000)).toBe(true);
      await h1.flush(5000);
      spans = decodeSpans(collector.requests.map((r) => r.body));
    } finally {
      await h2.shutdown();
      await h1.shutdown();
    }
    const matching = spans.filter((s) => s.attributes["gen_ai.request.model"] === "gpt-idem");
    expect(matching).toHaveLength(1);
  });
});
