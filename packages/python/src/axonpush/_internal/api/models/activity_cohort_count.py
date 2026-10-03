from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityCohortCount")


@_attrs_define
class ActivityCohortCount:
    """
    Attributes:
        client (str):
        count (int):
        side (str):
    """

    client: str
    count: int
    side: str

    def to_dict(self) -> dict[str, Any]:
        client = self.client

        count = self.count

        side = self.side

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "client": client,
                "count": count,
                "side": side,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client = d.pop("client")

        count = d.pop("count")

        side = d.pop("side")

        activity_cohort_count = cls(
            client=client,
            count=count,
            side=side,
        )

        return activity_cohort_count
