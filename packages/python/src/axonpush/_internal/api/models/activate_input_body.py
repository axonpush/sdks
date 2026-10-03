from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivateInputBody")


@_attrs_define
class ActivateInputBody:
    """
    Attributes:
        generation (int):
        revision (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    generation: int
    revision: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        generation = self.generation

        revision = self.revision

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "generation": generation,
                "revision": revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        generation = d.pop("generation")

        revision = d.pop("revision")

        schema = d.pop("$schema", UNSET)

        activate_input_body = cls(
            generation=generation,
            revision=revision,
            schema=schema,
        )

        return activate_input_body
