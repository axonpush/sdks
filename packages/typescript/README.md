# @axonpush/sdk

TypeScript SDK for [axonpush](https://axonpush.xyz), observability and event
infrastructure for AI agent systems. ESM-only, runs on Node 20+ and Bun.

- **Publish** events over a typed REST client generated from the axonpush
  OpenAPI spec.
- **Trace** multi-agent workflows via `traceId` / `parentEventId`.
- **Integrate** with LangChain, LangGraph, LlamaIndex, OpenAI Agents,
  Vercel AI SDK, Mastra, Google ADK, OpenTelemetry, Sentry, pino,
  winston, console capture, BullMQ, and the Anthropic SDK.

## Agent operations

Each workspace declares its own data dictionary and entities (usually drafted by
your coding agent over MCP). Your app then sends observations and profile traits.
Nothing is sent unless you call these methods.

```ts
const client = new AxonPush({ environment: "production" });

await client.observe(workspaceId, {
  event: "ticket.escalated",
  refs: { ticket: "t_42", agent: "a_7" },
  attributes: { priority: "high", queue: "billing" },
});

await client.identify(workspaceId, {
  entity: "agent",
  id: "a_7",
  traits: { display_name: "Triage bot", team: null },
});

// Same call as identify, for organisation-like entities.
await client.group(workspaceId, { entity: "company", id: "c_1", traits: { name: "Acme" } });
```

`observe` fills in `schema_version`, a UUID `source_event_id` and an ISO
`occurred_at` when you leave them out, plus the bound trace id when there is one.
Pass an array to send several; they go in batches of 100. Attribute keys the
workspace has not declared are dropped by the server and listed in the report's
`dropped`. `identify` merges traits; `null` deletes one. Both return `null`
instead of throwing on a connection failure while `failOpen` is on (the default).

The lower-level `workspaces`, `templates`, `observations` and `activity`
resources cover drafts, revisions and activity queries. See the
[shared operations contract](../../AGENT_OPERATIONS.md).


## Install

```bash
npm install @axonpush/sdk
# or
bun add @axonpush/sdk
```

The framework integrations live behind optional peer deps. The package
will load fine without any of them; install the host library you want to
wire up:

```bash
npm install @langchain/core         # for AxonPushCallbackHandler
npm install winston winston-transport
npm install pino
npm install @opentelemetry/api @opentelemetry/sdk-trace-base
npm install @sentry/node
npm install bullmq
npm install @anthropic-ai/sdk
```

## Quickstart

This snippet matches `examples/01-quickstart.ts` exactly.

```ts
import { AxonPush } from "@axonpush/sdk";

const client = new AxonPush();
const event = await client.events.publish({
  identifier: `quickstart-${Date.now()}`,
  channelId: process.env.AXONPUSH_CHANNEL_ID!,
  eventType: "custom",
  payload: { hello: "world", source: "examples/01-quickstart" },
});
console.log("published event:", event);
client.close();
```

`new AxonPush()` resolves credentials from `AXONPUSH_*` env vars (see
[Configuration](#configuration)). Pass an options bag to override.

## Configuration

| Field | Env var | Default | Notes |
|---|---|---|---|
| `apiKey` | `AXONPUSH_API_KEY` | - | Required. An `ak_` API key or a `pt_` public ingest token. |
| `tenantId` | `AXONPUSH_TENANT_ID` | - | Org UUID; falls back to `AXONPUSH_ORG_ID`. |
| `orgId` | `AXONPUSH_ORG_ID` | mirrors `tenantId` | |
| `appId` | `AXONPUSH_APP_ID` | - | Default app for resources that need one. |
| `baseUrl` | `AXONPUSH_BASE_URL` | `https://api.axonpush.xyz` | REST API root. |
| `environment` | `AXONPUSH_ENVIRONMENT` | - | Logical env slug (`production`, `staging`). |
| `timeout` | `AXONPUSH_TIMEOUT` | `30` | Per-request timeout. The option is milliseconds; the environment variable is seconds. |
| `maxRetries` | `AXONPUSH_MAX_RETRIES` | `3` | Retries on `RetryableError`. |
| `failOpen` | `AXONPUSH_FAIL_OPEN` | `true` | Swallow `APIConnectionError` and resolve `null`, so telemetry cannot take your app down. |

Caller-supplied options always win when defined.

### Authentication

Two ingest credentials are supported, both passed via `apiKey` (or
`AXONPUSH_API_KEY`):

| Credential | Header | Prefix | Use |
|---|---|---|---|
| API key | `X-API-Key` | `ak_` | Server-side ingestion and management according to the key’s scopes. |
| Public ingest token | `X-Public-Token` | `pt_` | Browser and untrusted clients. Publish-only, safe to ship in a frontend. |

The SDK routes `ak_` values to `X-API-Key` and `pt_` values to
`X-Public-Token` by prefix.

## Integrations

Every integration is reachable from the package root **and** as a
sub-path import for tree-shaking:

```ts
import { AxonPushCallbackHandler } from "@axonpush/sdk";
import { AxonPushCallbackHandler } from "@axonpush/sdk/integrations/langchain";
```

| Import | What it wires up |
|---|---|
| `AxonPushCallbackHandler` | LangChain.js callback handler. |
| `AxonPushLangGraphHandler` | LangGraph node lifecycle hook. |
| `AxonPushLlamaIndexHandler` | LlamaIndex.ts callback. |
| `AxonPushAnthropicTracer` | Wraps `@anthropic-ai/sdk` calls; records token usage and `streamMessage()`. |
| `AxonPushRunHooks` | OpenAI Agents SDK lifecycle hooks. |
| `axonPushMiddleware` | Vercel AI SDK middleware. |
| `AxonPushMastraHooks` | Mastra agent hooks. |
| `axonPushADKCallbacks` | Google ADK callback bundle. |
| `AxonPushSpanExporter` | OTel `SpanExporter`. |
| `installSentry(Sentry, opts)` | Builds the axonpush DSN and calls `Sentry.init`. |
| `createAxonPushPinoStream` | pino transport stream. |
| `createAxonPushWinstonTransport` | winston transport. |
| `setupConsoleCapture` | Mirror `console.*` to axonpush. |
| `BackgroundPublisher` | Bounded in-memory publish queue (used by transports). |
| `BullMQPublisher` | Forward events through a BullMQ queue. |
| `safePublish` / `truncate` / `coerceChannelId` | Building blocks for custom integrations. |

Each integration accepts the same `IntegrationConfig`:

```ts
{ client, channelId, agentId?, traceId?, mode?, queueSize?, overflowPolicy?, shutdownTimeoutMs?, concurrency?, bullmqOptions? }
```

`mode` is `"background"` (default), `"sync"`, or `"bullmq"`.

## Errors

```ts
import {
  AxonPushError,
  AuthenticationError,
  NotFoundError,
  RateLimitError,
  RetryableError,
  ValidationError,
} from "@axonpush/sdk";

try {
  await client.apps.get(id);
} catch (err) {
  if (err instanceof RateLimitError) {
    await new Promise((r) => setTimeout(r, (err.retryAfter ?? 1) * 1000));
  } else if (err instanceof AuthenticationError) {
    rotateApiKey();
  } else if (err instanceof RetryableError) {
    // safe to retry with your own backoff
  } else if (err instanceof NotFoundError || err instanceof ValidationError) {
    throw err; // not retryable
  }
}
```

The SDK already retries `RetryableError` with backoff
`[250, 500, 1000, 2000, 4000] ms` (honouring `Retry-After`) up to
`maxRetries` times - handle these in your code only when you need a
custom policy.

## Tracing

```ts
import { getOrCreateTrace } from "@axonpush/sdk";

const trace = getOrCreateTrace();
await client.events.publish({
  identifier: "plan",
  channelId,
  traceId: trace.traceId,
  eventType: "app.span",
  payload: { attributes: { "operation.kind": "planning" } },
});
```

`traceId` is propagated as `X-Axonpush-Trace-Id` and stored on every
event, so the UI can stitch agent runs across services. Pass
`parentEventId` to model hand-offs between agents.

## OpenTelemetry-native telemetry

`@axonpush/sdk/telemetry` ships GenAI spans as real OTLP over HTTP to
`${base}/v1/traces`, routed by the `X-Axonpush-Channel` header and authed
by `X-API-Key`. Spans follow the OpenTelemetry GenAI semantic conventions
(`gen_ai.*`), so they are portable to any OTLP backend, not just axonpush.
This is the recommended way to send traces.

The OpenTelemetry SDK peers load lazily, so the base SDK runs without them.
Install them alongside the SDK to use this module:

```bash
npm install @opentelemetry/api @opentelemetry/sdk-trace-node \
  @opentelemetry/exporter-trace-otlp-http @opentelemetry/resources
```

`configureTelemetry()` reuses an existing SDK `TracerProvider` when one is
already registered (it never replaces it) and only creates a
`NodeTracerProvider` when the app does not own OpenTelemetry. Config
resolves from options, then the matching `AXONPUSH_BASE_URL` /
`AXONPUSH_API_KEY` / `AXONPUSH_CHANNEL_ID` env var. Unlike Python's context
manager, the caller owns the span lifecycle. Call `span.end()`, typically
in a `finally`.

```ts
import {
  configureTelemetry,
  genaiSpan,
  recordGenaiResponse,
  recordGenaiContent,
} from "@axonpush/sdk/telemetry";

// Reuses or creates a TracerProvider, attaches a batch OTLP/HTTP exporter,
// and stamps a Resource with service.name / deployment.environment.name / service.version.
const handle = await configureTelemetry({
  serviceName: "my-agent",
  environment: "prod",
  serviceVersion: "1.4.0",
  contentCapture: "metadata_only", // or "redacted" / "full"
});
const tracer = handle.tracer();

const span = genaiSpan(tracer, {
  operation: "chat",
  requestModel: "gpt-4o",
  system: "openai",
});
try {
  // ... call the model ...
  recordGenaiResponse(span, {
    responseModel: "gpt-4o",
    inputTokens: 12,
    outputTokens: 48,
    cacheWriteTokens: 0,
  });
  recordGenaiContent(span, { prompt: "…", completion: "…" });
} finally {
  span.end();
}

await handle.flush(); // or handle.shutdown() on clean exit
```

Prompt and completion land as span events (`gen_ai.content.prompt` /
`gen_ai.content.completion`), gated by `contentCapture`: `metadata_only`
drops content, `redacted` truncates long strings, `full` keeps it. Pass
`redactKeys` to strip extra keys; credential-shaped keys are always
stripped regardless of mode.

On serverless (AWS Lambda, Cloud Functions, Azure Functions) the batch
processor's exit-time flush is unreliable because the container is frozen
between invocations. `configureTelemetry()` logs a note when it detects
one; call `handle.flush()` at the end of each invocation, or wrap the
handler with `flushAfterInvocation`:

```ts
import { flushAfterInvocation } from "@axonpush/sdk/telemetry";

export const handler = flushAfterInvocation(handle, async (event) => {
  const span = genaiSpan(handle.tracer(), { operation: "chat", requestModel: "gpt-4o" });
  try {
    // ...
  } finally {
    span.end();
  }
});
```

### Which should I use

The OTel-native path above is the recommended way to send traces. The
legacy per-framework event-model exporter
(`AxonPushSpanExporter` from `@axonpush/sdk/integrations/otel`, which maps
calls to `/event` payloads) still works and is kept for compatibility, but
it is being superseded by OTel-native. Frame it as the compatibility path:
keep it if you already depend on channel fan-out on the events plane,
otherwise reach for `@axonpush/sdk/telemetry`. Traces from both land in the
same dashboard (`/v2/traces`); the server reconciles them through the OTLP
normalizer, so you can migrate call sites incrementally without a gap in
your traces.

If a framework integration (LangChain, Mastra, the Vercel AI middleware,
`AxonPushSpanExporter`, …) already emits GenAI spans or events for a call,
do not also wrap that call with `genaiSpan` / `recordGenai*`. Pick one
plane so the operation is not recorded twice.

## Migration to 1.0.0

- **All IDs are `string` UUIDs.** `numeric` ids are gone from the public
  boundary; integrations still accept `number` for `channelId` with a
  one-time `console.warn` and migrate it for you.
- **Realtime is removed.** The backend no longer exposes MQTT, SSE,
  WebSocket, or `/auth/iot-credentials`, so `connectRealtime()`,
  `RealtimeClient`, the topic builders, the `iotEndpoint` / `wsUrl`
  options, and the `mqtt` dependency are gone. Ingest over the REST
  client, OTLP, or the Sentry DSN compat path instead.
- **`events.search()` returns the server search envelope.** Read `.events`
  for the events; use `.entities` and `.nextCursor` for workspace entity pages.
- **Models live in flat re-exports.** Import `App`, `Channel`, `Event`,
  `EventType`, etc. from `@axonpush/sdk` directly.
- **Zero-arg constructor.** `new AxonPush()` reads `AXONPUSH_*` env
  vars; the explicit options bag is optional.

See [`CHANGELOG.md`](./CHANGELOG.md) for the full list, including the
new exception envelope and the audit improvements that landed alongside
the rewrite.

## Examples

Runnable examples covering quickstart, tracing, multi-agent fan-out,
webhooks, error handling, and every framework integration live in
[`examples/`](./examples). Each one is a single file you can run with
`bun run examples/<name>.ts`.

## Advanced topics

For how the SDK is generated from the shared contract, the transport
chokepoint, the exception envelope, and generated-layer ownership, see
[`SHARED-CONTRACT.md`](./SHARED-CONTRACT.md).

## License

MIT.

## Contributing

Issues and PRs welcome at [github.com/axonpush/sdks](https://github.com/axonpush/sdks).
Please run `bun run lint && bun run typecheck && bun run test` before
sending a PR.
