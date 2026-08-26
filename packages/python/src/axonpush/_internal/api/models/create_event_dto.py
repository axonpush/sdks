from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_type import EventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_event_dto_metadata import CreateEventDtoMetadata
    from ..models.create_event_dto_payload import CreateEventDtoPayload


T = TypeVar("T", bound="CreateEventDto")


@_attrs_define
class CreateEventDto:
    """
    Attributes:
        channel_id (str):
        identifier (str):
        payload (CreateEventDtoPayload):
        agent_id (str | Unset):
        environment (str | Unset): Environment slug override. Only honored when the API key has
            allowEnvironmentOverride=true.
        event_type (EventType | Unset):  Default: EventType.CUSTOM.
        metadata (CreateEventDtoMetadata | Unset):
        parent_event_id (str | Unset):
        parent_span_id (str | Unset):
        span_id (str | Unset):
        sync (bool | Unset): When true, wait for the event to be persisted to the DB before returning. Use only for
            audit-critical calls — the default async path returns in under a millisecond. Default: False.
        trace_id (str | Unset):
    """

    channel_id: str
    identifier: str
    payload: CreateEventDtoPayload
    agent_id: str | Unset = UNSET
    environment: str | Unset = UNSET
    event_type: EventType | Unset = EventType.CUSTOM
    metadata: CreateEventDtoMetadata | Unset = UNSET
    parent_event_id: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    sync: bool | Unset = False
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_event_dto_metadata import CreateEventDtoMetadata
        from ..models.create_event_dto_payload import CreateEventDtoPayload

        channel_id = self.channel_id

        identifier = self.identifier

        payload = self.payload.to_dict()

        agent_id = self.agent_id

        environment = self.environment

        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        parent_event_id = self.parent_event_id

        parent_span_id = self.parent_span_id

        span_id = self.span_id

        sync = self.sync

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "identifier": identifier,
                "payload": payload,
            }
        )
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if environment is not UNSET:
            field_dict["environment"] = environment
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if parent_event_id is not UNSET:
            field_dict["parentEventId"] = parent_event_id
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
        from ..models.create_event_dto_metadata import CreateEventDtoMetadata
        from ..models.create_event_dto_payload import CreateEventDtoPayload

        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        identifier = d.pop("identifier")

        payload = CreateEventDtoPayload.from_dict(d.pop("payload"))

        agent_id = d.pop("agentId", UNSET)

        environment = d.pop("environment", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: EventType | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = EventType(_event_type)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateEventDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateEventDtoMetadata.from_dict(_metadata)

        parent_event_id = d.pop("parentEventId", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        span_id = d.pop("spanId", UNSET)

        sync = d.pop("sync", UNSET)

        trace_id = d.pop("traceId", UNSET)

        create_event_dto = cls(
            channel_id=channel_id,
            identifier=identifier,
            payload=payload,
            agent_id=agent_id,
            environment=environment,
            event_type=event_type,
            metadata=metadata,
            parent_event_id=parent_event_id,
            parent_span_id=parent_span_id,
            span_id=span_id,
            sync=sync,
            trace_id=trace_id,
        )

        create_event_dto.additional_properties = d
        return create_event_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
