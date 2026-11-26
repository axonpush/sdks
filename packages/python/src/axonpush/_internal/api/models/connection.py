from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Connection")


@_attrs_define
class Connection:
    """
    Attributes:
        client_key (str):
        client_name (str):
        client_version (str):
        first_seen (datetime.datetime):
        last_seen (datetime.datetime):
        user_id (str):
        oauth_client_id (str | Unset):
    """

    client_key: str
    client_name: str
    client_version: str
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    user_id: str
    oauth_client_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_key = self.client_key

        client_name = self.client_name

        client_version = self.client_version

        first_seen = self.first_seen.isoformat()

        last_seen = self.last_seen.isoformat()

        user_id = self.user_id

        oauth_client_id = self.oauth_client_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "clientKey": client_key,
                "clientName": client_name,
                "clientVersion": client_version,
                "firstSeen": first_seen,
                "lastSeen": last_seen,
                "userId": user_id,
            }
        )
        if oauth_client_id is not UNSET:
            field_dict["oauthClientId"] = oauth_client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_key = d.pop("clientKey")

        client_name = d.pop("clientName")

        client_version = d.pop("clientVersion")

        first_seen = isoparse(d.pop("firstSeen"))

        last_seen = isoparse(d.pop("lastSeen"))

        user_id = d.pop("userId")

        oauth_client_id = d.pop("oauthClientId", UNSET)

        connection = cls(
            client_key=client_key,
            client_name=client_name,
            client_version=client_version,
            first_seen=first_seen,
            last_seen=last_seen,
            user_id=user_id,
            oauth_client_id=oauth_client_id,
        )

        return connection
