from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_event_rule import ActivityEventRule


T = TypeVar("T", bound="ActivityEntityDefinition")


@_attrs_define
class ActivityEntityDefinition:
    """
    Attributes:
        type_ (str):
        description (str | Unset):
        events (list[ActivityEventRule] | None | Unset):
        fields (list[str] | None | Unset): Attribute keys stored on this entity
        label (str | Unset):
        profile (list[str] | None | Unset): Attribute keys settable through identify
        rollup (list[str] | None | Unset): Linked entity types whose open members are counted on each row, with the
            latest explicit wait
        stale_after_seconds (int | Unset): An open state older than this, or than the entity's expected_duration value,
            reads as stale rather than failed; a late terminal event still lands
        stale_states (list[str] | None | Unset): States that can go stale; default every non-terminal state
        terminal (list[str] | None | Unset): State values that only a newer revision of the same source record may
            reopen
    """

    type_: str
    description: str | Unset = UNSET
    events: list[ActivityEventRule] | None | Unset = UNSET
    fields: list[str] | None | Unset = UNSET
    label: str | Unset = UNSET
    profile: list[str] | None | Unset = UNSET
    rollup: list[str] | None | Unset = UNSET
    stale_after_seconds: int | Unset = UNSET
    stale_states: list[str] | None | Unset = UNSET
    terminal: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_event_rule import ActivityEventRule

        type_ = self.type_

        description = self.description

        events: list[dict[str, Any]] | None | Unset
        if isinstance(self.events, Unset):
            events = UNSET
        elif isinstance(self.events, list):
            events = []
            for events_type_0_item_data in self.events:
                events_type_0_item = events_type_0_item_data.to_dict()
                events.append(events_type_0_item)

        else:
            events = self.events

        fields: list[str] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = self.fields

        else:
            fields = self.fields

        label = self.label

        profile: list[str] | None | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, list):
            profile = self.profile

        else:
            profile = self.profile

        rollup: list[str] | None | Unset
        if isinstance(self.rollup, Unset):
            rollup = UNSET
        elif isinstance(self.rollup, list):
            rollup = self.rollup

        else:
            rollup = self.rollup

        stale_after_seconds = self.stale_after_seconds

        stale_states: list[str] | None | Unset
        if isinstance(self.stale_states, Unset):
            stale_states = UNSET
        elif isinstance(self.stale_states, list):
            stale_states = self.stale_states

        else:
            stale_states = self.stale_states

        terminal: list[str] | None | Unset
        if isinstance(self.terminal, Unset):
            terminal = UNSET
        elif isinstance(self.terminal, list):
            terminal = self.terminal

        else:
            terminal = self.terminal

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events
        if fields is not UNSET:
            field_dict["fields"] = fields
        if label is not UNSET:
            field_dict["label"] = label
        if profile is not UNSET:
            field_dict["profile"] = profile
        if rollup is not UNSET:
            field_dict["rollup"] = rollup
        if stale_after_seconds is not UNSET:
            field_dict["staleAfterSeconds"] = stale_after_seconds
        if stale_states is not UNSET:
            field_dict["staleStates"] = stale_states
        if terminal is not UNSET:
            field_dict["terminal"] = terminal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_event_rule import ActivityEventRule

        d = dict(src_dict)
        type_ = d.pop("type")

        description = d.pop("description", UNSET)

        def _parse_events(data: object) -> list[ActivityEventRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = []
                _events_type_0 = data
                for events_type_0_item_data in _events_type_0:
                    events_type_0_item = ActivityEventRule.from_dict(events_type_0_item_data)

                    events_type_0.append(events_type_0_item)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityEventRule] | None | Unset, data)

        events = _parse_events(d.pop("events", UNSET))

        def _parse_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = cast(list[str], data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        label = d.pop("label", UNSET)

        def _parse_profile(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                profile_type_0 = cast(list[str], data)

                return profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        def _parse_rollup(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rollup_type_0 = cast(list[str], data)

                return rollup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        rollup = _parse_rollup(d.pop("rollup", UNSET))

        stale_after_seconds = d.pop("staleAfterSeconds", UNSET)

        def _parse_stale_states(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stale_states_type_0 = cast(list[str], data)

                return stale_states_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        stale_states = _parse_stale_states(d.pop("staleStates", UNSET))

        def _parse_terminal(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                terminal_type_0 = cast(list[str], data)

                return terminal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        terminal = _parse_terminal(d.pop("terminal", UNSET))

        activity_entity_definition = cls(
            type_=type_,
            description=description,
            events=events,
            fields=fields,
            label=label,
            profile=profile,
            rollup=rollup,
            stale_after_seconds=stale_after_seconds,
            stale_states=stale_states,
            terminal=terminal,
        )

        return activity_entity_definition
