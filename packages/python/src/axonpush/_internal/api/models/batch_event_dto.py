from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_type import EventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_event_dto_metadata import BatchEventDtoMetadata
    from ..models.batch_event_dto_payload import BatchEventDtoPayload


T = TypeVar("T", bound="BatchEventDto")


@_attrs_define
class BatchEventDto:
    """
    Attributes:
        identifier (str):
        payload (BatchEventDtoPayload):
        agent_id (str | Unset):
        event_type (EventType | Unset):  Default: EventType.CUSTOM.
        metadata (BatchEventDtoMetadata | Unset):
        parent_event_id (str | Unset):
        parent_span_id (str | Unset):
        span_id (str | Unset):
        trace_id (str | Unset):
    """

    identifier: str
    payload: BatchEventDtoPayload
    agent_id: str | Unset = UNSET
    event_type: EventType | Unset = EventType.CUSTOM
    metadata: BatchEventDtoMetadata | Unset = UNSET
    parent_event_id: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_event_dto_metadata import BatchEventDtoMetadata
        from ..models.batch_event_dto_payload import BatchEventDtoPayload

        identifier = self.identifier

        payload = self.payload.to_dict()

        agent_id = self.agent_id

        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        parent_event_id = self.parent_event_id

        parent_span_id = self.parent_span_id

        span_id = self.span_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "payload": payload,
            }
        )
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
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
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_event_dto_metadata import BatchEventDtoMetadata
        from ..models.batch_event_dto_payload import BatchEventDtoPayload

        d = dict(src_dict)
        identifier = d.pop("identifier")

        payload = BatchEventDtoPayload.from_dict(d.pop("payload"))

        agent_id = d.pop("agentId", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: EventType | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = EventType(_event_type)

        _metadata = d.pop("metadata", UNSET)
        metadata: BatchEventDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BatchEventDtoMetadata.from_dict(_metadata)

        parent_event_id = d.pop("parentEventId", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        span_id = d.pop("spanId", UNSET)

        trace_id = d.pop("traceId", UNSET)

        batch_event_dto = cls(
            identifier=identifier,
            payload=payload,
            agent_id=agent_id,
            event_type=event_type,
            metadata=metadata,
            parent_event_id=parent_event_id,
            parent_span_id=parent_span_id,
            span_id=span_id,
            trace_id=trace_id,
        )

        batch_event_dto.additional_properties = d
        return batch_event_dto

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
