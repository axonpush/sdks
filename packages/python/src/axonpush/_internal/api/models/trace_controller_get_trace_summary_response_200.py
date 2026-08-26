from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceControllerGetTraceSummaryResponse200")


@_attrs_define
class TraceControllerGetTraceSummaryResponse200:
    """
    Attributes:
        agents (list[str]):
        duration (float):
        end_time (datetime.datetime):
        error_count (float):
        event_count (float):
        event_types (list[str]):
        handoff_count (float):
        start_time (datetime.datetime):
        tool_call_count (float):
        trace_id (str):
        cost_usd (float | None | Unset): Known reported/estimated cost. Omitted when pricing is unknown.
        status (str | Unset):
        total_tokens (float | Unset):
    """

    agents: list[str]
    duration: float
    end_time: datetime.datetime
    error_count: float
    event_count: float
    event_types: list[str]
    handoff_count: float
    start_time: datetime.datetime
    tool_call_count: float
    trace_id: str
    cost_usd: float | None | Unset = UNSET
    status: str | Unset = UNSET
    total_tokens: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agents = self.agents

        duration = self.duration

        end_time = self.end_time.isoformat()

        error_count = self.error_count

        event_count = self.event_count

        event_types = self.event_types

        handoff_count = self.handoff_count

        start_time = self.start_time.isoformat()

        tool_call_count = self.tool_call_count

        trace_id = self.trace_id

        cost_usd: float | None | Unset
        if isinstance(self.cost_usd, Unset):
            cost_usd = UNSET
        else:
            cost_usd = self.cost_usd

        status = self.status

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agents": agents,
                "duration": duration,
                "endTime": end_time,
                "errorCount": error_count,
                "eventCount": event_count,
                "eventTypes": event_types,
                "handoffCount": handoff_count,
                "startTime": start_time,
                "toolCallCount": tool_call_count,
                "traceId": trace_id,
            }
        )
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if status is not UNSET:
            field_dict["status"] = status
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agents = cast(list[str], d.pop("agents"))

        duration = d.pop("duration")

        end_time = isoparse(d.pop("endTime"))

        error_count = d.pop("errorCount")

        event_count = d.pop("eventCount")

        event_types = cast(list[str], d.pop("eventTypes"))

        handoff_count = d.pop("handoffCount")

        start_time = isoparse(d.pop("startTime"))

        tool_call_count = d.pop("toolCallCount")

        trace_id = d.pop("traceId")

        def _parse_cost_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_usd = _parse_cost_usd(d.pop("costUsd", UNSET))

        status = d.pop("status", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        trace_controller_get_trace_summary_response_200 = cls(
            agents=agents,
            duration=duration,
            end_time=end_time,
            error_count=error_count,
            event_count=event_count,
            event_types=event_types,
            handoff_count=handoff_count,
            start_time=start_time,
            tool_call_count=tool_call_count,
            trace_id=trace_id,
            cost_usd=cost_usd,
            status=status,
            total_tokens=total_tokens,
        )

        trace_controller_get_trace_summary_response_200.additional_properties = d
        return trace_controller_get_trace_summary_response_200

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
