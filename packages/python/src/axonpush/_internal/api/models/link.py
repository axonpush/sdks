from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime


T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        env_name (str): Environment variable the claimed key belongs in
        expires_at (datetime.datetime):
        url (str): Open this in the dashboard, signed in as the same user, to reveal the key once
    """

    env_name: str
    expires_at: datetime.datetime
    url: str

    def to_dict(self) -> dict[str, Any]:
        env_name = self.env_name

        expires_at = self.expires_at.isoformat()

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "envName": env_name,
                "expiresAt": expires_at,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        env_name = d.pop("envName")

        expires_at = isoparse(d.pop("expiresAt"))

        url = d.pop("url")

        link = cls(
            env_name=env_name,
            expires_at=expires_at,
            url=url,
        )

        return link
