"""14 — OpenTelemetry span exporter.

If your service is already instrumented with the OpenTelemetry SDK, plug
``AxonPushSpanExporter`` into your ``TracerProvider``. Every span you
record gets shipped to AxonPush as an ``app.span`` event alongside any
other backends you export to (Jaeger, Tempo, Honeycomb, etc.).

Run::

    uv sync --extra otel
    uv run examples/14_otel.py
"""

import sys

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402

try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor

    from axonpush.integrations.otel import AxonPushSpanExporter
except ImportError:
    print("Install OTel integration: uv sync --extra otel")
    sys.exit(1)


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        provider = TracerProvider()
        exporter = AxonPushSpanExporter(
            client=client,
            channel_id=channel_id,
            service_name="my-api",
            environment=ENVIRONMENT or "dev",
        )
        provider.add_span_processor(SimpleSpanProcessor(exporter))
        trace.set_tracer_provider(provider)
        tracer = trace.get_tracer("my_app")

        with tracer.start_as_current_span("POST /chat") as req:
            req.set_attribute("http.method", "POST")
            req.set_attribute("http.route", "/chat")

            with tracer.start_as_current_span("llm.call") as llm:
                llm.set_attribute("model", "gpt-4o-mini")
                llm.set_attribute("prompt_tokens", 128)

            with tracer.start_as_current_span("db.query") as db:
                db.set_attribute("db.statement", "SELECT * FROM users WHERE id=$1")
                db.set_attribute("db.rows_affected", 1)

        provider.force_flush()
        provider.shutdown()

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None:
            print(f"\nSpans published ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name} (event_id={ev.event_id})")
            # Payload reads are separate and audited: client.telemetry.content(event_id)
            # requires content:read; search returns metadata only.


if __name__ == "__main__":
    main()
