from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_catalog_event import ActivityCatalogEvent
    from ..models.activity_undeclared import ActivityUndeclared


T = TypeVar("T", bound="ActivityCatalog")


@_attrs_define
class ActivityCatalog:
    """
    Attributes:
        events (list[ActivityCatalogEvent] | None):
        from_ (datetime.datetime):
        undeclared (list[ActivityUndeclared] | None): Attribute keys sent but not declared, per event (identify drops
            appear as identify:<entity>)
        unmapped (int): Events no entity consumes
        window (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    events: list[ActivityCatalogEvent] | None
    from_: datetime.datetime
    undeclared: list[ActivityUndeclared] | None
    unmapped: int
    window: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_catalog_event import ActivityCatalogEvent
        from ..models.activity_undeclared import ActivityUndeclared

        events: list[dict[str, Any]] | None
        if isinstance(self.events, list):
            events = []
            for events_type_0_item_data in self.events:
                events_type_0_item = events_type_0_item_data.to_dict()
                events.append(events_type_0_item)

        else:
            events = self.events

        from_ = self.from_.isoformat()

        undeclared: list[dict[str, Any]] | None
        if isinstance(self.undeclared, list):
            undeclared = []
            for undeclared_type_0_item_data in self.undeclared:
                undeclared_type_0_item = undeclared_type_0_item_data.to_dict()
                undeclared.append(undeclared_type_0_item)

        else:
            undeclared = self.undeclared

        unmapped = self.unmapped

        window = self.window

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "from": from_,
                "undeclared": undeclared,
                "unmapped": unmapped,
                "window": window,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_catalog_event import ActivityCatalogEvent
        from ..models.activity_undeclared import ActivityUndeclared

        d = dict(src_dict)

        def _parse_events(data: object) -> list[ActivityCatalogEvent] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = []
                _events_type_0 = data
                for events_type_0_item_data in _events_type_0:
                    events_type_0_item = ActivityCatalogEvent.from_dict(events_type_0_item_data)

                    events_type_0.append(events_type_0_item)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityCatalogEvent] | None, data)

        events = _parse_events(d.pop("events"))

        from_ = isoparse(d.pop("from"))

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

        unmapped = d.pop("unmapped")

        window = d.pop("window")

        schema = d.pop("$schema", UNSET)

        activity_catalog = cls(
            events=events,
            from_=from_,
            undeclared=undeclared,
            unmapped=unmapped,
            window=window,
            schema=schema,
        )

        return activity_catalog
