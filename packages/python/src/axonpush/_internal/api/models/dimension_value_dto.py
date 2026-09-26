from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DimensionValueDTO")


@_attrs_define
class DimensionValueDTO:
    """
    Attributes:
        value (str):
        last_seen (str | Unset):
    """

    value: str
    last_seen: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        last_seen = self.last_seen

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        last_seen = d.pop("lastSeen", UNSET)

        dimension_value_dto = cls(
            value=value,
            last_seen=last_seen,
        )

        return dimension_value_dto
