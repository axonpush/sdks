from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="ClaimedKey")


@_attrs_define
class ClaimedKey:
    """
    Attributes:
        env_name (str):
        key (str):
        key_id (str):
        organization_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        sentry_dsn (str | Unset): SENTRY_DSN minted alongside the key by workspaces.connect
    """

    env_name: str
    key: str
    key_id: str
    organization_id: str
    schema: str | Unset = UNSET
    sentry_dsn: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        env_name = self.env_name

        key = self.key

        key_id = self.key_id

        organization_id = self.organization_id

        schema = self.schema

        sentry_dsn = self.sentry_dsn

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "envName": env_name,
                "key": key,
                "keyId": key_id,
                "organizationId": organization_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if sentry_dsn is not UNSET:
            field_dict["sentryDsn"] = sentry_dsn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        env_name = d.pop("envName")

        key = d.pop("key")

        key_id = d.pop("keyId")

        organization_id = d.pop("organizationId")

        schema = d.pop("$schema", UNSET)

        sentry_dsn = d.pop("sentryDsn", UNSET)

        claimed_key = cls(
            env_name=env_name,
            key=key,
            key_id=key_id,
            organization_id=organization_id,
            schema=schema,
            sentry_dsn=sentry_dsn,
        )

        return claimed_key
