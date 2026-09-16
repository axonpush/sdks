from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInputBody")


@_attrs_define
class CreateInputBody:
    """
    Attributes:
        name (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset): scope to an app; empty means org-wide
        daily_limit_usd (float | Unset): per-UTC-day ceiling in USD; 0 disables the daily cap
        monthly_limit_usd (float | Unset): per-UTC-month ceiling in USD; 0 disables the monthly cap
    """

    name: str
    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET
    daily_limit_usd: float | Unset = UNSET
    monthly_limit_usd: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        schema = self.schema

        app_id = self.app_id

        daily_limit_usd = self.daily_limit_usd

        monthly_limit_usd = self.monthly_limit_usd

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if daily_limit_usd is not UNSET:
            field_dict["dailyLimitUsd"] = daily_limit_usd
        if monthly_limit_usd is not UNSET:
            field_dict["monthlyLimitUsd"] = monthly_limit_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        daily_limit_usd = d.pop("dailyLimitUsd", UNSET)

        monthly_limit_usd = d.pop("monthlyLimitUsd", UNSET)

        create_input_body = cls(
            name=name,
            schema=schema,
            app_id=app_id,
            daily_limit_usd=daily_limit_usd,
            monthly_limit_usd=monthly_limit_usd,
        )

        return create_input_body
