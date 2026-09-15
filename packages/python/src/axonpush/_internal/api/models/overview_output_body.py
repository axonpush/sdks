from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverviewOutputBody")


@_attrs_define
class OverviewOutputBody:
    """
    Attributes:
        organizations (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    organizations: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        organizations = self.organizations

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "organizations": organizations,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organizations = d.pop("organizations")

        schema = d.pop("$schema", UNSET)

        overview_output_body = cls(
            organizations=organizations,
            schema=schema,
        )

        return overview_output_body
