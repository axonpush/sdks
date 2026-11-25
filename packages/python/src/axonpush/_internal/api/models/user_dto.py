from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="UserDTO")


@_attrs_define
class UserDTO:
    """
    Attributes:
        created_at (str):
        email (str):
        email_verified (bool):
        extra_free_orgs (int | None): Free organisations granted beyond the one everybody gets; null means none, -1
            unlimited
        id (str):
        owned_orgs (int): Live organisations this user owns
        deleted_at (str | Unset):
        disabled_at (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        organization_id (str | Unset):
        username (str | Unset):
    """

    created_at: str
    email: str
    email_verified: bool
    extra_free_orgs: int | None
    id: str
    owned_orgs: int
    deleted_at: str | Unset = UNSET
    disabled_at: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    organization_id: str | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        email = self.email

        email_verified = self.email_verified

        extra_free_orgs: int | None
        extra_free_orgs = self.extra_free_orgs

        id = self.id

        owned_orgs = self.owned_orgs

        deleted_at = self.deleted_at

        disabled_at = self.disabled_at

        first_name = self.first_name

        last_name = self.last_name

        organization_id = self.organization_id

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "email": email,
                "emailVerified": email_verified,
                "extraFreeOrgs": extra_free_orgs,
                "id": id,
                "ownedOrgs": owned_orgs,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
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
        created_at = d.pop("createdAt")

        email = d.pop("email")

        email_verified = d.pop("emailVerified")

        def _parse_extra_free_orgs(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        extra_free_orgs = _parse_extra_free_orgs(d.pop("extraFreeOrgs"))

        id = d.pop("id")

        owned_orgs = d.pop("ownedOrgs")

        deleted_at = d.pop("deletedAt", UNSET)

        disabled_at = d.pop("disabledAt", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        username = d.pop("username", UNSET)

        user_dto = cls(
            created_at=created_at,
            email=email,
            email_verified=email_verified,
            extra_free_orgs=extra_free_orgs,
            id=id,
            owned_orgs=owned_orgs,
            deleted_at=deleted_at,
            disabled_at=disabled_at,
            first_name=first_name,
            last_name=last_name,
            organization_id=organization_id,
            username=username,
        )

        return user_dto
