from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_reference import ComplianceReference
    from ..models.compliance_reference_defaults import ComplianceReferenceDefaults


T = TypeVar("T", bound="ReferenceOutputBody")


@_attrs_define
class ReferenceOutputBody:
    """
    Attributes:
        defaults (ComplianceReferenceDefaults):
        items (list[ComplianceReference] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_cursor (str | Unset):
        search_window (str | Unset):
    """

    defaults: ComplianceReferenceDefaults
    items: list[ComplianceReference] | None
    schema: str | Unset = UNSET
    next_cursor: str | Unset = UNSET
    search_window: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_reference import ComplianceReference
        from ..models.compliance_reference_defaults import ComplianceReferenceDefaults

        defaults = self.defaults.to_dict()

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

        search_window = self.search_window

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "defaults": defaults,
                "items": items,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if search_window is not UNSET:
            field_dict["searchWindow"] = search_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_reference import ComplianceReference
        from ..models.compliance_reference_defaults import ComplianceReferenceDefaults

        d = dict(src_dict)
        defaults = ComplianceReferenceDefaults.from_dict(d.pop("defaults"))

        def _parse_items(data: object) -> list[ComplianceReference] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = ComplianceReference.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceReference] | None, data)

        items = _parse_items(d.pop("items"))

        schema = d.pop("$schema", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        search_window = d.pop("searchWindow", UNSET)

        reference_output_body = cls(
            defaults=defaults,
            items=items,
            schema=schema,
            next_cursor=next_cursor,
            search_window=search_window,
        )

        return reference_output_body
