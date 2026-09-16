from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostBudget")


@_attrs_define
class CostBudget:
    """
    Attributes:
        budget_id (str):
        created_at (str):
        daily_limit_usd (float):
        enabled (bool):
        monthly_limit_usd (float):
        name (str):
        updated_at (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset):
    """

    budget_id: str
    created_at: str
    daily_limit_usd: float
    enabled: bool
    monthly_limit_usd: float
    name: str
    updated_at: str
    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        budget_id = self.budget_id

        created_at = self.created_at

        daily_limit_usd = self.daily_limit_usd

        enabled = self.enabled

        monthly_limit_usd = self.monthly_limit_usd

        name = self.name

        updated_at = self.updated_at

        schema = self.schema

        app_id = self.app_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "budgetId": budget_id,
                "createdAt": created_at,
                "dailyLimitUsd": daily_limit_usd,
                "enabled": enabled,
                "monthlyLimitUsd": monthly_limit_usd,
                "name": name,
                "updatedAt": updated_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if app_id is not UNSET:
            field_dict["appId"] = app_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_id = d.pop("budgetId")

        created_at = d.pop("createdAt")

        daily_limit_usd = d.pop("dailyLimitUsd")

        enabled = d.pop("enabled")

        monthly_limit_usd = d.pop("monthlyLimitUsd")

        name = d.pop("name")

        updated_at = d.pop("updatedAt")

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        cost_budget = cls(
            budget_id=budget_id,
            created_at=created_at,
            daily_limit_usd=daily_limit_usd,
            enabled=enabled,
            monthly_limit_usd=monthly_limit_usd,
            name=name,
            updated_at=updated_at,
            schema=schema,
            app_id=app_id,
        )

        return cost_budget
