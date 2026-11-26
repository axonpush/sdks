from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseHoldInputBody")


@_attrs_define
class ReleaseHoldInputBody:
    """
    Attributes:
        reason (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    reason: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reason": reason,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        schema = d.pop("$schema", UNSET)

        release_hold_input_body = cls(
            reason=reason,
            schema=schema,
        )

        return release_hold_input_body
