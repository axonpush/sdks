from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityEntityDefinition")


@_attrs_define
class ActivityEntityDefinition:
    """
    Attributes:
        fields (list[str] | None):
        label (str):
        type_ (str):
        terminal_states (list[str] | None | Unset):
    """

    fields: list[str] | None
    label: str
    type_: str
    terminal_states: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        fields: list[str] | None
        if isinstance(self.fields, list):
            fields = self.fields

        else:
            fields = self.fields

        label = self.label

        type_ = self.type_

        terminal_states: list[str] | None | Unset
        if isinstance(self.terminal_states, Unset):
            terminal_states = UNSET
        elif isinstance(self.terminal_states, list):
            terminal_states = self.terminal_states

        else:
            terminal_states = self.terminal_states

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
                "label": label,
                "type": type_,
            }
        )
        if terminal_states is not UNSET:
            field_dict["terminalStates"] = terminal_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fields(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = cast(list[str], data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        fields = _parse_fields(d.pop("fields"))

        label = d.pop("label")

        type_ = d.pop("type")

        def _parse_terminal_states(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                terminal_states_type_0 = cast(list[str], data)

                return terminal_states_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        terminal_states = _parse_terminal_states(d.pop("terminalStates", UNSET))

        activity_entity_definition = cls(
            fields=fields,
            label=label,
            type_=type_,
            terminal_states=terminal_states,
        )

        return activity_entity_definition
