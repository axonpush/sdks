from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverviewBodyEventsStruct")


@_attrs_define
class OverviewBodyEventsStruct:
    """
    Attributes:
        this_cycle (int):
        today (int):
        total (int):
    """

    this_cycle: int
    today: int
    total: int

    def to_dict(self) -> dict[str, Any]:
        this_cycle = self.this_cycle

        today = self.today

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "thisCycle": this_cycle,
                "today": today,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        this_cycle = d.pop("thisCycle")

        today = d.pop("today")

        total = d.pop("total")

        overview_body_events_struct = cls(
            this_cycle=this_cycle,
            today=today,
            total=total,
        )

        return overview_body_events_struct
