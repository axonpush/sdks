from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityReceipt")


@_attrs_define
class ActivityReceipt:
    """
    Attributes:
        projected_at (datetime.datetime | None):
        received_at (datetime.datetime):
        source_event_id (str):
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    projected_at: datetime.datetime | None
    received_at: datetime.datetime
    source_event_id: str
    status: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        projected_at: None | str
        if isinstance(self.projected_at, datetime.datetime):
            projected_at = self.projected_at.isoformat()
        else:
            projected_at = self.projected_at

        received_at = self.received_at.isoformat()

        source_event_id = self.source_event_id

        status = self.status

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "projectedAt": projected_at,
                "receivedAt": received_at,
                "sourceEventId": source_event_id,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_projected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                projected_at_type_0 = isoparse(data)

                return projected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        projected_at = _parse_projected_at(d.pop("projectedAt"))

        received_at = isoparse(d.pop("receivedAt"))

        source_event_id = d.pop("sourceEventId")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        activity_receipt = cls(
            projected_at=projected_at,
            received_at=received_at,
            source_event_id=source_event_id,
            status=status,
            schema=schema,
        )

        return activity_receipt
