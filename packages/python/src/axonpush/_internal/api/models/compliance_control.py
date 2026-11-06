from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceControl")


@_attrs_define
class ComplianceControl:
    """
    Attributes:
        control (str):
        framework (str):
    """

    control: str
    framework: str

    def to_dict(self) -> dict[str, Any]:
        control = self.control

        framework = self.framework

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "control": control,
                "framework": framework,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        control = d.pop("control")

        framework = d.pop("framework")

        compliance_control = cls(
            control=control,
            framework=framework,
        )

        return compliance_control
