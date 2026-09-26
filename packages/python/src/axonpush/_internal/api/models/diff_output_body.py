from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diff_attribute_dto import DiffAttributeDTO


T = TypeVar("T", bound="DiffOutputBody")


@_attrs_define
class DiffOutputBody:
    """
    Attributes:
        attributes (list[DiffAttributeDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    attributes: list[DiffAttributeDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.diff_attribute_dto import DiffAttributeDTO

        attributes: list[dict[str, Any]] | None
        if isinstance(self.attributes, list):
            attributes = []
            for attributes_type_0_item_data in self.attributes:
                attributes_type_0_item = attributes_type_0_item_data.to_dict()
                attributes.append(attributes_type_0_item)

        else:
            attributes = self.attributes

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diff_attribute_dto import DiffAttributeDTO

        d = dict(src_dict)

        def _parse_attributes(data: object) -> list[DiffAttributeDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attributes_type_0 = []
                _attributes_type_0 = data
                for attributes_type_0_item_data in _attributes_type_0:
                    attributes_type_0_item = DiffAttributeDTO.from_dict(attributes_type_0_item_data)

                    attributes_type_0.append(attributes_type_0_item)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DiffAttributeDTO] | None, data)

        attributes = _parse_attributes(d.pop("attributes"))

        schema = d.pop("$schema", UNSET)

        diff_output_body = cls(
            attributes=attributes,
            schema=schema,
        )

        return diff_output_body
