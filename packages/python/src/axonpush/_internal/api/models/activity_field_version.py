from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityFieldVersion")


@_attrs_define
class ActivityFieldVersion:
    """
    Attributes:
        event_id (str):
        revision (int):
        source_ref (str):
        time (datetime.datetime):
    """

    event_id: str
    revision: int
    source_ref: str
    time: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        revision = self.revision

        source_ref = self.source_ref

        time = self.time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eventId": event_id,
                "revision": revision,
                "sourceRef": source_ref,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("eventId")

        revision = d.pop("revision")

        source_ref = d.pop("sourceRef")

        time = isoparse(d.pop("time"))

        activity_field_version = cls(
            event_id=event_id,
            revision=revision,
            source_ref=source_ref,
            time=time,
        )

        return activity_field_version
