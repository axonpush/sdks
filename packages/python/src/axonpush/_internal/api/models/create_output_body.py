from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOutputBody")


@_attrs_define
class CreateOutputBody:
    """
    Attributes:
        id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        schema = d.pop("$schema", UNSET)

        create_output_body = cls(
            id=id,
            schema=schema,
        )

        return create_output_body
