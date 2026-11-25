from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="IngestCategoryTotalDTO")


@_attrs_define
class IngestCategoryTotalDTO:
    """
    Attributes:
        accepted (int):
        category (str):
        dropped (int):
    """

    accepted: int
    category: str
    dropped: int

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        category = self.category

        dropped = self.dropped

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accepted": accepted,
                "category": category,
                "dropped": dropped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        category = d.pop("category")

        dropped = d.pop("dropped")

        ingest_category_total_dto = cls(
            accepted=accepted,
            category=category,
            dropped=dropped,
        )

        return ingest_category_total_dto
