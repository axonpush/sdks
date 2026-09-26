from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverviewBodyManagedLlmStruct")


@_attrs_define
class OverviewBodyManagedLlmStruct:
    """
    Attributes:
        cost_usd_this_month (float):
        tokens_this_month (int):
        traces_this_month (int):
    """

    cost_usd_this_month: float
    tokens_this_month: int
    traces_this_month: int

    def to_dict(self) -> dict[str, Any]:
        cost_usd_this_month = self.cost_usd_this_month

        tokens_this_month = self.tokens_this_month

        traces_this_month = self.traces_this_month

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costUsdThisMonth": cost_usd_this_month,
                "tokensThisMonth": tokens_this_month,
                "tracesThisMonth": traces_this_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_usd_this_month = d.pop("costUsdThisMonth")

        tokens_this_month = d.pop("tokensThisMonth")

        traces_this_month = d.pop("tracesThisMonth")

        overview_body_managed_llm_struct = cls(
            cost_usd_this_month=cost_usd_this_month,
            tokens_this_month=tokens_this_month,
            traces_this_month=traces_this_month,
        )

        return overview_body_managed_llm_struct
