from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_row_dto import BreakdownRowDTO


T = TypeVar("T", bound="BreakdownOutputBody")


@_attrs_define
class BreakdownOutputBody:
    """
    Attributes:
        dimension (str):
        rows (list[BreakdownRowDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    dimension: str
    rows: list[BreakdownRowDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.breakdown_row_dto import BreakdownRowDTO

        dimension = self.dimension

        rows: list[dict[str, Any]] | None
        if isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)

        else:
            rows = self.rows

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
                "rows": rows,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breakdown_row_dto import BreakdownRowDTO

        d = dict(src_dict)
        dimension = d.pop("dimension")

        def _parse_rows(data: object) -> list[BreakdownRowDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in _rows_type_0:
                    rows_type_0_item = BreakdownRowDTO.from_dict(rows_type_0_item_data)

                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BreakdownRowDTO] | None, data)

        rows = _parse_rows(d.pop("rows"))

        schema = d.pop("$schema", UNSET)

        breakdown_output_body = cls(
            dimension=dimension,
            rows=rows,
            schema=schema,
        )

        return breakdown_output_body
