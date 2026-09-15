import time
import uuid

import pytest

from axonpush.models import EventType

pytestmark = pytest.mark.e2e


class TestTraces:
    def _publish_traced_events(self, client, channel):
        trace_id = str(uuid.uuid4())
        client.events.publish(
            "trace_start",
            {"step": "begin"},
            channel_id=channel.channel_id,
            agent_id="tracer",
            trace_id=trace_id,
            event_type=EventType.AGENT_START,
        )
        client.events.publish(
            "trace_tool",
            {"tool": "search"},
            channel_id=channel.channel_id,
            agent_id="tracer",
            trace_id=trace_id,
            event_type=EventType.AGENT_TOOL_CALL_START,
        )
        client.events.publish(
            "trace_end",
            {"step": "finish"},
            channel_id=channel.channel_id,
            agent_id="tracer",
            trace_id=trace_id,
            event_type=EventType.AGENT_END,
        )
        return trace_id

    def test_list_traces(self, client, channel):
        trace_id = self._publish_traced_events(client, channel)
        time.sleep(0.5)
        result = client.traces.list()
        assert result is not None
        trace_ids = [t.trace_id for t in (result.traces or [])]
        assert trace_id in trace_ids

    def test_get_trace(self, client, channel):
        trace_id = self._publish_traced_events(client, channel)
        time.sleep(0.5)
        detail = client.traces.get(trace_id)
        assert detail is not None
        assert detail.trace_id == trace_id
        spans = detail.spans or []
        assert len(spans) >= 3

    def test_traces_v2_alias_still_works(self, client, channel):
        self._publish_traced_events(client, channel)
        time.sleep(0.5)
        result = client.traces_v2.list()
        assert result is not None
