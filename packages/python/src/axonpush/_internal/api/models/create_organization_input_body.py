from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOrganizationInputBody")


@_attrs_define
class CreateOrganizationInputBody:
    """
    Attributes:
        name (str):
        slug (str): URL name: lowercase letters, digits and single hyphens
        schema (str | Unset): A URL to the JSON Schema for this object.
        description (str | Unset):
    """

    name: str
    slug: str
    schema: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        schema = self.schema

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        schema = d.pop("$schema", UNSET)

        description = d.pop("description", UNSET)

        create_organization_input_body = cls(
            name=name,
            slug=slug,
            schema=schema,
            description=description,
        )

        return create_organization_input_body
