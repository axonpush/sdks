from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeatmapBandDTO")


@_attrs_define
class HeatmapBandDTO:
    """
    Attributes:
        hi_ms (float):
        lo_ms (float):
    """

    hi_ms: float
    lo_ms: float

    def to_dict(self) -> dict[str, Any]:
        hi_ms = self.hi_ms

        lo_ms = self.lo_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hiMs": hi_ms,
                "loMs": lo_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hi_ms = d.pop("hiMs")

        lo_ms = d.pop("loMs")

        heatmap_band_dto = cls(
            hi_ms=hi_ms,
            lo_ms=lo_ms,
        )

        return heatmap_band_dto
