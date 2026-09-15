from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetTrialInputBody")


@_attrs_define
class SetTrialInputBody:
    """
    Attributes:
        days (int): Trial length in days from now
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    days: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "days": days,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days")

        schema = d.pop("$schema", UNSET)

        set_trial_input_body = cls(
            days=days,
            schema=schema,
        )

        return set_trial_input_body
