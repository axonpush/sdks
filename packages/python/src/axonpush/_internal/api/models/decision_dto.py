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
        event_id (str | Unset):
        model (str | Unset):
        operation_name (str | Unset):
        parent_span_id (str | Unset):
        provider (str | Unset):
        semantic_kind (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        status (str | Unset):
        task_id (str | Unset):
        tool_name (str | Unset):
        trace_id (str | Unset):
    """

    cost_usd: float
    event_type: str
    occurred_at: str
    app_id: str | Unset = UNSET
    budget_approaching: str | Unset = UNSET
    enforcement_action: str | Unset = UNSET
    event_id: str | Unset = UNSET
    model: str | Unset = UNSET
    operation_name: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    semantic_kind: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    status: str | Unset = UNSET
    task_id: str | Unset = UNSET
    tool_name: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cost_usd = self.cost_usd

        event_type = self.event_type

        occurred_at = self.occurred_at

        app_id = self.app_id

        budget_approaching = self.budget_approaching

        enforcement_action = self.enforcement_action

        event_id = self.event_id

        model = self.model

        operation_name = self.operation_name

        parent_span_id = self.parent_span_id

        provider = self.provider

        semantic_kind = self.semantic_kind

        source = self.source

        span_id = self.span_id

        status = self.status

        task_id = self.task_id

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
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if model is not UNSET:
            field_dict["model"] = model
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if parent_span_id is not UNSET:
            field_dict["parentSpanId"] = parent_span_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if status is not UNSET:
            field_dict["status"] = status
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
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

        event_id = d.pop("eventId", UNSET)

        model = d.pop("model", UNSET)

        operation_name = d.pop("operationName", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        provider = d.pop("provider", UNSET)

        semantic_kind = d.pop("semanticKind", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("spanId", UNSET)

        status = d.pop("status", UNSET)

        task_id = d.pop("taskId", UNSET)

        tool_name = d.pop("toolName", UNSET)

        trace_id = d.pop("traceId", UNSET)

        decision_dto = cls(
            cost_usd=cost_usd,
            event_type=event_type,
            occurred_at=occurred_at,
            app_id=app_id,
            budget_approaching=budget_approaching,
            enforcement_action=enforcement_action,
            event_id=event_id,
            model=model,
            operation_name=operation_name,
            parent_span_id=parent_span_id,
            provider=provider,
            semantic_kind=semantic_kind,
            source=source,
            span_id=span_id,
            status=status,
            task_id=task_id,
            tool_name=tool_name,
            trace_id=trace_id,
        )

        return decision_dto
