from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffValueDTO")


@_attrs_define
class DiffValueDTO:
    """
    Attributes:
        baseline_count (int):
        baseline_fraction (float):
        delta (float):
        selection_count (int):
        selection_fraction (float):
        value (str):
    """

    baseline_count: int
    baseline_fraction: float
    delta: float
    selection_count: int
    selection_fraction: float
    value: str

    def to_dict(self) -> dict[str, Any]:
        baseline_count = self.baseline_count

        baseline_fraction = self.baseline_fraction

        delta = self.delta

        selection_count = self.selection_count

        selection_fraction = self.selection_fraction

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "baselineCount": baseline_count,
                "baselineFraction": baseline_fraction,
                "delta": delta,
                "selectionCount": selection_count,
                "selectionFraction": selection_fraction,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        baseline_count = d.pop("baselineCount")

        baseline_fraction = d.pop("baselineFraction")

        delta = d.pop("delta")

        selection_count = d.pop("selectionCount")

        selection_fraction = d.pop("selectionFraction")

        value = d.pop("value")

        diff_value_dto = cls(
            baseline_count=baseline_count,
            baseline_fraction=baseline_fraction,
            delta=delta,
            selection_count=selection_count,
            selection_fraction=selection_fraction,
            value=value,
        )

        return diff_value_dto
