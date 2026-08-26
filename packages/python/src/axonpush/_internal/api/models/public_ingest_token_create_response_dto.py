from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicIngestTokenCreateResponseDto")


@_attrs_define
class PublicIngestTokenCreateResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        org_id (str):
        token (str): Raw token, only returned at creation time
        token_id (str):
        app_id (str | Unset):
        channel_id (str | Unset):
        environment_id (str | Unset):
        last_used_at (datetime.datetime | Unset):
        prefix (str | Unset):
        revoked_at (datetime.datetime | Unset):
        scopes (list[str] | Unset):
    """

    created_at: datetime.datetime
    id: str
    name: str
    org_id: str
    token: str
    token_id: str
    app_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    prefix: str | Unset = UNSET
    revoked_at: datetime.datetime | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        org_id = self.org_id

        token = self.token

        token_id = self.token_id

        app_id = self.app_id

        channel_id = self.channel_id

        environment_id = self.environment_id

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        prefix = self.prefix

        revoked_at: str | Unset = UNSET
        if not isinstance(self.revoked_at, Unset):
            revoked_at = self.revoked_at.isoformat()

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "orgId": org_id,
                "token": token,
                "tokenId": token_id,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if revoked_at is not UNSET:
            field_dict["revokedAt"] = revoked_at
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        org_id = d.pop("orgId")

        token = d.pop("token")

        token_id = d.pop("tokenId")

        app_id = d.pop("appId", UNSET)

        channel_id = d.pop("channelId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        _last_used_at = d.pop("lastUsedAt", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = isoparse(_last_used_at)

        prefix = d.pop("prefix", UNSET)

        _revoked_at = d.pop("revokedAt", UNSET)
        revoked_at: datetime.datetime | Unset
        if isinstance(_revoked_at, Unset):
            revoked_at = UNSET
        else:
            revoked_at = isoparse(_revoked_at)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        public_ingest_token_create_response_dto = cls(
            created_at=created_at,
            id=id,
            name=name,
            org_id=org_id,
            token=token,
            token_id=token_id,
            app_id=app_id,
            channel_id=channel_id,
            environment_id=environment_id,
            last_used_at=last_used_at,
            prefix=prefix,
            revoked_at=revoked_at,
            scopes=scopes,
        )

        public_ingest_token_create_response_dto.additional_properties = d
        return public_ingest_token_create_response_dto

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
