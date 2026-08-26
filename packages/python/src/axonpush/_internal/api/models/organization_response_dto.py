from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_response_dto import EnvironmentResponseDto
    from ..models.invitation_response_dto import InvitationResponseDto


T = TypeVar("T", bound="OrganizationResponseDto")


@_attrs_define
class OrganizationResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        events_quota_used_current (float):
        id (str):
        name (str):
        org_id (str):
        plan (str):
        slug (str):
        sso_enforced (bool):
        deleted_at (datetime.datetime | Unset):
        description (str | Unset):
        environments (list[EnvironmentResponseDto] | Unset):
        events_quota_monthly (float | Unset):
        invitations (list[InvitationResponseDto] | Unset):
        lemonsqueezy_customer_id (str | Unset):
        lemonsqueezy_subscription_id (str | Unset):
        retention_days (float | Unset):
        seat_limit (float | Unset):
        sso_connection_id (str | Unset):
        updated_at (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    events_quota_used_current: float
    id: str
    name: str
    org_id: str
    plan: str
    slug: str
    sso_enforced: bool
    deleted_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    environments: list[EnvironmentResponseDto] | Unset = UNSET
    events_quota_monthly: float | Unset = UNSET
    invitations: list[InvitationResponseDto] | Unset = UNSET
    lemonsqueezy_customer_id: str | Unset = UNSET
    lemonsqueezy_subscription_id: str | Unset = UNSET
    retention_days: float | Unset = UNSET
    seat_limit: float | Unset = UNSET
    sso_connection_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_response_dto import EnvironmentResponseDto
        from ..models.invitation_response_dto import InvitationResponseDto

        created_at = self.created_at.isoformat()

        events_quota_used_current = self.events_quota_used_current

        id = self.id

        name = self.name

        org_id = self.org_id

        plan = self.plan

        slug = self.slug

        sso_enforced = self.sso_enforced

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        description = self.description

        environments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for environments_item_data in self.environments:
                environments_item = environments_item_data.to_dict()
                environments.append(environments_item)

        events_quota_monthly = self.events_quota_monthly

        invitations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invitations, Unset):
            invitations = []
            for invitations_item_data in self.invitations:
                invitations_item = invitations_item_data.to_dict()
                invitations.append(invitations_item)

        lemonsqueezy_customer_id = self.lemonsqueezy_customer_id

        lemonsqueezy_subscription_id = self.lemonsqueezy_subscription_id

        retention_days = self.retention_days

        seat_limit = self.seat_limit

        sso_connection_id = self.sso_connection_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "eventsQuotaUsedCurrent": events_quota_used_current,
                "id": id,
                "name": name,
                "orgId": org_id,
                "plan": plan,
                "slug": slug,
                "ssoEnforced": sso_enforced,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if environments is not UNSET:
            field_dict["environments"] = environments
        if events_quota_monthly is not UNSET:
            field_dict["eventsQuotaMonthly"] = events_quota_monthly
        if invitations is not UNSET:
            field_dict["invitations"] = invitations
        if lemonsqueezy_customer_id is not UNSET:
            field_dict["lemonsqueezyCustomerId"] = lemonsqueezy_customer_id
        if lemonsqueezy_subscription_id is not UNSET:
            field_dict["lemonsqueezySubscriptionId"] = lemonsqueezy_subscription_id
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days
        if seat_limit is not UNSET:
            field_dict["seatLimit"] = seat_limit
        if sso_connection_id is not UNSET:
            field_dict["ssoConnectionId"] = sso_connection_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_response_dto import EnvironmentResponseDto
        from ..models.invitation_response_dto import InvitationResponseDto

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        events_quota_used_current = d.pop("eventsQuotaUsedCurrent")

        id = d.pop("id")

        name = d.pop("name")

        org_id = d.pop("orgId")

        plan = d.pop("plan")

        slug = d.pop("slug")

        sso_enforced = d.pop("ssoEnforced")

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        description = d.pop("description", UNSET)

        _environments = d.pop("environments", UNSET)
        environments: list[EnvironmentResponseDto] | Unset = UNSET
        if _environments is not UNSET:
            environments = []
            for environments_item_data in _environments:
                environments_item = EnvironmentResponseDto.from_dict(environments_item_data)

                environments.append(environments_item)

        events_quota_monthly = d.pop("eventsQuotaMonthly", UNSET)

        _invitations = d.pop("invitations", UNSET)
        invitations: list[InvitationResponseDto] | Unset = UNSET
        if _invitations is not UNSET:
            invitations = []
            for invitations_item_data in _invitations:
                invitations_item = InvitationResponseDto.from_dict(invitations_item_data)

                invitations.append(invitations_item)

        lemonsqueezy_customer_id = d.pop("lemonsqueezyCustomerId", UNSET)

        lemonsqueezy_subscription_id = d.pop("lemonsqueezySubscriptionId", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        seat_limit = d.pop("seatLimit", UNSET)

        sso_connection_id = d.pop("ssoConnectionId", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        organization_response_dto = cls(
            created_at=created_at,
            events_quota_used_current=events_quota_used_current,
            id=id,
            name=name,
            org_id=org_id,
            plan=plan,
            slug=slug,
            sso_enforced=sso_enforced,
            deleted_at=deleted_at,
            description=description,
            environments=environments,
            events_quota_monthly=events_quota_monthly,
            invitations=invitations,
            lemonsqueezy_customer_id=lemonsqueezy_customer_id,
            lemonsqueezy_subscription_id=lemonsqueezy_subscription_id,
            retention_days=retention_days,
            seat_limit=seat_limit,
            sso_connection_id=sso_connection_id,
            updated_at=updated_at,
        )

        organization_response_dto.additional_properties = d
        return organization_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
