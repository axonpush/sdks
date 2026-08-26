from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IotTokenResponseDto")


@_attrs_define
class IotTokenResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        organization_id (str):
        prefix (str):
        expires_at (datetime.datetime | Unset):
        last_used_at (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    id: str
    name: str
    organization_id: str
    prefix: str
    expires_at: datetime.datetime | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        organization_id = self.organization_id

        prefix = self.prefix

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "organizationId": organization_id,
                "prefix": prefix,
            }
        )
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        organization_id = d.pop("organizationId")

        prefix = d.pop("prefix")

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        _last_used_at = d.pop("lastUsedAt", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = isoparse(_last_used_at)

        iot_token_response_dto = cls(
            created_at=created_at,
            id=id,
            name=name,
            organization_id=organization_id,
            prefix=prefix,
            expires_at=expires_at,
            last_used_at=last_used_at,
        )

        iot_token_response_dto.additional_properties = d
        return iot_token_response_dto

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
