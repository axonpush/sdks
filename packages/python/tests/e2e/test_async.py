import uuid

import pytest

from axonpush import EventType
from axonpush.models import App, Channel, Event

pytestmark = pytest.mark.e2e


class TestAsyncEvents:
    async def test_publish_event(self, async_client, backend):
        ch = await async_client.channels.create(backend.app_id, f"async-ch-{uuid.uuid4().hex[:8]}")

        event = await async_client.events.publish(
            "async_action",
            {"key": "value"},
            channel_id=ch.channel_id,
            agent_id="async-agent",
            event_type=EventType.AGENT_TOOL_CALL_START,
        )
        assert isinstance(event, Event)
        assert event.event_id is not None

        try:
            await async_client.channels.delete(backend.app_id, ch.channel_id)
        except Exception:
            pass

    async def test_search_events(self, async_client, backend):
        ch = await async_client.channels.create(backend.app_id, f"async-ch-{uuid.uuid4().hex[:8]}")

        await async_client.events.publish("async_list_1", {"i": 1}, channel_id=ch.channel_id)

        result = await async_client.events.search(channel_id=ch.channel_id)
        assert result is not None
        assert isinstance(result.events, list)

        try:
            await async_client.channels.delete(backend.app_id, ch.channel_id)
        except Exception:
            pass


class TestAsyncApps:
    async def test_get_app(self, async_client, backend):
        app = await async_client.apps.get(backend.app_id)
        assert isinstance(app, App)
        assert app.app_id == backend.app_id


class TestAsyncChannels:
    async def test_crud(self, async_client, backend):
        name = f"async-ch-{uuid.uuid4().hex[:8]}"
        ch = await async_client.channels.create(backend.app_id, name)
        assert isinstance(ch, Channel)
        assert ch.name == name

        fetched = await async_client.channels.get(backend.app_id, ch.channel_id)
        assert fetched.channel_id == ch.channel_id

        try:
            await async_client.channels.delete(backend.app_id, ch.channel_id)
        except Exception:
            pass
