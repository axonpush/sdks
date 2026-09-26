from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension_value_dto import DimensionValueDTO


T = TypeVar("T", bound="DimensionValuesOutputBody")


@_attrs_define
class DimensionValuesOutputBody:
    """
    Attributes:
        key (str):
        values (list[DimensionValueDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    key: str
    values: list[DimensionValueDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_value_dto import DimensionValueDTO

        key = self.key

        values: list[dict[str, Any]] | None
        if isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "values": values,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_value_dto import DimensionValueDTO

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_values(data: object) -> list[DimensionValueDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = DimensionValueDTO.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DimensionValueDTO] | None, data)

        values = _parse_values(d.pop("values"))

        schema = d.pop("$schema", UNSET)

        dimension_values_output_body = cls(
            key=key,
            values=values,
            schema=schema,
        )

        return dimension_values_output_body
