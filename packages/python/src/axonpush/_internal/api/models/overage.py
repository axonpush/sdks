from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Overage")


@_attrs_define
class Overage:
    """
    Attributes:
        events_per_unit (int):
        unit_price_cents (int):
    """

    events_per_unit: int
    unit_price_cents: int

    def to_dict(self) -> dict[str, Any]:
        events_per_unit = self.events_per_unit

        unit_price_cents = self.unit_price_cents

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eventsPerUnit": events_per_unit,
                "unitPriceCents": unit_price_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events_per_unit = d.pop("eventsPerUnit")

        unit_price_cents = d.pop("unitPriceCents")

        overage = cls(
            events_per_unit=events_per_unit,
            unit_price_cents=unit_price_cents,
        )

        return overage
