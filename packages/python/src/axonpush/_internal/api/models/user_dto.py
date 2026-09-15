from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDTO")


@_attrs_define
class UserDTO:
    """
    Attributes:
        email (str):
        id (str):
        disabled_at (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        organization_id (str | Unset):
        username (str | Unset):
    """

    email: str
    id: str
    disabled_at: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    organization_id: str | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        id = self.id

        disabled_at = self.disabled_at

        first_name = self.first_name

        last_name = self.last_name

        organization_id = self.organization_id

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "id": id,
            }
        )
        if disabled_at is not UNSET:
            field_dict["disabledAt"] = disabled_at
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        id = d.pop("id")

        disabled_at = d.pop("disabledAt", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        username = d.pop("username", UNSET)

        user_dto = cls(
            email=email,
            id=id,
            disabled_at=disabled_at,
            first_name=first_name,
            last_name=last_name,
            organization_id=organization_id,
            username=username,
        )

        return user_dto
