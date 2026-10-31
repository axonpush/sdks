"""04 — Multi-agent handoff.

A planner agent delegates work to an executor agent. Both agents share the
same ``trace_id`` so the backend assembles the full execution path into one
trace, and we query its projected event metadata at the end.

Run::

    uv run examples/04_multi_agent.py
"""

import time
from typing import Any

from config import BASE_URL, ENVIRONMENT, require_credentials

from resources import example_channel

require_credentials()

from axonpush import AxonPush, EventType, get_or_create_trace  # noqa: E402


def main() -> None:
    with (
        AxonPush(base_url=BASE_URL, environment=ENVIRONMENT, fail_open=False) as client,
        example_channel(client) as channel_id,
    ):
        trace = get_or_create_trace()
        print(f"Trace: {trace.trace_id}\n")

        def emit(
            agent_id: str,
            identifier: str,
            payload: dict[str, Any],
            event_type: EventType,
            **extra: Any,
        ) -> None:
            client.events.publish(
                identifier,
                payload,
                channel_id,
                agent_id=agent_id,
                trace_id=trace.trace_id,
                span_id=trace.next_span_id(),
                event_type=event_type,
                **extra,
            )
            print(f"  [{agent_id}] {event_type.value}: {identifier}")

        emit(
            "planner",
            "plan.start",
            {"task": "Write a blog post about AI safety"},
            EventType.AGENT_START,
        )
        time.sleep(0.2)
        emit(
            "planner",
            "plan.outline",
            {"outline": ["Introduction", "Key risks", "Mitigation", "Conclusion"]},
            EventType.AGENT_MESSAGE,
        )
        time.sleep(0.2)
        emit(
            "planner",
            "handoff",
            {"target_agent": "executor", "task": "Write sections from outline"},
            EventType.AGENT_HANDOFF,
            metadata={"from_agent": "planner", "to_agent": "executor"},
        )
        time.sleep(0.2)
        emit("planner", "plan.end", {"status": "delegated"}, EventType.AGENT_END)
        time.sleep(0.3)

        emit("executor", "write.start", {"sections": 4}, EventType.AGENT_START)
        time.sleep(0.2)
        emit(
            "executor",
            "web_search",
            {"query": "AI safety current research 2026"},
            EventType.AGENT_TOOL_CALL_START,
            metadata={"tool_name": "web_search"},
        )
        time.sleep(0.4)
        emit(
            "executor",
            "web_search",
            {"results_count": 8},
            EventType.AGENT_TOOL_CALL_END,
            metadata={"tool_name": "web_search"},
        )
        time.sleep(0.2)
        emit(
            "executor",
            "write.draft",
            {"word_count": 1200, "sections_written": 4},
            EventType.AGENT_MESSAGE,
        )
        time.sleep(0.2)
        emit(
            "executor", "write.end", {"status": "success", "word_count": 1200}, EventType.AGENT_END
        )

        time.sleep(0.5)
        # Query projected metadata; ingestion may still be catching up.
        page = client.events.search(trace_id=trace.trace_id, limit=100)
        if page is not None:
            print(f"Visible trace events: {len(page.events or [])}")


if __name__ == "__main__":
    main()
