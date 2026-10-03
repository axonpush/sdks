# Isolate exporter failures

The host application keeps its normal return values, exceptions, cancellation and transactions when telemetry is off, on or failing. Export lifecycle observations from a separate durable journal worker. Use a bounded nonblocking buffer for transient signals and report overflow, retries, dead letters and observation gaps independently.

```python
from axonpush import AxonPush, APIConnectionError, AuthenticationError, RateLimitError, ServerError

with AxonPush(fail_open=False) as client:
    try:
        receipt = client.observations.accept(workspace_id, persisted_allowlisted_batch)
    except AuthenticationError:
        mark_exporter_unhealthy("credentials")
    except RateLimitError as error:
        schedule_same_batch_retry(error.retry_after)
    except (APIConnectionError, ServerError):
        schedule_same_batch_retry(None)
```

The helper functions and variables above belong to your exporter worker. They are not SDK methods. SDK retries are finite and use backoff; retain the same IDs, original occurrence time and exact allowlisted content when scheduling a later attempt. Record an error category rather than raw exception text.

`fail_open=True` returns `None` for connection failures. It does not hide authentication or validation errors. A `None` result means delivery is unconfirmed, so leave the durable journal item pending. A stored receipt is distinct from projection; verify the scoped status before acknowledging end-to-end freshness.

Do not synchronously publish in a business transaction or sleep in a request handler while waiting for AxonPush. A telemetry outage must not alter the business outcome. Test acceptance, duplicates, delayed delivery, source snapshots, capture off/on/failing, scoped access, retention/deletion and replay before enabling a pilot.
