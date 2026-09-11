/**
 * OTel-native telemetry for AxonPush (TypeScript).
 *
 * Emits real OTLP over HTTP to the AxonPush ingest endpoint
 * (`POST {base}/v1/traces`), routed by the `X-Axonpush-Channel` header and
 * authed by `X-API-Key`. Spans follow the GenAI semantic conventions so they
 * are portable to any OTLP backend, not just AxonPush.
 *
 * Unlike `@axonpush/sdk/integrations/otel` (the `AxonPushSpanExporter`, which
 * converts spans to proprietary `app.span` events through the events API),
 * this module reuses the application's own `TracerProvider` and attaches a
 * `BatchSpanProcessor` with an OTLP/HTTP exporter that ships spans directly.
 *
 * Requires the OpenTelemetry SDK peers (loaded lazily so the base SDK builds
 * and runs without OTel installed):
 *
 *   npm install @opentelemetry/api @opentelemetry/sdk-trace-node \
 *     @opentelemetry/exporter-trace-otlp-http @opentelemetry/resources
 *
 * Usage:
 *
 *   import { configureTelemetry, genaiSpan, recordGenaiResponse }
 *     from "@axonpush/sdk/telemetry";
 *
 *   const handle = await configureTelemetry({ serviceName: "my-agent", environment: "prod" });
 *   const tracer = handle.tracer();
 *   const span = genaiSpan(tracer, { operation: "chat", requestModel: "gpt-4o", system: "openai" });
 *   try {
 *     recordGenaiResponse(span, { inputTokens: 12, outputTokens: 48 });
 *   } finally {
 *     span.end();
 *   }
 *   await handle.flush(); // serverless: call per invocation
 *
 * Double-instrumentation note: if a framework integration (LangChain, Mastra,
 * the Vercel AI middleware, `AxonPushSpanExporter`, ...) already produces
 * GenAI spans or events for the same call, do NOT also wrap that call with
 * `genaiSpan`/`recordGenai*` — you would emit the operation twice. Pick one
 * plane: native OTLP via this module, or the events plane via the
 * integrations. `configureTelemetry` attaches to an existing SDK
 * `TracerProvider` when present and never replaces it, so an app that already
 * owns OpenTelemetry keeps its own instrumentation and only gains the AxonPush
 * exporter.
 *
 * On serverless (AWS Lambda, Cloud Functions, Azure Functions) the batch
 * processor's exit-time flush is unreliable because the container is frozen
 * between invocations — call `handle.flush()` at the end of each invocation
 * (or wrap the handler with `flushAfterInvocation`).
 */

import { type ResolvedSettings, resolveSettings } from "../config.js";
import { detectServerless, flushAfterInvocation } from "../integrations/_publisher.js";
import { logger as sdkLogger } from "../logger.js";
import { redactTelemetry } from "../redaction.js";

export { flushAfterInvocation };

// OTel is an optional peer. We deliberately avoid *any* static import of the
// `@opentelemetry/*` packages (even type-only) so the base SDK compiles and
// runs when they are not installed — matching the convention in
// `integrations/otel.ts`. The runtime types below are minimal structural
// stand-ins for the OTel API surface we touch; the real modules are pulled in
// lazily via dynamic `import()` inside {@link configureTelemetry}.

/** Minimal shape we rely on from an OTel `Span` (avoids a hard type dep). */
export interface TelemetrySpan {
  setAttribute(key: string, value: unknown): unknown;
  addEvent(name: string, attributes?: Record<string, unknown>): unknown;
  end(): void;
}

/** Minimal `Tracer`: enough to start a span with kind + attributes. */
export interface Tracer {
  startSpan(
    name: string,
    options?: { kind?: number; attributes?: Record<string, unknown> },
  ): TelemetrySpan;
}

/** Minimal `TracerProvider`: yields tracers by name. */
export interface TracerProvider {
  getTracer(name: string, version?: string): Tracer;
}

type ContentCaptureMode = ResolvedSettings["contentCaptureMode"];

export interface ConfigureTelemetryOptions {
  baseUrl?: string;
  apiKey?: string;
  channelId?: string;
  serviceName?: string;
  environment?: string;
  serviceVersion?: string;
  tracerProvider?: TracerProvider;
  contentCapture?: ContentCaptureMode;
  redactKeys?: string[];
}

