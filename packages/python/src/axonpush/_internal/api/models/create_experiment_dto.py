from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_experiment_dto_configuration import CreateExperimentDtoConfiguration
    from ..models.create_experiment_dto_model_configuration import (
        CreateExperimentDtoModelConfiguration,
    )
    from ..models.evaluator_version_ref_dto import EvaluatorVersionRefDto


T = TypeVar("T", bound="CreateExperimentDto")


@_attrs_define
class CreateExperimentDto:
    """
    Attributes:
        dataset_id (str):
        dataset_revision (float):
        evaluator_versions (list[EvaluatorVersionRefDto]):
        name (str):
        target_id (str):
        baseline_experiment_id (str | Unset):
        configuration (CreateExperimentDtoConfiguration | Unset):
        git_branch (str | Unset):
        git_commit (str | Unset):
        git_dirty (bool | Unset):
        model_configuration (CreateExperimentDtoModelConfiguration | Unset):
        prompt_version_id (str | Unset):
        release (str | Unset):
    """

    dataset_id: str
    dataset_revision: float
    evaluator_versions: list[EvaluatorVersionRefDto]
    name: str
    target_id: str
    baseline_experiment_id: str | Unset = UNSET
    configuration: CreateExperimentDtoConfiguration | Unset = UNSET
    git_branch: str | Unset = UNSET
    git_commit: str | Unset = UNSET
    git_dirty: bool | Unset = UNSET
    model_configuration: CreateExperimentDtoModelConfiguration | Unset = UNSET
    prompt_version_id: str | Unset = UNSET
    release: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_experiment_dto_configuration import CreateExperimentDtoConfiguration
        from ..models.create_experiment_dto_model_configuration import (
            CreateExperimentDtoModelConfiguration,
        )
        from ..models.evaluator_version_ref_dto import EvaluatorVersionRefDto

        dataset_id = self.dataset_id

        dataset_revision = self.dataset_revision

        evaluator_versions = []
        for evaluator_versions_item_data in self.evaluator_versions:
            evaluator_versions_item = evaluator_versions_item_data.to_dict()
            evaluator_versions.append(evaluator_versions_item)

        name = self.name

        target_id = self.target_id

        baseline_experiment_id = self.baseline_experiment_id

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        git_branch = self.git_branch

        git_commit = self.git_commit

        git_dirty = self.git_dirty

        model_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_configuration, Unset):
            model_configuration = self.model_configuration.to_dict()

        prompt_version_id = self.prompt_version_id

        release = self.release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "datasetRevision": dataset_revision,
                "evaluatorVersions": evaluator_versions,
                "name": name,
                "targetId": target_id,
            }
        )
        if baseline_experiment_id is not UNSET:
            field_dict["baselineExperimentId"] = baseline_experiment_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if git_branch is not UNSET:
            field_dict["gitBranch"] = git_branch
        if git_commit is not UNSET:
            field_dict["gitCommit"] = git_commit
        if git_dirty is not UNSET:
            field_dict["gitDirty"] = git_dirty
        if model_configuration is not UNSET:
            field_dict["modelConfiguration"] = model_configuration
        if prompt_version_id is not UNSET:
            field_dict["promptVersionId"] = prompt_version_id
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_experiment_dto_configuration import CreateExperimentDtoConfiguration
        from ..models.create_experiment_dto_model_configuration import (
            CreateExperimentDtoModelConfiguration,
        )
        from ..models.evaluator_version_ref_dto import EvaluatorVersionRefDto

        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        dataset_revision = d.pop("datasetRevision")

        evaluator_versions = []
        _evaluator_versions = d.pop("evaluatorVersions")
        for evaluator_versions_item_data in _evaluator_versions:
            evaluator_versions_item = EvaluatorVersionRefDto.from_dict(evaluator_versions_item_data)

            evaluator_versions.append(evaluator_versions_item)

        name = d.pop("name")

        target_id = d.pop("targetId")

        baseline_experiment_id = d.pop("baselineExperimentId", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: CreateExperimentDtoConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = CreateExperimentDtoConfiguration.from_dict(_configuration)

        git_branch = d.pop("gitBranch", UNSET)

        git_commit = d.pop("gitCommit", UNSET)

        git_dirty = d.pop("gitDirty", UNSET)

        _model_configuration = d.pop("modelConfiguration", UNSET)
        model_configuration: CreateExperimentDtoModelConfiguration | Unset
        if isinstance(_model_configuration, Unset):
            model_configuration = UNSET
        else:
            model_configuration = CreateExperimentDtoModelConfiguration.from_dict(
                _model_configuration
            )

        prompt_version_id = d.pop("promptVersionId", UNSET)

        release = d.pop("release", UNSET)

        create_experiment_dto = cls(
            dataset_id=dataset_id,
            dataset_revision=dataset_revision,
            evaluator_versions=evaluator_versions,
            name=name,
            target_id=target_id,
            baseline_experiment_id=baseline_experiment_id,
            configuration=configuration,
            git_branch=git_branch,
            git_commit=git_commit,
            git_dirty=git_dirty,
            model_configuration=model_configuration,
            prompt_version_id=prompt_version_id,
            release=release,
        )

        create_experiment_dto.additional_properties = d
        return create_experiment_dto

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
