from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateActionContractDto")


@_attrs_define
class CreateActionContractDto:
    """
    Attributes:
        contract_id (str):
        description (str):
        name (str):
        observation_window_seconds (float):
        required_checks (list[str]):
        version (float):
    """

    contract_id: str
    description: str
    name: str
    observation_window_seconds: float
    required_checks: list[str]
    version: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_id = self.contract_id

        description = self.description

        name = self.name

        observation_window_seconds = self.observation_window_seconds

        required_checks = self.required_checks

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contractId": contract_id,
                "description": description,
                "name": name,
                "observationWindowSeconds": observation_window_seconds,
                "requiredChecks": required_checks,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_id = d.pop("contractId")

        description = d.pop("description")

        name = d.pop("name")

        observation_window_seconds = d.pop("observationWindowSeconds")

        required_checks = cast(list[str], d.pop("requiredChecks"))

        version = d.pop("version")

        create_action_contract_dto = cls(
            contract_id=contract_id,
            description=description,
            name=name,
            observation_window_seconds=observation_window_seconds,
            required_checks=required_checks,
            version=version,
        )

        create_action_contract_dto.additional_properties = d
        return create_action_contract_dto

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
