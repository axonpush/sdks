from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_dto_governed_by import UsageDTOGovernedBy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_up import TopUp


T = TypeVar("T", bound="UsageDTO")


@_attrs_define
class UsageDTO:
    """
    Attributes:
        billing_enabled (bool):
        ceiling (int | None):
        credits_ (int):
        cycle_started_at (None | str):
        enforced (bool):
        governed_by (UsageDTOGovernedBy):
        has_billing_portal (bool):
        limit (int | None):
        period (str):
        plan (str):
        retention_days (int | None):
        seats (int | None):
        subscription_status (str):
        trial_ends_at (None | str):
        used (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        top_up (TopUp | Unset):
    """

    billing_enabled: bool
    ceiling: int | None
    credits_: int
    cycle_started_at: None | str
    enforced: bool
    governed_by: UsageDTOGovernedBy
    has_billing_portal: bool
    limit: int | None
    period: str
    plan: str
    retention_days: int | None
    seats: int | None
    subscription_status: str
    trial_ends_at: None | str
    used: int
    schema: str | Unset = UNSET
    top_up: TopUp | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.top_up import TopUp

        billing_enabled = self.billing_enabled

        ceiling: int | None
        ceiling = self.ceiling

        credits_ = self.credits_

        cycle_started_at: None | str
        cycle_started_at = self.cycle_started_at

        enforced = self.enforced

        governed_by = self.governed_by.value

        has_billing_portal = self.has_billing_portal

        limit: int | None
        limit = self.limit

        period = self.period

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

        top_up: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_up, Unset):
            top_up = self.top_up.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billingEnabled": billing_enabled,
                "ceiling": ceiling,
                "credits": credits_,
                "cycleStartedAt": cycle_started_at,
                "enforced": enforced,
                "governedBy": governed_by,
                "hasBillingPortal": has_billing_portal,
                "limit": limit,
                "period": period,
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
        if top_up is not UNSET:
            field_dict["topUp"] = top_up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_up import TopUp

        d = dict(src_dict)
        billing_enabled = d.pop("billingEnabled")

        def _parse_ceiling(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ceiling = _parse_ceiling(d.pop("ceiling"))

        credits_ = d.pop("credits")

        def _parse_cycle_started_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cycle_started_at = _parse_cycle_started_at(d.pop("cycleStartedAt"))

        enforced = d.pop("enforced")

        governed_by = UsageDTOGovernedBy(d.pop("governedBy"))

        has_billing_portal = d.pop("hasBillingPortal")

        def _parse_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        limit = _parse_limit(d.pop("limit"))

        period = d.pop("period")

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

        _top_up = d.pop("topUp", UNSET)
        top_up: TopUp | Unset
        if isinstance(_top_up, Unset):
            top_up = UNSET
        else:
            top_up = TopUp.from_dict(_top_up)

        usage_dto = cls(
            billing_enabled=billing_enabled,
            ceiling=ceiling,
            credits_=credits_,
            cycle_started_at=cycle_started_at,
            enforced=enforced,
            governed_by=governed_by,
            has_billing_portal=has_billing_portal,
            limit=limit,
            period=period,
            plan=plan,
            retention_days=retention_days,
            seats=seats,
            subscription_status=subscription_status,
            trial_ends_at=trial_ends_at,
            used=used,
            schema=schema,
            top_up=top_up,
        )

        return usage_dto
