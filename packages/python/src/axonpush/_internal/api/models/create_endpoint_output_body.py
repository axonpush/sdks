from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEndpointOutputBody")


@_attrs_define
class CreateEndpointOutputBody:
    """
    Attributes:
        active (bool):
        channel_id (str):
        created_at (str):
        endpoint_id (str):
        event_types (list[str] | None):
        has_secret (bool):
        raw_secret (str): Signing secret, only returned at creation time
        url (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
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
    raw_secret: str
    url: str
    schema: str | Unset = UNSET
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

        raw_secret = self.raw_secret

        url = self.url

        schema = self.schema

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
                "rawSecret": raw_secret,
                "url": url,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
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

        raw_secret = d.pop("rawSecret")

        url = d.pop("url")

        schema = d.pop("$schema", UNSET)

        description = d.pop("description", UNSET)

        org_id = d.pop("orgId", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        create_endpoint_output_body = cls(
            active=active,
            channel_id=channel_id,
            created_at=created_at,
            endpoint_id=endpoint_id,
            event_types=event_types,
            has_secret=has_secret,
            raw_secret=raw_secret,
            url=url,
            schema=schema,
            description=description,
            org_id=org_id,
            updated_at=updated_at,
        )

        return create_endpoint_output_body
