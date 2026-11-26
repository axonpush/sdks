from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentDTO")


@_attrs_define
class EnvironmentDTO:
    """
    Attributes:
        color (str):
        created_at (str):
        environment_id (str):
        is_default (bool):
        is_ephemeral (bool):
        is_production (bool):
        name (str):
        org_id (str):
        slug (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        expires_at (str | Unset):
        updated_at (str | Unset):
    """

    color: str
    created_at: str
    environment_id: str
    is_default: bool
    is_ephemeral: bool
    is_production: bool
    name: str
    org_id: str
    slug: str
    schema: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        created_at = self.created_at

        environment_id = self.environment_id

        is_default = self.is_default

        is_ephemeral = self.is_ephemeral

        is_production = self.is_production

        name = self.name

        org_id = self.org_id

        slug = self.slug

        schema = self.schema

        expires_at = self.expires_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "color": color,
                "createdAt": created_at,
                "environmentId": environment_id,
                "isDefault": is_default,
                "isEphemeral": is_ephemeral,
                "isProduction": is_production,
                "name": name,
                "orgId": org_id,
                "slug": slug,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color")

        created_at = d.pop("createdAt")

        environment_id = d.pop("environmentId")

        is_default = d.pop("isDefault")

        is_ephemeral = d.pop("isEphemeral")

        is_production = d.pop("isProduction")

        name = d.pop("name")

        org_id = d.pop("orgId")

        slug = d.pop("slug")

        schema = d.pop("$schema", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        environment_dto = cls(
            color=color,
            created_at=created_at,
            environment_id=environment_id,
            is_default=is_default,
            is_ephemeral=is_ephemeral,
            is_production=is_production,
            name=name,
            org_id=org_id,
            slug=slug,
            schema=schema,
            expires_at=expires_at,
            updated_at=updated_at,
        )

        return environment_dto
