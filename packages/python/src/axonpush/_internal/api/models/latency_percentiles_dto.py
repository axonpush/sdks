from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LatencyPercentilesDTO")


@_attrs_define
class LatencyPercentilesDTO:
    """
    Attributes:
        max_duration_ms (float):
        max_ttft_ms (float):
        p_50_duration_ms (float):
        p_50_ttft_ms (float):
        p_95_duration_ms (float):
        p_95_ttft_ms (float):
        p_99_duration_ms (float):
        p_99_ttft_ms (float):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    max_duration_ms: float
    max_ttft_ms: float
    p_50_duration_ms: float
    p_50_ttft_ms: float
    p_95_duration_ms: float
    p_95_ttft_ms: float
    p_99_duration_ms: float
    p_99_ttft_ms: float
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_duration_ms = self.max_duration_ms

        max_ttft_ms = self.max_ttft_ms

        p_50_duration_ms = self.p_50_duration_ms

        p_50_ttft_ms = self.p_50_ttft_ms

        p_95_duration_ms = self.p_95_duration_ms

        p_95_ttft_ms = self.p_95_ttft_ms

        p_99_duration_ms = self.p_99_duration_ms

        p_99_ttft_ms = self.p_99_ttft_ms

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "maxDurationMs": max_duration_ms,
                "maxTtftMs": max_ttft_ms,
                "p50DurationMs": p_50_duration_ms,
                "p50TtftMs": p_50_ttft_ms,
                "p95DurationMs": p_95_duration_ms,
                "p95TtftMs": p_95_ttft_ms,
                "p99DurationMs": p_99_duration_ms,
                "p99TtftMs": p_99_ttft_ms,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_duration_ms = d.pop("maxDurationMs")

        max_ttft_ms = d.pop("maxTtftMs")

        p_50_duration_ms = d.pop("p50DurationMs")

        p_50_ttft_ms = d.pop("p50TtftMs")

        p_95_duration_ms = d.pop("p95DurationMs")

        p_95_ttft_ms = d.pop("p95TtftMs")

        p_99_duration_ms = d.pop("p99DurationMs")

        p_99_ttft_ms = d.pop("p99TtftMs")

        schema = d.pop("$schema", UNSET)

        latency_percentiles_dto = cls(
            max_duration_ms=max_duration_ms,
            max_ttft_ms=max_ttft_ms,
            p_50_duration_ms=p_50_duration_ms,
            p_50_ttft_ms=p_50_ttft_ms,
            p_95_duration_ms=p_95_duration_ms,
            p_95_ttft_ms=p_95_ttft_ms,
            p_99_duration_ms=p_99_duration_ms,
            p_99_ttft_ms=p_99_ttft_ms,
            schema=schema,
        )

        return latency_percentiles_dto
