from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyOutputBody")


@_attrs_define
class VerifyOutputBody:
    """
    Attributes:
        events (int):
        segment_id (str):
        valid (bool):
        verified_at (datetime.datetime):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    events: int
    segment_id: str
    valid: bool
    verified_at: datetime.datetime
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        segment_id = self.segment_id

        valid = self.valid

        verified_at = self.verified_at.isoformat()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "segmentId": segment_id,
                "valid": valid,
                "verifiedAt": verified_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = d.pop("events")

        segment_id = d.pop("segmentId")

        valid = d.pop("valid")

        verified_at = isoparse(d.pop("verifiedAt"))

        schema = d.pop("$schema", UNSET)

        verify_output_body = cls(
            events=events,
            segment_id=segment_id,
            valid=valid,
            verified_at=verified_at,
            schema=schema,
        )

        return verify_output_body
