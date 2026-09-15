from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_dto import OrgDTO
    from ..models.org_invitation_dto import OrgInvitationDTO
    from ..models.org_member_dto import OrgMemberDTO


T = TypeVar("T", bound="GetOrgOutputBody")


@_attrs_define
class GetOrgOutputBody:
    """
    Attributes:
        invitations (list[OrgInvitationDTO] | None):
        members (list[OrgMemberDTO] | None):
        org (OrgDTO):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    invitations: list[OrgInvitationDTO] | None
    members: list[OrgMemberDTO] | None
    org: OrgDTO
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.org_dto import OrgDTO
        from ..models.org_invitation_dto import OrgInvitationDTO
        from ..models.org_member_dto import OrgMemberDTO

        invitations: list[dict[str, Any]] | None
        if isinstance(self.invitations, list):
            invitations = []
            for invitations_type_0_item_data in self.invitations:
                invitations_type_0_item = invitations_type_0_item_data.to_dict()
                invitations.append(invitations_type_0_item)

        else:
            invitations = self.invitations

        members: list[dict[str, Any]] | None
        if isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)

        else:
            members = self.members

        org = self.org.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invitations": invitations,
                "members": members,
                "org": org,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_dto import OrgDTO
        from ..models.org_invitation_dto import OrgInvitationDTO
        from ..models.org_member_dto import OrgMemberDTO

        d = dict(src_dict)

        def _parse_invitations(data: object) -> list[OrgInvitationDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                invitations_type_0 = []
                _invitations_type_0 = data
                for invitations_type_0_item_data in _invitations_type_0:
                    invitations_type_0_item = OrgInvitationDTO.from_dict(
                        invitations_type_0_item_data
                    )

                    invitations_type_0.append(invitations_type_0_item)

                return invitations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrgInvitationDTO] | None, data)

        invitations = _parse_invitations(d.pop("invitations"))

        def _parse_members(data: object) -> list[OrgMemberDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in _members_type_0:
                    members_type_0_item = OrgMemberDTO.from_dict(members_type_0_item_data)

                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrgMemberDTO] | None, data)

        members = _parse_members(d.pop("members"))

        org = OrgDTO.from_dict(d.pop("org"))

        schema = d.pop("$schema", UNSET)

        get_org_output_body = cls(
            invitations=invitations,
            members=members,
            org=org,
            schema=schema,
        )

        return get_org_output_body
