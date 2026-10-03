from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityPipelineHealth")


@_attrs_define
class ActivityPipelineHealth:
    """
    Attributes:
        capture_failures (int):
        dead_letters (int):
        dropped_transient (int):
        pending (int):
        reconciled_records (int):
        retries (int):
        last_export_at (datetime.datetime | Unset):
        reconciled_at (datetime.datetime | Unset):
    """

    capture_failures: int
    dead_letters: int
    dropped_transient: int
    pending: int
    reconciled_records: int
    retries: int
    last_export_at: datetime.datetime | Unset = UNSET
    reconciled_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        capture_failures = self.capture_failures

        dead_letters = self.dead_letters

        dropped_transient = self.dropped_transient

        pending = self.pending

        reconciled_records = self.reconciled_records

        retries = self.retries

        last_export_at: str | Unset = UNSET
        if not isinstance(self.last_export_at, Unset):
            last_export_at = self.last_export_at.isoformat()

        reconciled_at: str | Unset = UNSET
        if not isinstance(self.reconciled_at, Unset):
            reconciled_at = self.reconciled_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "capture_failures": capture_failures,
                "dead_letters": dead_letters,
                "dropped_transient": dropped_transient,
                "pending": pending,
                "reconciled_records": reconciled_records,
                "retries": retries,
            }
        )
        if last_export_at is not UNSET:
            field_dict["last_export_at"] = last_export_at
        if reconciled_at is not UNSET:
            field_dict["reconciled_at"] = reconciled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capture_failures = d.pop("capture_failures")

        dead_letters = d.pop("dead_letters")

        dropped_transient = d.pop("dropped_transient")

        pending = d.pop("pending")

        reconciled_records = d.pop("reconciled_records")

        retries = d.pop("retries")

        _last_export_at = d.pop("last_export_at", UNSET)
        last_export_at: datetime.datetime | Unset
        if isinstance(_last_export_at, Unset):
            last_export_at = UNSET
        else:
            last_export_at = isoparse(_last_export_at)

        _reconciled_at = d.pop("reconciled_at", UNSET)
        reconciled_at: datetime.datetime | Unset
        if isinstance(_reconciled_at, Unset):
            reconciled_at = UNSET
        else:
            reconciled_at = isoparse(_reconciled_at)

        activity_pipeline_health = cls(
            capture_failures=capture_failures,
            dead_letters=dead_letters,
            dropped_transient=dropped_transient,
            pending=pending,
            reconciled_records=reconciled_records,
            retries=retries,
            last_export_at=last_export_at,
            reconciled_at=reconciled_at,
        )

        return activity_pipeline_health
