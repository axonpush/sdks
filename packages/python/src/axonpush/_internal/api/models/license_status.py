from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseStatus")


@_attrs_define
class LicenseStatus:
    """
    Attributes:
        expires_at (None | str):
        status (str):
        tier (None | str):
    """

    expires_at: None | str
    status: str
    tier: None | str

    def to_dict(self) -> dict[str, Any]:
        expires_at: None | str
        expires_at = self.expires_at

        status = self.status

        tier: None | str
        tier = self.tier

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expiresAt": expires_at,
                "status": status,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        status = d.pop("status")

        def _parse_tier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier = _parse_tier(d.pop("tier"))

        license_status = cls(
            expires_at=expires_at,
            status=status,
            tier=tier,
        )

        return license_status
