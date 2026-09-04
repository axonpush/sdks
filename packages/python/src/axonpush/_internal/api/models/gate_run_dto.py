from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gate_run_dto_metrics import GateRunDtoMetrics
    from ..models.gate_run_dto_thresholds import GateRunDtoThresholds


T = TypeVar("T", bound="GateRunDto")


@_attrs_define
class GateRunDto:
    """
    Attributes:
        created_at (datetime.datetime):
        experiment_id (str):
        gate_run_id (str):
        metrics (GateRunDtoMetrics):
        org_id (str):
        passed (bool):
        reasons (list[str]):
        source (str):
        thresholds (GateRunDtoThresholds):
        baseline_experiment_id (str | Unset):
        dataset_id (str | Unset):
        git_branch (str | Unset):
        git_commit (str | Unset):
        release (str | Unset):
        target_id (str | Unset):
    """

    created_at: datetime.datetime
    experiment_id: str
    gate_run_id: str
    metrics: GateRunDtoMetrics
    org_id: str
    passed: bool
    reasons: list[str]
    source: str
    thresholds: GateRunDtoThresholds
    baseline_experiment_id: str | Unset = UNSET
    dataset_id: str | Unset = UNSET
    git_branch: str | Unset = UNSET
    git_commit: str | Unset = UNSET
    release: str | Unset = UNSET
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.gate_run_dto_metrics import GateRunDtoMetrics
        from ..models.gate_run_dto_thresholds import GateRunDtoThresholds

        created_at = self.created_at.isoformat()

        experiment_id = self.experiment_id

        gate_run_id = self.gate_run_id

        metrics = self.metrics.to_dict()

        org_id = self.org_id

        passed = self.passed

        reasons = self.reasons

        source = self.source

        thresholds = self.thresholds.to_dict()

        baseline_experiment_id = self.baseline_experiment_id

        dataset_id = self.dataset_id

        git_branch = self.git_branch

        git_commit = self.git_commit

        release = self.release

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "experimentId": experiment_id,
                "gateRunId": gate_run_id,
                "metrics": metrics,
                "orgId": org_id,
                "passed": passed,
                "reasons": reasons,
                "source": source,
                "thresholds": thresholds,
            }
        )
        if baseline_experiment_id is not UNSET:
            field_dict["baselineExperimentId"] = baseline_experiment_id
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if git_branch is not UNSET:
            field_dict["gitBranch"] = git_branch
        if git_commit is not UNSET:
            field_dict["gitCommit"] = git_commit
        if release is not UNSET:
            field_dict["release"] = release
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gate_run_dto_metrics import GateRunDtoMetrics
        from ..models.gate_run_dto_thresholds import GateRunDtoThresholds

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        experiment_id = d.pop("experimentId")

        gate_run_id = d.pop("gateRunId")

        metrics = GateRunDtoMetrics.from_dict(d.pop("metrics"))

        org_id = d.pop("orgId")

        passed = d.pop("passed")

        reasons = cast(list[str], d.pop("reasons"))

        source = d.pop("source")

        thresholds = GateRunDtoThresholds.from_dict(d.pop("thresholds"))

        baseline_experiment_id = d.pop("baselineExperimentId", UNSET)

        dataset_id = d.pop("datasetId", UNSET)

        git_branch = d.pop("gitBranch", UNSET)

        git_commit = d.pop("gitCommit", UNSET)

        release = d.pop("release", UNSET)

        target_id = d.pop("targetId", UNSET)

        gate_run_dto = cls(
            created_at=created_at,
            experiment_id=experiment_id,
            gate_run_id=gate_run_id,
            metrics=metrics,
            org_id=org_id,
            passed=passed,
            reasons=reasons,
            source=source,
            thresholds=thresholds,
            baseline_experiment_id=baseline_experiment_id,
            dataset_id=dataset_id,
            git_branch=git_branch,
            git_commit=git_commit,
            release=release,
            target_id=target_id,
        )

        gate_run_dto.additional_properties = d
        return gate_run_dto

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
