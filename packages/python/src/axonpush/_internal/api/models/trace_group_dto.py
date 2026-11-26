from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceGroupDTO")


@_attrs_define
class TraceGroupDTO:
    """
    Attributes:
        activity_class (str):
        app_id (str):
        environment (str):
        failed (bool):
        first_error_type (str):
        first_seen (str):
        group_key (str):
        last_seen (str):
        max_duration_ms (float):
        min_duration_ms (float):
        outcome (str):
        representative_trace_id (str):
        root_span_name (str):
        service_name (str):
        trace_count (int):
    """

    activity_class: str
    app_id: str
    environment: str
    failed: bool
    first_error_type: str
    first_seen: str
    group_key: str
    last_seen: str
    max_duration_ms: float
    min_duration_ms: float
    outcome: str
    representative_trace_id: str
    root_span_name: str
    service_name: str
    trace_count: int

    def to_dict(self) -> dict[str, Any]:
        activity_class = self.activity_class

        app_id = self.app_id

        environment = self.environment

        failed = self.failed

        first_error_type = self.first_error_type

        first_seen = self.first_seen

        group_key = self.group_key

        last_seen = self.last_seen

        max_duration_ms = self.max_duration_ms

        min_duration_ms = self.min_duration_ms

        outcome = self.outcome

        representative_trace_id = self.representative_trace_id

        root_span_name = self.root_span_name

        service_name = self.service_name

        trace_count = self.trace_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "activityClass": activity_class,
                "appId": app_id,
                "environment": environment,
                "failed": failed,
                "firstErrorType": first_error_type,
                "firstSeen": first_seen,
                "groupKey": group_key,
                "lastSeen": last_seen,
                "maxDurationMs": max_duration_ms,
                "minDurationMs": min_duration_ms,
                "outcome": outcome,
                "representativeTraceId": representative_trace_id,
                "rootSpanName": root_span_name,
                "serviceName": service_name,
                "traceCount": trace_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_class = d.pop("activityClass")

        app_id = d.pop("appId")

        environment = d.pop("environment")

        failed = d.pop("failed")

        first_error_type = d.pop("firstErrorType")

        first_seen = d.pop("firstSeen")

        group_key = d.pop("groupKey")

        last_seen = d.pop("lastSeen")

        max_duration_ms = d.pop("maxDurationMs")

        min_duration_ms = d.pop("minDurationMs")

        outcome = d.pop("outcome")

        representative_trace_id = d.pop("representativeTraceId")

        root_span_name = d.pop("rootSpanName")

        service_name = d.pop("serviceName")

        trace_count = d.pop("traceCount")

        trace_group_dto = cls(
            activity_class=activity_class,
            app_id=app_id,
            environment=environment,
            failed=failed,
            first_error_type=first_error_type,
            first_seen=first_seen,
            group_key=group_key,
            last_seen=last_seen,
            max_duration_ms=max_duration_ms,
            min_duration_ms=min_duration_ms,
            outcome=outcome,
            representative_trace_id=representative_trace_id,
            root_span_name=root_span_name,
            service_name=service_name,
            trace_count=trace_count,
        )

        return trace_group_dto
