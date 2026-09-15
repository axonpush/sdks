from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plans_output_body_plans import PlansOutputBodyPlans


T = TypeVar("T", bound="PlansOutputBody")


@_attrs_define
class PlansOutputBody:
    """
    Attributes:
        plans (PlansOutputBodyPlans):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    plans: PlansOutputBodyPlans
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.plans_output_body_plans import PlansOutputBodyPlans

        plans = self.plans.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "plans": plans,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plans_output_body_plans import PlansOutputBodyPlans

        d = dict(src_dict)
        plans = PlansOutputBodyPlans.from_dict(d.pop("plans"))

        schema = d.pop("$schema", UNSET)

        plans_output_body = cls(
            plans=plans,
            schema=schema,
        )

        return plans_output_body
