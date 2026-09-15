from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgMemberDTO")


@_attrs_define
class OrgMemberDTO:
    """
    Attributes:
        joined_at (str):
        role (str):
        user_id (str):
    """

    joined_at: str
    role: str
    user_id: str

    def to_dict(self) -> dict[str, Any]:
        joined_at = self.joined_at

        role = self.role

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "joinedAt": joined_at,
                "role": role,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        joined_at = d.pop("joinedAt")

        role = d.pop("role")

        user_id = d.pop("userId")

        org_member_dto = cls(
            joined_at=joined_at,
            role=role,
            user_id=user_id,
        )

        return org_member_dto
