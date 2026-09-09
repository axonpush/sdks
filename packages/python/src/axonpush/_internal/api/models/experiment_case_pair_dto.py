from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_result_dto import ExperimentResultDto


T = TypeVar("T", bound="ExperimentCasePairDto")


@_attrs_define
class ExperimentCasePairDto:
    """
    Attributes:
        item_id (str):
        baseline (ExperimentResultDto | Unset):
        candidate (ExperimentResultDto | Unset):
    """

    item_id: str
    baseline: ExperimentResultDto | Unset = UNSET
    candidate: ExperimentResultDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_result_dto import ExperimentResultDto

        item_id = self.item_id

        baseline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.baseline, Unset):
            baseline = self.baseline.to_dict()

        candidate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.candidate, Unset):
            candidate = self.candidate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemId": item_id,
            }
        )
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if candidate is not UNSET:
            field_dict["candidate"] = candidate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_result_dto import ExperimentResultDto

        d = dict(src_dict)
        item_id = d.pop("itemId")

        _baseline = d.pop("baseline", UNSET)
        baseline: ExperimentResultDto | Unset
        if isinstance(_baseline, Unset):
            baseline = UNSET
        else:
            baseline = ExperimentResultDto.from_dict(_baseline)

        _candidate = d.pop("candidate", UNSET)
        candidate: ExperimentResultDto | Unset
        if isinstance(_candidate, Unset):
            candidate = UNSET
        else:
            candidate = ExperimentResultDto.from_dict(_candidate)

        experiment_case_pair_dto = cls(
            item_id=item_id,
            baseline=baseline,
            candidate=candidate,
        )

        experiment_case_pair_dto.additional_properties = d
        return experiment_case_pair_dto

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
