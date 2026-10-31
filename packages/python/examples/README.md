# axonpush Python SDK examples

Runnable recipes for the SDK in this checkout, using the current generated resource facades.

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) installed
- A running axonpush backend (default: `http://localhost:3000`)
- An API key and tenant (organisation) UUID

## Setup

```bash
cd packages/python  # from the monorepo root
uv sync                       # core SDK and example configuration loader
uv sync --extra langchain     # + LangChain (07)
uv sync --extra deepagents    # + Deep Agents (09)
uv sync --extra loguru        # + Loguru (11)
uv sync --extra structlog     # + structlog (12)
uv sync --extra otel          # + OpenTelemetry (14)
```

Set credentials in your shell or in `examples/.env`:

```bash
export AXONPUSH_API_KEY=ak_…
export AXONPUSH_TENANT_ID=…       # your org UUID
# optional
export AXONPUSH_BASE_URL=http://localhost:3000
export AXONPUSH_ENVIRONMENT=dev
export AXONPUSH_APP_ID=…          # reuse an existing app
export AXONPUSH_CHANNEL_ID=…      # reuse an existing channel
```

`AxonPush()` reads these env vars directly, so the examples never hard-code credentials. Event examples use `resources.py`: an existing `AXONPUSH_CHANNEL_ID` is reused without creating or deleting resources. Otherwise they create a channel in `AXONPUSH_APP_ID` or a scratch app. Standard `contextlib` exit stacks clean up only newly created resources, including on exceptions. Use a development organization and a key with the scopes needed by the example; creating resources requires management scopes.

Run a recipe from `packages/python`, for example `uv run examples/01_quickstart.py`.
The optional `uv sync --extra ...` commands above select dependencies for individual recipes.

## Examples

| # | File | What it shows |
|---|------|---------------|
| 01 | `01_quickstart.py` | Create app + channel, publish three events, list, clean up. |
| 02 | `02_agent_tracing.py` | Multi-step agent trace: shared `trace_id`, span ids, `events.search(trace_id=...)` for projected metadata. |
| 04 | `04_multi_agent.py` | Planner → executor handoff. Both agents share one `trace_id` so the backend stitches the path together. |
| 05 | `05_webhooks.py` | Register a webhook endpoint with an `event_types=["agent.error"]` filter, publish matching + non-matching events, poll deliveries. Set `WEBHOOK_URL` to a receiver you control. |
| 06 | `06_async_client.py` | `AsyncAxonPush` + `asyncio.gather` - five "agents" publish concurrently. |
| 07 | `07_langchain.py` | `AxonPushCallbackHandler` for LangChain. Set `OPENAI_API_KEY` to actually run the chain. Use `uv run --extra langchain --with langchain-openai examples/07_langchain.py`. |
| 08 | `08_error_handling.py` | Walk through `AuthenticationError`, `NotFoundError`, `ValidationError`, the `RetryableError` mixin, plus the recommended catch-all order. |
| 09 | `09_deepagents.py` | `AxonPushDeepAgentHandler` for LangChain Deep Agents. Set `OPENAI_API_KEY` to run the agent. Needs `--extra deepagents`. |
| 10 | `10_stdlib_logging.py` | `AxonPushLoggingHandler` ships stdlib `logging` records as OTel-shaped `app.log` events. Includes a Django dictConfig snippet at the bottom. |
| 11 | `11_loguru.py` | `create_axonpush_loguru_sink` - Loguru sink with `serialize=True`. Needs `--extra loguru`. |
| 12 | `12_structlog.py` | `axonpush_structlog_processor` - non-destructive processor for structlog. Needs `--extra structlog`. |
| 13 | `13_print_capture.py` | `setup_print_capture` tees `sys.stdout` / `sys.stderr` into axonpush as `agent.log` events. |
| 14 | `14_otel.py` | `AxonPushSpanExporter` plugged into a `TracerProvider`. Needs `--extra otel`. |

## Configuration

All examples import `examples/config.py`, which loads `.env` and exposes:

| Variable | Required | Default | Used by |
|----------|----------|---------|---------|
| `AXONPUSH_API_KEY` | Yes | - | All |
| `AXONPUSH_TENANT_ID` | Yes | - | All |
| `AXONPUSH_BASE_URL` | No | `http://localhost:3000` | All |
| `AXONPUSH_ENVIRONMENT` | No | - | All |
| `AXONPUSH_APP_ID` | No | scratch app | All |
| `AXONPUSH_CHANNEL_ID` | No | scratch channel | All |
| `OPENAI_API_KEY` | No | - | 07, 09 |
| `WEBHOOK_URL` | Yes for webhook example | - | 05 |
