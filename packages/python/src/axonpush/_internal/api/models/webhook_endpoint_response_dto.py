from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpointResponseDto")


@_attrs_define
class WebhookEndpointResponseDto:
    """
    Attributes:
        active (bool):
        channel_id (str):
        created_at (datetime.datetime):
        endpoint_id (str):
        id (str):
        url (str):
        deleted_at (datetime.datetime | Unset):
        description (str | Unset):
        event_types (list[str] | Unset):
        has_secret (bool | Unset):
        org_id (str | Unset):
        signing_secret_prefix (str | Unset):
        updated_at (datetime.datetime | Unset):
    """

    active: bool
    channel_id: str
    created_at: datetime.datetime
    endpoint_id: str
    id: str
    url: str
    deleted_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    has_secret: bool | Unset = UNSET
    org_id: str | Unset = UNSET
    signing_secret_prefix: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        channel_id = self.channel_id

        created_at = self.created_at.isoformat()

        endpoint_id = self.endpoint_id

        id = self.id

        url = self.url

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        description = self.description

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        has_secret = self.has_secret

        org_id = self.org_id

        signing_secret_prefix = self.signing_secret_prefix

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "channelId": channel_id,
                "createdAt": created_at,
                "endpointId": endpoint_id,
                "id": id,
                "url": url,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if has_secret is not UNSET:
            field_dict["hasSecret"] = has_secret
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if signing_secret_prefix is not UNSET:
            field_dict["signingSecretPrefix"] = signing_secret_prefix
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        channel_id = d.pop("channelId")

        created_at = isoparse(d.pop("createdAt"))

        endpoint_id = d.pop("endpointId")

        id = d.pop("id")

        url = d.pop("url")

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        description = d.pop("description", UNSET)

        event_types = cast(list[str], d.pop("eventTypes", UNSET))

        has_secret = d.pop("hasSecret", UNSET)

        org_id = d.pop("orgId", UNSET)

        signing_secret_prefix = d.pop("signingSecretPrefix", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        webhook_endpoint_response_dto = cls(
            active=active,
            channel_id=channel_id,
            created_at=created_at,
            endpoint_id=endpoint_id,
            id=id,
            url=url,
            deleted_at=deleted_at,
            description=description,
            event_types=event_types,
            has_secret=has_secret,
            org_id=org_id,
            signing_secret_prefix=signing_secret_prefix,
            updated_at=updated_at,
        )

        webhook_endpoint_response_dto.additional_properties = d
        return webhook_endpoint_response_dto

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
