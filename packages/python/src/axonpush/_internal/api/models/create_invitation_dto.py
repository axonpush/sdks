from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_role import OrganizationRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInvitationDto")


@_attrs_define
class CreateInvitationDto:
    """
    Attributes:
        desired_role (OrganizationRole):
        invited_email (str):
    """

    desired_role: OrganizationRole
    invited_email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desired_role = self.desired_role.value

        invited_email = self.invited_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desired_role": desired_role,
                "invitedEmail": invited_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        desired_role = OrganizationRole(d.pop("desired_role"))

        invited_email = d.pop("invitedEmail")

        create_invitation_dto = cls(
            desired_role=desired_role,
            invited_email=invited_email,
        )

        create_invitation_dto.additional_properties = d
        return create_invitation_dto

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
