from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookEndpointDto")


@_attrs_define
class CreateWebhookEndpointDto:
    """
    Attributes:
        channel_id (str):
        url (str):
        description (str | Unset):
        event_types (list[str] | Unset): Event types to filter (null = all)
        secret (str | Unset):
    """

    channel_id: str
    url: str
    description: str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        url = self.url

        description = self.description

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channelId")

        url = d.pop("url")

        description = d.pop("description", UNSET)

        event_types = cast(list[str], d.pop("eventTypes", UNSET))

        secret = d.pop("secret", UNSET)

        create_webhook_endpoint_dto = cls(
            channel_id=channel_id,
            url=url,
            description=description,
            event_types=event_types,
            secret=secret,
        )

        create_webhook_endpoint_dto.additional_properties = d
        return create_webhook_endpoint_dto

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
