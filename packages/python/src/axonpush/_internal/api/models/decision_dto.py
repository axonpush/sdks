from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecisionDTO")


@_attrs_define
class DecisionDTO:
    """
    Attributes:
        cost_usd (float):
        event_type (str):
        occurred_at (str):
        app_id (str | Unset):
        budget_approaching (str | Unset):
        enforcement_action (str | Unset):
        model (str | Unset):
        parent_span_id (str | Unset):
        provider (str | Unset):
        semantic_kind (str | Unset):
        span_id (str | Unset):
        status (str | Unset):
        tool_name (str | Unset):
        trace_id (str | Unset):
    """

    cost_usd: float
    event_type: str
    occurred_at: str
    app_id: str | Unset = UNSET
    budget_approaching: str | Unset = UNSET
    enforcement_action: str | Unset = UNSET
    model: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    semantic_kind: str | Unset = UNSET
    span_id: str | Unset = UNSET
    status: str | Unset = UNSET
    tool_name: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cost_usd = self.cost_usd

        event_type = self.event_type

        occurred_at = self.occurred_at

        app_id = self.app_id

        budget_approaching = self.budget_approaching

        enforcement_action = self.enforcement_action

        model = self.model

        parent_span_id = self.parent_span_id

        provider = self.provider

        semantic_kind = self.semantic_kind

        span_id = self.span_id

        status = self.status

        tool_name = self.tool_name

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costUsd": cost_usd,
                "eventType": event_type,
                "occurredAt": occurred_at,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if budget_approaching is not UNSET:
            field_dict["budgetApproaching"] = budget_approaching
        if enforcement_action is not UNSET:
            field_dict["enforcementAction"] = enforcement_action
        if model is not UNSET:
            field_dict["model"] = model
        if parent_span_id is not UNSET:
            field_dict["parentSpanId"] = parent_span_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if status is not UNSET:
            field_dict["status"] = status
        if tool_name is not UNSET:
            field_dict["toolName"] = tool_name
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_usd = d.pop("costUsd")

        event_type = d.pop("eventType")

        occurred_at = d.pop("occurredAt")

        app_id = d.pop("appId", UNSET)

        budget_approaching = d.pop("budgetApproaching", UNSET)

        enforcement_action = d.pop("enforcementAction", UNSET)

        model = d.pop("model", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        provider = d.pop("provider", UNSET)

        semantic_kind = d.pop("semanticKind", UNSET)

        span_id = d.pop("spanId", UNSET)

        status = d.pop("status", UNSET)

        tool_name = d.pop("toolName", UNSET)

        trace_id = d.pop("traceId", UNSET)

        decision_dto = cls(
            cost_usd=cost_usd,
            event_type=event_type,
            occurred_at=occurred_at,
            app_id=app_id,
            budget_approaching=budget_approaching,
            enforcement_action=enforcement_action,
            model=model,
            parent_span_id=parent_span_id,
            provider=provider,
            semantic_kind=semantic_kind,
            span_id=span_id,
            status=status,
            tool_name=tool_name,
            trace_id=trace_id,
        )

        return decision_dto
