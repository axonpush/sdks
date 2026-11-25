from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="SourceInputBody")


@_attrs_define
class SourceInputBody:
    """
    Attributes:
        source (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    source: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        schema = d.pop("$schema", UNSET)

        source_input_body = cls(
            source=source,
            schema=schema,
        )

        return source_input_body
