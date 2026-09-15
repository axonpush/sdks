from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEnvironmentInputBody")


@_attrs_define
class UpdateEnvironmentInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        color (str | Unset):
        is_production (bool | Unset):
        name (str | Unset):
    """

    schema: str | Unset = UNSET
    color: str | Unset = UNSET
    is_production: bool | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        color = self.color

        is_production = self.is_production

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if color is not UNSET:
            field_dict["color"] = color
        if is_production is not UNSET:
            field_dict["isProduction"] = is_production
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        color = d.pop("color", UNSET)

        is_production = d.pop("isProduction", UNSET)

        name = d.pop("name", UNSET)

        update_environment_input_body = cls(
            schema=schema,
            color=color,
            is_production=is_production,
            name=name,
        )

        return update_environment_input_body
