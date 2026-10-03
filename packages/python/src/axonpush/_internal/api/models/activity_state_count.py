from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityStateCount")


@_attrs_define
class ActivityStateCount:
    """
    Attributes:
        active15m (int):
        count (int):
        entity (str):
        state (str):
    """

    active15m: int
    count: int
    entity: str
    state: str

    def to_dict(self) -> dict[str, Any]:
        active15m = self.active15m

        count = self.count

        entity = self.entity

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active15m": active15m,
                "count": count,
                "entity": entity,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active15m = d.pop("active15m")

        count = d.pop("count")

        entity = d.pop("entity")

        state = d.pop("state")

        activity_state_count = cls(
            active15m=active15m,
            count=count,
            entity=entity,
            state=state,
        )

        return activity_state_count
