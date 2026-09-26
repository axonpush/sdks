from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DimensionDTO")


@_attrs_define
class DimensionDTO:
    """
    Attributes:
        key (str):
        last_seen (str | Unset):
        source (str | Unset):
    """

    key: str
    last_seen: str | Unset = UNSET
    source: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        last_seen = self.last_seen

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
            }
        )
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        last_seen = d.pop("lastSeen", UNSET)

        source = d.pop("source", UNSET)

        dimension_dto = cls(
            key=key,
            last_seen=last_seen,
            source=source,
        )

        return dimension_dto
