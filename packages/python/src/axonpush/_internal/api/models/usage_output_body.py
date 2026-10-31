from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageOutputBody")


@_attrs_define
class UsageOutputBody:
    """
    Attributes:
        cycle_started_at (None | str):
        has_billing_portal (bool):
        limit (int | None):
        plan (str):
        retention_days (int | None):
        seats (int | None):
        subscription_status (str):
        trial_ends_at (None | str):
        used (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    cycle_started_at: None | str
    has_billing_portal: bool
    limit: int | None
    plan: str
    retention_days: int | None
    seats: int | None
    subscription_status: str
    trial_ends_at: None | str
    used: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cycle_started_at: None | str
        cycle_started_at = self.cycle_started_at

        has_billing_portal = self.has_billing_portal

        limit: int | None
        limit = self.limit

        plan = self.plan

        retention_days: int | None
        retention_days = self.retention_days

        seats: int | None
        seats = self.seats

        subscription_status = self.subscription_status

        trial_ends_at: None | str
        trial_ends_at = self.trial_ends_at

        used = self.used

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cycleStartedAt": cycle_started_at,
                "hasBillingPortal": has_billing_portal,
                "limit": limit,
                "plan": plan,
                "retentionDays": retention_days,
                "seats": seats,
                "subscriptionStatus": subscription_status,
                "trialEndsAt": trial_ends_at,
                "used": used,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cycle_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cycle_started_at = _parse_cycle_started_at(d.pop("cycleStartedAt"))

        has_billing_portal = d.pop("hasBillingPortal")

        def _parse_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        limit = _parse_limit(d.pop("limit"))

        plan = d.pop("plan")

        def _parse_retention_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        retention_days = _parse_retention_days(d.pop("retentionDays"))

        def _parse_seats(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        seats = _parse_seats(d.pop("seats"))

        subscription_status = d.pop("subscriptionStatus")

        def _parse_trial_ends_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trial_ends_at = _parse_trial_ends_at(d.pop("trialEndsAt"))

        used = d.pop("used")

        schema = d.pop("$schema", UNSET)

        usage_output_body = cls(
            cycle_started_at=cycle_started_at,
            has_billing_portal=has_billing_portal,
            limit=limit,
            plan=plan,
            retention_days=retention_days,
            seats=seats,
            subscription_status=subscription_status,
            trial_ends_at=trial_ends_at,
            used=used,
            schema=schema,
        )

        return usage_output_body
