from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gate_run_source import GateRunSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentGateDto")


@_attrs_define
class ExperimentGateDto:
    """
    Attributes:
        git_branch (str | Unset): Branch to record against the decision. Falls back to the experiment.
        git_commit (str | Unset): Commit to record against the decision. Falls back to the experiment.
        max_cost_increase_percent (float | Unset): Maximum cost increase against the baseline, in percent.
        max_cost_usd (float | Unset): Maximum total run cost in USD.
        max_failure_rate (float | Unset): Maximum share of dataset items allowed to error, 0-1.
        max_latency_increase_percent (float | Unset): Maximum latency increase against the baseline, in percent.
        max_latency_ms (float | Unset): Maximum mean latency in milliseconds.
        min_score (float | Unset): Minimum absolute score the candidate must reach.
        min_score_delta (float | Unset): Smallest score change against the baseline that still passes. Usually negative.
        release (str | Unset): Release to record against the decision. Falls back to the experiment.
        source (GateRunSource | Unset): Who asked for the decision. Defaults to api.
    """

    git_branch: str | Unset = UNSET
    git_commit: str | Unset = UNSET
    max_cost_increase_percent: float | Unset = UNSET
    max_cost_usd: float | Unset = UNSET
    max_failure_rate: float | Unset = UNSET
    max_latency_increase_percent: float | Unset = UNSET
    max_latency_ms: float | Unset = UNSET
    min_score: float | Unset = UNSET
    min_score_delta: float | Unset = UNSET
    release: str | Unset = UNSET
    source: GateRunSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_branch = self.git_branch

        git_commit = self.git_commit

        max_cost_increase_percent = self.max_cost_increase_percent

        max_cost_usd = self.max_cost_usd

        max_failure_rate = self.max_failure_rate

        max_latency_increase_percent = self.max_latency_increase_percent

        max_latency_ms = self.max_latency_ms

        min_score = self.min_score

        min_score_delta = self.min_score_delta

        release = self.release

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git_branch is not UNSET:
            field_dict["gitBranch"] = git_branch
        if git_commit is not UNSET:
            field_dict["gitCommit"] = git_commit
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
        if release is not UNSET:
            field_dict["release"] = release
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_branch = d.pop("gitBranch", UNSET)

        git_commit = d.pop("gitCommit", UNSET)

        max_cost_increase_percent = d.pop("maxCostIncreasePercent", UNSET)

        max_cost_usd = d.pop("maxCostUsd", UNSET)

        max_failure_rate = d.pop("maxFailureRate", UNSET)

        max_latency_increase_percent = d.pop("maxLatencyIncreasePercent", UNSET)

        max_latency_ms = d.pop("maxLatencyMs", UNSET)

        min_score = d.pop("minScore", UNSET)

        min_score_delta = d.pop("minScoreDelta", UNSET)

        release = d.pop("release", UNSET)

        _source = d.pop("source", UNSET)
        source: GateRunSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = GateRunSource(_source)

        experiment_gate_dto = cls(
            git_branch=git_branch,
            git_commit=git_commit,
            max_cost_increase_percent=max_cost_increase_percent,
            max_cost_usd=max_cost_usd,
            max_failure_rate=max_failure_rate,
            max_latency_increase_percent=max_latency_increase_percent,
            max_latency_ms=max_latency_ms,
            min_score=min_score,
            min_score_delta=min_score_delta,
            release=release,
            source=source,
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
