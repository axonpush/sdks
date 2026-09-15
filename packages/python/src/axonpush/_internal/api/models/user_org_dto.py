from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_dto import OrganizationDTO


T = TypeVar("T", bound="UserOrgDTO")


@_attrs_define
class UserOrgDTO:
    """
    Attributes:
        organization (OrganizationDTO):
        role (str):
    """

    organization: OrganizationDTO
    role: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_dto import OrganizationDTO

        organization = self.organization.to_dict()

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "organization": organization,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_dto import OrganizationDTO

        d = dict(src_dict)
        organization = OrganizationDTO.from_dict(d.pop("organization"))

        role = d.pop("role")

        user_org_dto = cls(
            organization=organization,
            role=role,
        )

        return user_org_dto
