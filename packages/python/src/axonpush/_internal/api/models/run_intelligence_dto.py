from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunIntelligenceDto")


@_attrs_define
class RunIntelligenceDto:
    """
    Attributes:
        evaluator_id (str | Unset):
        evaluator_version (float | Unset):
        max_cost_usd (float | Unset):  Default: 0.0.
        max_labels (float | Unset):  Default: 0.0.
        minimum_cohort_size (float | Unset):  Default: 3.0.
    """

    evaluator_id: str | Unset = UNSET
    evaluator_version: float | Unset = UNSET
    max_cost_usd: float | Unset = 0.0
    max_labels: float | Unset = 0.0
    minimum_cohort_size: float | Unset = 3.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluator_id = self.evaluator_id

        evaluator_version = self.evaluator_version

        max_cost_usd = self.max_cost_usd

        max_labels = self.max_labels

        minimum_cohort_size = self.minimum_cohort_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if evaluator_id is not UNSET:
            field_dict["evaluatorId"] = evaluator_id
        if evaluator_version is not UNSET:
            field_dict["evaluatorVersion"] = evaluator_version
        if max_cost_usd is not UNSET:
            field_dict["maxCostUsd"] = max_cost_usd
        if max_labels is not UNSET:
            field_dict["maxLabels"] = max_labels
        if minimum_cohort_size is not UNSET:
            field_dict["minimumCohortSize"] = minimum_cohort_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        evaluator_id = d.pop("evaluatorId", UNSET)

        evaluator_version = d.pop("evaluatorVersion", UNSET)

        max_cost_usd = d.pop("maxCostUsd", UNSET)

        max_labels = d.pop("maxLabels", UNSET)

        minimum_cohort_size = d.pop("minimumCohortSize", UNSET)

        run_intelligence_dto = cls(
            evaluator_id=evaluator_id,
            evaluator_version=evaluator_version,
            max_cost_usd=max_cost_usd,
            max_labels=max_labels,
            minimum_cohort_size=minimum_cohort_size,
        )

        run_intelligence_dto.additional_properties = d
        return run_intelligence_dto

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
