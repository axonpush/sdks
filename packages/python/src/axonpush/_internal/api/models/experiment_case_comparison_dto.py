from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_case_pair_dto import ExperimentCasePairDto


T = TypeVar("T", bound="ExperimentCaseComparisonDto")


@_attrs_define
class ExperimentCaseComparisonDto:
    """
    Attributes:
        data (list[ExperimentCasePairDto]):
        cursor (str | Unset):
    """

    data: list[ExperimentCasePairDto]
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_case_pair_dto import ExperimentCasePairDto

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_case_pair_dto import ExperimentCasePairDto

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ExperimentCasePairDto.from_dict(data_item_data)

            data.append(data_item)

        cursor = d.pop("cursor", UNSET)

        experiment_case_comparison_dto = cls(
            data=data,
            cursor=cursor,
        )

        experiment_case_comparison_dto.additional_properties = d
        return experiment_case_comparison_dto

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
