from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_member_role_input_body_role import UpdateMemberRoleInputBodyRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMemberRoleInputBody")


@_attrs_define
class UpdateMemberRoleInputBody:
    """
    Attributes:
        role (UpdateMemberRoleInputBodyRole):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    role: UpdateMemberRoleInputBodyRole
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = UpdateMemberRoleInputBodyRole(d.pop("role"))

        schema = d.pop("$schema", UNSET)

        update_member_role_input_body = cls(
            role=role,
            schema=schema,
        )

        return update_member_role_input_body
