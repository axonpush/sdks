from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityAlert")


@_attrs_define
class ActivityAlert:
    """
    Attributes:
        after_seconds (int):
        entity (str):
        name (str):
        state (str):
    """

    after_seconds: int
    entity: str
    name: str
    state: str

    def to_dict(self) -> dict[str, Any]:
        after_seconds = self.after_seconds

        entity = self.entity

        name = self.name

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "afterSeconds": after_seconds,
                "entity": entity,
                "name": name,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after_seconds = d.pop("afterSeconds")

        entity = d.pop("entity")

        name = d.pop("name")

        state = d.pop("state")

        activity_alert = cls(
            after_seconds=after_seconds,
            entity=entity,
            name=name,
            state=state,
        )

        return activity_alert
