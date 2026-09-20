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
        avg_duration_ms (float | Unset):
        error_count (int | Unset):
        total_tokens (int | Unset):
    """

    cost_usd: float
    event_count: int
    key: str
    avg_duration_ms: float | Unset = UNSET
    error_count: int | Unset = UNSET
    total_tokens: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cost_usd = self.cost_usd

        event_count = self.event_count

        key = self.key

        avg_duration_ms = self.avg_duration_ms

        error_count = self.error_count

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costUsd": cost_usd,
                "eventCount": event_count,
                "key": key,
            }
        )
        if avg_duration_ms is not UNSET:
            field_dict["avgDurationMs"] = avg_duration_ms
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_usd = d.pop("costUsd")

        event_count = d.pop("eventCount")

        key = d.pop("key")

        avg_duration_ms = d.pop("avgDurationMs", UNSET)

        error_count = d.pop("errorCount", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        breakdown_row_dto = cls(
            cost_usd=cost_usd,
            event_count=event_count,
            key=key,
            avg_duration_ms=avg_duration_ms,
            error_count=error_count,
            total_tokens=total_tokens,
        )

        return breakdown_row_dto
