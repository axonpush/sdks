from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_key_purpose import ApiKeyPurpose
from ..models.api_key_scope import ApiKeyScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyResponseDto")


@_attrs_define
class ApiKeyResponseDto:
    """
    Attributes:
        allow_environment_override (bool):
        created_at (datetime.datetime):
        id (str):
        name (str):
        scopes (list[ApiKeyScope]):
        app_id (str | Unset):
        environment_id (str | Unset):
        last_used_at (datetime.datetime | Unset):
        prefix (str | Unset):
        purpose (ApiKeyPurpose | Unset):
    """

    allow_environment_override: bool
    created_at: datetime.datetime
    id: str
    name: str
    scopes: list[ApiKeyScope]
    app_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    prefix: str | Unset = UNSET
    purpose: ApiKeyPurpose | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_environment_override = self.allow_environment_override

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        app_id = self.app_id

        environment_id = self.environment_id

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        prefix = self.prefix

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowEnvironmentOverride": allow_environment_override,
                "createdAt": created_at,
                "id": id,
                "name": name,
                "scopes": scopes,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_environment_override = d.pop("allowEnvironmentOverride")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = ApiKeyScope(scopes_item_data)

            scopes.append(scopes_item)

        app_id = d.pop("appId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        _last_used_at = d.pop("lastUsedAt", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = isoparse(_last_used_at)

        prefix = d.pop("prefix", UNSET)

        _purpose = d.pop("purpose", UNSET)
        purpose: ApiKeyPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = ApiKeyPurpose(_purpose)

        api_key_response_dto = cls(
            allow_environment_override=allow_environment_override,
            created_at=created_at,
            id=id,
            name=name,
            scopes=scopes,
            app_id=app_id,
            environment_id=environment_id,
            last_used_at=last_used_at,
            prefix=prefix,
            purpose=purpose,
        )

        api_key_response_dto.additional_properties = d
        return api_key_response_dto

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
