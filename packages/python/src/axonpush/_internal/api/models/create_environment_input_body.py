from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEnvironmentInputBody")


@_attrs_define
class CreateEnvironmentInputBody:
    """
    Attributes:
        name (str): Environment display name
        schema (str | Unset): A URL to the JSON Schema for this object.
        color (str | Unset):
        is_default (bool | Unset):
        is_production (bool | Unset):
        slug (str | Unset): URL-safe slug; derived from name when omitted
    """

    name: str
    schema: str | Unset = UNSET
    color: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_production: bool | Unset = UNSET
    slug: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        schema = self.schema

        color = self.color

        is_default = self.is_default

        is_production = self.is_production

        slug = self.slug

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if color is not UNSET:
            field_dict["color"] = color
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_production is not UNSET:
            field_dict["isProduction"] = is_production
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        schema = d.pop("$schema", UNSET)

        color = d.pop("color", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_production = d.pop("isProduction", UNSET)

        slug = d.pop("slug", UNSET)

        create_environment_input_body = cls(
            name=name,
            schema=schema,
            color=color,
            is_default=is_default,
            is_production=is_production,
            slug=slug,
        )

        return create_environment_input_body
