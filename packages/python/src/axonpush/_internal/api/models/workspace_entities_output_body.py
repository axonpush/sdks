from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_entity import ActivityEntity


T = TypeVar("T", bound="WorkspaceEntitiesOutputBody")


@_attrs_define
class WorkspaceEntitiesOutputBody:
    """
    Attributes:
        entities (list[ActivityEntity] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        dropped (list[str] | None | Unset): Preview only: undeclared attribute keys that were dropped
        next_cursor (str | Unset):
    """

    entities: list[ActivityEntity] | None
    schema: str | Unset = UNSET
    dropped: list[str] | None | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_entity import ActivityEntity

        entities: list[dict[str, Any]] | None
        if isinstance(self.entities, list):
            entities = []
            for entities_type_0_item_data in self.entities:
                entities_type_0_item = entities_type_0_item_data.to_dict()
                entities.append(entities_type_0_item)

        else:
            entities = self.entities

        schema = self.schema

        dropped: list[str] | None | Unset
        if isinstance(self.dropped, Unset):
            dropped = UNSET
        elif isinstance(self.dropped, list):
            dropped = self.dropped

        else:
            dropped = self.dropped

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entities": entities,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if dropped is not UNSET:
            field_dict["dropped"] = dropped
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_entity import ActivityEntity

        d = dict(src_dict)

        def _parse_entities(data: object) -> list[ActivityEntity] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entities_type_0 = []
                _entities_type_0 = data
                for entities_type_0_item_data in _entities_type_0:
                    entities_type_0_item = ActivityEntity.from_dict(entities_type_0_item_data)

                    entities_type_0.append(entities_type_0_item)

                return entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityEntity] | None, data)

        entities = _parse_entities(d.pop("entities"))

        schema = d.pop("$schema", UNSET)

        def _parse_dropped(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dropped_type_0 = cast(list[str], data)

                return dropped_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dropped = _parse_dropped(d.pop("dropped", UNSET))

        next_cursor = d.pop("nextCursor", UNSET)

        workspace_entities_output_body = cls(
            entities=entities,
            schema=schema,
            dropped=dropped,
            next_cursor=next_cursor,
        )

        return workspace_entities_output_body
