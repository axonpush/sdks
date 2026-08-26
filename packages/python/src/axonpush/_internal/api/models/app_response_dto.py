from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_response_dto import ChannelResponseDto


T = TypeVar("T", bound="AppResponseDto")


@_attrs_define
class AppResponseDto:
    """
    Attributes:
        app_id (str):
        created_at (datetime.datetime):
        id (str):
        name (str):
        org_id (str):
        channels (list[ChannelResponseDto] | Unset):
        creator_user_id (str | Unset):
        deleted_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    app_id: str
    created_at: datetime.datetime
    id: str
    name: str
    org_id: str
    channels: list[ChannelResponseDto] | Unset = UNSET
    creator_user_id: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_response_dto import ChannelResponseDto

        app_id = self.app_id

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        org_id = self.org_id

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        creator_user_id = self.creator_user_id

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "createdAt": created_at,
                "id": id,
                "name": name,
                "orgId": org_id,
            }
        )
        if channels is not UNSET:
            field_dict["channels"] = channels
        if creator_user_id is not UNSET:
            field_dict["creatorUserId"] = creator_user_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_response_dto import ChannelResponseDto

        d = dict(src_dict)
        app_id = d.pop("appId")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        org_id = d.pop("orgId")

        _channels = d.pop("channels", UNSET)
        channels: list[ChannelResponseDto] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ChannelResponseDto.from_dict(channels_item_data)

                channels.append(channels_item)

        creator_user_id = d.pop("creatorUserId", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        app_response_dto = cls(
            app_id=app_id,
            created_at=created_at,
            id=id,
            name=name,
            org_id=org_id,
            channels=channels,
            creator_user_id=creator_user_id,
            deleted_at=deleted_at,
            updated_at=updated_at,
        )

        app_response_dto.additional_properties = d
        return app_response_dto

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
