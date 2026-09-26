from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagValueCountDTO")


@_attrs_define
class TagValueCountDTO:
    """
    Attributes:
        count (int):
        value (str):
    """

    count: int
    value: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        value = d.pop("value")

        tag_value_count_dto = cls(
            count=count,
            value=value,
        )

        return tag_value_count_dto
