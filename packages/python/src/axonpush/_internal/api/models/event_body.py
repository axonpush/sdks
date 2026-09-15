from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_body_metadata import EventBodyMetadata
    from ..models.event_body_payload import EventBodyPayload


T = TypeVar("T", bound="EventBody")


@_attrs_define
class EventBody:
    """
    Attributes:
        channel_id (str): Target channel id
        identifier (str): Event identifier / operation name
        payload (EventBodyPayload): Event payload
        schema (str | Unset): A URL to the JSON Schema for this object.
        agent_id (str | Unset):
        dedup_key (str | Unset):
        event_type (str | Unset): Canonical event type; defaults to custom
        metadata (EventBodyMetadata | Unset):
        parent_span_id (str | Unset):
        span_id (str | Unset):
        sync (bool | Unset): Ignored; ingest is always asynchronous
        trace_id (str | Unset):
    """

    channel_id: str
    identifier: str
    payload: EventBodyPayload
    schema: str | Unset = UNSET
    agent_id: str | Unset = UNSET
    dedup_key: str | Unset = UNSET
    event_type: str | Unset = UNSET
    metadata: EventBodyMetadata | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    sync: bool | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_body_metadata import EventBodyMetadata
        from ..models.event_body_payload import EventBodyPayload

        channel_id = self.channel_id

        identifier = self.identifier

        payload = self.payload.to_dict()

        schema = self.schema

        agent_id = self.agent_id

        dedup_key = self.dedup_key

        event_type = self.event_type

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        parent_span_id = self.parent_span_id

        span_id = self.span_id

        sync = self.sync

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channel_id": channel_id,
                "identifier": identifier,
                "payload": payload,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if dedup_key is not UNSET:
            field_dict["dedupKey"] = dedup_key
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if parent_span_id is not UNSET:
            field_dict["parentSpanId"] = parent_span_id
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if sync is not UNSET:
            field_dict["sync"] = sync
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_body_metadata import EventBodyMetadata
        from ..models.event_body_payload import EventBodyPayload

        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        identifier = d.pop("identifier")

        payload = EventBodyPayload.from_dict(d.pop("payload"))

        schema = d.pop("$schema", UNSET)

        agent_id = d.pop("agentId", UNSET)

        dedup_key = d.pop("dedupKey", UNSET)

        event_type = d.pop("eventType", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: EventBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EventBodyMetadata.from_dict(_metadata)

        parent_span_id = d.pop("parentSpanId", UNSET)

        span_id = d.pop("spanId", UNSET)

        sync = d.pop("sync", UNSET)

        trace_id = d.pop("traceId", UNSET)

        event_body = cls(
            channel_id=channel_id,
            identifier=identifier,
            payload=payload,
            schema=schema,
            agent_id=agent_id,
            dedup_key=dedup_key,
            event_type=event_type,
            metadata=metadata,
            parent_span_id=parent_span_id,
            span_id=span_id,
            sync=sync,
            trace_id=trace_id,
        )

        return event_body
