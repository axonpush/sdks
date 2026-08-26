from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.license_status import LicenseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseStateDto")


@_attrs_define
class LicenseStateDto:
    """
    Attributes:
        applicable (bool):
        expires_at (datetime.datetime | None):
        grace_ends_at (datetime.datetime | None):
        last_diagnostics_at (datetime.datetime | None):
        message (None | str):
        reason (None | str):
        status (LicenseStatus):
        tier (None | str):
    """

    applicable: bool
    expires_at: datetime.datetime | None
    grace_ends_at: datetime.datetime | None
    last_diagnostics_at: datetime.datetime | None
    message: None | str
    reason: None | str
    status: LicenseStatus
    tier: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applicable = self.applicable

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        grace_ends_at: None | str
        if isinstance(self.grace_ends_at, datetime.datetime):
            grace_ends_at = self.grace_ends_at.isoformat()
        else:
            grace_ends_at = self.grace_ends_at

        last_diagnostics_at: None | str
        if isinstance(self.last_diagnostics_at, datetime.datetime):
            last_diagnostics_at = self.last_diagnostics_at.isoformat()
        else:
            last_diagnostics_at = self.last_diagnostics_at

        message: None | str
        message = self.message

        reason: None | str
        reason = self.reason

        status = self.status.value

        tier: None | str
        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicable": applicable,
                "expiresAt": expires_at,
                "graceEndsAt": grace_ends_at,
                "lastDiagnosticsAt": last_diagnostics_at,
                "message": message,
                "reason": reason,
                "status": status,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applicable = d.pop("applicable")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        def _parse_grace_ends_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grace_ends_at_type_0 = isoparse(data)

                return grace_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        grace_ends_at = _parse_grace_ends_at(d.pop("graceEndsAt"))

        def _parse_last_diagnostics_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_diagnostics_at_type_0 = isoparse(data)

                return last_diagnostics_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_diagnostics_at = _parse_last_diagnostics_at(d.pop("lastDiagnosticsAt"))

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        status = LicenseStatus(d.pop("status"))

        def _parse_tier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier = _parse_tier(d.pop("tier"))

        license_state_dto = cls(
            applicable=applicable,
            expires_at=expires_at,
            grace_ends_at=grace_ends_at,
            last_diagnostics_at=last_diagnostics_at,
            message=message,
            reason=reason,
            status=status,
            tier=tier,
        )

        license_state_dto.additional_properties = d
        return license_state_dto

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
