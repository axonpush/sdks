from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProfileInputBody")


@_attrs_define
class UpdateProfileInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        first_name (str | Unset):
        last_name (str | Unset):
    """

    schema: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        update_profile_input_body = cls(
            schema=schema,
            first_name=first_name,
            last_name=last_name,
        )

        return update_profile_input_body
