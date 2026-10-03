from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityUndeclared")


@_attrs_define
class ActivityUndeclared:
    """
    Attributes:
        count (int):
        event (str):
        key (str):
        last_seen_at (datetime.datetime):
    """

    count: int
    event: str
    key: str
    last_seen_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        event = self.event

        key = self.key

        last_seen_at = self.last_seen_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "event": event,
                "key": key,
                "lastSeenAt": last_seen_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        event = d.pop("event")

        key = d.pop("key")

        last_seen_at = isoparse(d.pop("lastSeenAt"))

        activity_undeclared = cls(
            count=count,
            event=event,
            key=key,
            last_seen_at=last_seen_at,
        )

        return activity_undeclared
