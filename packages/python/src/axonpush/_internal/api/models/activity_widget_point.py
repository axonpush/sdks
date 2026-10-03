from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityWidgetPoint")


@_attrs_define
class ActivityWidgetPoint:
    """
    Attributes:
        count (int):
        label (str):
        value (float | Unset):
    """

    count: int
    label: str
    value: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        label = self.label

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "label": label,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        label = d.pop("label")

        value = d.pop("value", UNSET)

        activity_widget_point = cls(
            count=count,
            label=label,
            value=value,
        )

        return activity_widget_point
