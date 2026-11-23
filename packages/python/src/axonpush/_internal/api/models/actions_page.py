from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_record import ActionRecord
    from ..models.actions_page_available import ActionsPageAvailable


T = TypeVar("T", bound="ActionsPage")


@_attrs_define
class ActionsPage:
    """
    Attributes:
        actions (list[ActionRecord] | None):
        available (ActionsPageAvailable):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_cursor (str | Unset):
    """

    actions: list[ActionRecord] | None
    available: ActionsPageAvailable
    schema: str | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_record import ActionRecord
        from ..models.actions_page_available import ActionsPageAvailable

        actions: list[dict[str, Any]] | None
        if isinstance(self.actions, list):
            actions = []
            for actions_type_0_item_data in self.actions:
                actions_type_0_item = actions_type_0_item_data.to_dict()
                actions.append(actions_type_0_item)

        else:
            actions = self.actions

        available = self.available.to_dict()

        schema = self.schema

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actions": actions,
                "available": available,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_record import ActionRecord
        from ..models.actions_page_available import ActionsPageAvailable

        d = dict(src_dict)

        def _parse_actions(data: object) -> list[ActionRecord] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_0 = []
                _actions_type_0 = data
                for actions_type_0_item_data in _actions_type_0:
                    actions_type_0_item = ActionRecord.from_dict(
                        actions_type_0_item_data
                    )

                    actions_type_0.append(actions_type_0_item)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActionRecord] | None, data)

        actions = _parse_actions(d.pop("actions"))

        available = ActionsPageAvailable.from_dict(d.pop("available"))

        schema = d.pop("$schema", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        actions_page = cls(
            actions=actions,
            available=available,
            schema=schema,
            next_cursor=next_cursor,
        )

        return actions_page
