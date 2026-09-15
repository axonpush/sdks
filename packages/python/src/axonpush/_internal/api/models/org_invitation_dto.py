from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgInvitationDTO")


@_attrs_define
class OrgInvitationDTO:
    """
    Attributes:
        code (str):
        created_at (str):
        invitation_id (str):
        invite_role (str):
        invited_email (str):
        status (str):
    """

    code: str
    created_at: str
    invitation_id: str
    invite_role: str
    invited_email: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        created_at = self.created_at

        invitation_id = self.invitation_id

        invite_role = self.invite_role

        invited_email = self.invited_email

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "createdAt": created_at,
                "invitationId": invitation_id,
                "inviteRole": invite_role,
                "invitedEmail": invited_email,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        created_at = d.pop("createdAt")

        invitation_id = d.pop("invitationId")

        invite_role = d.pop("inviteRole")

        invited_email = d.pop("invitedEmail")

        status = d.pop("status")

        org_invitation_dto = cls(
            code=code,
            created_at=created_at,
            invitation_id=invitation_id,
            invite_role=invite_role,
            invited_email=invited_email,
            status=status,
        )

        return org_invitation_dto
