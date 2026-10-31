"""05 — Webhooks.

Register a webhook endpoint on a channel, publish an event that matches
the endpoint's filter, then poll the deliveries log.

Set ``WEBHOOK_URL`` to a receiver you control. There is no third-party
default destination.

Run::

    uv run examples/05_webhooks.py
"""

import time
from contextlib import ExitStack

from config import (
    BASE_URL,
    ENVIRONMENT,
    WEBHOOK_URL,
    require_credentials,
)

from resources import example_channel

require_credentials()

from axonpush import AxonPush, EventType  # noqa: E402


def main() -> None:
    if not WEBHOOK_URL:
        raise RuntimeError("Set WEBHOOK_URL to a receiver you control")
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
        ExitStack() as cleanup,
    ):
        endpoint = client.webhooks.create_endpoint(
            url=WEBHOOK_URL,
            channel_id=channel_id,
            event_types=["agent.error"],
            description="Error alerting webhook",
        )
        assert endpoint is not None
        endpoint_id = endpoint.endpoint_id
        cleanup.callback(client.webhooks.delete_endpoint, endpoint_id)
        print(f"Created endpoint: id={endpoint_id} url={endpoint.url}")
        print(f"  Filters: {endpoint.event_types}")
        # Store endpoint.raw_secret in your receiver's secret store; never log it.

        client.events.publish(
            "agent.step",
            {"status": "processing"},
            channel_id,
            event_type=EventType.AGENT_MESSAGE,
        )
        print("Published normal event (filtered out)")

        client.events.publish(
            "agent.crash",
            {"error": "ConnectionTimeout", "message": "Failed to reach external API"},
            channel_id,
            event_type=EventType.AGENT_ERROR,
            agent_id="data-fetcher",
        )
        print("Published error event (should trigger delivery)\n")

        print("Waiting for delivery...")
        time.sleep(3.0)

        deliveries = client.webhooks.deliveries(endpoint_id=endpoint_id)
        if deliveries:
            print(f"\n{len(deliveries)} delivery attempt(s):")
            for d in deliveries:
                http_code = int(d.status_code) if d.status_code else "-"
                print(f"  status={d.status} attempts={int(d.attempts)} http={http_code}")
        else:
            print("No deliveries recorded yet (they may still be in flight).")


if __name__ == "__main__":
    main()
