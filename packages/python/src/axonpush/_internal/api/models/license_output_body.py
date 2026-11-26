from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseOutputBody")


@_attrs_define
class LicenseOutputBody:
    """
    Attributes:
        edition (str):
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        expires_at (str | Unset):
        message (str | Unset):
        tier (str | Unset):
    """

    edition: str
    status: str
    schema: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    message: str | Unset = UNSET
    tier: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        edition = self.edition

        status = self.status

        schema = self.schema

        expires_at = self.expires_at

        message = self.message

        tier = self.tier

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "edition": edition,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if message is not UNSET:
            field_dict["message"] = message
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edition = d.pop("edition")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        message = d.pop("message", UNSET)

        tier = d.pop("tier", UNSET)

        license_output_body = cls(
            edition=edition,
            status=status,
            schema=schema,
            expires_at=expires_at,
            message=message,
            tier=tier,
        )

        return license_output_body
