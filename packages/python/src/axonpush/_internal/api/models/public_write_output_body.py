from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicWriteOutputBody")


@_attrs_define
class PublicWriteOutputBody:
    """
    Attributes:
        id (str):
        state (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    id: str
    state: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        state = self.state

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "state": state,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        state = d.pop("state")

        schema = d.pop("$schema", UNSET)

        public_write_output_body = cls(
            id=id,
            state=state,
            schema=schema,
        )

        return public_write_output_body
