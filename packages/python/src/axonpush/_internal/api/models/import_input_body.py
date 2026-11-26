from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportInputBody")


@_attrs_define
class ImportInputBody:
    """
    Attributes:
        csv (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    csv: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        csv = self.csv

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "csv": csv,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csv = d.pop("csv")

        schema = d.pop("$schema", UNSET)

        import_input_body = cls(
            csv=csv,
            schema=schema,
        )

        return import_input_body
