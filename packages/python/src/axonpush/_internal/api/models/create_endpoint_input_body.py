from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEndpointInputBody")


@_attrs_define
class CreateEndpointInputBody:
    """
    Attributes:
        channel_id (str):
        url (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        description (str | Unset):
        event_types (list[str] | None | Unset): Event types to filter (empty = all)
    """

    channel_id: str
    url: str
    schema: str | Unset = UNSET
    description: str | Unset = UNSET
    event_types: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        url = self.url

        schema = self.schema

        description = self.description

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = self.event_types

        else:
            event_types = self.event_types

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channelId": channel_id,
                "url": url,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if description is not UNSET:
            field_dict["description"] = description
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channelId")

        url = d.pop("url")

        schema = d.pop("$schema", UNSET)

        description = d.pop("description", UNSET)

        def _parse_event_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_types = _parse_event_types(d.pop("eventTypes", UNSET))

        create_endpoint_input_body = cls(
            channel_id=channel_id,
            url=url,
            schema=schema,
            description=description,
            event_types=event_types,
        )

        return create_endpoint_input_body
