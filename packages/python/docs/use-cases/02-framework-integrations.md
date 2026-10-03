# Add framework evidence

Framework integrations observe existing calls and supply spans, model usage and errors. They do not replace business observations for registration, committed domain transitions, concurrent operations or workflow waits.

```bash
pip install 'axonpush[langchain]'
```

```python
from axonpush import AxonPush
from axonpush.integrations.langchain import AxonPushCallbackHandler

client = AxonPush(content_capture_mode="metadata_only")
handler = AxonPushCallbackHandler(client, channel_id="channel-id", mode="background")
# Attach handler to the callback configuration of your existing chain.
# Preserve the chain's provider, authentication, inputs and return values.
```

The [SDK README](../../README.md#integrations) lists supported frameworks and publishing modes. Install only the integration used by the application. Use one tracing plane per existing call to avoid duplicate operations. Close the handler and client during application shutdown according to their existing lifecycle.

Capture is metadata-only by default. A source-specific allowlist must still remove documents, messages, arguments/results, contacts, compensation terms, secrets and raw exception text before buffering or logging. Prefer isolated nonblocking export; a queue overflow or exporter failure needs a visible health signal.

For cross-service evidence, preserve trusted trace/span identifiers from the application's existing tracing context and include those same identifiers in business observations. A span never proves registration, client vendor identity or a hiring decision by itself.

See [tracing](04-distributed-tracing.md) and the [shared operations contract](../../../../AGENT_OPERATIONS.md).
