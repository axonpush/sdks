"""12 — Structlog integration.

``axonpush_structlog_processor`` is a structlog processor. Drop it into
your processor chain and every event_dict gets forwarded to AxonPush as
an ``app.log`` event. The processor is non-destructive — it does not
touch the event_dict, so it composes cleanly with the rest of your chain.

Run::

    uv sync --extra structlog
    uv run examples/12_structlog.py
"""

import sys

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402

try:
    import structlog

    from axonpush.integrations.structlog import axonpush_structlog_processor
except ImportError:
    print("Install structlog integration: uv sync --extra structlog")
    sys.exit(1)


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        forwarder = axonpush_structlog_processor(
            client=client,
            channel_id=channel_id,
            service_name="my-api",
            environment=ENVIRONMENT or "dev",
        )

        structlog.configure(
            processors=[
                structlog.processors.add_log_level,
                structlog.processors.TimeStamper(fmt="iso"),
                forwarder,
                structlog.dev.ConsoleRenderer(),
            ],
        )

        log = structlog.get_logger("my_app")
        log.info("user signed in", user_id=42, method="oauth")
        log.warning("rate limit approaching", endpoint="/api/search", remaining=3)
        log.error("downstream timeout", endpoint="/api/search", elapsed_ms=5000)

        forwarder.flush(timeout=5.0)

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None:
            print(f"\nEvents published ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name} (event_id={ev.event_id})")
            # Payload reads are separate and audited: client.telemetry.content(event_id)
            # requires content:read; search returns metadata only.

        forwarder.close()
        # Prevent downstream examples in the same process from inheriting the
        # processor chain we just installed.
        structlog.reset_defaults()


if __name__ == "__main__":
    main()
