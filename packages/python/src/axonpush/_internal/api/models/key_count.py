from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyCount")


@_attrs_define
class KeyCount:
    """
    Attributes:
        count (int):
        key (str):
    """

    count: int
    key: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        key = d.pop("key")

        key_count = cls(
            count=count,
            key=key,
        )

        return key_count
