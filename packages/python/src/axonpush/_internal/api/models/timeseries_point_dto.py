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
        avg_ttft_ms (float):
        bucket (str):
        cache_read_tokens (int):
        cache_write_tokens (int):
        cost_usd (float):
        error_count (int):
        event_count (int):
        input_tokens (int):
        output_tokens (int):
        reasoning_tokens (int):
        total_tokens (int):
        trace_count (int):
    """

    avg_duration_ms: float
    avg_ttft_ms: float
    bucket: str
    cache_read_tokens: int
    cache_write_tokens: int
    cost_usd: float
    error_count: int
    event_count: int
    input_tokens: int
    output_tokens: int
    reasoning_tokens: int
    total_tokens: int
    trace_count: int

    def to_dict(self) -> dict[str, Any]:
        avg_duration_ms = self.avg_duration_ms

        avg_ttft_ms = self.avg_ttft_ms

        bucket = self.bucket

        cache_read_tokens = self.cache_read_tokens

        cache_write_tokens = self.cache_write_tokens

        cost_usd = self.cost_usd

        error_count = self.error_count

        event_count = self.event_count

        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        reasoning_tokens = self.reasoning_tokens

        total_tokens = self.total_tokens

        trace_count = self.trace_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avgDurationMs": avg_duration_ms,
                "avgTtftMs": avg_ttft_ms,
                "bucket": bucket,
                "cacheReadTokens": cache_read_tokens,
                "cacheWriteTokens": cache_write_tokens,
                "costUsd": cost_usd,
                "errorCount": error_count,
                "eventCount": event_count,
                "inputTokens": input_tokens,
                "outputTokens": output_tokens,
                "reasoningTokens": reasoning_tokens,
                "totalTokens": total_tokens,
                "traceCount": trace_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_duration_ms = d.pop("avgDurationMs")

        avg_ttft_ms = d.pop("avgTtftMs")

        bucket = d.pop("bucket")

        cache_read_tokens = d.pop("cacheReadTokens")

        cache_write_tokens = d.pop("cacheWriteTokens")

        cost_usd = d.pop("costUsd")

        error_count = d.pop("errorCount")

        event_count = d.pop("eventCount")

        input_tokens = d.pop("inputTokens")

        output_tokens = d.pop("outputTokens")

        reasoning_tokens = d.pop("reasoningTokens")

        total_tokens = d.pop("totalTokens")

        trace_count = d.pop("traceCount")

        timeseries_point_dto = cls(
            avg_duration_ms=avg_duration_ms,
            avg_ttft_ms=avg_ttft_ms,
            bucket=bucket,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
            cost_usd=cost_usd,
            error_count=error_count,
            event_count=event_count,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            reasoning_tokens=reasoning_tokens,
            total_tokens=total_tokens,
            trace_count=trace_count,
        )

        return timeseries_point_dto