/** Handle over the span processor installed by {@link configureTelemetry}. */
export interface TelemetryHandle {
  /**
   * Block until buffered spans are exported, or until `timeoutMs`. Resolves
   * `true` when the flush completed. Call at the end of each invocation on
   * serverless platforms where the container is frozen between calls.
   */
  flush(timeoutMs?: number): Promise<boolean>;
  /** Flush and stop the processor. Idempotent. */
  shutdown(): Promise<void>;
  /** Return a tracer from the underlying provider. */
  tracer(name?: string): Tracer;
}

//: Guards against attaching our processor to the same (endpoint, channel)
//: twice — e.g. when `configureTelemetry` is called from multiple modules
//: that all reuse the global provider.
const INSTALLED = new Set<string>();

interface ProviderLike extends TracerProvider {
  addSpanProcessor?(processor: OtelProcessor): void;
}

/**
 * Install an OTLP span processor that ships GenAI spans to AxonPush.
 *
 * Resolution order for `baseUrl` / `apiKey` / `channelId` is argument, then
 * the matching `AXONPUSH_*` environment variable.
 *
 * Provider selection:
 *   - `tracerProvider` given — attach to it.
 *   - the global provider is already a real SDK provider — attach to it (never
 *     replace).
 *   - otherwise — create a `NodeTracerProvider` with a resource describing the
 *     service and register it as the global provider.
 *
 * The returned {@link TelemetryHandle} carries the `contentCapture` /
 * `redactKeys` policy consumed by {@link recordGenaiContent}.
 */
export async function configureTelemetry(
  options: ConfigureTelemetryOptions = {},
): Promise<TelemetryHandle> {
  const otel = await loadOtel();

  const settings = resolveSettings({
    baseUrl: options.baseUrl,
    apiKey: options.apiKey,
    contentCaptureMode: options.contentCapture,
    redactKeys: options.redactKeys,
  });
  const root = settings.baseUrl.replace(/\/+$/, "");
  const endpoint = `${root}/v1/traces`;
  const channelId = options.channelId ?? envChannelId();

  const provider = resolveProvider(otel, options);
  const processor = installProcessor(otel, provider as ProviderLike, {
    endpoint,
    apiKey: settings.apiKey,
    channelId,
  });

  const serverless = detectServerless();
  if (serverless) {
    sdkLogger.info(
      `axonpush telemetry detected a serverless host (${serverless}). The batch ` +
        "processor's exit-time flush is unreliable when the container is frozen — " +
        "call handle.flush() at the end of each invocation.",
    );
  }

  return {
    flush: (timeoutMs = 2000): Promise<boolean> => forceFlush(processor, timeoutMs),
    shutdown: (): Promise<void> => processor.shutdown(),
    tracer: (name = "axonpush"): Tracer => provider.getTracer(name),
  };
}

function envChannelId(): string | undefined {
  if (typeof process === "undefined" || !process.env) return undefined;
  const v = process.env.AXONPUSH_CHANNEL_ID;
  return v && v.length > 0 ? v : undefined;
}

// --- lazy OTel loading ------------------------------------------------------

// Structural stand-ins for the loaded OTel modules. We never statically import
// their real types (they are optional peers), so these describe only the
// members we call. Dynamic `import()` returns `unknown`-typed namespaces cast
// to these shapes.
interface OtelProcessor {
  forceFlush(): Promise<void>;
  shutdown(): Promise<void>;
}

interface Otel {
  trace: {
    getTracerProvider(): TracerProvider;
    setGlobalTracerProvider(provider: TracerProvider): boolean;
  };
  Resource: new (attrs: Record<string, string>) => unknown;
  NodeTracerProvider: new (config?: { resource?: unknown }) => TracerProvider;
  BatchSpanProcessor: new (exporter: unknown) => OtelProcessor;
  OTLPTraceExporter: new (config: {
    url: string;
    headers: Record<string, string>;
    compression?: string;
  }) => unknown;
}

// Specifiers are held in variables so TS treats them as runtime `import()` of
// an unknown module (returning `any`) rather than resolving the optional peer
// at compile time. This keeps the base SDK type-checking without OTel present.
async function importOptional(specifier: string): Promise<Record<string, unknown>> {
  return (await import(specifier)) as Record<string, unknown>;
}

