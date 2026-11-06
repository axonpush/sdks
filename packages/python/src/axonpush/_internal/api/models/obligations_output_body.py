from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_obligation import ComplianceObligation


T = TypeVar("T", bound="ObligationsOutputBody")


@_attrs_define
class ObligationsOutputBody:
    """
    Attributes:
        catalogue_version (str):
        items (list[ComplianceObligation] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    catalogue_version: str
    items: list[ComplianceObligation] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_obligation import ComplianceObligation

        catalogue_version = self.catalogue_version

        items: list[dict[str, Any]] | None
        if isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "catalogueVersion": catalogue_version,
                "items": items,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_obligation import ComplianceObligation

        d = dict(src_dict)
        catalogue_version = d.pop("catalogueVersion")

        def _parse_items(data: object) -> list[ComplianceObligation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = ComplianceObligation.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceObligation] | None, data)

        items = _parse_items(d.pop("items"))

        schema = d.pop("$schema", UNSET)

        obligations_output_body = cls(
            catalogue_version=catalogue_version,
            items=items,
            schema=schema,
        )

        return obligations_output_body
