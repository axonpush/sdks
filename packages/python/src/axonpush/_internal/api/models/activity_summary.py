from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_state_count import ActivityStateCount


T = TypeVar("T", bound="ActivitySummary")


@_attrs_define
class ActivitySummary:
    """
    Attributes:
        as_of (datetime.datetime):
        counts (list[ActivityStateCount] | None):
        window_minutes (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    as_of: datetime.datetime
    counts: list[ActivityStateCount] | None
    window_minutes: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_state_count import ActivityStateCount

        as_of = self.as_of.isoformat()

        counts: list[dict[str, Any]] | None
        if isinstance(self.counts, list):
            counts = []
            for counts_type_0_item_data in self.counts:
                counts_type_0_item = counts_type_0_item_data.to_dict()
                counts.append(counts_type_0_item)

        else:
            counts = self.counts

        window_minutes = self.window_minutes

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asOf": as_of,
                "counts": counts,
                "windowMinutes": window_minutes,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_state_count import ActivityStateCount

        d = dict(src_dict)
        as_of = isoparse(d.pop("asOf"))

        def _parse_counts(data: object) -> list[ActivityStateCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                counts_type_0 = []
                _counts_type_0 = data
                for counts_type_0_item_data in _counts_type_0:
                    counts_type_0_item = ActivityStateCount.from_dict(counts_type_0_item_data)

                    counts_type_0.append(counts_type_0_item)

                return counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityStateCount] | None, data)

        counts = _parse_counts(d.pop("counts"))

        window_minutes = d.pop("windowMinutes")

        schema = d.pop("$schema", UNSET)

        activity_summary = cls(
            as_of=as_of,
            counts=counts,
            window_minutes=window_minutes,
            schema=schema,
        )

        return activity_summary
