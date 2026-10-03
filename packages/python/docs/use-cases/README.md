# axonpush Use Case Guides

Scenario-driven guides for building with axonpush. The guides distinguish source lifecycle observations from supporting framework evidence.

## Prerequisites

```bash
pip install axonpush
```

You need an axonpush API key and tenant ID. Get them from the [axonpush dashboard](https://axonpush.xyz).

## Guides

| # | Guide | Difficulty | What you'll learn |
|---|-------|------------|-------------------|
| 1 | [See what your agent is doing](01-realtime-agent-events.md) | Beginner | Store observations, verify projection and query scoped activity |
| 2 | [Add observability in 3 lines](02-framework-integrations.md) | Beginner | Observe existing framework calls with metadata-only capture |
| 4 | [Trace a multi-step agent run](04-distributed-tracing.md) | Intermediate | Distributed tracing with auto-generated trace/span IDs |
| 5 | [Get notified when your agent fails](05-error-webhooks.md) | Intermediate | Lifecycle incidents and operator notifications |
| 7 | [Production error handling](07-production-error-handling.md) | Advanced | Graceful failures, retries, and rate limits |

Start with Guide 1 if you're new to axonpush. Jump to Guide 2 if you already use LangChain, OpenAI Agents, Claude, or CrewAI.

Looking for the full API reference? See the [README](../../README.md) for the resource table and method signatures.
