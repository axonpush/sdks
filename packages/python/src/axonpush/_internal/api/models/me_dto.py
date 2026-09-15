from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_dto import MembershipDTO


T = TypeVar("T", bound="MeDTO")


@_attrs_define
class MeDTO:
    """
    Attributes:
        auth_method (str):
        email_verified (bool):
        memberships (list[MembershipDTO] | None):
        org_id (str):
        roles (list[str] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        email (str | Unset):
        user_id (str | Unset):
    """

    auth_method: str
    email_verified: bool
    memberships: list[MembershipDTO] | None
    org_id: str
    roles: list[str] | None
    schema: str | Unset = UNSET
    email: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.membership_dto import MembershipDTO

        auth_method = self.auth_method

        email_verified = self.email_verified

        memberships: list[dict[str, Any]] | None
        if isinstance(self.memberships, list):
            memberships = []
            for memberships_type_0_item_data in self.memberships:
                memberships_type_0_item = memberships_type_0_item_data.to_dict()
                memberships.append(memberships_type_0_item)

        else:
            memberships = self.memberships

        org_id = self.org_id

        roles: list[str] | None
        if isinstance(self.roles, list):
            roles = self.roles

        else:
            roles = self.roles

        schema = self.schema

        email = self.email

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authMethod": auth_method,
                "emailVerified": email_verified,
                "memberships": memberships,
                "orgId": org_id,
                "roles": roles,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if email is not UNSET:
            field_dict["email"] = email
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_dto import MembershipDTO

        d = dict(src_dict)
        auth_method = d.pop("authMethod")

        email_verified = d.pop("emailVerified")

        def _parse_memberships(data: object) -> list[MembershipDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                memberships_type_0 = []
                _memberships_type_0 = data
                for memberships_type_0_item_data in _memberships_type_0:
                    memberships_type_0_item = MembershipDTO.from_dict(memberships_type_0_item_data)

                    memberships_type_0.append(memberships_type_0_item)

                return memberships_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipDTO] | None, data)

        memberships = _parse_memberships(d.pop("memberships"))

        org_id = d.pop("orgId")

        def _parse_roles(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = cast(list[str], data)

                return roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        roles = _parse_roles(d.pop("roles"))

        schema = d.pop("$schema", UNSET)

        email = d.pop("email", UNSET)

        user_id = d.pop("userId", UNSET)

        me_dto = cls(
            auth_method=auth_method,
            email_verified=email_verified,
            memberships=memberships,
            org_id=org_id,
            roles=roles,
            schema=schema,
            email=email,
            user_id=user_id,
        )

        return me_dto
