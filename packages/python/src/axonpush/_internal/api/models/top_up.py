from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopUp")


@_attrs_define
class TopUp:
    """
    Attributes:
        events (int):
        price_usd (int):
    """

    events: int
    price_usd: int

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        price_usd = self.price_usd

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "priceUsd": price_usd,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = d.pop("events")

        price_usd = d.pop("priceUsd")

        top_up = cls(
            events=events,
            price_usd=price_usd,
        )

        return top_up
