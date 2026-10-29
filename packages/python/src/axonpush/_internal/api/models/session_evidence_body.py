from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_dto import EventDTO


T = TypeVar("T", bound="SessionEvidenceBody")


@_attrs_define
class SessionEvidenceBody:
    """
    Attributes:
        events (list[EventDTO] | None):
        has_more (bool):
        next_offset (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    events: list[EventDTO] | None
    has_more: bool
    next_offset: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_dto import EventDTO

        events: list[dict[str, Any]] | None
        if isinstance(self.events, list):
            events = []
            for events_type_0_item_data in self.events:
                events_type_0_item = events_type_0_item_data.to_dict()
                events.append(events_type_0_item)

        else:
            events = self.events

        has_more = self.has_more

        next_offset = self.next_offset

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "hasMore": has_more,
                "nextOffset": next_offset,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_dto import EventDTO

        d = dict(src_dict)

        def _parse_events(data: object) -> list[EventDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = []
                _events_type_0 = data
                for events_type_0_item_data in _events_type_0:
                    events_type_0_item = EventDTO.from_dict(events_type_0_item_data)

                    events_type_0.append(events_type_0_item)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventDTO] | None, data)

        events = _parse_events(d.pop("events"))

        has_more = d.pop("hasMore")

        next_offset = d.pop("nextOffset")

        schema = d.pop("$schema", UNSET)

        session_evidence_body = cls(
            events=events,
            has_more=has_more,
            next_offset=next_offset,
            schema=schema,
        )

        return session_evidence_body
