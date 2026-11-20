from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterSourceInputBody")


@_attrs_define
class RegisterSourceInputBody:
    """
    Attributes:
        publisher (str): key:<key ID> or user:<user ID>
        source (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    publisher: str
    source: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        publisher = self.publisher

        source = self.source

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publisher": publisher,
                "source": source,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        publisher = d.pop("publisher")

        source = d.pop("source")

        schema = d.pop("$schema", UNSET)

        register_source_input_body = cls(
            publisher=publisher,
            source=source,
            schema=schema,
        )

        return register_source_input_body
