from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgDTO")


@_attrs_define
class OrgDTO:
    """
    Attributes:
        created_at (str):
        events_quota_used_current (int):
        name (str):
        org_id (str):
        plan (str):
        slug (str):
        subscription_status (str):
        billing_monthly_amount_usd (float | Unset):
        billing_notes (str | Unset):
        events_quota_monthly (int | Unset):
        events_quota_monthly_override (int | Unset):
        retention_days (int | Unset):
        retention_days_override (int | Unset):
        seat_limit (int | Unset):
        seat_limit_override (int | Unset):
        trial_ends_at (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str
    events_quota_used_current: int
    name: str
    org_id: str
    plan: str
    slug: str
    subscription_status: str
    billing_monthly_amount_usd: float | Unset = UNSET
    billing_notes: str | Unset = UNSET
    events_quota_monthly: int | Unset = UNSET
    events_quota_monthly_override: int | Unset = UNSET
    retention_days: int | Unset = UNSET
    retention_days_override: int | Unset = UNSET
    seat_limit: int | Unset = UNSET
    seat_limit_override: int | Unset = UNSET
    trial_ends_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        events_quota_used_current = self.events_quota_used_current

        name = self.name

        org_id = self.org_id

        plan = self.plan

        slug = self.slug

        subscription_status = self.subscription_status

        billing_monthly_amount_usd = self.billing_monthly_amount_usd

        billing_notes = self.billing_notes

        events_quota_monthly = self.events_quota_monthly

        events_quota_monthly_override = self.events_quota_monthly_override

        retention_days = self.retention_days

        retention_days_override = self.retention_days_override

        seat_limit = self.seat_limit

        seat_limit_override = self.seat_limit_override

        trial_ends_at = self.trial_ends_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "eventsQuotaUsedCurrent": events_quota_used_current,
                "name": name,
                "orgId": org_id,
                "plan": plan,
                "slug": slug,
                "subscriptionStatus": subscription_status,
            }
        )
        if billing_monthly_amount_usd is not UNSET:
            field_dict["billingMonthlyAmountUsd"] = billing_monthly_amount_usd
        if billing_notes is not UNSET:
            field_dict["billingNotes"] = billing_notes
        if events_quota_monthly is not UNSET:
            field_dict["eventsQuotaMonthly"] = events_quota_monthly
        if events_quota_monthly_override is not UNSET:
            field_dict["eventsQuotaMonthlyOverride"] = events_quota_monthly_override
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days
        if retention_days_override is not UNSET:
            field_dict["retentionDaysOverride"] = retention_days_override
        if seat_limit is not UNSET:
            field_dict["seatLimit"] = seat_limit
        if seat_limit_override is not UNSET:
            field_dict["seatLimitOverride"] = seat_limit_override
        if trial_ends_at is not UNSET:
            field_dict["trialEndsAt"] = trial_ends_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        events_quota_used_current = d.pop("eventsQuotaUsedCurrent")

        name = d.pop("name")

        org_id = d.pop("orgId")

        plan = d.pop("plan")

        slug = d.pop("slug")

        subscription_status = d.pop("subscriptionStatus")

        billing_monthly_amount_usd = d.pop("billingMonthlyAmountUsd", UNSET)

        billing_notes = d.pop("billingNotes", UNSET)

        events_quota_monthly = d.pop("eventsQuotaMonthly", UNSET)

        events_quota_monthly_override = d.pop("eventsQuotaMonthlyOverride", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        retention_days_override = d.pop("retentionDaysOverride", UNSET)

        seat_limit = d.pop("seatLimit", UNSET)

        seat_limit_override = d.pop("seatLimitOverride", UNSET)

        trial_ends_at = d.pop("trialEndsAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        org_dto = cls(
            created_at=created_at,
            events_quota_used_current=events_quota_used_current,
            name=name,
            org_id=org_id,
            plan=plan,
            slug=slug,
            subscription_status=subscription_status,
            billing_monthly_amount_usd=billing_monthly_amount_usd,
            billing_notes=billing_notes,
            events_quota_monthly=events_quota_monthly,
            events_quota_monthly_override=events_quota_monthly_override,
            retention_days=retention_days,
            retention_days_override=retention_days_override,
            seat_limit=seat_limit,
            seat_limit_override=seat_limit_override,
            trial_ends_at=trial_ends_at,
            updated_at=updated_at,
        )

        return org_dto
