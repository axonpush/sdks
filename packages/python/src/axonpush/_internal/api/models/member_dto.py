from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberDTO")


@_attrs_define
class MemberDTO:
    """
    Attributes:
        joined_at (str):
        member_id (str):
        org_id (str):
        role (str):
        user_id (str):
        email (str | Unset):
    """

    joined_at: str
    member_id: str
    org_id: str
    role: str
    user_id: str
    email: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        joined_at = self.joined_at

        member_id = self.member_id

        org_id = self.org_id

        role = self.role

        user_id = self.user_id

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "joinedAt": joined_at,
                "memberId": member_id,
                "orgId": org_id,
                "role": role,
                "userId": user_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        joined_at = d.pop("joinedAt")

        member_id = d.pop("memberId")

        org_id = d.pop("orgId")

        role = d.pop("role")

        user_id = d.pop("userId")

        email = d.pop("email", UNSET)

        member_dto = cls(
            joined_at=joined_at,
            member_id=member_id,
            org_id=org_id,
            role=role,
            user_id=user_id,
            email=email,
        )

        return member_dto
