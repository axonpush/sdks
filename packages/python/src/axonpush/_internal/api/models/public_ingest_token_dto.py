from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicIngestTokenDTO")


@_attrs_define
class PublicIngestTokenDTO:
    """
    Attributes:
        active (bool):
        channel_id (str):
        created_at (str):
        environment_id (str):
        name (str):
        org_id (str):
        prefix (str):
        token_id (str):
        app_id (str | Unset):
        last_used_at (str | Unset):
    """

    active: bool
    channel_id: str
    created_at: str
    environment_id: str
    name: str
    org_id: str
    prefix: str
    token_id: str
    app_id: str | Unset = UNSET
    last_used_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        channel_id = self.channel_id

        created_at = self.created_at

        environment_id = self.environment_id

        name = self.name

        org_id = self.org_id

        prefix = self.prefix

        token_id = self.token_id

        app_id = self.app_id

        last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
                "channelId": channel_id,
                "createdAt": created_at,
                "environmentId": environment_id,
                "name": name,
                "orgId": org_id,
                "prefix": prefix,
                "tokenId": token_id,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        channel_id = d.pop("channelId")

        created_at = d.pop("createdAt")

        environment_id = d.pop("environmentId")

        name = d.pop("name")

        org_id = d.pop("orgId")

        prefix = d.pop("prefix")

        token_id = d.pop("tokenId")

        app_id = d.pop("appId", UNSET)

        last_used_at = d.pop("lastUsedAt", UNSET)

        public_ingest_token_dto = cls(
            active=active,
            channel_id=channel_id,
            created_at=created_at,
            environment_id=environment_id,
            name=name,
            org_id=org_id,
            prefix=prefix,
            token_id=token_id,
            app_id=app_id,
            last_used_at=last_used_at,
        )

        return public_ingest_token_dto
