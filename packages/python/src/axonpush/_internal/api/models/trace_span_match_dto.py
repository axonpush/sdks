from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceSpanMatchDto")


@_attrs_define
class TraceSpanMatchDto:
    """
    Attributes:
        event_id (str):
        occurred_at (datetime.datetime):
        snippet (str): Text either side of the first match, for highlighting.
        agent_name (str | Unset):
        duration_ms (float | Unset):
        model (str | Unset):
        operation_name (str | Unset):
        parent_span_id (str | Unset):
        semantic_kind (str | Unset):
        service_name (str | Unset):
        span_id (str | Unset):
        status (str | Unset):
        tool_name (str | Unset):
    """

    event_id: str
    occurred_at: datetime.datetime
    snippet: str
    agent_name: str | Unset = UNSET
    duration_ms: float | Unset = UNSET
    model: str | Unset = UNSET
    operation_name: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    semantic_kind: str | Unset = UNSET
    service_name: str | Unset = UNSET
    span_id: str | Unset = UNSET
    status: str | Unset = UNSET
    tool_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        occurred_at = self.occurred_at.isoformat()

        snippet = self.snippet

        agent_name = self.agent_name

        duration_ms = self.duration_ms

        model = self.model

        operation_name = self.operation_name

        parent_span_id = self.parent_span_id

        semantic_kind = self.semantic_kind

        service_name = self.service_name

        span_id = self.span_id

        status = self.status

        tool_name = self.tool_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "occurredAt": occurred_at,
                "snippet": snippet,
            }
        )
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if model is not UNSET:
            field_dict["model"] = model
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if parent_span_id is not UNSET:
            field_dict["parentSpanId"] = parent_span_id
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if status is not UNSET:
            field_dict["status"] = status
        if tool_name is not UNSET:
            field_dict["toolName"] = tool_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId")

        occurred_at = isoparse(d.pop("occurredAt"))

        snippet = d.pop("snippet")

        agent_name = d.pop("agentName", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        model = d.pop("model", UNSET)

        operation_name = d.pop("operationName", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        semantic_kind = d.pop("semanticKind", UNSET)

        service_name = d.pop("serviceName", UNSET)

        span_id = d.pop("spanId", UNSET)

        status = d.pop("status", UNSET)

        tool_name = d.pop("toolName", UNSET)

        trace_span_match_dto = cls(
            event_id=event_id,
            occurred_at=occurred_at,
            snippet=snippet,
            agent_name=agent_name,
            duration_ms=duration_ms,
            model=model,
            operation_name=operation_name,
            parent_span_id=parent_span_id,
            semantic_kind=semantic_kind,
            service_name=service_name,
            span_id=span_id,
            status=status,
            tool_name=tool_name,
        )

        trace_span_match_dto.additional_properties = d
        return trace_span_match_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
