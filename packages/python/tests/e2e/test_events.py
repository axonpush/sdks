import pytest

from axonpush.models import Event, EventType

pytestmark = pytest.mark.e2e


class TestEvents:
    def test_publish_event(self, client, channel):
        event = client.events.publish(
            "test_action",
            {"key": "value"},
            channel_id=channel.channel_id,
            agent_id="test-agent",
            event_type=EventType.AGENT_TOOL_CALL_START,
        )
        assert isinstance(event, Event)
        assert event.event_id is not None

    def test_publish_with_string_event_type(self, client, channel):
        event = client.events.publish(
            "string_type_action",
            {"data": 123},
            channel_id=channel.channel_id,
            event_type="agent.tool_call.end",
        )
        assert event is not None
        assert event.event_id is not None

    def test_publish_with_enum_event_type(self, client, channel):
        event = client.events.publish(
            "enum_type_action",
            {"data": "test"},
            channel_id=channel.channel_id,
            event_type=EventType.AGENT_MESSAGE,
        )
        assert event is not None

    def test_publish_with_metadata(self, client, channel):
        meta = {"source": "test", "version": 1}
        ev = client.events.publish(
            "meta_action",
            {"data": "test"},
            channel_id=channel.channel_id,
            metadata=meta,
        )
        assert ev is not None

    def test_search_events(self, client, channel):
        client.events.publish(
            "search_test_1",
            {"order": 1},
            channel_id=channel.channel_id,
        )
        result = client.events.search(channel_id=channel.channel_id)
        assert result is not None
        assert isinstance(result.events, list)
