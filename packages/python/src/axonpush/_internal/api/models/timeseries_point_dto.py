from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeseriesPointDTO")


@_attrs_define
class TimeseriesPointDTO:
    """
    Attributes:
        avg_duration_ms (float):
        bucket (str):
        cost_usd (float):
        error_count (int):
        event_count (int):
        total_tokens (int):
        trace_count (int):
    """

    avg_duration_ms: float
    bucket: str
    cost_usd: float
    error_count: int
    event_count: int
    total_tokens: int
    trace_count: int

    def to_dict(self) -> dict[str, Any]:
        avg_duration_ms = self.avg_duration_ms

        bucket = self.bucket

        cost_usd = self.cost_usd

        error_count = self.error_count

        event_count = self.event_count

        total_tokens = self.total_tokens

        trace_count = self.trace_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avgDurationMs": avg_duration_ms,
                "bucket": bucket,
                "costUsd": cost_usd,
                "errorCount": error_count,
                "eventCount": event_count,
                "totalTokens": total_tokens,
                "traceCount": trace_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_duration_ms = d.pop("avgDurationMs")

        bucket = d.pop("bucket")

        cost_usd = d.pop("costUsd")

        error_count = d.pop("errorCount")

        event_count = d.pop("eventCount")

        total_tokens = d.pop("totalTokens")

        trace_count = d.pop("traceCount")

        timeseries_point_dto = cls(
            avg_duration_ms=avg_duration_ms,
            bucket=bucket,
            cost_usd=cost_usd,
            error_count=error_count,
            event_count=event_count,
            total_tokens=total_tokens,
            trace_count=trace_count,
        )

        return timeseries_point_dto
