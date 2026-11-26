from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivateDraftInputBody")


@_attrs_define
class ActivateDraftInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        version (int | Unset): When set, activate only if the draft is still at this version
    """

    schema: str | Unset = UNSET
    version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        version = d.pop("version", UNSET)

        activate_draft_input_body = cls(
            schema=schema,
            version=version,
        )

        return activate_draft_input_body
