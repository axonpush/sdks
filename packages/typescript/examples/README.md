# axonpush SDK examples

From the monorepo root, run `bun install --frozen-lockfile`, then `cd packages/typescript`.
Each file is runnable on its own with `bun run examples/<file>.ts`.
The shared loader lives in `examples/config.ts`.

Set the standard SDK env vars before running anything:

```
export AXONPUSH_API_KEY=ak_...          # scopes depend on the example
export AXONPUSH_TENANT_ID=<org-uuid>
export AXONPUSH_CHANNEL_ID=<channel-uuid>
export AXONPUSH_BASE_URL=http://localhost:3000   # optional
export AXONPUSH_ENVIRONMENT=development          # optional
```

| File | What it does | Extra env / deps |
|---|---|---|
| `01-quickstart.ts` | Construct `new AxonPush()` from env, publish one event. | - |
| `02-agent-tracing.ts` | Three events under one `traceId`, linked via `parentEventId`. | - |
| `04-multi-agent.ts` | Fan-out across `agentId`s on one channel, then list and filter by `eventType`. | - |
| `05-webhooks.ts` | Create a webhook endpoint, list endpoints, inspect deliveries. | `WEBHOOK_URL` (public HTTPS, ngrok ok) |
| `06-error-handling.ts` | Catch `AuthenticationError`, `NotFoundError`, `RateLimitError`, `RetryableError`. | - |
| `07-langchain.ts` | Drive `AxonPushCallbackHandler` from a synthetic LangChain runtree. | optional `@langchain/core` |
| `08-winston-logger.ts` | Ship winston log records as `app.log` events with severity mapping. | optional `winston`, `winston-transport` |
| `09-sentry.ts` | Build the axonpush DSN and call `installSentry(Sentry, opts)`. | optional `@sentry/node` |
| `10-otel-export.ts` | Register `AxonPushSpanExporter` with a `BasicTracerProvider`. | optional `@opentelemetry/api`, `@opentelemetry/sdk-trace-base` |

Public ingest tokens can publish but cannot run management or search examples.
A local API URL must be supplied explicitly; `new AxonPush()` otherwise uses the
SDK's hosted API default.

The optional peer-dep examples (07–10) detect their host library at
runtime and exit cleanly with a hint when it isn't installed, so they
don't crash on a fresh checkout.
