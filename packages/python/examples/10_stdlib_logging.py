"""10 — Stdlib logging handler.

Ship records emitted via Python's built-in ``logging`` to AxonPush as
OpenTelemetry-shaped ``app.log`` events. This is the integration most
backend services want — FastAPI, Flask, and Django all funnel through
stdlib logging.

The handler installs a self-recursion filter that drops records from
``httpx`` / ``httpcore`` / ``axonpush`` so a publish never loops back
through the handler.

Run::

    uv run examples/10_stdlib_logging.py
"""

import logging

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush  # noqa: E402
from axonpush.integrations.logging_handler import AxonPushLoggingHandler  # noqa: E402


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        handler = AxonPushLoggingHandler(
            client=client,
            channel_id=channel_id,
            service_name="my-api",
            environment=ENVIRONMENT or "dev",
        )

        root = logging.getLogger()
        root.setLevel(logging.INFO)
        root.addHandler(handler)

        log = logging.getLogger("my_app.orders")
        log.info("order created", extra={"order_id": 1234, "total": 49.99})
        log.warning("stock low for sku=%s", "A-42", extra={"remaining": 3})
        try:
            raise RuntimeError("payment gateway timeout")
        except RuntimeError:
            log.exception("failed to charge card", extra={"order_id": 1234})

        # Drain in-flight HTTP calls before tearing down the channel/app so
        # the publish race doesn't drop the last record.
        handler.flush(timeout=5.0)
        root.removeHandler(handler)
        handler.close()

        listing = client.events.search(channel_id=channel_id, limit=20)
        if listing is not None:
            print(f"\nEvents published ({len((listing.events or []))}):")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name} (event_id={ev.event_id})")
            # Payload reads are separate and audited: client.telemetry.content(event_id)
            # requires content:read; search returns metadata only.


# --- Django integration snippet (reference) --------------------------------
#
# Add this to ``settings.py`` to wire the handler via dictConfig. The handler
# reads AXONPUSH_API_KEY / AXONPUSH_TENANT_ID from the environment if you
# don't pass an explicit ``client``.
#
#     LOGGING = {
#         "version": 1,
#         "disable_existing_loggers": False,
#         "handlers": {
#             "axonpush": {
#                 "class": "axonpush.integrations.logging_handler.AxonPushLoggingHandler",
#                 "channel_id": "ch_…",
#                 "service_name": "my-django-app",
#                 "exclude_loggers": ["django.db.backends"],
#             },
#             "console": {"class": "logging.StreamHandler"},
#         },
#         "root": {"handlers": ["axonpush", "console"], "level": "INFO"},
#     }


if __name__ == "__main__":
    main()
