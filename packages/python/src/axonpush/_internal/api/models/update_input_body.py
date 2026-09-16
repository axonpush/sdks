from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateInputBody")


@_attrs_define
class UpdateInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset):
        daily_limit_usd (float | Unset):
        enabled (bool | Unset):
        monthly_limit_usd (float | Unset):
        name (str | Unset):
    """

    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET
    daily_limit_usd: float | Unset = UNSET
    enabled: bool | Unset = UNSET
    monthly_limit_usd: float | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        app_id = self.app_id

        daily_limit_usd = self.daily_limit_usd

        enabled = self.enabled

        monthly_limit_usd = self.monthly_limit_usd

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if daily_limit_usd is not UNSET:
            field_dict["dailyLimitUsd"] = daily_limit_usd
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if monthly_limit_usd is not UNSET:
            field_dict["monthlyLimitUsd"] = monthly_limit_usd
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        daily_limit_usd = d.pop("dailyLimitUsd", UNSET)

        enabled = d.pop("enabled", UNSET)

        monthly_limit_usd = d.pop("monthlyLimitUsd", UNSET)

        name = d.pop("name", UNSET)

        update_input_body = cls(
            schema=schema,
            app_id=app_id,
            daily_limit_usd=daily_limit_usd,
            enabled=enabled,
            monthly_limit_usd=monthly_limit_usd,
            name=name,
        )

        return update_input_body
