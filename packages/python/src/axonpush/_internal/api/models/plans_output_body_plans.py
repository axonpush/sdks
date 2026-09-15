from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_limits import PlanLimits


T = TypeVar("T", bound="PlansOutputBodyPlans")


@_attrs_define
class PlansOutputBodyPlans:
    """ """

    additional_properties: dict[str, PlanLimits] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plan_limits import PlanLimits

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_limits import PlanLimits

        d = dict(src_dict)
        plans_output_body_plans = cls()

        from ..models.plan_features import PlanFeatures
        from ..models.plan_limits_lemonsqueezy_variants import PlanLimitsLemonsqueezyVariants

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PlanLimits.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        plans_output_body_plans.additional_properties = additional_properties
        return plans_output_body_plans

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PlanLimits:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: PlanLimits) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
