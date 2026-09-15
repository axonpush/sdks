from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventOutputBody")


@_attrs_define
class EventOutputBody:
    """
    Attributes:
        event_id (str):
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    event_id: str
    status: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        status = self.status

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eventId": event_id,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        event_output_body = cls(
            event_id=event_id,
            status=status,
            schema=schema,
        )

        return event_output_body
