"""06 — Async client.

``AsyncAxonPush`` is the asyncio mirror of ``AxonPush``. The resource
methods are awaitable; everything else (resource layout, kwargs) is
identical.

Run::

    uv run examples/06_async_client.py
"""

import asyncio
import time

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import async_example_channel

require_credentials()

from axonpush import AsyncAxonPush, EventType  # noqa: E402


async def publish_agent_events(
    client: AsyncAxonPush, channel_id: str, agent_id: str, count: int
) -> tuple[str, int]:
    for i in range(count):
        await client.events.publish(
            f"{agent_id}.step",
            {"step": i + 1, "agent": agent_id},
            channel_id,
            agent_id=agent_id,
            event_type=EventType.AGENT_MESSAGE,
        )
    return agent_id, count


async def main() -> None:
    async with (
        AsyncAxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        async_example_channel(client) as channel_id,
    ):
        print(f"channel={channel_id}\n")

        agents = ["agent-alpha", "agent-beta", "agent-gamma", "agent-delta", "agent-epsilon"]
        per_agent = 10

        print(f"Publishing {per_agent} events from {len(agents)} agents concurrently...")
        start = time.monotonic()
        results = await asyncio.gather(
            *[publish_agent_events(client, channel_id, a, per_agent) for a in agents]
        )
        elapsed = time.monotonic() - start
        total = sum(c for _, c in results)
        print(f"Published {total} events in {elapsed:.2f}s ({total / elapsed:.0f} events/sec)\n")
        for agent_id, count in results:
            print(f"  {agent_id}: {count} events")

        listing = await client.events.search(channel_id=channel_id, limit=100)
        if listing is not None:
            print(f"\nTotal events visible: {len((listing.events or []))}")


if __name__ == "__main__":
    asyncio.run(main())
