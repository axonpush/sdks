"""Unit tests for the ``Events`` / ``AsyncEvents`` resources.

These tests don't open a real HTTP connection. They instantiate the resource
with a fake ``_invoke``-shaped client and assert the body that would be
shipped to the backend (the generated DTO instance) matches the user's
inputs.
"""

from __future__ import annotations

from typing import Any, Awaitable, Callable

import pytest

from axonpush._internal.api.api.event import create_event as _create_op
from axonpush._internal.api.api.events import events_search as _search_op
from axonpush._internal.api.models import EventBody, EventOutputBody
from axonpush._internal.api.types import UNSET
from axonpush.models import EventType
from axonpush.resources.events import AsyncEvents, Events

CHANNEL_ID = "11111111-1111-1111-1111-111111111111"


def _ingest_response(**overrides: Any) -> EventOutputBody:
    base = {"event_id": "ev_1", "status": "queued"}
    base.update(overrides)
    return EventOutputBody(**base)


class FakeSyncClient:
    """Captures the op + kwargs the resource passes to ``_invoke``."""

    def __init__(self, return_value: Any = None) -> None:
        self.calls: list[tuple[Callable[..., Any], dict[str, Any]]] = []
        self.return_value = return_value

    def _invoke(self, op: Callable[..., Any], /, _coerce: Any = None, **kwargs: Any) -> Any:
        self.calls.append((op, kwargs))
        return _coerce(self.return_value) if _coerce else self.return_value


class FakeAsyncClient:
    def __init__(self, return_value: Any = None) -> None:
        self.calls: list[tuple[Callable[..., Awaitable[Any]], dict[str, Any]]] = []
        self.return_value = return_value

    async def _invoke(
        self, op: Callable[..., Awaitable[Any]], /, _coerce: Any = None, **kwargs: Any
    ) -> Any:
        self.calls.append((op, kwargs))
        return _coerce(self.return_value) if _coerce else self.return_value


class TestPublishBody:
    def test_minimal_publish_assembles_dto(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        result = events.publish("greet", {"hello": "world"}, channel_id=CHANNEL_ID)

        assert isinstance(result, EventOutputBody)
        op, kwargs = fake.calls[0]
        assert op is _create_op
        body = kwargs["body"]
        assert isinstance(body, EventBody)
        assert body.identifier == "greet"
        assert body.channel_id == CHANNEL_ID
        assert body.payload.additional_properties == {"hello": "world"}
        # trace_id auto-generated when none was provided (UUID4 string)
        assert isinstance(body.trace_id, str)
        assert len(body.trace_id) == 36 and body.trace_id.count("-") == 4
        # Optional fields default to UNSET
        assert body.agent_id is UNSET
        assert isinstance(body.span_id, str)
        assert len(body.span_id) == 16
        int(body.span_id, 16)
        assert body.metadata is UNSET
        assert body.event_type is UNSET
        assert body.dedup_key is UNSET

    def test_explicit_trace_id_is_passed_through(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        events.publish("x", {}, channel_id=CHANNEL_ID, trace_id="tr_explicit")

        body = fake.calls[0][1]["body"]
        assert body.trace_id == "tr_explicit"

    def test_string_event_type_is_kept_as_string(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        events.publish("x", {}, channel_id=CHANNEL_ID, event_type="agent.handoff")

        body = fake.calls[0][1]["body"]
        assert body.event_type == "agent.handoff"

    def test_enum_event_type_serialized_to_value(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        events.publish("x", {}, channel_id=CHANNEL_ID, event_type=EventType.AGENT_END)

        body = fake.calls[0][1]["body"]
        assert body.event_type == "agent.end"

    def test_metadata_wrapped_into_dto(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        events.publish("x", {}, channel_id=CHANNEL_ID, metadata={"src": "test"})

        body = fake.calls[0][1]["body"]
        assert body.metadata is not UNSET
        assert body.metadata.additional_properties == {"src": "test"}

    def test_prompt_lineage_uses_current_otel_genai_attributes(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        events.publish(
            "x",
            {},
            channel_id=CHANNEL_ID,
            metadata={"release": "2026.07"},
            prompt_id="support-answer",
            prompt_version_id="7",
        )

        body = fake.calls[0][1]["body"]
        assert body.metadata.additional_properties == {
            "release": "2026.07",
            "gen_ai.prompt.id": "support-answer",
            "gen_ai.prompt.version": "7",
        }

    def test_all_tracing_fields_propagate(self) -> None:
        fake = FakeSyncClient(return_value=_ingest_response())
        events = Events(fake)
        events.publish(
            "x",
            {},
            channel_id=CHANNEL_ID,
            agent_id="bot",
            trace_id="tr_fixed",
            span_id="sp_fixed",
            parent_span_id="sp_parent",
            dedup_key="dk_1",
        )

        body = fake.calls[0][1]["body"]
        assert body.agent_id == "bot"
        assert body.trace_id == "tr_fixed"
        assert body.span_id == "sp_fixed"
        assert body.parent_span_id == "sp_parent"
        assert body.to_dict()["parentSpanId"] == "sp_parent"
        assert body.dedup_key == "dk_1"

    def test_real_client_redacts_payload_before_building_request(self) -> None:
        from axonpush import AxonPush

        client = AxonPush(
            api_key="ak_test",
            tenant_id="org_test",
            base_url="http://example.test",
            redact_keys=["customerEmail"],
        )
        try:
            events = Events(client)
            with pytest.MonkeyPatch.context() as monkeypatch:
                monkeypatch.setattr(client, "_invoke", lambda *args, **kwargs: kwargs["body"])
                body = events.publish(
                    "safe",
                    {
                        "input": "private prompt",
                        "authorization": "Bearer secret",
                        "customerEmail": "person@example.com",
                        "label": "safe",
                    },
                    channel_id=CHANNEL_ID,
                )
            assert isinstance(body, EventBody)
            assert body.payload.additional_properties == {
                "input": "[REDACTED]",
                "authorization": "[REDACTED]",
                "customerEmail": "[REDACTED]",
                "label": "safe",
            }
        finally:
            client.close()


class TestSearch:
    def test_search_calls_search_op_with_no_args(self) -> None:
        fake = FakeSyncClient(return_value=None)
        events = Events(fake)
        events.search()

        op, kwargs = fake.calls[0]
        assert op is _search_op
        assert kwargs == {}

    def test_search_forwards_filters(self) -> None:
        fake = FakeSyncClient(return_value=None)
        events = Events(fake)
        events.search(channel_id=CHANNEL_ID, event_type="agent.start", limit=10)

        op, kwargs = fake.calls[0]
        assert op is _search_op
        assert kwargs == {"channel_id": CHANNEL_ID, "event_type": "agent.start", "limit": 10}


class TestAsyncEvents:
    @pytest.mark.asyncio
    async def test_async_publish_dispatches_asyncio_op(self) -> None:
        fake = FakeAsyncClient(return_value=_ingest_response())
        events = AsyncEvents(fake)
        result = await events.publish("greet", {}, channel_id=CHANNEL_ID)

        assert isinstance(result, EventOutputBody)
        op, kwargs = fake.calls[0]
        assert op is _create_op
        body = kwargs["body"]
        assert isinstance(body, EventBody)
        assert body.identifier == "greet"

    @pytest.mark.asyncio
    async def test_async_search_dispatches_asyncio_op(self) -> None:
        fake = FakeAsyncClient(return_value=None)
        events = AsyncEvents(fake)
        await events.search(channel_id=CHANNEL_ID)

        op, kwargs = fake.calls[0]
        assert op is _search_op
        assert kwargs == {"channel_id": CHANNEL_ID}
