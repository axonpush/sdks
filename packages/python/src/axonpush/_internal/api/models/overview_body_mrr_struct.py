from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_mrr import PlanMrr


T = TypeVar("T", bound="OverviewBodyMrrStruct")


@_attrs_define
class OverviewBodyMrrStruct:
    """
    Attributes:
        by_plan (list[PlanMrr] | None):
        estimate_usd (float):
        paying_orgs (int):
    """

    by_plan: list[PlanMrr] | None
    estimate_usd: float
    paying_orgs: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.plan_mrr import PlanMrr

        by_plan: list[dict[str, Any]] | None
        if isinstance(self.by_plan, list):
            by_plan = []
            for by_plan_type_0_item_data in self.by_plan:
                by_plan_type_0_item = by_plan_type_0_item_data.to_dict()
                by_plan.append(by_plan_type_0_item)

        else:
            by_plan = self.by_plan

        estimate_usd = self.estimate_usd

        paying_orgs = self.paying_orgs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "byPlan": by_plan,
                "estimateUsd": estimate_usd,
                "payingOrgs": paying_orgs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_mrr import PlanMrr

        d = dict(src_dict)

        def _parse_by_plan(data: object) -> list[PlanMrr] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                by_plan_type_0 = []
                _by_plan_type_0 = data
                for by_plan_type_0_item_data in _by_plan_type_0:
                    by_plan_type_0_item = PlanMrr.from_dict(by_plan_type_0_item_data)

                    by_plan_type_0.append(by_plan_type_0_item)

                return by_plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlanMrr] | None, data)

        by_plan = _parse_by_plan(d.pop("byPlan"))

        estimate_usd = d.pop("estimateUsd")

        paying_orgs = d.pop("payingOrgs")

        overview_body_mrr_struct = cls(
            by_plan=by_plan,
            estimate_usd=estimate_usd,
            paying_orgs=paying_orgs,
        )

        return overview_body_mrr_struct
