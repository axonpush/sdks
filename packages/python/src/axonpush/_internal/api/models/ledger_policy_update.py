from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ledger_policy_update_days import LedgerPolicyUpdateDays
from ..models.ledger_policy_update_lock_mode import LedgerPolicyUpdateLockMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerPolicyUpdate")


@_attrs_define
class LedgerPolicyUpdate:
    """
    Attributes:
        archive_content (bool):
        days (LedgerPolicyUpdateDays):
        enabled (bool):
        lock_mode (LedgerPolicyUpdateLockMode):
        reason (str):
        region (str):
        revision (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        confirm_compliance (bool | Unset):
    """

    archive_content: bool
    days: LedgerPolicyUpdateDays
    enabled: bool
    lock_mode: LedgerPolicyUpdateLockMode
    reason: str
    region: str
    revision: int
    schema: str | Unset = UNSET
    confirm_compliance: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        archive_content = self.archive_content

        days = self.days.value

        enabled = self.enabled

        lock_mode = self.lock_mode.value

        reason = self.reason

        region = self.region

        revision = self.revision

        schema = self.schema

        confirm_compliance = self.confirm_compliance

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "archiveContent": archive_content,
                "days": days,
                "enabled": enabled,
                "lockMode": lock_mode,
                "reason": reason,
                "region": region,
                "revision": revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if confirm_compliance is not UNSET:
            field_dict["confirmCompliance"] = confirm_compliance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archive_content = d.pop("archiveContent")

        days = LedgerPolicyUpdateDays(d.pop("days"))

        enabled = d.pop("enabled")

        lock_mode = LedgerPolicyUpdateLockMode(d.pop("lockMode"))

        reason = d.pop("reason")

        region = d.pop("region")

        revision = d.pop("revision")

        schema = d.pop("$schema", UNSET)

        confirm_compliance = d.pop("confirmCompliance", UNSET)

        ledger_policy_update = cls(
            archive_content=archive_content,
            days=days,
            enabled=enabled,
            lock_mode=lock_mode,
            reason=reason,
            region=region,
            revision=revision,
            schema=schema,
            confirm_compliance=confirm_compliance,
        )

        return ledger_policy_update
