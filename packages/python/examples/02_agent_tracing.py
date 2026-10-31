"""02 — Agent tracing.

Walk a research agent through a multi-step task. Every event shares a
``trace_id`` so the backend can stitch them back into a single trace and
query projected event metadata at the end.

Run::

    uv run examples/02_agent_tracing.py
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
        agent_id = "research-agent"
        print(f"Trace: {trace.trace_id}\n")

        def emit(
            identifier: str, payload: dict[str, Any], event_type: EventType, **extra: Any
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

        emit(
            "research.start",
            {"goal": "Find recent papers on transformer architectures"},
            EventType.AGENT_START,
        )
        print("[start] research agent started")
        time.sleep(0.2)

        emit(
            "web_search",
            {"query": "transformer architecture papers 2026", "engine": "google_scholar"},
            EventType.AGENT_TOOL_CALL_START,
            metadata={"tool_name": "web_search"},
        )
        print("[tool_call.start] searching")
        time.sleep(0.4)

        emit(
            "web_search",
            {
                "results": [
                    {"title": "Attention Is Still All You Need", "year": 2026},
                    {"title": "Sparse Transformers at Scale", "year": 2026},
                ],
                "count": 2,
            },
            EventType.AGENT_TOOL_CALL_END,
            metadata={"tool_name": "web_search"},
        )
        print("[tool_call.end] found 2 papers")
        time.sleep(0.2)

        emit(
            "summary",
            {"message": "Found 2 relevant papers on transformer architectures from 2026."},
            EventType.AGENT_MESSAGE,
        )
        print("[agent.message] summary generated")
        time.sleep(0.2)

        emit("research.end", {"status": "success", "papers_found": 2}, EventType.AGENT_END)
        print("[end] research complete\n")

        # Backend ingest is eventually consistent — give it a beat before
        # querying projected trace events.
        time.sleep(0.5)
        # Query projected metadata; ingestion may still be catching up.
        page = client.events.search(trace_id=trace.trace_id, limit=100)
        if page is not None:
            print(f"Visible trace events: {len(page.events or [])}")


if __name__ == "__main__":
    main()
