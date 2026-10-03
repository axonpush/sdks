# Link activity to finite traces

A finite trace explains one request or operation. Business entities remain linked across many traces through opaque operation, thread, attempt and confirmed agent references. Use the original trace ID from the source context in both spans and lifecycle observations.

```python
from axonpush import AxonPush, EventType, get_or_create_trace

trace = get_or_create_trace()
with AxonPush() as client:
    client.events.publish(
        "tool_execution",
        {"attributes": {"operation.kind": "tool", "outcome": "completed"}},
        channel_id="channel-id",
        trace_id=trace.trace_id,
        span_id=trace.next_span_id(),
        event_type=EventType.APP_SPAN,
        dedup_key="persisted-source-event-id",
    )
    detail = client.traces.get(trace.trace_id)
    if detail is not None:
        print(detail.trace_id, len(detail.spans or []))
```

`next_span_id()` creates a W3C-compatible span identifier. When publishing through a durable source journal, persist the chosen span ID, deduplication key and `occurred_at` once and reuse them on retries. A regenerated timestamp or ID can turn a retry into different evidence.

For OpenTelemetry, reuse the application's existing provider and context; [telemetry configuration](../../README.md#opentelemetry-native-telemetry) describes the exporter. Do not mix UUID and compact W3C trace spellings for the same operation without verifying the server's normalization. Do not keep one trace open for an agent's entire lifetime.

Use `activity.timeline` for source evidence across traces and `activity.entities` for current concurrent operation/thread state. A completed operation cannot clear unrelated work. Capture only allowlisted metadata.
