from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndpointDTO")


@_attrs_define
class EndpointDTO:
    """
    Attributes:
        active (bool):
        channel_id (str):
        created_at (str):
        endpoint_id (str):
        event_types (list[str] | None):
        has_secret (bool):
        url (str):
        description (str | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    active: bool
    channel_id: str
    created_at: str
    endpoint_id: str
    event_types: list[str] | None
    has_secret: bool
    url: str
    description: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        channel_id = self.channel_id

        created_at = self.created_at

        endpoint_id = self.endpoint_id

        event_types: list[str] | None
        if isinstance(self.event_types, list):
            event_types = self.event_types

        else:
            event_types = self.event_types

        has_secret = self.has_secret

        url = self.url

        description = self.description

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
                "channelId": channel_id,
                "createdAt": created_at,
                "endpointId": endpoint_id,
                "eventTypes": event_types,
                "hasSecret": has_secret,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        channel_id = d.pop("channelId")

        created_at = d.pop("createdAt")

        endpoint_id = d.pop("endpointId")

        def _parse_event_types(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        event_types = _parse_event_types(d.pop("eventTypes"))

        has_secret = d.pop("hasSecret")

        url = d.pop("url")

        description = d.pop("description", UNSET)

        org_id = d.pop("orgId", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        endpoint_dto = cls(
            active=active,
            channel_id=channel_id,
            created_at=created_at,
            endpoint_id=endpoint_id,
            event_types=event_types,
            has_secret=has_secret,
            url=url,
            description=description,
            org_id=org_id,
            updated_at=updated_at,
        )

        return endpoint_dto
