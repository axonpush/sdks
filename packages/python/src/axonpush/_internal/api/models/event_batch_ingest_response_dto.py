from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_ingest_response_dto import EventIngestResponseDto


T = TypeVar("T", bound="EventBatchIngestResponseDto")


@_attrs_define
class EventBatchIngestResponseDto:
    """
    Attributes:
        accepted (float): Number of events accepted onto the ingest path.
        data (list[EventIngestResponseDto]): One entry per submitted event, in the order they were submitted.
        environment_id (None | str | Unset):
    """

    accepted: float
    data: list[EventIngestResponseDto]
    environment_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_ingest_response_dto import EventIngestResponseDto

        accepted = self.accepted

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "data": data,
            }
        )
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_ingest_response_dto import EventIngestResponseDto

        d = dict(src_dict)
        accepted = d.pop("accepted")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = EventIngestResponseDto.from_dict(data_item_data)

            data.append(data_item)

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        event_batch_ingest_response_dto = cls(
            accepted=accepted,
            data=data,
            environment_id=environment_id,
        )

        event_batch_ingest_response_dto.additional_properties = d
        return event_batch_ingest_response_dto

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
