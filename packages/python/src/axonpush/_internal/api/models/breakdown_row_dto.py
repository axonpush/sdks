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
        avg_duration_ms (float):
        cost_usd (float):
        error_count (int):
        event_count (int):
        input_tokens (int):
        key (str):
        output_tokens (int):
        total_tokens (int):
    """

    avg_duration_ms: float
    cost_usd: float
    error_count: int
    event_count: int
    input_tokens: int
    key: str
    output_tokens: int
    total_tokens: int

    def to_dict(self) -> dict[str, Any]:
        avg_duration_ms = self.avg_duration_ms

        cost_usd = self.cost_usd

        error_count = self.error_count

        event_count = self.event_count

        input_tokens = self.input_tokens

        key = self.key

        output_tokens = self.output_tokens

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avgDurationMs": avg_duration_ms,
                "costUsd": cost_usd,
                "errorCount": error_count,
                "eventCount": event_count,
                "inputTokens": input_tokens,
                "key": key,
                "outputTokens": output_tokens,
                "totalTokens": total_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_duration_ms = d.pop("avgDurationMs")

        cost_usd = d.pop("costUsd")

        error_count = d.pop("errorCount")

        event_count = d.pop("eventCount")

        input_tokens = d.pop("inputTokens")

        key = d.pop("key")

        output_tokens = d.pop("outputTokens")

        total_tokens = d.pop("totalTokens")

        breakdown_row_dto = cls(
            avg_duration_ms=avg_duration_ms,
            cost_usd=cost_usd,
            error_count=error_count,
            event_count=event_count,
            input_tokens=input_tokens,
            key=key,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
        )

        return breakdown_row_dto
