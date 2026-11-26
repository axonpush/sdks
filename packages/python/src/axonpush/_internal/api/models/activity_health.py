from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_health_source import ActivityHealthSource
    from ..models.activity_undeclared import ActivityUndeclared


T = TypeVar("T", bound="ActivityHealth")


@_attrs_define
class ActivityHealth:
    """
    Attributes:
        checked_at (datetime.datetime):
        last_projected_at (datetime.datetime | None):
        last_received_at (datetime.datetime | None):
        oldest_pending_at (datetime.datetime | None):
        pending (int):
        undeclared (list[ActivityUndeclared] | None): Attribute keys sent in the last 7 days that the dictionary does
            not declare; they were dropped
        schema (str | Unset): A URL to the JSON Schema for this object.
        source (ActivityHealthSource | Unset): Attributes of the latest declared heartbeat event
        source_heartbeat_at (datetime.datetime | Unset):
    """

    checked_at: datetime.datetime
    last_projected_at: datetime.datetime | None
    last_received_at: datetime.datetime | None
    oldest_pending_at: datetime.datetime | None
    pending: int
    undeclared: list[ActivityUndeclared] | None
    schema: str | Unset = UNSET
    source: ActivityHealthSource | Unset = UNSET
    source_heartbeat_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_health_source import ActivityHealthSource
        from ..models.activity_undeclared import ActivityUndeclared

        checked_at = self.checked_at.isoformat()

        last_projected_at: None | str
        if isinstance(self.last_projected_at, datetime.datetime):
            last_projected_at = self.last_projected_at.isoformat()
        else:
            last_projected_at = self.last_projected_at

        last_received_at: None | str
        if isinstance(self.last_received_at, datetime.datetime):
            last_received_at = self.last_received_at.isoformat()
        else:
            last_received_at = self.last_received_at

        oldest_pending_at: None | str
        if isinstance(self.oldest_pending_at, datetime.datetime):
            oldest_pending_at = self.oldest_pending_at.isoformat()
        else:
            oldest_pending_at = self.oldest_pending_at

        pending = self.pending

        undeclared: list[dict[str, Any]] | None
        if isinstance(self.undeclared, list):
            undeclared = []
            for undeclared_type_0_item_data in self.undeclared:
                undeclared_type_0_item = undeclared_type_0_item_data.to_dict()
                undeclared.append(undeclared_type_0_item)

        else:
            undeclared = self.undeclared

        schema = self.schema

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        source_heartbeat_at: str | Unset = UNSET
        if not isinstance(self.source_heartbeat_at, Unset):
            source_heartbeat_at = self.source_heartbeat_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "checkedAt": checked_at,
                "lastProjectedAt": last_projected_at,
                "lastReceivedAt": last_received_at,
                "oldestPendingAt": oldest_pending_at,
                "pending": pending,
                "undeclared": undeclared,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if source is not UNSET:
            field_dict["source"] = source
        if source_heartbeat_at is not UNSET:
            field_dict["sourceHeartbeatAt"] = source_heartbeat_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_health_source import ActivityHealthSource
        from ..models.activity_undeclared import ActivityUndeclared

        d = dict(src_dict)
        checked_at = isoparse(d.pop("checkedAt"))

        def _parse_last_projected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_projected_at_type_0 = isoparse(data)

                return last_projected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_projected_at = _parse_last_projected_at(d.pop("lastProjectedAt"))

        def _parse_last_received_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_received_at_type_0 = isoparse(data)

                return last_received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_received_at = _parse_last_received_at(d.pop("lastReceivedAt"))

        def _parse_oldest_pending_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                oldest_pending_at_type_0 = isoparse(data)

                return oldest_pending_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        oldest_pending_at = _parse_oldest_pending_at(d.pop("oldestPendingAt"))

        pending = d.pop("pending")

        def _parse_undeclared(data: object) -> list[ActivityUndeclared] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                undeclared_type_0 = []
                _undeclared_type_0 = data
                for undeclared_type_0_item_data in _undeclared_type_0:
                    undeclared_type_0_item = ActivityUndeclared.from_dict(
                        undeclared_type_0_item_data
                    )

                    undeclared_type_0.append(undeclared_type_0_item)

                return undeclared_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityUndeclared] | None, data)

        undeclared = _parse_undeclared(d.pop("undeclared"))

        schema = d.pop("$schema", UNSET)

        _source = d.pop("source", UNSET)
        source: ActivityHealthSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ActivityHealthSource.from_dict(_source)

        _source_heartbeat_at = d.pop("sourceHeartbeatAt", UNSET)
        source_heartbeat_at: datetime.datetime | Unset
        if isinstance(_source_heartbeat_at, Unset):
            source_heartbeat_at = UNSET
        else:
            source_heartbeat_at = isoparse(_source_heartbeat_at)

        activity_health = cls(
            checked_at=checked_at,
            last_projected_at=last_projected_at,
            last_received_at=last_received_at,
            oldest_pending_at=oldest_pending_at,
            pending=pending,
            undeclared=undeclared,
            schema=schema,
            source=source,
            source_heartbeat_at=source_heartbeat_at,
        )

        return activity_health
