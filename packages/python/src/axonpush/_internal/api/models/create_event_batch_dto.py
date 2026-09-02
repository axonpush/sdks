from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_event_dto import BatchEventDto


T = TypeVar("T", bound="CreateEventBatchDto")


@_attrs_define
class CreateEventBatchDto:
    """
    Attributes:
        channel_id (str):
        events (list[BatchEventDto]):
        environment (str | Unset): Environment slug override applied to every event in the batch. Only honored when the
            API key has allowEnvironmentOverride=true.
    """

    channel_id: str
    events: list[BatchEventDto]
    environment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_event_dto import BatchEventDto

        channel_id = self.channel_id

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        environment = self.environment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "events": events,
            }
        )
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_event_dto import BatchEventDto

        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = BatchEventDto.from_dict(events_item_data)

            events.append(events_item)

        environment = d.pop("environment", UNSET)

        create_event_batch_dto = cls(
            channel_id=channel_id,
            events=events,
            environment=environment,
        )

        create_event_batch_dto.additional_properties = d
        return create_event_batch_dto

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
