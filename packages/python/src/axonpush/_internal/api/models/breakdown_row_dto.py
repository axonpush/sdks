from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BreakdownRowDTO")


@_attrs_define
class BreakdownRowDTO:
    """
    Attributes:
        cost_usd (float):
        event_count (int):
        key (str):
        total_tokens (int | Unset):
    """

    cost_usd: float
    event_count: int
    key: str
    total_tokens: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cost_usd = self.cost_usd

        event_count = self.event_count

        key = self.key

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costUsd": cost_usd,
                "eventCount": event_count,
                "key": key,
            }
        )
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_usd = d.pop("costUsd")

        event_count = d.pop("eventCount")

        key = d.pop("key")

        total_tokens = d.pop("totalTokens", UNSET)

        breakdown_row_dto = cls(
            cost_usd=cost_usd,
            event_count=event_count,
            key=key,
            total_tokens=total_tokens,
        )

        return breakdown_row_dto
