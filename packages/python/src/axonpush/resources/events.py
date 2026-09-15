"""Events resource — publish (``POST /event``) and search (``GET /events``)."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from axonpush._internal.api.api.event import create_event as _create_op
from axonpush._internal.api.api.events import events_search as _search_op
from axonpush._internal.api.models import (
    EventBody,
    EventBodyMetadata,
    EventBodyPayload,
)
from axonpush._internal.api.types import UNSET
from axonpush._tracing import get_or_create_trace
from axonpush.models import Event, EventType

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _coerce_event_type(value: EventType | str | None) -> str | object:
    if value is None:
        return UNSET
    if isinstance(value, EventType):
        return value.value
    return value


def _filter_kwargs(values: dict[str, Any]) -> dict[str, Any]:
    """Drop keys whose value is ``None`` so the generated op sees ``UNSET``."""
    return {k: v for k, v in values.items() if v is not None}


def _build_event_body(
    *,
    identifier: str,
    payload: dict[str, Any],
    channel_id: str,
    agent_id: str | None,
    trace_id: str | None,
    span_id: str | None,
    parent_span_id: str | None,
    dedup_key: str | None,
    event_type: EventType | str | None,
    metadata: dict[str, Any] | None,
    prompt_id: str | None,
    prompt_version_id: str | None,
    redact: Callable[[Any], Any] | None = None,
) -> EventBody:
    """Assemble the generated :class:`EventBody` with ``UNSET`` for omitted optionals."""
    trace = get_or_create_trace(trace_id)
    resolved_trace = trace.trace_id
    resolved_span = span_id if span_id is not None else trace.next_span_id()

    payload_dto = EventBodyPayload()
    payload_dto.additional_properties = dict(redact(payload) if redact is not None else payload)

    metadata_dto: EventBodyMetadata | object = UNSET
    canonical_metadata = dict(metadata or {})
    if prompt_id is not None:
        canonical_metadata["gen_ai.prompt.id"] = prompt_id
    if prompt_version_id is not None:
        canonical_metadata["gen_ai.prompt.version"] = prompt_version_id
    if canonical_metadata:
        md = EventBodyMetadata()
        md.additional_properties = dict(
            redact(canonical_metadata) if redact is not None else canonical_metadata
        )
        metadata_dto = md

    return EventBody(
        channel_id=channel_id,
        identifier=identifier,
        payload=payload_dto,
        agent_id=agent_id if agent_id is not None else UNSET,
        trace_id=resolved_trace,
        span_id=resolved_span,
        parent_span_id=parent_span_id if parent_span_id is not None else UNSET,
        dedup_key=dedup_key if dedup_key is not None else UNSET,
        event_type=_coerce_event_type(event_type),  # type: ignore[arg-type]
        metadata=metadata_dto,  # type: ignore[arg-type]
    )


def _client_redactor(client: object) -> Callable[[Any], Any] | None:
    redactor = getattr(client, "_redact_telemetry", None)
    return redactor if callable(redactor) else None


class Events:
    """Publish and search events."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def publish(
        self,
        identifier: str,
        payload: dict[str, Any],
        channel_id: str,
        *,
        agent_id: str | None = None,
        trace_id: str | None = None,
        span_id: str | None = None,
        parent_span_id: str | None = None,
        dedup_key: str | None = None,
        event_type: EventType | str | None = None,
        metadata: dict[str, Any] | None = None,
        prompt_id: str | None = None,
        prompt_version_id: str | None = None,
    ) -> Event | None:
        """Publish a single event to a channel via ``POST /event``.

        Args:
            identifier: Event identifier / operation name.
            payload: Event body.
            channel_id: Target channel id.
            agent_id: Optional agent that emitted the event.
            trace_id: Optional trace id; one is auto-created when omitted.
            span_id: Optional span id for span linking.
            parent_span_id: Optional parent span id.
            dedup_key: Optional idempotency key for the ingest pipeline.
            event_type: Enum or string. Defaults to ``custom`` server-side.
            metadata: Free-form metadata map.
            prompt_id: Optional prompt registry identifier (folded into metadata).
            prompt_version_id: Optional prompt version (folded into metadata).

        Returns:
            The :class:`Event` ingest ack (``event_id`` + ``status``), or
            ``None`` if ``fail_open`` swallowed a transport error.

        Raises:
            AxonPushError: When ``fail_open`` is False and the call fails.
        """
        body = _build_event_body(
            identifier=identifier,
            payload=payload,
            channel_id=channel_id,
            agent_id=agent_id,
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=parent_span_id,
            dedup_key=dedup_key,
            event_type=event_type,
            metadata=metadata,
            prompt_id=prompt_id,
            prompt_version_id=prompt_version_id,
            redact=_client_redactor(self._client),
        )
        return self._client._invoke(_create_op, body=body)

    def search(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
        app_id: str | None = None,
        channel_id: str | None = None,
        environment_id: str | None = None,
        event_type: str | None = None,
        source: str | None = None,
        status: str | None = None,
        trace_id: str | None = None,
        q: str | None = None,
        attr_key: str | None = None,
        attr_value: str | None = None,
    ) -> Any | None:
        """Search events across the organization via ``GET /events``.

        All filters are AND-ed; omit a filter to include everything.

        Args:
            since: ISO 8601 datetime, inclusive lower bound.
            until: ISO 8601 datetime, exclusive upper bound.
            limit: Page size.
            app_id: Restrict to a single app id.
            channel_id: Restrict to a single channel id.
            environment_id: Restrict to a single environment id.
            event_type: Filter by canonical event type.
            source: Filter by ingest source (``app``, ``sentry``, ``otlp``).
            status: Filter by event status.
            trace_id: Filter by trace id.
            q: Case-insensitive free-text match over event fields.
            attr_key: Attribute key to match.
            attr_value: Attribute value to match.

        Returns:
            A :class:`SearchEventsOutputBody` (``events`` list) or ``None`` on
            fail-open.
        """
        kwargs = _filter_kwargs(
            {
                "since": since,
                "until": until,
                "limit": limit,
                "app_id": app_id,
                "channel_id": channel_id,
                "environment_id": environment_id,
                "event_type": event_type,
                "source": source,
                "status": status,
                "trace_id": trace_id,
                "q": q,
                "attr_key": attr_key,
                "attr_value": attr_value,
            }
        )
        return self._client._invoke(_search_op, **kwargs)


