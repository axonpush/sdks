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
        min_count (int | Unset): Fire only when at least this many entities are affected
        window_seconds (int | Unset): Only count entities that changed inside this window
    """

    after_seconds: int
    entity: str
    name: str
    state: str
    min_count: int | Unset = UNSET
    window_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        after_seconds = self.after_seconds

        entity = self.entity

        name = self.name

        state = self.state

        min_count = self.min_count

        window_seconds = self.window_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "afterSeconds": after_seconds,
                "entity": entity,
                "name": name,
                "state": state,
            }
        )
        if min_count is not UNSET:
            field_dict["minCount"] = min_count
        if window_seconds is not UNSET:
            field_dict["windowSeconds"] = window_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after_seconds = d.pop("afterSeconds")

        entity = d.pop("entity")

        name = d.pop("name")

        state = d.pop("state")

        min_count = d.pop("minCount", UNSET)

        window_seconds = d.pop("windowSeconds", UNSET)

        activity_alert = cls(
            after_seconds=after_seconds,
            entity=entity,
            name=name,
            state=state,
            min_count=min_count,
            window_seconds=window_seconds,
        )

        return activity_alert
