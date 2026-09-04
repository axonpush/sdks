from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_v2_controller_stats_response_200_events_by_hour_item import (
        TraceV2ControllerStatsResponse200EventsByHourItem,
    )


T = TypeVar("T", bound="TraceV2ControllerStatsResponse200")


@_attrs_define
class TraceV2ControllerStatsResponse200:
    """
    Attributes:
        avg_trace_duration (float):
        error_count (float):
        error_rate (float):
        events_by_hour (list[TraceV2ControllerStatsResponse200EventsByHourItem]):
        events_today (float):
        total_events (float):
        total_traces (float):
        traces_today (float):
    """

    avg_trace_duration: float
    error_count: float
    error_rate: float
    events_by_hour: list[TraceV2ControllerStatsResponse200EventsByHourItem]
    events_today: float
    total_events: float
    total_traces: float
    traces_today: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_v2_controller_stats_response_200_events_by_hour_item import (
            TraceV2ControllerStatsResponse200EventsByHourItem,
        )

        avg_trace_duration = self.avg_trace_duration

        error_count = self.error_count

        error_rate = self.error_rate

        events_by_hour = []
        for events_by_hour_item_data in self.events_by_hour:
            events_by_hour_item = events_by_hour_item_data.to_dict()
            events_by_hour.append(events_by_hour_item)

        events_today = self.events_today

        total_events = self.total_events

        total_traces = self.total_traces

        traces_today = self.traces_today

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avgTraceDuration": avg_trace_duration,
                "errorCount": error_count,
                "errorRate": error_rate,
                "eventsByHour": events_by_hour,
                "eventsToday": events_today,
                "totalEvents": total_events,
                "totalTraces": total_traces,
                "tracesToday": traces_today,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_v2_controller_stats_response_200_events_by_hour_item import (
            TraceV2ControllerStatsResponse200EventsByHourItem,
        )

        d = dict(src_dict)
        avg_trace_duration = d.pop("avgTraceDuration")

        error_count = d.pop("errorCount")

        error_rate = d.pop("errorRate")

        events_by_hour = []
        _events_by_hour = d.pop("eventsByHour")
        for events_by_hour_item_data in _events_by_hour:
            events_by_hour_item = TraceV2ControllerStatsResponse200EventsByHourItem.from_dict(
                events_by_hour_item_data
            )

            events_by_hour.append(events_by_hour_item)

        events_today = d.pop("eventsToday")

        total_events = d.pop("totalEvents")

        total_traces = d.pop("totalTraces")

        traces_today = d.pop("tracesToday")

        trace_v2_controller_stats_response_200 = cls(
            avg_trace_duration=avg_trace_duration,
            error_count=error_count,
            error_rate=error_rate,
            events_by_hour=events_by_hour,
            events_today=events_today,
            total_events=total_events,
            total_traces=total_traces,
            traces_today=traces_today,
        )

        trace_v2_controller_stats_response_200.additional_properties = d
        return trace_v2_controller_stats_response_200

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
