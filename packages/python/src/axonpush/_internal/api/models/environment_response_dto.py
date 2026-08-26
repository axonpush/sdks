from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentResponseDto")


@_attrs_define
class EnvironmentResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        environment_id (str):
        id (str):
        name (str):
        org_id (str):
        slug (str):
        color (str | Unset):
        deleted_at (datetime.datetime | Unset):
        expires_at (datetime.datetime | Unset):
        is_default (bool | Unset):
        is_ephemeral (bool | Unset):
        is_production (bool | Unset):
        updated_at (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    environment_id: str
    id: str
    name: str
    org_id: str
    slug: str
    color: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_ephemeral: bool | Unset = UNSET
    is_production: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        environment_id = self.environment_id

        id = self.id

        name = self.name

        org_id = self.org_id

        slug = self.slug

        color = self.color

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        is_default = self.is_default

        is_ephemeral = self.is_ephemeral

        is_production = self.is_production

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "environmentId": environment_id,
                "id": id,
                "name": name,
                "orgId": org_id,
                "slug": slug,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_ephemeral is not UNSET:
            field_dict["isEphemeral"] = is_ephemeral
        if is_production is not UNSET:
            field_dict["isProduction"] = is_production
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        environment_id = d.pop("environmentId")

        id = d.pop("id")

        name = d.pop("name")

        org_id = d.pop("orgId")

        slug = d.pop("slug")

        color = d.pop("color", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        is_default = d.pop("isDefault", UNSET)

        is_ephemeral = d.pop("isEphemeral", UNSET)

        is_production = d.pop("isProduction", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        environment_response_dto = cls(
            created_at=created_at,
            environment_id=environment_id,
            id=id,
            name=name,
            org_id=org_id,
            slug=slug,
            color=color,
            deleted_at=deleted_at,
            expires_at=expires_at,
            is_default=is_default,
            is_ephemeral=is_ephemeral,
            is_production=is_production,
            updated_at=updated_at,
        )

        environment_response_dto.additional_properties = d
        return environment_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
