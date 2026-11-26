from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipDTO")


@_attrs_define
class MembershipDTO:
    """
    Attributes:
        org_id (str):
        role (str):
    """

    org_id: str
    role: str

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "orgId": org_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        role = d.pop("role")

        membership_dto = cls(
            org_id=org_id,
            role=role,
        )

        return membership_dto
