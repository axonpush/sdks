from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportOutputBody")


@_attrs_define
class ImportOutputBody:
    """
    Attributes:
        duplicates (int):
        imported (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    duplicates: int
    imported: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        duplicates = self.duplicates

        imported = self.imported

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duplicates": duplicates,
                "imported": imported,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duplicates = d.pop("duplicates")

        imported = d.pop("imported")

        schema = d.pop("$schema", UNSET)

        import_output_body = cls(
            duplicates=duplicates,
            imported=imported,
            schema=schema,
        )

        return import_output_body
