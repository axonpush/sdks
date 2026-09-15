from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationDTO")


@_attrs_define
class InvitationDTO:
    """
    Attributes:
        code (str):
        created_at (str):
        invitation_id (str):
        invite_role (str):
        invited_email (str):
        org_id (str):
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        expires_at (str | Unset):
        inviter_id (str | Unset):
    """

    code: str
    created_at: str
    invitation_id: str
    invite_role: str
    invited_email: str
    org_id: str
    status: str
    schema: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    inviter_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        created_at = self.created_at

        invitation_id = self.invitation_id

        invite_role = self.invite_role

        invited_email = self.invited_email

        org_id = self.org_id

        status = self.status

        schema = self.schema

        expires_at = self.expires_at

        inviter_id = self.inviter_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "createdAt": created_at,
                "invitationId": invitation_id,
                "inviteRole": invite_role,
                "invitedEmail": invited_email,
                "orgId": org_id,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if inviter_id is not UNSET:
            field_dict["inviterId"] = inviter_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        created_at = d.pop("createdAt")

        invitation_id = d.pop("invitationId")

        invite_role = d.pop("inviteRole")

        invited_email = d.pop("invitedEmail")

        org_id = d.pop("orgId")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        inviter_id = d.pop("inviterId", UNSET)

        invitation_dto = cls(
            code=code,
            created_at=created_at,
            invitation_id=invitation_id,
            invite_role=invite_role,
            invited_email=invited_email,
            org_id=org_id,
            status=status,
            schema=schema,
            expires_at=expires_at,
            inviter_id=inviter_id,
        )

        return invitation_dto
