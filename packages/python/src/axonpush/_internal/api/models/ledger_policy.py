from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerPolicy")


@_attrs_define
class LedgerPolicy:
    """
    Attributes:
        archive_content (bool):
        configured (bool):
        days (int):
        enabled (bool):
        lock_mode (str):
        maximum_days (int):
        region (str):
        revision (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    archive_content: bool
    configured: bool
    days: int
    enabled: bool
    lock_mode: str
    maximum_days: int
    region: str
    revision: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        archive_content = self.archive_content

        configured = self.configured

        days = self.days

        enabled = self.enabled

        lock_mode = self.lock_mode

        maximum_days = self.maximum_days

        region = self.region

        revision = self.revision

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "archiveContent": archive_content,
                "configured": configured,
                "days": days,
                "enabled": enabled,
                "lockMode": lock_mode,
                "maximumDays": maximum_days,
                "region": region,
                "revision": revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archive_content = d.pop("archiveContent")

        configured = d.pop("configured")

        days = d.pop("days")

        enabled = d.pop("enabled")

        lock_mode = d.pop("lockMode")

        maximum_days = d.pop("maximumDays")

        region = d.pop("region")

        revision = d.pop("revision")

        schema = d.pop("$schema", UNSET)

        ledger_policy = cls(
            archive_content=archive_content,
            configured=configured,
            days=days,
            enabled=enabled,
            lock_mode=lock_mode,
            maximum_days=maximum_days,
            region=region,
            revision=revision,
            schema=schema,
        )

        return ledger_policy
