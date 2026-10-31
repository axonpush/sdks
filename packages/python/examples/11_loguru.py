"""11 — Loguru integration.

Loguru is a popular alternative to stdlib logging. The
``create_axonpush_loguru_sink`` helper returns a callable that you pass to
``logger.add(sink, serialize=True)``. ``serialize=True`` is required —
Loguru hands the sink a JSON string, which the sink then parses.

Run::

    uv sync --extra loguru
    uv run examples/11_loguru.py
"""

import sys

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402

try:
    from loguru import logger

    from axonpush.integrations.loguru import create_axonpush_loguru_sink
except ImportError:
    print("Install Loguru integration: uv sync --extra loguru")
    sys.exit(1)


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        sink = create_axonpush_loguru_sink(
            client=client,
            channel_id=channel_id,
            service_name="my-api",
            environment=ENVIRONMENT or "dev",
        )
        sink_id = logger.add(sink, serialize=True)

        logger.info("user signed in", user_id=42, method="oauth")
        logger.warning("rate limit approaching", endpoint="/api/search", remaining=3)
        try:
            raise RuntimeError("downstream timeout")
        except RuntimeError:
            logger.exception("search backend failed", endpoint="/api/search")

        sink.flush(timeout=5.0)
        logger.remove(sink_id)
        sink.close()

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None:
            print(f"\nEvents published ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name} (event_id={ev.event_id})")
            # Payload reads are separate and audited: client.telemetry.content(event_id)
            # requires content:read; search returns metadata only.


if __name__ == "__main__":
    main()
