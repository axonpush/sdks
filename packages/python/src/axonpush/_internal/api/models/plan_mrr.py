from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanMrr")


@_attrs_define
class PlanMrr:
    """
    Attributes:
        count (int):
        mrr_usd (float):
        plan (str):
    """

    count: int
    mrr_usd: float
    plan: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        mrr_usd = self.mrr_usd

        plan = self.plan

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "mrrUsd": mrr_usd,
                "plan": plan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        mrr_usd = d.pop("mrrUsd")

        plan = d.pop("plan")

        plan_mrr = cls(
            count=count,
            mrr_usd=mrr_usd,
            plan=plan,
        )

        return plan_mrr
