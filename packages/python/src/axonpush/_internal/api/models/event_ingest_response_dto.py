from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_ingest_response_dto_environment_id_type_0 import (
        EventIngestResponseDtoEnvironmentIdType0,
    )


T = TypeVar("T", bound="EventIngestResponseDto")


@_attrs_define
class EventIngestResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        dedup_key (str):
        event_id (str):
        id (str): Alias of eventId, populated by the global IdAliasInterceptor.
        identifier (str):
        queued (bool):
        duplicate (bool | Unset):
        environment_id (EventIngestResponseDtoEnvironmentIdType0 | None | Unset):
    """

    created_at: datetime.datetime
    dedup_key: str
    event_id: str
    id: str
    identifier: str
    queued: bool
    duplicate: bool | Unset = UNSET
    environment_id: EventIngestResponseDtoEnvironmentIdType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_ingest_response_dto_environment_id_type_0 import (
            EventIngestResponseDtoEnvironmentIdType0,
        )

        created_at = self.created_at.isoformat()

        dedup_key = self.dedup_key

        event_id = self.event_id

        id = self.id

        identifier = self.identifier

        queued = self.queued

        duplicate = self.duplicate

        environment_id: dict[str, Any] | None | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        elif isinstance(self.environment_id, EventIngestResponseDtoEnvironmentIdType0):
            environment_id = self.environment_id.to_dict()
        else:
            environment_id = self.environment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "dedupKey": dedup_key,
                "eventId": event_id,
                "id": id,
                "identifier": identifier,
                "queued": queued,
            }
        )
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_ingest_response_dto_environment_id_type_0 import (
            EventIngestResponseDtoEnvironmentIdType0,
        )

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        dedup_key = d.pop("dedupKey")

        event_id = d.pop("eventId")

        id = d.pop("id")

        identifier = d.pop("identifier")

        queued = d.pop("queued")

        duplicate = d.pop("duplicate", UNSET)

        def _parse_environment_id(
            data: object,
        ) -> EventIngestResponseDtoEnvironmentIdType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_id_type_0 = EventIngestResponseDtoEnvironmentIdType0.from_dict(data)

                return environment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventIngestResponseDtoEnvironmentIdType0 | None | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        event_ingest_response_dto = cls(
            created_at=created_at,
            dedup_key=dedup_key,
            event_id=event_id,
            id=id,
            identifier=identifier,
            queued=queued,
            duplicate=duplicate,
            environment_id=environment_id,
        )

        event_ingest_response_dto.additional_properties = d
        return event_ingest_response_dto

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
