from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_comparison_dto_baseline import ExperimentComparisonDtoBaseline
    from ..models.experiment_comparison_dto_candidate import ExperimentComparisonDtoCandidate
    from ..models.experiment_comparison_dto_delta import ExperimentComparisonDtoDelta


T = TypeVar("T", bound="ExperimentComparisonDto")


@_attrs_define
class ExperimentComparisonDto:
    """
    Attributes:
        baseline (ExperimentComparisonDtoBaseline):
        baseline_experiment_id (str):
        candidate (ExperimentComparisonDtoCandidate):
        candidate_experiment_id (str):
        delta (ExperimentComparisonDtoDelta):
    """

    baseline: ExperimentComparisonDtoBaseline
    baseline_experiment_id: str
    candidate: ExperimentComparisonDtoCandidate
    candidate_experiment_id: str
    delta: ExperimentComparisonDtoDelta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_comparison_dto_baseline import ExperimentComparisonDtoBaseline
        from ..models.experiment_comparison_dto_candidate import ExperimentComparisonDtoCandidate
        from ..models.experiment_comparison_dto_delta import ExperimentComparisonDtoDelta

        baseline = self.baseline.to_dict()

        baseline_experiment_id = self.baseline_experiment_id

        candidate = self.candidate.to_dict()

        candidate_experiment_id = self.candidate_experiment_id

        delta = self.delta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseline": baseline,
                "baselineExperimentId": baseline_experiment_id,
                "candidate": candidate,
                "candidateExperimentId": candidate_experiment_id,
                "delta": delta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_comparison_dto_baseline import ExperimentComparisonDtoBaseline
        from ..models.experiment_comparison_dto_candidate import ExperimentComparisonDtoCandidate
        from ..models.experiment_comparison_dto_delta import ExperimentComparisonDtoDelta

        d = dict(src_dict)
        baseline = ExperimentComparisonDtoBaseline.from_dict(d.pop("baseline"))

        baseline_experiment_id = d.pop("baselineExperimentId")

        candidate = ExperimentComparisonDtoCandidate.from_dict(d.pop("candidate"))

        candidate_experiment_id = d.pop("candidateExperimentId")

        delta = ExperimentComparisonDtoDelta.from_dict(d.pop("delta"))

        experiment_comparison_dto = cls(
            baseline=baseline,
            baseline_experiment_id=baseline_experiment_id,
            candidate=candidate,
            candidate_experiment_id=candidate_experiment_id,
            delta=delta,
        )

        experiment_comparison_dto.additional_properties = d
        return experiment_comparison_dto

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
