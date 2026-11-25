from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="IngestOutcomeDTO")


@_attrs_define
class IngestOutcomeDTO:
    """
    Attributes:
        category (str):
        quantity (int):
        reason (str):
        source (str): sdk (client reports) | server (ingestion)
    """

    category: str
    quantity: int
    reason: str
    source: str

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        quantity = self.quantity

        reason = self.reason

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category": category,
                "quantity": quantity,
                "reason": reason,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        quantity = d.pop("quantity")

        reason = d.pop("reason")

        source = d.pop("source")

        ingest_outcome_dto = cls(
            category=category,
            quantity=quantity,
            reason=reason,
            source=source,
        )

        return ingest_outcome_dto
