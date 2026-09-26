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
        customer (str):
        duration_ms (float):
        ended_at (str):
        environment (str):
        error_count (int):
        first_error_type (str):
        models (list[str] | None):
        outcome (str):
        providers (list[str] | None):
        release (str):
        root_span_name (str):
        service_name (str):
        session_id (str):
        span_count (int):
        started_at (str):
        total_tokens (int):
        trace_id (str):
        workflow (str):
    """

    cost_usd: float
    customer: str
    duration_ms: float
    ended_at: str
    environment: str
    error_count: int
    first_error_type: str
    models: list[str] | None
    outcome: str
    providers: list[str] | None
    release: str
    root_span_name: str
    service_name: str
    session_id: str
    span_count: int
    started_at: str
    total_tokens: int
    trace_id: str
    workflow: str

    def to_dict(self) -> dict[str, Any]:
        cost_usd = self.cost_usd

        customer = self.customer

        duration_ms = self.duration_ms

        ended_at = self.ended_at

        environment = self.environment

        error_count = self.error_count

        first_error_type = self.first_error_type

        models: list[str] | None
        if isinstance(self.models, list):
            models = self.models

        else:
            models = self.models

        outcome = self.outcome

        providers: list[str] | None
        if isinstance(self.providers, list):
            providers = self.providers

        else:
            providers = self.providers

        release = self.release

        root_span_name = self.root_span_name

        service_name = self.service_name

        session_id = self.session_id

        span_count = self.span_count

        started_at = self.started_at

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        workflow = self.workflow

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costUsd": cost_usd,
                "customer": customer,
                "durationMs": duration_ms,
                "endedAt": ended_at,
                "environment": environment,
                "errorCount": error_count,
                "firstErrorType": first_error_type,
                "models": models,
                "outcome": outcome,
                "providers": providers,
                "release": release,
                "rootSpanName": root_span_name,
                "serviceName": service_name,
                "sessionId": session_id,
                "spanCount": span_count,
                "startedAt": started_at,
                "totalTokens": total_tokens,
                "traceId": trace_id,
                "workflow": workflow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_usd = d.pop("costUsd")

        customer = d.pop("customer")

        duration_ms = d.pop("durationMs")

        ended_at = d.pop("endedAt")

        environment = d.pop("environment")

        error_count = d.pop("errorCount")

        first_error_type = d.pop("firstErrorType")

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

        outcome = d.pop("outcome")

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

        release = d.pop("release")

        root_span_name = d.pop("rootSpanName")

        service_name = d.pop("serviceName")

        session_id = d.pop("sessionId")

        span_count = d.pop("spanCount")

        started_at = d.pop("startedAt")

        total_tokens = d.pop("totalTokens")

        trace_id = d.pop("traceId")

        workflow = d.pop("workflow")

        trace_summary_dto = cls(
            cost_usd=cost_usd,
            customer=customer,
            duration_ms=duration_ms,
            ended_at=ended_at,
            environment=environment,
            error_count=error_count,
            first_error_type=first_error_type,
            models=models,
            outcome=outcome,
            providers=providers,
            release=release,
            root_span_name=root_span_name,
            service_name=service_name,
            session_id=session_id,
            span_count=span_count,
            started_at=started_at,
            total_tokens=total_tokens,
            trace_id=trace_id,
            workflow=workflow,
        )

        return trace_summary_dto