async function loadOtel(): Promise<Otel> {
  let api: Record<string, unknown>;
  let base: Record<string, unknown>;
  let node: Record<string, unknown>;
  let resources: Record<string, unknown>;
  let exporter: Record<string, unknown>;
  try {
    [api, base, node, resources, exporter] = await Promise.all([
      importOptional("@opentelemetry/api"),
      importOptional("@opentelemetry/sdk-trace-base"),
      importOptional("@opentelemetry/sdk-trace-node"),
      importOptional("@opentelemetry/resources"),
      importOptional("@opentelemetry/exporter-trace-otlp-http"),
    ]);
  } catch {
    throw new Error(
      "@axonpush/sdk/telemetry requires the OpenTelemetry SDK. Install it with: " +
        "npm install @opentelemetry/api @opentelemetry/sdk-trace-node " +
        "@opentelemetry/exporter-trace-otlp-http @opentelemetry/resources",
    );
  }
  return {
    trace: api.trace as Otel["trace"],
    Resource: resources.Resource as Otel["Resource"],
    NodeTracerProvider: node.NodeTracerProvider as Otel["NodeTracerProvider"],
    BatchSpanProcessor: base.BatchSpanProcessor as Otel["BatchSpanProcessor"],
    OTLPTraceExporter: exporter.OTLPTraceExporter as Otel["OTLPTraceExporter"],
  };
}

function resolveProvider(otel: Otel, options: ConfigureTelemetryOptions): TracerProvider {
  if (options.tracerProvider) return options.tracerProvider;

  const current = unwrapDelegate(otel.trace.getTracerProvider());
  if (isSdkProvider(current)) return current;

  const attrs: Record<string, string> = {};
  if (options.serviceName) attrs["service.name"] = options.serviceName;
  if (options.environment) attrs["deployment.environment.name"] = options.environment;
  if (options.serviceVersion) attrs["service.version"] = options.serviceVersion;

  const resource = new otel.Resource(attrs);
  const provider = new otel.NodeTracerProvider({ resource });
  otel.trace.setGlobalTracerProvider(provider);
  return provider;
}

function unwrapDelegate(provider: TracerProvider): TracerProvider {
  const proxy = provider as { getDelegate?: () => TracerProvider };
  return typeof proxy.getDelegate === "function" ? proxy.getDelegate() : provider;
}

function isSdkProvider(provider: TracerProvider): provider is ProviderLike {
  return typeof (provider as ProviderLike).addSpanProcessor === "function";
}

function installProcessor(
  otel: Otel,
  provider: ProviderLike,
  cfg: { endpoint: string; apiKey: string | undefined; channelId: string | undefined },
): OtelProcessor {
  const headers: Record<string, string> = {};
  if (cfg.apiKey) headers["X-API-Key"] = cfg.apiKey;
  if (cfg.channelId) headers["X-Axonpush-Channel"] = cfg.channelId;

  const exporter = new otel.OTLPTraceExporter({
    url: cfg.endpoint,
    headers,
    compression: "gzip",
  });
  const processor = new otel.BatchSpanProcessor(exporter);

  const key = `${cfg.endpoint}|${cfg.channelId ?? ""}`;
  if (INSTALLED.has(key)) {
    sdkLogger.debug(
      `axonpush telemetry already installed for ${key}; skipping duplicate processor`,
    );
  } else if (typeof provider.addSpanProcessor === "function") {
    provider.addSpanProcessor(processor);
    INSTALLED.add(key);
  }
  return processor;
}

function forceFlush(processor: OtelProcessor, timeoutMs: number): Promise<boolean> {
  return new Promise<boolean>((resolve) => {
    const timer = setTimeout(() => resolve(false), timeoutMs);
    processor
      .forceFlush()
      .then(() => {
        clearTimeout(timer);
        resolve(true);
      })
      .catch(() => {
        clearTimeout(timer);
        resolve(false);
      });
  });
}

// --- GenAI semantic-convention helpers -------------------------------------

/** `SpanKind.CLIENT` from `@opentelemetry/api` (stable across versions). */
const SPAN_KIND_CLIENT = 3;

export interface GenaiSpanOptions {
  operation: string;
  requestModel: string;
  system?: string;
  agentName?: string;
  name?: string;
}

/**
 * Start a CLIENT span for a GenAI operation, named per semconv.
 *
 * The span name defaults to `"{operation} {requestModel}"`. Sets
 * `gen_ai.operation.name`, `gen_ai.request.model` and, when provided,
 * `gen_ai.system` / `gen_ai.provider.name` and `gen_ai.agent.name`. Unlike the
 * Python context manager, the caller owns the span lifecycle: call `span.end()`
 * (typically in a `finally`).
 */
