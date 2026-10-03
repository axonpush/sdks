from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_catalog_attribute import ActivityCatalogAttribute


T = TypeVar("T", bound="ActivityCatalogEvent")


@_attrs_define
class ActivityCatalogEvent:
    """
    Attributes:
        attributes (list[ActivityCatalogAttribute] | None):
        consumers (list[str] | None): Entity types whose rules match this event; empty means unmapped
        count (int):
        event (str):
        last_seen_at (datetime.datetime):
        refs (list[str] | None): Entity types referenced in refs
    """

    attributes: list[ActivityCatalogAttribute] | None
    consumers: list[str] | None
    count: int
    event: str
    last_seen_at: datetime.datetime
    refs: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_catalog_attribute import ActivityCatalogAttribute

        attributes: list[dict[str, Any]] | None
        if isinstance(self.attributes, list):
            attributes = []
            for attributes_type_0_item_data in self.attributes:
                attributes_type_0_item = attributes_type_0_item_data.to_dict()
                attributes.append(attributes_type_0_item)

        else:
            attributes = self.attributes

        consumers: list[str] | None
        if isinstance(self.consumers, list):
            consumers = self.consumers

        else:
            consumers = self.consumers

        count = self.count

        event = self.event

        last_seen_at = self.last_seen_at.isoformat()

        refs: list[str] | None
        if isinstance(self.refs, list):
            refs = self.refs

        else:
            refs = self.refs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
                "consumers": consumers,
                "count": count,
                "event": event,
                "lastSeenAt": last_seen_at,
                "refs": refs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_catalog_attribute import ActivityCatalogAttribute

        d = dict(src_dict)

        def _parse_attributes(data: object) -> list[ActivityCatalogAttribute] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attributes_type_0 = []
                _attributes_type_0 = data
                for attributes_type_0_item_data in _attributes_type_0:
                    attributes_type_0_item = ActivityCatalogAttribute.from_dict(
                        attributes_type_0_item_data
                    )

                    attributes_type_0.append(attributes_type_0_item)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityCatalogAttribute] | None, data)

        attributes = _parse_attributes(d.pop("attributes"))

        def _parse_consumers(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                consumers_type_0 = cast(list[str], data)

                return consumers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        consumers = _parse_consumers(d.pop("consumers"))

        count = d.pop("count")

        event = d.pop("event")

        last_seen_at = isoparse(d.pop("lastSeenAt"))

        def _parse_refs(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refs_type_0 = cast(list[str], data)

                return refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        refs = _parse_refs(d.pop("refs"))

        activity_catalog_event = cls(
            attributes=attributes,
            consumers=consumers,
            count=count,
            event=event,
            last_seen_at=last_seen_at,
            refs=refs,
        )

        return activity_catalog_event