class AsyncEvents:
    """Async sibling of :class:`Events`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def publish(
        self,
        identifier: str,
        payload: dict[str, Any],
        channel_id: str,
        *,
        agent_id: str | None = None,
        trace_id: str | None = None,
        span_id: str | None = None,
        parent_span_id: str | None = None,
        dedup_key: str | None = None,
        event_type: EventType | str | None = None,
        metadata: dict[str, Any] | None = None,
        prompt_id: str | None = None,
        prompt_version_id: str | None = None,
    ) -> Event | None:
        """Publish a single event to a channel. See :meth:`Events.publish`."""
        body = _build_event_body(
            identifier=identifier,
            payload=payload,
            channel_id=channel_id,
            agent_id=agent_id,
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=parent_span_id,
            dedup_key=dedup_key,
            event_type=event_type,
            metadata=metadata,
            prompt_id=prompt_id,
            prompt_version_id=prompt_version_id,
            redact=_client_redactor(self._client),
        )
        return await self._client._invoke(_create_op, body=body)

    async def search(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
        app_id: str | None = None,
        channel_id: str | None = None,
        environment_id: str | None = None,
        event_type: str | None = None,
        source: str | None = None,
        status: str | None = None,
        trace_id: str | None = None,
        q: str | None = None,
        attr_key: str | None = None,
        attr_value: str | None = None,
    ) -> Any | None:
        """Search events. See :meth:`Events.search`."""
        kwargs = _filter_kwargs(
            {
                "since": since,
                "until": until,
                "limit": limit,
                "app_id": app_id,
                "channel_id": channel_id,
                "environment_id": environment_id,
                "event_type": event_type,
                "source": source,
                "status": status,
                "trace_id": trace_id,
                "q": q,
                "attr_key": attr_key,
                "attr_value": attr_value,
            }
        )
        return await self._client._invoke(_search_op, **kwargs)
