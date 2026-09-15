from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_dto import UserDTO


T = TypeVar("T", bound="SearchUsersOutputBody")


@_attrs_define
class SearchUsersOutputBody:
    """
    Attributes:
        users (list[UserDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    users: list[UserDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_dto import UserDTO

        users: list[dict[str, Any]] | None
        if isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "users": users,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_dto import UserDTO

        d = dict(src_dict)

        def _parse_users(data: object) -> list[UserDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = UserDTO.from_dict(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UserDTO] | None, data)

        users = _parse_users(d.pop("users"))

        schema = d.pop("$schema", UNSET)

        search_users_output_body = cls(
            users=users,
            schema=schema,
        )

        return search_users_output_body
