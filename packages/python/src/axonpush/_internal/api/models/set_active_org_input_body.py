from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetActiveOrgInputBody")


@_attrs_define
class SetActiveOrgInputBody:
    """
    Attributes:
        org_id (str): Organization to make active
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    org_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "orgId": org_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = d.pop("orgId")

        schema = d.pop("$schema", UNSET)

        set_active_org_input_body = cls(
            org_id=org_id,
            schema=schema,
        )

        return set_active_org_input_body
