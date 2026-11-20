from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffInputBody1")


@_attrs_define
class DiffInputBody1:
    """
    Attributes:
        against (str):
        source (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    against: str
    source: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        against = self.against

        source = self.source

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "against": against,
                "source": source,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        against = d.pop("against")

        source = d.pop("source")

        schema = d.pop("$schema", UNSET)

        diff_input_body_1 = cls(
            against=against,
            source=source,
            schema=schema,
        )

        return diff_input_body_1
