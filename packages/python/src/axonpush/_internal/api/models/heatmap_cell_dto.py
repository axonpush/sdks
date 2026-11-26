from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeatmapCellDTO")


@_attrs_define
class HeatmapCellDTO:
    """
    Attributes:
        band (int):
        count (int):
        t (int):
    """

    band: int
    count: int
    t: int

    def to_dict(self) -> dict[str, Any]:
        band = self.band

        count = self.count

        t = self.t

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "band": band,
                "count": count,
                "t": t,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        band = d.pop("band")

        count = d.pop("count")

        t = d.pop("t")

        heatmap_cell_dto = cls(
            band=band,
            count=count,
            t=t,
        )

        return heatmap_cell_dto
