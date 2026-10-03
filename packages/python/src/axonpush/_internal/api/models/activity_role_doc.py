from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityRoleDoc")


@_attrs_define
class ActivityRoleDoc:
    """
    Attributes:
        meaning (str):
        role (str):
    """

    meaning: str
    role: str

    def to_dict(self) -> dict[str, Any]:
        meaning = self.meaning

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "meaning": meaning,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        meaning = d.pop("meaning")

        role = d.pop("role")

        activity_role_doc = cls(
            meaning=meaning,
            role=role,
        )

        return activity_role_doc
