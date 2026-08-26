from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationResponseDto")


@_attrs_define
class InvitationResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        invitation_id (str):
        invited_email (str):
        org_id (str):
        role (str):
        status (str):
        accepted_at (datetime.datetime | Unset):
        code (str | Unset):
        expires_at (datetime.datetime | Unset):
        invite_role (str | Unset):
        updated_at (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    id: str
    invitation_id: str
    invited_email: str
    org_id: str
    role: str
    status: str
    accepted_at: datetime.datetime | Unset = UNSET
    code: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    invite_role: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        invitation_id = self.invitation_id

        invited_email = self.invited_email

        org_id = self.org_id

        role = self.role

        status = self.status

        accepted_at: str | Unset = UNSET
        if not isinstance(self.accepted_at, Unset):
            accepted_at = self.accepted_at.isoformat()

        code = self.code

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        invite_role = self.invite_role

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "invitationId": invitation_id,
                "invitedEmail": invited_email,
                "orgId": org_id,
                "role": role,
                "status": status,
            }
        )
        if accepted_at is not UNSET:
            field_dict["acceptedAt"] = accepted_at
        if code is not UNSET:
            field_dict["code"] = code
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if invite_role is not UNSET:
            field_dict["inviteRole"] = invite_role
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        invitation_id = d.pop("invitationId")

        invited_email = d.pop("invitedEmail")

        org_id = d.pop("orgId")

        role = d.pop("role")

        status = d.pop("status")

        _accepted_at = d.pop("acceptedAt", UNSET)
        accepted_at: datetime.datetime | Unset
        if isinstance(_accepted_at, Unset):
            accepted_at = UNSET
        else:
            accepted_at = isoparse(_accepted_at)

        code = d.pop("code", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        invite_role = d.pop("inviteRole", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        invitation_response_dto = cls(
            created_at=created_at,
            id=id,
            invitation_id=invitation_id,
            invited_email=invited_email,
            org_id=org_id,
            role=role,
            status=status,
            accepted_at=accepted_at,
            code=code,
            expires_at=expires_at,
            invite_role=invite_role,
            updated_at=updated_at,
        )

        invitation_response_dto.additional_properties = d
        return invitation_response_dto

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
