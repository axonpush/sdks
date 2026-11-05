from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerSegment")


@_attrs_define
class LedgerSegment:
    """
    Attributes:
        bytes_raw (int):
        bytes_stored (int):
        events (int):
        locked_until (datetime.datetime):
        period_start (datetime.datetime):
        root (str):
        sealed_at (datetime.datetime):
        segment_id (str):
        state (str):
        verified_at (datetime.datetime):
    """

    bytes_raw: int
    bytes_stored: int
    events: int
    locked_until: datetime.datetime
    period_start: datetime.datetime
    root: str
    sealed_at: datetime.datetime
    segment_id: str
    state: str
    verified_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        bytes_raw = self.bytes_raw

        bytes_stored = self.bytes_stored

        events = self.events

        locked_until = self.locked_until.isoformat()

        period_start = self.period_start.isoformat()

        root = self.root

        sealed_at = self.sealed_at.isoformat()

        segment_id = self.segment_id

        state = self.state

        verified_at = self.verified_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bytesRaw": bytes_raw,
                "bytesStored": bytes_stored,
                "events": events,
                "lockedUntil": locked_until,
                "periodStart": period_start,
                "root": root,
                "sealedAt": sealed_at,
                "segmentId": segment_id,
                "state": state,
                "verifiedAt": verified_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_raw = d.pop("bytesRaw")

        bytes_stored = d.pop("bytesStored")

        events = d.pop("events")

        locked_until = isoparse(d.pop("lockedUntil"))

        period_start = isoparse(d.pop("periodStart"))

        root = d.pop("root")

        sealed_at = isoparse(d.pop("sealedAt"))

        segment_id = d.pop("segmentId")

        state = d.pop("state")

        verified_at = isoparse(d.pop("verifiedAt"))

        ledger_segment = cls(
            bytes_raw=bytes_raw,
            bytes_stored=bytes_stored,
            events=events,
            locked_until=locked_until,
            period_start=period_start,
            root=root,
            sealed_at=sealed_at,
            segment_id=segment_id,
            state=state,
            verified_at=verified_at,
        )

        return ledger_segment
