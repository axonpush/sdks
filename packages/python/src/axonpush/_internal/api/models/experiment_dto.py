from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.experiment_status import ExperimentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluator_version_ref_dto import EvaluatorVersionRefDto
    from ..models.experiment_dto_configuration import ExperimentDtoConfiguration
    from ..models.experiment_dto_model_configuration import ExperimentDtoModelConfiguration


T = TypeVar("T", bound="ExperimentDto")


@_attrs_define
class ExperimentDto:
    """
    Attributes:
        completed_items (float):
        created_at (datetime.datetime):
        dataset_id (str):
        dataset_revision (float):
        evaluator_versions (list[EvaluatorVersionRefDto]):
        experiment_id (str):
        failed_items (float):
        name (str):
        org_id (str):
        status (ExperimentStatus):
        target_id (str):
        total_items (float):
        updated_at (datetime.datetime):
        baseline_experiment_id (str | Unset):
        configuration (ExperimentDtoConfiguration | Unset):
        cost_usd (float | Unset):
        git_branch (str | Unset):
        git_commit (str | Unset):
        git_dirty (bool | Unset):
        latency_ms (float | Unset):
        model_configuration (ExperimentDtoModelConfiguration | Unset):
        prompt_version_id (str | Unset):
        release (str | Unset):
        score (float | Unset):
        total_tokens (float | Unset):
    """

    completed_items: float
    created_at: datetime.datetime
    dataset_id: str
    dataset_revision: float
    evaluator_versions: list[EvaluatorVersionRefDto]
    experiment_id: str
    failed_items: float
    name: str
    org_id: str
    status: ExperimentStatus
    target_id: str
    total_items: float
    updated_at: datetime.datetime
    baseline_experiment_id: str | Unset = UNSET
    configuration: ExperimentDtoConfiguration | Unset = UNSET
    cost_usd: float | Unset = UNSET
    git_branch: str | Unset = UNSET
    git_commit: str | Unset = UNSET
    git_dirty: bool | Unset = UNSET
    latency_ms: float | Unset = UNSET
    model_configuration: ExperimentDtoModelConfiguration | Unset = UNSET
    prompt_version_id: str | Unset = UNSET
    release: str | Unset = UNSET
    score: float | Unset = UNSET
    total_tokens: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluator_version_ref_dto import EvaluatorVersionRefDto
        from ..models.experiment_dto_configuration import ExperimentDtoConfiguration
        from ..models.experiment_dto_model_configuration import ExperimentDtoModelConfiguration

        completed_items = self.completed_items

        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        dataset_revision = self.dataset_revision

        evaluator_versions = []
        for evaluator_versions_item_data in self.evaluator_versions:
            evaluator_versions_item = evaluator_versions_item_data.to_dict()
            evaluator_versions.append(evaluator_versions_item)

        experiment_id = self.experiment_id

        failed_items = self.failed_items

        name = self.name

        org_id = self.org_id

        status = self.status.value

        target_id = self.target_id

        total_items = self.total_items

        updated_at = self.updated_at.isoformat()

        baseline_experiment_id = self.baseline_experiment_id

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        cost_usd = self.cost_usd

        git_branch = self.git_branch

        git_commit = self.git_commit

        git_dirty = self.git_dirty

        latency_ms = self.latency_ms

        model_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_configuration, Unset):
            model_configuration = self.model_configuration.to_dict()

        prompt_version_id = self.prompt_version_id

        release = self.release

        score = self.score

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completedItems": completed_items,
                "createdAt": created_at,
                "datasetId": dataset_id,
                "datasetRevision": dataset_revision,
                "evaluatorVersions": evaluator_versions,
                "experimentId": experiment_id,
                "failedItems": failed_items,
                "name": name,
                "orgId": org_id,
                "status": status,
                "targetId": target_id,
                "totalItems": total_items,
                "updatedAt": updated_at,
            }
        )
        if baseline_experiment_id is not UNSET:
            field_dict["baselineExperimentId"] = baseline_experiment_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if git_branch is not UNSET:
            field_dict["gitBranch"] = git_branch
        if git_commit is not UNSET:
            field_dict["gitCommit"] = git_commit
        if git_dirty is not UNSET:
            field_dict["gitDirty"] = git_dirty
        if latency_ms is not UNSET:
            field_dict["latencyMs"] = latency_ms
        if model_configuration is not UNSET:
            field_dict["modelConfiguration"] = model_configuration
        if prompt_version_id is not UNSET:
            field_dict["promptVersionId"] = prompt_version_id
        if release is not UNSET:
            field_dict["release"] = release
        if score is not UNSET:
            field_dict["score"] = score
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluator_version_ref_dto import EvaluatorVersionRefDto
        from ..models.experiment_dto_configuration import ExperimentDtoConfiguration
        from ..models.experiment_dto_model_configuration import ExperimentDtoModelConfiguration

        d = dict(src_dict)
        completed_items = d.pop("completedItems")

        created_at = isoparse(d.pop("createdAt"))

        dataset_id = d.pop("datasetId")

        dataset_revision = d.pop("datasetRevision")

        evaluator_versions = []
        _evaluator_versions = d.pop("evaluatorVersions")
        for evaluator_versions_item_data in _evaluator_versions:
            evaluator_versions_item = EvaluatorVersionRefDto.from_dict(evaluator_versions_item_data)

            evaluator_versions.append(evaluator_versions_item)

        experiment_id = d.pop("experimentId")

        failed_items = d.pop("failedItems")

        name = d.pop("name")

        org_id = d.pop("orgId")

        status = ExperimentStatus(d.pop("status"))

        target_id = d.pop("targetId")

        total_items = d.pop("totalItems")

        updated_at = isoparse(d.pop("updatedAt"))

        baseline_experiment_id = d.pop("baselineExperimentId", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: ExperimentDtoConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = ExperimentDtoConfiguration.from_dict(_configuration)

        cost_usd = d.pop("costUsd", UNSET)

        git_branch = d.pop("gitBranch", UNSET)

        git_commit = d.pop("gitCommit", UNSET)

        git_dirty = d.pop("gitDirty", UNSET)

        latency_ms = d.pop("latencyMs", UNSET)

        _model_configuration = d.pop("modelConfiguration", UNSET)
        model_configuration: ExperimentDtoModelConfiguration | Unset
        if isinstance(_model_configuration, Unset):
            model_configuration = UNSET
        else:
            model_configuration = ExperimentDtoModelConfiguration.from_dict(_model_configuration)

        prompt_version_id = d.pop("promptVersionId", UNSET)

        release = d.pop("release", UNSET)

        score = d.pop("score", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        experiment_dto = cls(
            completed_items=completed_items,
            created_at=created_at,
            dataset_id=dataset_id,
            dataset_revision=dataset_revision,
            evaluator_versions=evaluator_versions,
            experiment_id=experiment_id,
            failed_items=failed_items,
            name=name,
            org_id=org_id,
            status=status,
            target_id=target_id,
            total_items=total_items,
            updated_at=updated_at,
            baseline_experiment_id=baseline_experiment_id,
            configuration=configuration,
            cost_usd=cost_usd,
            git_branch=git_branch,
            git_commit=git_commit,
            git_dirty=git_dirty,
            latency_ms=latency_ms,
            model_configuration=model_configuration,
            prompt_version_id=prompt_version_id,
            release=release,
            score=score,
            total_tokens=total_tokens,
        )

        experiment_dto.additional_properties = d
        return experiment_dto

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
