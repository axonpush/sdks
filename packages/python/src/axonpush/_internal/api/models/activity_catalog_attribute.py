from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityCatalogAttribute")


@_attrs_define
class ActivityCatalogAttribute:
    """
    Attributes:
        count (int): Observations carrying the key; for undeclared keys, how many were dropped
        declared (bool):
        key (str):
    """

    count: int
    declared: bool
    key: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        declared = self.declared

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "declared": declared,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        declared = d.pop("declared")

        key = d.pop("key")

        activity_catalog_attribute = cls(
            count=count,
            declared=declared,
            key=key,
        )

        return activity_catalog_attribute
