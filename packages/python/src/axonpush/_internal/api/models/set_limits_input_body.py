from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetLimitsInputBody")


@_attrs_define
class SetLimitsInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        events_quota_monthly_override (int | Unset):
        retention_days_override (int | Unset):
        seat_limit_override (int | Unset): -1 = unlimited, null clears the override
    """

    schema: str | Unset = UNSET
    events_quota_monthly_override: int | Unset = UNSET
    retention_days_override: int | Unset = UNSET
    seat_limit_override: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        events_quota_monthly_override = self.events_quota_monthly_override

        retention_days_override = self.retention_days_override

        seat_limit_override = self.seat_limit_override

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if events_quota_monthly_override is not UNSET:
            field_dict["eventsQuotaMonthlyOverride"] = events_quota_monthly_override
        if retention_days_override is not UNSET:
            field_dict["retentionDaysOverride"] = retention_days_override
        if seat_limit_override is not UNSET:
            field_dict["seatLimitOverride"] = seat_limit_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        events_quota_monthly_override = d.pop("eventsQuotaMonthlyOverride", UNSET)

        retention_days_override = d.pop("retentionDaysOverride", UNSET)

        seat_limit_override = d.pop("seatLimitOverride", UNSET)

        set_limits_input_body = cls(
            schema=schema,
            events_quota_monthly_override=events_quota_monthly_override,
            retention_days_override=retention_days_override,
            seat_limit_override=seat_limit_override,
        )

        return set_limits_input_body
