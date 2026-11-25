# @axonpush/sdk

[AxonPush](https://axonpush.xyz) verifies that automation providers delivered what
they promised. Deploy a workflow contract per customer process, run the handlers
that perform side effects, send the facts your systems observe, and inspect each
case to see whether the promised outcome was confirmed. This is the TypeScript SDK.
ESM-only, Node 20+ and Bun.

Zod and Effect Schema are optional ways to author contracts. Telemetry, agent
operations, OpenTelemetry traces and framework integrations remain supported as
diagnostics; see [Diagnostics](#diagnostics).

## Install

```bash
npm install @axonpush/sdk
# or
bun add @axonpush/sdk
```

## Workflow runtime

Run `npx axonpush workflow version` to check the bundled CLI. Try a packaged
scenario in a new directory with `npx axonpush workflow init --template booking-reschedule --out booking`, then
`npx axonpush workflow action-test --file booking/workflow.yaml --fixture booking/review.json`.
The fixture expects the reschedule to require review.

When a workflow declares actions, run a handler beside the system that performs
them. `WorkflowRuntime` leases one command at a time, calls your `execute` or
`lookup`, and reports a receipt.

```ts
import { WorkflowRuntime } from "@axonpush/sdk/workflow";

const runtime = new WorkflowRuntime(
  {
    baseUrl: "https://api.axonpush.xyz",
    workspace: workspaceId,
    environment: "production",
    apiKey: process.env.AXONPUSH_API_KEY!,
    handler: "create_booking",
  },
  {
    execute: async (action) => ({ booking_ref: await createBooking(action) }),
    lookup: async (action) => {
      const ref = await findBooking(action);
      return ref ? { result: "found", observed: { booking_ref: ref } } : { result: "absent" };
    },
  },
);

const stop = new AbortController();
process.on("SIGTERM", () => stop.abort());
await runtime.run({ signal: stop.signal });
```

- Give each side effect a stable, idempotent identity so `lookup` can find it later.
- If `execute` throws, the side effect may still have happened. The runtime
  reports `ambiguous` and does not rerun it blindly; the next lease is a `lookup`.
- `lookup` recovers the outcome as `found` (with what it observed), `absent` or
  `unavailable`. A `lookup` that throws is reported as `unavailable`.
- Publish facts and checkpoints only after the source transaction commits.
- A `ready` deployment means the contract is configured. Evaluated cases are what
  show whether outcomes happened.

The runtime requires HTTPS (loopback HTTP is allowed for local development).
Keep provider credentials in your app; the runtime does not send them to AxonPush.

For local `validate`, `test` and `diff` without network calls, use `runWorkflow`
from the same entrypoint. Version `0.0.13` includes compiler `0.1.0` for Windows,
Linux and macOS on x64 and ARM64. To try it in an empty project:

```js
import { runWorkflow } from "@axonpush/sdk/workflow";
await runWorkflow(["init", "--file", "workflow.yaml"]);
console.log(await runWorkflow(["validate", "--file", "workflow.yaml"]));
await runWorkflow(["generate", "--file", "workflow.yaml", "--language", "typescript", "--out", "generated"]);
```

Run as an ES module (`node example.mjs`). No credentials are needed locally.

## Workflow quickstart

The path from contract to evaluated case. `workspaceId` is your workspace UUID,
`new AxonPush()` reads credentials from `AXONPUSH_*` env vars (see
[Configuration](#configuration)), and the source is the contract text, such as the
`workflow.source` produced by the Zod provider below.

```ts
import { readFile } from "node:fs/promises";
import { AxonPush } from "@axonpush/sdk";

const client = new AxonPush({ environment: "production" });
const source = await readFile("booking.contract.json", "utf8");

// 0. Optional: setup questions and the recommended tool sequence (read-only).
const guide = await client.workflows.describe(workspaceId);

// 1. Preview: compiles and diffs against what is live. Nothing is written.
const preview = await client.workflows.previewDeployment(workspaceId, { source });
console.log(preview?.required_sources, preview?.required_handlers, preview?.warnings);

// 2. Apply: publish, activate and bind to a connected runtime in one atomic step.
const deployment = await client.workflows.applyDeployment(workspaceId, preview!.workflow, {
  source,
  runtime_id: preview!.compatible_runtime_ids![0],
  expected_active_version_id: preview!.current_version_id, // optimistic concurrency guard
});
console.log(deployment?.status, deployment?.problems); // "ready" | "degraded" | "not_ready"

// 3. Send facts from a registered source. The receipt means stored, not verified.
await client.workflows.facts(workspaceId, {
  workflow: "appointment_booking",
  input: {
    case_id: "request-1",
    facts: [{
      id: "request-1:accepted",
      event: "booking.accepted",
      case_id: "request-1",
      source: "booking_adapter",
      occurred_at: new Date().toISOString(),
      fields: { booking_request_id: "request-1", person_ref: "p_1",
                starts_at: "2026-11-21T10:00:00Z", service_ref: "s_1" },
    }],
    coverage: null,
  },
});

// 4. Inspect cases and outcomes.
const { cases } = (await client.workflows.cases(workspaceId, { workflow: "appointment_booking" })) ?? {};
for (const c of cases ?? []) {
  for (const o of c.result.obligations ?? []) console.log(c.key, o.requirement, o.state, o.reason);
}
const live = await client.workflows.deployment(workspaceId, "appointment_booking");
console.log(live?.recent_results); // { confirmed, not_completed, could_not_confirm, no_result, pending }
```

Useful next calls:

| Need | Method |
|---|---|
| Inspect one case: pinned contract, evidence, verification | `workflows.case(workspaceId, caseKey)` |
| Try evidence against a contract with an explicit clock, no state saved | `workflows.simulate` |
| Preview a newer version against an existing case | `workflows.replay` |
| Bind an evidence source to a publisher identity | `workflows.registerSource` / `workflows.sources` |
| Record a human disposition on an obligation | `workflows.disposition` |
| Review, propose or decide typed actions | `workflows.actions` / `proposeAction` / `decideAction` |
| Close ingestion for a case (does not verify it) | `workflows.close` |

## Authoring workflows

Zod and Effect Schema are optional authoring providers. Both compile through the
same pinned compiler as the server.

### Zod provider

The `@axonpush/sdk/workflow/zod` entrypoint provides `defineZodWorkflow`,
`compileZodWorkflow` and `verifyZodWorkflow`. Define fact schemas as strict Zod 4
objects; the provider emits stable contract source and delegates compilation and
verification to the same Go executable used by the server. There is no separate
TypeScript evaluator. Install with `npm install @axonpush/sdk@0.0.13 zod@4`.

Supported fields: plain `z.string()`, `z.number()`, `z.boolean()` and
`z.iso.datetime({ offset: true })`. Unsupported checks, transforms, refinements,
coercion, defaults, optional fields and nested structures fail explicitly.
See [the complete runnable example](examples/workflow-zod.ts) and
[the provider guide](https://docs.axonpush.xyz/workflows-zod).

Build the SDK first, then run `bun run examples/workflow-zod.ts`. It writes
`booking.contract.json`; commit that generated artifact alongside your TypeScript
source in your own application. The exported source is accepted by existing
CLI generation and HTTP publication operations; activation remains explicit.

For native parity tests, set the binary environment variable and run
`bunx vitest run src/__tests__/workflow-zod.test.ts` from `packages/typescript`.
The parity test is skipped when the executable is not configured; schema rejection
and source determinism tests always run.

### Effect Schema provider

`@axonpush/sdk/workflow/effect` exports `defineEffectWorkflow`,
`compileEffectWorkflow`, `verifyEffectWorkflow` and `WorkflowTimestamp`. Install
with `npm install @axonpush/sdk@0.0.13 effect@^4.1.5` to use it. Effect 3 is not supported. Define facts
with `Schema.Struct`, plain scalar fields and the exported timestamp helper.
Custom filters, transformations and unsupported constraints fail explicitly.
Compilation and verification share the same native Go bridge as the Zod provider.

See [the runnable example](examples/workflow-effect.ts) and
[the provider guide](https://docs.axonpush.xyz/workflows-effect), which uses the bundled compiler. To run the repository parity tests against an explicit compiler `0.1.0`, set `AXONPUSH_WORKFLOW_BINARY` and run
`bunx vitest run src/__tests__/workflow-effect.test.ts` with that variable set.
Native tests skip when no executable is configured; schema tests always run.

### Offline compiler commands

`@axonpush/sdk/workflow` exports `runWorkflow(args)`, a shell-free wrapper over the
pinned compiler's `init`, `validate`, `generate`, `test`, `action-test` and `diff` commands,
plus `resolveWorkflowBinary()`. It makes no network calls and refuses a compiler
whose version is not `workflowCompilerVersion`.

## Configuration

| Field | Env var | Default | Notes |
|---|---|---|---|
| `apiKey` | `AXONPUSH_API_KEY` | - | Required. An `ak_` API key or a `pt_` public ingest token. |
| `tenantId` | `AXONPUSH_TENANT_ID` | - | Org UUID; falls back to `AXONPUSH_ORG_ID`. |
| `orgId` | `AXONPUSH_ORG_ID` | mirrors `tenantId` | |
| `appId` | `AXONPUSH_APP_ID` | - | Default app for resources that need one. |
| `baseUrl` | `AXONPUSH_BASE_URL` | `https://api.axonpush.xyz` | REST API root. |
| `environment` | `AXONPUSH_ENVIRONMENT` | - | Logical env slug (`production`, `staging`). |
| `timeout` | `AXONPUSH_TIMEOUT` | `30000` ms / `30` s | Total invocation budget, including retries and response reading. The option is milliseconds; the environment variable is seconds. |
| `maxRetries` | `AXONPUSH_MAX_RETRIES` | `3` | Additional attempts for eligible reads and deduplicated event/observation writes. Other mutations run once. |
| `failOpen` | `AXONPUSH_FAIL_OPEN` | `true` | Swallow `APIConnectionError` and resolve `null`, so telemetry cannot take your app down. |

Caller-supplied options always win when defined. Because `failOpen` defaults to
`true`, workflow reads can resolve `null` on a connection failure; check for it, or
set `failOpen: false` on clients that deploy workflows or record decisions.

### Authentication

Two ingest credentials are supported, both passed via `apiKey` (or
`AXONPUSH_API_KEY`):

| Credential | Header | Prefix | Use |
|---|---|---|---|
| API key | `X-API-Key` | `ak_` | Server-side ingestion and management according to the key’s scopes. |
| Public ingest token | `X-Public-Token` | `pt_` | Browser and untrusted clients. Publish-only, safe to ship in a frontend. |

The SDK routes `ak_` values to `X-API-Key` and `pt_` values to
`X-Public-Token` by prefix. Workflow deployment, facts and workers need an `ak_` key.

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
    // The transport budget was exhausted. Retry only an idempotent operation.
  } else if (err instanceof NotFoundError || err instanceof ValidationError) {
    throw err; // not retryable
  }
}
```

The p-retry transport uses jittered backoff with a 250ms base and 4s cap, respecting `Retry-After` within the invocation deadline. `RetryableError` classifies a transient failure; it does not make arbitrary mutations safe to repeat. Avoid nesting a second retry loop around the built-in policy. When retrying a publish in a later SDK call, preserve its original deduplication key or observation identity. Caller cancellation is never swallowed by `failOpen`. See [transport and queue behavior](../../docs/infrastructure-libraries.md).

## Diagnostics

Use these to debug the automation behind a workflow, or on their own. None of them
is required to deploy or verify workflows.

### Agent operations

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

### Publishing events

Run the fuller example in `examples/01-quickstart.ts`.

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

### Integrations

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
| `installSentry(Sentry, opts)` | Builds the axonpush DSN from a `pt_` public ingest token (`publicToken` or `AXONPUSH_PUBLIC_TOKEN`) and calls `Sentry.init`. API keys are refused by Sentry ingest. |
| `createAxonPushPinoStream` | pino transport stream. |
| `createAxonPushWinstonTransport` | winston transport. |
| `setupConsoleCapture` | Mirror `console.*` to axonpush. |
| `BackgroundPublisher` | Bounded in-memory publish queue (used by transports). |
| `BullMQPublisher` / `createBullMQWorker` | Forward events through a BullMQ queue (`@axonpush/sdk/integrations/bullmq`). |
| `safePublish` / `truncate` / `coerceChannelId` | Building blocks for custom integrations. |

Each integration accepts the same `IntegrationConfig`:

```ts
{ client, channelId, agentId?, traceId?, mode?, queueSize?, overflowPolicy?, shutdownTimeoutMs?, concurrency?, bullmqOptions? }
```

`mode` is `"background"` (default), `"sync"`, or `"bullmq"`.

See [declared framework task lifecycles](../../docs/framework-task-lifecycle.md) for opt-in root goals, failure boundaries and callback correlation.

### Tracing

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

### OpenTelemetry-native telemetry

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

#### Which should I use

The OTel-native path above is the recommended way to send traces. The
legacy per-framework event-model exporter
(`AxonPushSpanExporter` from `@axonpush/sdk/integrations/otel`, which maps
calls to `/event` payloads) still works and is kept for compatibility, but
it is being superseded by OTel-native. Frame it as the compatibility path:
keep it if you already depend on channel fan-out on the events plane,
otherwise reach for `@axonpush/sdk/telemetry`. Traces from both land in the
same trace views (`GET /traces`); the server reconciles them through the OTLP
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

Runnable examples live in [`examples/`](./examples). Each one is a single file you
can run with `bun run examples/<name>.ts`. Start with the workflow providers
(`workflow-zod.ts`, `workflow-effect.ts`); the numbered files cover diagnostics:
quickstart, tracing, multi-agent fan-out, webhooks, error handling, and the framework
integrations.

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

## Customer identity and request context

Identify profiles separately from request attribution. Use TypeScript `withContext`, Python `with_context`, or .NET `BeginContext` after authentication to link customer subjects to observations, diagnostic events and workflow cases. Capture context before queued jobs and restore it in the worker. Generated workflow publishing helpers accept the same scope; the deterministic verifier is unchanged.

See the [customer attribution guide](https://docs.axonpush.xyz/customer-attribution) for sync/async examples, explicit business reference mappings, OpenTelemetry integration, background work and local validation.
