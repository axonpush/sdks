from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityEventMatch")


@_attrs_define
class ActivityEventMatch:
    """
    Attributes:
        event (str): Exact event name, or a prefix ending in *
    """

    event: str

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        activity_event_match = cls(
            event=event,
        )

        return activity_event_match
