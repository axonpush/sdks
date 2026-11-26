from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivateDraftOutputBody")


@_attrs_define
class ActivateDraftOutputBody:
    """
    Attributes:
        revision (str):
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    revision: str
    status: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        revision = self.revision

        status = self.status

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "revision": revision,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision = d.pop("revision")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        activate_draft_output_body = cls(
            revision=revision,
            status=status,
            schema=schema,
        )

        return activate_draft_output_body
