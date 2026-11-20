from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_dto import PlanDTO


T = TypeVar("T", bound="PlansOutputBody")


@_attrs_define
class PlansOutputBody:
    """
    Attributes:
        billing_enabled (bool):
        plans (list[PlanDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    billing_enabled: bool
    plans: list[PlanDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.plan_dto import PlanDTO

        billing_enabled = self.billing_enabled

        plans: list[dict[str, Any]] | None
        if isinstance(self.plans, list):
            plans = []
            for plans_type_0_item_data in self.plans:
                plans_type_0_item = plans_type_0_item_data.to_dict()
                plans.append(plans_type_0_item)

        else:
            plans = self.plans

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billingEnabled": billing_enabled,
                "plans": plans,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_dto import PlanDTO

        d = dict(src_dict)
        billing_enabled = d.pop("billingEnabled")

        def _parse_plans(data: object) -> list[PlanDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                plans_type_0 = []
                _plans_type_0 = data
                for plans_type_0_item_data in _plans_type_0:
                    plans_type_0_item = PlanDTO.from_dict(plans_type_0_item_data)

                    plans_type_0.append(plans_type_0_item)

                return plans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlanDTO] | None, data)

        plans = _parse_plans(d.pop("plans"))

        schema = d.pop("$schema", UNSET)

        plans_output_body = cls(
            billing_enabled=billing_enabled,
            plans=plans,
            schema=schema,
        )

        return plans_output_body
