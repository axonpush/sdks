from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusOutputBody")


@_attrs_define
class StatusOutputBody:
    """
    Attributes:
        active_holds (int):
        anchor_sequence (int):
        bytes_raw (int):
        bytes_stored (int):
        checkpoint_state (str):
        configured (bool):
        enabled (bool):
        events (int):
        head_hash (str):
        head_sequence (int):
        pending_jobs (int):
        restoring (bool):
        segments (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        last_sealed_at (datetime.datetime | Unset):
        last_timestamped_at (datetime.datetime | Unset):
    """

    active_holds: int
    anchor_sequence: int
    bytes_raw: int
    bytes_stored: int
    checkpoint_state: str
    configured: bool
    enabled: bool
    events: int
    head_hash: str
    head_sequence: int
    pending_jobs: int
    restoring: bool
    segments: int
    schema: str | Unset = UNSET
    last_sealed_at: datetime.datetime | Unset = UNSET
    last_timestamped_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active_holds = self.active_holds

        anchor_sequence = self.anchor_sequence

        bytes_raw = self.bytes_raw

        bytes_stored = self.bytes_stored

        checkpoint_state = self.checkpoint_state

        configured = self.configured

        enabled = self.enabled

        events = self.events

        head_hash = self.head_hash

        head_sequence = self.head_sequence

        pending_jobs = self.pending_jobs

        restoring = self.restoring

        segments = self.segments

        schema = self.schema

        last_sealed_at: str | Unset = UNSET
        if not isinstance(self.last_sealed_at, Unset):
            last_sealed_at = self.last_sealed_at.isoformat()

        last_timestamped_at: str | Unset = UNSET
        if not isinstance(self.last_timestamped_at, Unset):
            last_timestamped_at = self.last_timestamped_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "activeHolds": active_holds,
                "anchorSequence": anchor_sequence,
                "bytesRaw": bytes_raw,
                "bytesStored": bytes_stored,
                "checkpointState": checkpoint_state,
                "configured": configured,
                "enabled": enabled,
                "events": events,
                "headHash": head_hash,
                "headSequence": head_sequence,
                "pendingJobs": pending_jobs,
                "restoring": restoring,
                "segments": segments,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if last_sealed_at is not UNSET:
            field_dict["lastSealedAt"] = last_sealed_at
        if last_timestamped_at is not UNSET:
            field_dict["lastTimestampedAt"] = last_timestamped_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_holds = d.pop("activeHolds")

        anchor_sequence = d.pop("anchorSequence")

        bytes_raw = d.pop("bytesRaw")

        bytes_stored = d.pop("bytesStored")

        checkpoint_state = d.pop("checkpointState")

        configured = d.pop("configured")

        enabled = d.pop("enabled")

        events = d.pop("events")

        head_hash = d.pop("headHash")

        head_sequence = d.pop("headSequence")

        pending_jobs = d.pop("pendingJobs")

        restoring = d.pop("restoring")

        segments = d.pop("segments")

        schema = d.pop("$schema", UNSET)

        _last_sealed_at = d.pop("lastSealedAt", UNSET)
        last_sealed_at: datetime.datetime | Unset
        if isinstance(_last_sealed_at, Unset):
            last_sealed_at = UNSET
        else:
            last_sealed_at = isoparse(_last_sealed_at)

        _last_timestamped_at = d.pop("lastTimestampedAt", UNSET)
        last_timestamped_at: datetime.datetime | Unset
        if isinstance(_last_timestamped_at, Unset):
            last_timestamped_at = UNSET
        else:
            last_timestamped_at = isoparse(_last_timestamped_at)

        status_output_body = cls(
            active_holds=active_holds,
            anchor_sequence=anchor_sequence,
            bytes_raw=bytes_raw,
            bytes_stored=bytes_stored,
            checkpoint_state=checkpoint_state,
            configured=configured,
            enabled=enabled,
            events=events,
            head_hash=head_hash,
            head_sequence=head_sequence,
            pending_jobs=pending_jobs,
            restoring=restoring,
            segments=segments,
            schema=schema,
            last_sealed_at=last_sealed_at,
            last_timestamped_at=last_timestamped_at,
        )

        return status_output_body
