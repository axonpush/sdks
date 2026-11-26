from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetPlanInputBody")


@_attrs_define
class SetPlanInputBody:
    """
    Attributes:
        plan (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    plan: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "plan": plan,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan = d.pop("plan")

        schema = d.pop("$schema", UNSET)

        set_plan_input_body = cls(
            plan=plan,
            schema=schema,
        )

        return set_plan_input_body
