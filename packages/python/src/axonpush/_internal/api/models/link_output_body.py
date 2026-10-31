from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkOutputBody")


@_attrs_define
class LinkOutputBody:
    """
    Attributes:
        url (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    url: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        schema = d.pop("$schema", UNSET)

        link_output_body = cls(
            url=url,
            schema=schema,
        )

        return link_output_body
