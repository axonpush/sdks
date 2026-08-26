from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_key_scope import ApiKeyScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyCreateResponseDto")


@_attrs_define
class ApiKeyCreateResponseDto:
    """
    Attributes:
        allow_environment_override (bool):
        created_at (datetime.datetime):
        id (str):
        key (str): Raw API key, only returned at creation time
        name (str):
        scopes (list[ApiKeyScope]):
        environment_id (str | Unset):
        prefix (str | Unset):
    """

    allow_environment_override: bool
    created_at: datetime.datetime
    id: str
    key: str
    name: str
    scopes: list[ApiKeyScope]
    environment_id: str | Unset = UNSET
    prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_environment_override = self.allow_environment_override

        created_at = self.created_at.isoformat()

        id = self.id

        key = self.key

        name = self.name

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        environment_id = self.environment_id

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowEnvironmentOverride": allow_environment_override,
                "createdAt": created_at,
                "id": id,
                "key": key,
                "name": name,
                "scopes": scopes,
            }
        )
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_environment_override = d.pop("allowEnvironmentOverride")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        key = d.pop("key")

        name = d.pop("name")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = ApiKeyScope(scopes_item_data)

            scopes.append(scopes_item)

        environment_id = d.pop("environmentId", UNSET)

        prefix = d.pop("prefix", UNSET)

        api_key_create_response_dto = cls(
            allow_environment_override=allow_environment_override,
            created_at=created_at,
            id=id,
            key=key,
            name=name,
            scopes=scopes,
            environment_id=environment_id,
            prefix=prefix,
        )

        api_key_create_response_dto.additional_properties = d
        return api_key_create_response_dto

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
