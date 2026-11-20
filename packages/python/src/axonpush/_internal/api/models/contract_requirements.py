from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.requirement import Requirement


T = TypeVar("T", bound="ContractRequirements")


@_attrs_define
class ContractRequirements:
    """ """

    additional_properties: dict[str, Requirement] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.requirement import Requirement

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement import Requirement

        d = dict(src_dict)
        contract_requirements = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Requirement.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        contract_requirements.additional_properties = additional_properties
        return contract_requirements

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Requirement:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Requirement) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
