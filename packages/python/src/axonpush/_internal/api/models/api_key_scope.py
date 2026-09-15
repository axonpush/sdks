from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyScope")


@_attrs_define
class ApiKeyScope:
    """
    Attributes:
        category (str):
        description (str):
        scope (str):
    """

    category: str
    description: str
    scope: str

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        scope = self.scope

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category": category,
                "description": description,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        description = d.pop("description")

        scope = d.pop("scope")

        api_key_scope = cls(
            category=category,
            description=description,
            scope=scope,
        )

        return api_key_scope
