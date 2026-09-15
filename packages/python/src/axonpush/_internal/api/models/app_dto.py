from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppDTO")


@_attrs_define
class AppDTO:
    """
    Attributes:
        app_id (str):
        created_at (str):
        name (str):
        org_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        creator_user_id (str | Unset):
        updated_at (str | Unset):
    """

    app_id: str
    created_at: str
    name: str
    org_id: str
    schema: str | Unset = UNSET
    creator_user_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        created_at = self.created_at

        name = self.name

        org_id = self.org_id

        schema = self.schema

        creator_user_id = self.creator_user_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "appId": app_id,
                "createdAt": created_at,
                "name": name,
                "orgId": org_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if creator_user_id is not UNSET:
            field_dict["creatorUserId"] = creator_user_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId")

        created_at = d.pop("createdAt")

        name = d.pop("name")

        org_id = d.pop("orgId")

        schema = d.pop("$schema", UNSET)

        creator_user_id = d.pop("creatorUserId", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        app_dto = cls(
            app_id=app_id,
            created_at=created_at,
            name=name,
            org_id=org_id,
            schema=schema,
            creator_user_id=creator_user_id,
            updated_at=updated_at,
        )

        return app_dto
