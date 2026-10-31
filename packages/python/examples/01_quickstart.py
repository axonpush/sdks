"""01 — Quickstart.

Create an app and channel, publish a few events, list them, then clean up.

Run::

    uv run examples/01_quickstart.py
"""

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush, EventType  # noqa: E402


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        # Reuse caller-supplied IDs when present; otherwise spin up scratch resources.

        # Publishes are async-ingested. The returned Event carries event_id +
        # status on acceptance; search results appear once the write is projected.
        # Read full content separately through the audited telemetry resource.
        steps = [
            (
                "task.started",
                {"task": "summarize article", "url": "https://example.com"},
                EventType.AGENT_START,
            ),
            ("task.progress", {"progress": 50, "status": "fetching content"}, "custom"),
            (
                "task.completed",
                {"summary": "Article discusses AI advances in 2026."},
                EventType.AGENT_END,
            ),
        ]
        for identifier, payload, event_type in steps:
            ev = client.events.publish(
                identifier,
                payload,
                channel_id,
                agent_id="research-agent",
                event_type=event_type,
            )
            assert ev is not None
            print(f"Published: {identifier} (event_id={ev.event_id}, status={ev.status})")

        listing = client.events.search(channel_id=channel_id, limit=10)
        if listing is not None:
            print(f"\nChannel has {len((listing.events or []))} event(s) listed:")
            for ev in listing.events or []:
                print(f"  [{ev.event_type}] {ev.operation_name}")


if __name__ == "__main__":
    main()
