from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EfficacyRowDTO")


@_attrs_define
class EfficacyRowDTO:
    """
    Attributes:
        action (str):
        avg_latency_ms (float):
        detector (str):
        max_latency_ms (float):
        target (str):
        violation_count (int):
    """

    action: str
    avg_latency_ms: float
    detector: str
    max_latency_ms: float
    target: str
    violation_count: int

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        avg_latency_ms = self.avg_latency_ms

        detector = self.detector

        max_latency_ms = self.max_latency_ms

        target = self.target

        violation_count = self.violation_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "avgLatencyMs": avg_latency_ms,
                "detector": detector,
                "maxLatencyMs": max_latency_ms,
                "target": target,
                "violationCount": violation_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        avg_latency_ms = d.pop("avgLatencyMs")

        detector = d.pop("detector")

        max_latency_ms = d.pop("maxLatencyMs")

        target = d.pop("target")

        violation_count = d.pop("violationCount")

        efficacy_row_dto = cls(
            action=action,
            avg_latency_ms=avg_latency_ms,
            detector=detector,
            max_latency_ms=max_latency_ms,
            target=target,
            violation_count=violation_count,
        )

        return efficacy_row_dto
