from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member_dto import MemberDTO


T = TypeVar("T", bound="ListMembersOutputBody")


@_attrs_define
class ListMembersOutputBody:
    """
    Attributes:
        members (list[MemberDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    members: list[MemberDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.member_dto import MemberDTO

        members: list[dict[str, Any]] | None
        if isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)

        else:
            members = self.members

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "members": members,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member_dto import MemberDTO

        d = dict(src_dict)

        def _parse_members(data: object) -> list[MemberDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in _members_type_0:
                    members_type_0_item = MemberDTO.from_dict(members_type_0_item_data)

                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MemberDTO] | None, data)

        members = _parse_members(d.pop("members"))

        schema = d.pop("$schema", UNSET)

        list_members_output_body = cls(
            members=members,
            schema=schema,
        )

        return list_members_output_body
