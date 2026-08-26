from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IotCredentialsResponseDto")


@_attrs_define
class IotCredentialsResponseDto:
    """
    Attributes:
        client_id (str):
        endpoint (str):
        env_slug (str): Default environment slug for this org. Frontends should slot this segment between `topicPrefix`
            and the appId when subscribing without an explicit env.
        expires_at (datetime.datetime):
        presigned_wss_url (str):
        region (str):
        topic_prefix (str): Org-scoped MQTT topic prefix. Subscribe topics must extend this with
            `/{envSlug}/{appId}/{channelId}/{eventType}/{agentId}` (use `+` for wildcards).
        topic_template (str): Human-readable template showing every topic segment the broker will publish to. Mirrors
            the publish-side topic-builder layout.
        auth_token (str | Unset): Bearer token to pass as the MQTT CONNECT username. The IoT custom authorizer reads it
            from `mqttContext.username`.
        authorizer_name (str | Unset): IoT custom authorizer name to invoke. Already encoded in `presignedWssUrl` query
            string; exposed for clients that need to set it via header.
    """

    client_id: str
    endpoint: str
    env_slug: str
    expires_at: datetime.datetime
    presigned_wss_url: str
    region: str
    topic_prefix: str
    topic_template: str
    auth_token: str | Unset = UNSET
    authorizer_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        endpoint = self.endpoint

        env_slug = self.env_slug

        expires_at = self.expires_at.isoformat()

        presigned_wss_url = self.presigned_wss_url

        region = self.region

        topic_prefix = self.topic_prefix

        topic_template = self.topic_template

        auth_token = self.auth_token

        authorizer_name = self.authorizer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "endpoint": endpoint,
                "envSlug": env_slug,
                "expiresAt": expires_at,
                "presignedWssUrl": presigned_wss_url,
                "region": region,
                "topicPrefix": topic_prefix,
                "topicTemplate": topic_template,
            }
        )
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if authorizer_name is not UNSET:
            field_dict["authorizerName"] = authorizer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId")

        endpoint = d.pop("endpoint")

        env_slug = d.pop("envSlug")

        expires_at = isoparse(d.pop("expiresAt"))

        presigned_wss_url = d.pop("presignedWssUrl")

        region = d.pop("region")

        topic_prefix = d.pop("topicPrefix")

        topic_template = d.pop("topicTemplate")

        auth_token = d.pop("authToken", UNSET)

        authorizer_name = d.pop("authorizerName", UNSET)

        iot_credentials_response_dto = cls(
            client_id=client_id,
            endpoint=endpoint,
            env_slug=env_slug,
            expires_at=expires_at,
            presigned_wss_url=presigned_wss_url,
            region=region,
            topic_prefix=topic_prefix,
            topic_template=topic_template,
            auth_token=auth_token,
            authorizer_name=authorizer_name,
        )

        iot_credentials_response_dto.additional_properties = d
        return iot_credentials_response_dto

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
