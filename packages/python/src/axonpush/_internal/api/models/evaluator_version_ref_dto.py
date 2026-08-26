from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvaluatorVersionRefDto")


@_attrs_define
class EvaluatorVersionRefDto:
    """
    Attributes:
        evaluator_id (str):
        version (float):
    """

    evaluator_id: str
    version: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluator_id = self.evaluator_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "evaluatorId": evaluator_id,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        evaluator_id = d.pop("evaluatorId")

        version = d.pop("version")

        evaluator_version_ref_dto = cls(
            evaluator_id=evaluator_id,
            version=version,
        )

        evaluator_version_ref_dto.additional_properties = d
        return evaluator_version_ref_dto

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
