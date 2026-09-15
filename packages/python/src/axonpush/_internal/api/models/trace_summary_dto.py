from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceSummaryDTO")


@_attrs_define
class TraceSummaryDTO:
    """
    Attributes:
        cost_usd (float):
        duration_ms (float):
        ended_at (str):
        error_count (int):
        models (list[str] | None):
        providers (list[str] | None):
        span_count (int):
        started_at (str):
        total_tokens (int):
        trace_id (str):
    """

    cost_usd: float
    duration_ms: float
    ended_at: str
    error_count: int
    models: list[str] | None
    providers: list[str] | None
    span_count: int
    started_at: str
    total_tokens: int
    trace_id: str

    def to_dict(self) -> dict[str, Any]:
        cost_usd = self.cost_usd

        duration_ms = self.duration_ms

        ended_at = self.ended_at

        error_count = self.error_count

        models: list[str] | None
        if isinstance(self.models, list):
            models = self.models

        else:
            models = self.models

        providers: list[str] | None
        if isinstance(self.providers, list):
            providers = self.providers

        else:
            providers = self.providers

        span_count = self.span_count

        started_at = self.started_at

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costUsd": cost_usd,
                "durationMs": duration_ms,
                "endedAt": ended_at,
                "errorCount": error_count,
                "models": models,
                "providers": providers,
                "spanCount": span_count,
                "startedAt": started_at,
                "totalTokens": total_tokens,
                "traceId": trace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_usd = d.pop("costUsd")

        duration_ms = d.pop("durationMs")

        ended_at = d.pop("endedAt")

        error_count = d.pop("errorCount")

        def _parse_models(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                models_type_0 = cast(list[str], data)

                return models_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        models = _parse_models(d.pop("models"))

        def _parse_providers(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                providers_type_0 = cast(list[str], data)

                return providers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        providers = _parse_providers(d.pop("providers"))

        span_count = d.pop("spanCount")

        started_at = d.pop("startedAt")

        total_tokens = d.pop("totalTokens")

        trace_id = d.pop("traceId")

        trace_summary_dto = cls(
            cost_usd=cost_usd,
            duration_ms=duration_ms,
            ended_at=ended_at,
            error_count=error_count,
            models=models,
            providers=providers,
            span_count=span_count,
            started_at=started_at,
            total_tokens=total_tokens,
            trace_id=trace_id,
        )

        return trace_summary_dto
