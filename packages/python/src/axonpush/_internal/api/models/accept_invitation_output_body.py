from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptInvitationOutputBody")


@_attrs_define
class AcceptInvitationOutputBody:
    """
    Attributes:
        org_id (str):
        org_name (str):
        role (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    org_id: str
    org_name: str
    role: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        org_name = self.org_name

        role = self.role

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "orgId": org_id,
                "orgName": org_name,
                "role": role,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        org_name = d.pop("orgName")

        role = d.pop("role")

        schema = d.pop("$schema", UNSET)

        accept_invitation_output_body = cls(
            org_id=org_id,
            org_name=org_name,
            role=role,
            schema=schema,
        )

        return accept_invitation_output_body
