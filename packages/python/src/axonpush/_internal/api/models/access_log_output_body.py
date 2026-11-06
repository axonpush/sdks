from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_log_output_body_items_type_0_item import AccessLogOutputBodyItemsType0Item


T = TypeVar("T", bound="AccessLogOutputBody")


@_attrs_define
class AccessLogOutputBody:
    """
    Attributes:
        items (list[AccessLogOutputBodyItemsType0Item] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_cursor (str | Unset):
    """

    items: list[AccessLogOutputBodyItemsType0Item] | None
    schema: str | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.access_log_output_body_items_type_0_item import (
            AccessLogOutputBodyItemsType0Item,
        )

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        schema = self.schema

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_log_output_body_items_type_0_item import (
            AccessLogOutputBodyItemsType0Item,
        )

        d = dict(src_dict)

        def _parse_items(data: object) -> list[AccessLogOutputBodyItemsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = AccessLogOutputBodyItemsType0Item.from_dict(
                        items_type_0_item_data
                    )

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccessLogOutputBodyItemsType0Item] | None, data)

        items = _parse_items(d.pop("items"))

        schema = d.pop("$schema", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        access_log_output_body = cls(
            items=items,
            schema=schema,
            next_cursor=next_cursor,
        )

        return access_log_output_body
