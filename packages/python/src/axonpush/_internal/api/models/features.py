from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Features")


@_attrs_define
class Features:
    """
    Attributes:
        compliance (bool):
    """

    compliance: bool

    def to_dict(self) -> dict[str, Any]:
        compliance = self.compliance

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "compliance": compliance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        compliance = d.pop("compliance")

        features = cls(
            compliance=compliance,
        )

        return features