export function genaiSpan(tracer: Tracer, options: GenaiSpanOptions): TelemetrySpan {
  const name = options.name ?? `${options.operation} ${options.requestModel}`;
  const attributes: Record<string, string> = {
    "gen_ai.operation.name": options.operation,
    "gen_ai.request.model": options.requestModel,
  };
  if (options.system) {
    attributes["gen_ai.system"] = options.system;
    attributes["gen_ai.provider.name"] = options.system;
  }
  if (options.agentName) attributes["gen_ai.agent.name"] = options.agentName;

  // SpanKind.CLIENT is stably 3 across OTel API versions; hard-coded so this
  // helper needs no reference to the (optional) `@opentelemetry/api` enum.
  return tracer.startSpan(name, { kind: SPAN_KIND_CLIENT, attributes });
}

export interface GenaiResponseOptions {
  responseModel?: string;
  finishReasons?: string[];
  inputTokens?: number;
  outputTokens?: number;
  reasoningTokens?: number;
  cacheReadTokens?: number;
  cacheWriteTokens?: number;
}

/** Record GenAI response and usage attributes on `span`. */
export function recordGenaiResponse(span: TelemetrySpan, options: GenaiResponseOptions): void {
  if (options.responseModel !== undefined)
    span.setAttribute("gen_ai.response.model", options.responseModel);
  if (options.finishReasons !== undefined)
    span.setAttribute("gen_ai.response.finish_reasons", options.finishReasons);
  if (options.inputTokens !== undefined)
    span.setAttribute("gen_ai.usage.input_tokens", options.inputTokens);
  if (options.outputTokens !== undefined)
    span.setAttribute("gen_ai.usage.output_tokens", options.outputTokens);
  if (options.reasoningTokens !== undefined)
    span.setAttribute("gen_ai.usage.reasoning_tokens", options.reasoningTokens);
  if (options.cacheReadTokens !== undefined)
    span.setAttribute("gen_ai.usage.cache_read_input_tokens", options.cacheReadTokens);
  if (options.cacheWriteTokens !== undefined)
    span.setAttribute("gen_ai.usage.cache_write_input_tokens", options.cacheWriteTokens);
}

export interface GenaiContentOptions {
  prompt?: unknown;
  completion?: unknown;
  contentCapture?: ContentCaptureMode;
  redactKeys?: string[];
}

/**
 * Emit prompt / completion as span events, gated by the capture policy.
 *
 * Content is emitted as span *events* (`gen_ai.content.prompt` /
 * `gen_ai.content.completion`) rather than attributes so large payloads don't
 * inflate the span's attribute set. Redaction follows
 * {@link redactTelemetry}: `metadata_only` drops content outright, `redacted`
 * truncates long strings, `full` keeps it — and credential-shaped keys are
 * always stripped regardless of mode.
 */
export function recordGenaiContent(span: TelemetrySpan, options: GenaiContentOptions): void {
  const settings = resolveSettings({
    contentCaptureMode: options.contentCapture,
    redactKeys: options.redactKeys,
  });
  if (settings.contentCaptureMode === "metadata_only") return;

  if (options.prompt !== undefined) {
    const redacted = redactTelemetry({ prompt: options.prompt }, settings);
    span.addEvent("gen_ai.content.prompt", flatten(redacted));
  }
  if (options.completion !== undefined) {
    const redacted = redactTelemetry({ completion: options.completion }, settings);
    span.addEvent("gen_ai.content.completion", flatten(redacted));
  }
}

/**
 * Coerce a redacted value into span-event attributes. OTel span-event
 * attributes must be flat primitives (or homogeneous arrays); nested
 * structures are serialised to a string so they survive the OTLP boundary.
 */
function flatten(value: unknown): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  if (value && typeof value === "object" && !Array.isArray(value)) {
    for (const [key, item] of Object.entries(value as Record<string, unknown>)) {
      if (isPrimitive(item)) {
        out[key] = item;
      } else if (Array.isArray(item) && item.every(isPrimitive)) {
        out[key] = item;
      } else {
        out[key] = JSON.stringify(item);
      }
    }
  } else {
    out.value = isPrimitive(value) ? value : JSON.stringify(value);
  }
  return out;
}

function isPrimitive(v: unknown): v is string | number | boolean {
  return typeof v === "string" || typeof v === "number" || typeof v === "boolean";
}
