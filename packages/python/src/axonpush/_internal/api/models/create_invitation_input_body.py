from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_invitation_input_body_role import CreateInvitationInputBodyRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInvitationInputBody")


@_attrs_define
class CreateInvitationInputBody:
    """
    Attributes:
        invited_email (str): Email to invite
        role (CreateInvitationInputBodyRole): Role to grant on accept
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    invited_email: str
    role: CreateInvitationInputBodyRole
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        invited_email = self.invited_email

        role = self.role.value

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invitedEmail": invited_email,
                "role": role,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invited_email = d.pop("invitedEmail")

        role = CreateInvitationInputBodyRole(d.pop("role"))

        schema = d.pop("$schema", UNSET)

        create_invitation_input_body = cls(
            invited_email=invited_email,
            role=role,
            schema=schema,
        )

        return create_invitation_input_body
