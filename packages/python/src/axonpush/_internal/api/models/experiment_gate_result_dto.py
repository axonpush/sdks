from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_gate_result_dto_metrics import ExperimentGateResultDtoMetrics


T = TypeVar("T", bound="ExperimentGateResultDto")


@_attrs_define
class ExperimentGateResultDto:
    """
    Attributes:
        experiment_id (str):
        metrics (ExperimentGateResultDtoMetrics):
        passed (bool):
        reasons (list[str]):
        baseline_experiment_id (str | Unset):
    """

    experiment_id: str
    metrics: ExperimentGateResultDtoMetrics
    passed: bool
    reasons: list[str]
    baseline_experiment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_gate_result_dto_metrics import ExperimentGateResultDtoMetrics

        experiment_id = self.experiment_id

        metrics = self.metrics.to_dict()

        passed = self.passed

        reasons = self.reasons

        baseline_experiment_id = self.baseline_experiment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimentId": experiment_id,
                "metrics": metrics,
                "passed": passed,
                "reasons": reasons,
            }
        )
        if baseline_experiment_id is not UNSET:
            field_dict["baselineExperimentId"] = baseline_experiment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_gate_result_dto_metrics import ExperimentGateResultDtoMetrics

        d = dict(src_dict)
        experiment_id = d.pop("experimentId")

        metrics = ExperimentGateResultDtoMetrics.from_dict(d.pop("metrics"))

        passed = d.pop("passed")

        reasons = cast(list[str], d.pop("reasons"))

        baseline_experiment_id = d.pop("baselineExperimentId", UNSET)

        experiment_gate_result_dto = cls(
            experiment_id=experiment_id,
            metrics=metrics,
            passed=passed,
            reasons=reasons,
            baseline_experiment_id=baseline_experiment_id,
        )

        experiment_gate_result_dto.additional_properties = d
        return experiment_gate_result_dto

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
