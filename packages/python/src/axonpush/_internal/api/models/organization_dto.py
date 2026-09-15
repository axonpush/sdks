from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationDTO")


@_attrs_define
class OrganizationDTO:
    """
    Attributes:
        created_at (str):
        name (str):
        org_id (str):
        plan (str):
        slug (str):
        subscription_status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        description (str | Unset):
        events_quota_monthly (int | Unset):
        retention_days (int | Unset):
        seat_limit (int | Unset):
        updated_at (str | Unset):
    """

    created_at: str
    name: str
    org_id: str
    plan: str
    slug: str
    subscription_status: str
    schema: str | Unset = UNSET
    description: str | Unset = UNSET
    events_quota_monthly: int | Unset = UNSET
    retention_days: int | Unset = UNSET
    seat_limit: int | Unset = UNSET
    updated_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        name = self.name

        org_id = self.org_id

        plan = self.plan

        slug = self.slug

        subscription_status = self.subscription_status

        schema = self.schema

        description = self.description

        events_quota_monthly = self.events_quota_monthly

        retention_days = self.retention_days

        seat_limit = self.seat_limit

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "name": name,
                "orgId": org_id,
                "plan": plan,
                "slug": slug,
                "subscriptionStatus": subscription_status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if description is not UNSET:
            field_dict["description"] = description
        if events_quota_monthly is not UNSET:
            field_dict["eventsQuotaMonthly"] = events_quota_monthly
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days
        if seat_limit is not UNSET:
            field_dict["seatLimit"] = seat_limit
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        name = d.pop("name")

        org_id = d.pop("orgId")

        plan = d.pop("plan")

        slug = d.pop("slug")

        subscription_status = d.pop("subscriptionStatus")

        schema = d.pop("$schema", UNSET)

        description = d.pop("description", UNSET)

        events_quota_monthly = d.pop("eventsQuotaMonthly", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        seat_limit = d.pop("seatLimit", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        organization_dto = cls(
            created_at=created_at,
            name=name,
            org_id=org_id,
            plan=plan,
            slug=slug,
            subscription_status=subscription_status,
            schema=schema,
            description=description,
            events_quota_monthly=events_quota_monthly,
            retention_days=retention_days,
            seat_limit=seat_limit,
            updated_at=updated_at,
        )

        return organization_dto
