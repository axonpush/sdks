from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_signal_kind import TraceSignalKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceFlowNodeResponseDto")


@_attrs_define
class TraceIntelligenceFlowNodeResponseDto:
    """
    Attributes:
        description (str):
        id (str):
        label (str):
        percentage (float):
        signal_kind (TraceSignalKind):
        trace_count (float):
        confidence (float | Unset):
        representative_trace_ids (list[str] | Unset):
        trend (float | Unset):
        unclustered (bool | Unset):
    """

    description: str
    id: str
    label: str
    percentage: float
    signal_kind: TraceSignalKind
    trace_count: float
    confidence: float | Unset = UNSET
    representative_trace_ids: list[str] | Unset = UNSET
    trend: float | Unset = UNSET
    unclustered: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        label = self.label

        percentage = self.percentage

        signal_kind = self.signal_kind.value

        trace_count = self.trace_count

        confidence = self.confidence

        representative_trace_ids: list[str] | Unset = UNSET
        if not isinstance(self.representative_trace_ids, Unset):
            representative_trace_ids = self.representative_trace_ids

        trend = self.trend

        unclustered = self.unclustered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "id": id,
                "label": label,
                "percentage": percentage,
                "signalKind": signal_kind,
                "traceCount": trace_count,
            }
        )
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if representative_trace_ids is not UNSET:
            field_dict["representativeTraceIds"] = representative_trace_ids
        if trend is not UNSET:
            field_dict["trend"] = trend
        if unclustered is not UNSET:
            field_dict["unclustered"] = unclustered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        id = d.pop("id")

        label = d.pop("label")

        percentage = d.pop("percentage")

        signal_kind = TraceSignalKind(d.pop("signalKind"))

        trace_count = d.pop("traceCount")

        confidence = d.pop("confidence", UNSET)

        representative_trace_ids = cast(list[str], d.pop("representativeTraceIds", UNSET))

        trend = d.pop("trend", UNSET)

        unclustered = d.pop("unclustered", UNSET)

        trace_intelligence_flow_node_response_dto = cls(
            description=description,
            id=id,
            label=label,
            percentage=percentage,
            signal_kind=signal_kind,
            trace_count=trace_count,
            confidence=confidence,
            representative_trace_ids=representative_trace_ids,
            trend=trend,
            unclustered=unclustered,
        )

        trace_intelligence_flow_node_response_dto.additional_properties = d
        return trace_intelligence_flow_node_response_dto

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
