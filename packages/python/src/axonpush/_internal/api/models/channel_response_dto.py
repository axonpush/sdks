from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_response_dto import AppResponseDto


T = TypeVar("T", bound="ChannelResponseDto")


@_attrs_define
class ChannelResponseDto:
    """
    Attributes:
        app_id (str):
        channel_id (str):
        created_at (datetime.datetime):
        id (str):
        name (str):
        org_id (str):
        app (AppResponseDto | Unset):
        deleted_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    app_id: str
    channel_id: str
    created_at: datetime.datetime
    id: str
    name: str
    org_id: str
    app: AppResponseDto | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.app_response_dto import AppResponseDto

        app_id = self.app_id

        channel_id = self.channel_id

        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        org_id = self.org_id

        app: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

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
                "channelId": channel_id,
                "createdAt": created_at,
                "id": id,
                "name": name,
                "orgId": org_id,
            }
        )
        if app is not UNSET:
            field_dict["app"] = app
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_response_dto import AppResponseDto

        d = dict(src_dict)
        app_id = d.pop("appId")

        channel_id = d.pop("channelId")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        org_id = d.pop("orgId")

        _app = d.pop("app", UNSET)
        app: AppResponseDto | Unset
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = AppResponseDto.from_dict(_app)

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

        channel_response_dto = cls(
            app_id=app_id,
            channel_id=channel_id,
            created_at=created_at,
            id=id,
            name=name,
            org_id=org_id,
            app=app,
            deleted_at=deleted_at,
            updated_at=updated_at,
        )

        channel_response_dto.additional_properties = d
        return channel_response_dto

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
