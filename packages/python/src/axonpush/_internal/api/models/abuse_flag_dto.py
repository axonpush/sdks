from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbuseFlagDTO")


@_attrs_define
class AbuseFlagDTO:
    """
    Attributes:
        created_at (str):
        flag_id (str):
        org_id (str):
        reason (str):
        severity (str):
        status (str):
        reviewed_at (str | Unset):
        reviewed_by (str | Unset):
        signals (Any | Unset):
    """

    created_at: str
    flag_id: str
    org_id: str
    reason: str
    severity: str
    status: str
    reviewed_at: str | Unset = UNSET
    reviewed_by: str | Unset = UNSET
    signals: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        flag_id = self.flag_id

        org_id = self.org_id

        reason = self.reason

        severity = self.severity

        status = self.status

        reviewed_at = self.reviewed_at

        reviewed_by = self.reviewed_by

        signals = self.signals

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "flagId": flag_id,
                "orgId": org_id,
                "reason": reason,
                "severity": severity,
                "status": status,
            }
        )
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if reviewed_by is not UNSET:
            field_dict["reviewedBy"] = reviewed_by
        if signals is not UNSET:
            field_dict["signals"] = signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        flag_id = d.pop("flagId")

        org_id = d.pop("orgId")

        reason = d.pop("reason")

        severity = d.pop("severity")

        status = d.pop("status")

        reviewed_at = d.pop("reviewedAt", UNSET)

        reviewed_by = d.pop("reviewedBy", UNSET)

        signals = d.pop("signals", UNSET)

        abuse_flag_dto = cls(
            created_at=created_at,
            flag_id=flag_id,
            org_id=org_id,
            reason=reason,
            severity=severity,
            status=status,
            reviewed_at=reviewed_at,
            reviewed_by=reviewed_by,
            signals=signals,
        )

        return abuse_flag_dto
