from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentGateDto")


@_attrs_define
class ExperimentGateDto:
    """
    Attributes:
        max_cost_increase_percent (float | Unset):
        max_cost_usd (float | Unset):
        max_failure_rate (float | Unset):
        max_latency_increase_percent (float | Unset):
        max_latency_ms (float | Unset):
        min_score (float | Unset):
        min_score_delta (float | Unset):
    """

    max_cost_increase_percent: float | Unset = UNSET
    max_cost_usd: float | Unset = UNSET
    max_failure_rate: float | Unset = UNSET
    max_latency_increase_percent: float | Unset = UNSET
    max_latency_ms: float | Unset = UNSET
    min_score: float | Unset = UNSET
    min_score_delta: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_cost_increase_percent = self.max_cost_increase_percent

        max_cost_usd = self.max_cost_usd

        max_failure_rate = self.max_failure_rate

        max_latency_increase_percent = self.max_latency_increase_percent

        max_latency_ms = self.max_latency_ms

        min_score = self.min_score

        min_score_delta = self.min_score_delta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_cost_increase_percent is not UNSET:
            field_dict["maxCostIncreasePercent"] = max_cost_increase_percent
        if max_cost_usd is not UNSET:
            field_dict["maxCostUsd"] = max_cost_usd
        if max_failure_rate is not UNSET:
            field_dict["maxFailureRate"] = max_failure_rate
        if max_latency_increase_percent is not UNSET:
            field_dict["maxLatencyIncreasePercent"] = max_latency_increase_percent
        if max_latency_ms is not UNSET:
            field_dict["maxLatencyMs"] = max_latency_ms
        if min_score is not UNSET:
            field_dict["minScore"] = min_score
        if min_score_delta is not UNSET:
            field_dict["minScoreDelta"] = min_score_delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_cost_increase_percent = d.pop("maxCostIncreasePercent", UNSET)

        max_cost_usd = d.pop("maxCostUsd", UNSET)

        max_failure_rate = d.pop("maxFailureRate", UNSET)

        max_latency_increase_percent = d.pop("maxLatencyIncreasePercent", UNSET)

        max_latency_ms = d.pop("maxLatencyMs", UNSET)

        min_score = d.pop("minScore", UNSET)

        min_score_delta = d.pop("minScoreDelta", UNSET)

        experiment_gate_dto = cls(
            max_cost_increase_percent=max_cost_increase_percent,
            max_cost_usd=max_cost_usd,
            max_failure_rate=max_failure_rate,
            max_latency_increase_percent=max_latency_increase_percent,
            max_latency_ms=max_latency_ms,
            min_score=min_score,
            min_score_delta=min_score_delta,
        )

        experiment_gate_dto.additional_properties = d
        return experiment_gate_dto

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
