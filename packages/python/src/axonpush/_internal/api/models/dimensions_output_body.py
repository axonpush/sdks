from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension_dto import DimensionDTO


T = TypeVar("T", bound="DimensionsOutputBody")


@_attrs_define
class DimensionsOutputBody:
    """
    Attributes:
        dimensions (list[DimensionDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    dimensions: list[DimensionDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_dto import DimensionDTO

        dimensions: list[dict[str, Any]] | None
        if isinstance(self.dimensions, list):
            dimensions = []
            for dimensions_type_0_item_data in self.dimensions:
                dimensions_type_0_item = dimensions_type_0_item_data.to_dict()
                dimensions.append(dimensions_type_0_item)

        else:
            dimensions = self.dimensions

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimensions": dimensions,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_dto import DimensionDTO

        d = dict(src_dict)

        def _parse_dimensions(data: object) -> list[DimensionDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dimensions_type_0 = []
                _dimensions_type_0 = data
                for dimensions_type_0_item_data in _dimensions_type_0:
                    dimensions_type_0_item = DimensionDTO.from_dict(dimensions_type_0_item_data)

                    dimensions_type_0.append(dimensions_type_0_item)

                return dimensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DimensionDTO] | None, data)

        dimensions = _parse_dimensions(d.pop("dimensions"))

        schema = d.pop("$schema", UNSET)

        dimensions_output_body = cls(
            dimensions=dimensions,
            schema=schema,
        )

        return dimensions_output_body
