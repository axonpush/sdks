from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invitation_dto import InvitationDTO


T = TypeVar("T", bound="ListInvitationsOutputBody")


@_attrs_define
class ListInvitationsOutputBody:
    """
    Attributes:
        invitations (list[InvitationDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    invitations: list[InvitationDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.invitation_dto import InvitationDTO

        invitations: list[dict[str, Any]] | None
        if isinstance(self.invitations, list):
            invitations = []
            for invitations_type_0_item_data in self.invitations:
                invitations_type_0_item = invitations_type_0_item_data.to_dict()
                invitations.append(invitations_type_0_item)

        else:
            invitations = self.invitations

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invitations": invitations,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation_dto import InvitationDTO

        d = dict(src_dict)

        def _parse_invitations(data: object) -> list[InvitationDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                invitations_type_0 = []
                _invitations_type_0 = data
                for invitations_type_0_item_data in _invitations_type_0:
                    invitations_type_0_item = InvitationDTO.from_dict(invitations_type_0_item_data)

                    invitations_type_0.append(invitations_type_0_item)

                return invitations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InvitationDTO] | None, data)

        invitations = _parse_invitations(d.pop("invitations"))

        schema = d.pop("$schema", UNSET)

        list_invitations_output_body = cls(
            invitations=invitations,
            schema=schema,
        )

        return list_invitations_output_body
