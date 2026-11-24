from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.usage_dto_governed_by import UsageDTOGovernedBy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_case_usage import WorkflowCaseUsage


T = TypeVar("T", bound="UsageDTO")


@_attrs_define
class UsageDTO:
    """
    Attributes:
        billing_enabled (bool):
        bills_overage (bool):
        ceiling (int | None):
        cycle_started_at (None | str):
        enforced (bool):
        governed_by (UsageDTOGovernedBy):
        has_billing_portal (bool):
        limit (int | None):
        overage_cap_usd (int | None):
        overage_cents (int):
        overage_events (int):
        period (str):
        plan (str):
        retention_days (int | None):
        seats (int | None):
        subscription_status (str):
        trial_ends_at (None | str):
        used (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        workflow_cases (WorkflowCaseUsage | Unset):
    """

    billing_enabled: bool
    bills_overage: bool
    ceiling: int | None
    cycle_started_at: None | str
    enforced: bool
    governed_by: UsageDTOGovernedBy
    has_billing_portal: bool
    limit: int | None
    overage_cap_usd: int | None
    overage_cents: int
    overage_events: int
    period: str
    plan: str
    retention_days: int | None
    seats: int | None
    subscription_status: str
    trial_ends_at: None | str
    used: int
    schema: str | Unset = UNSET
    workflow_cases: WorkflowCaseUsage | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_case_usage import WorkflowCaseUsage

        billing_enabled = self.billing_enabled

        bills_overage = self.bills_overage

        ceiling: int | None
        ceiling = self.ceiling

        cycle_started_at: None | str
        cycle_started_at = self.cycle_started_at

        enforced = self.enforced

        governed_by = self.governed_by.value

        has_billing_portal = self.has_billing_portal

        limit: int | None
        limit = self.limit

        overage_cap_usd: int | None
        overage_cap_usd = self.overage_cap_usd

        overage_cents = self.overage_cents

        overage_events = self.overage_events

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

        workflow_cases: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_cases, Unset):
            workflow_cases = self.workflow_cases.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billingEnabled": billing_enabled,
                "billsOverage": bills_overage,
                "ceiling": ceiling,
                "cycleStartedAt": cycle_started_at,
                "enforced": enforced,
                "governedBy": governed_by,
                "hasBillingPortal": has_billing_portal,
                "limit": limit,
                "overageCapUsd": overage_cap_usd,
                "overageCents": overage_cents,
                "overageEvents": overage_events,
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
        if workflow_cases is not UNSET:
            field_dict["workflowCases"] = workflow_cases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_case_usage import WorkflowCaseUsage

        d = dict(src_dict)
        billing_enabled = d.pop("billingEnabled")

        bills_overage = d.pop("billsOverage")

        def _parse_ceiling(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ceiling = _parse_ceiling(d.pop("ceiling"))

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

        def _parse_overage_cap_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        overage_cap_usd = _parse_overage_cap_usd(d.pop("overageCapUsd"))

        overage_cents = d.pop("overageCents")

        overage_events = d.pop("overageEvents")

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

        _workflow_cases = d.pop("workflowCases", UNSET)
        workflow_cases: WorkflowCaseUsage | Unset
        if isinstance(_workflow_cases, Unset):
            workflow_cases = UNSET
        else:
            workflow_cases = WorkflowCaseUsage.from_dict(_workflow_cases)

        usage_dto = cls(
            billing_enabled=billing_enabled,
            bills_overage=bills_overage,
            ceiling=ceiling,
            cycle_started_at=cycle_started_at,
            enforced=enforced,
            governed_by=governed_by,
            has_billing_portal=has_billing_portal,
            limit=limit,
            overage_cap_usd=overage_cap_usd,
            overage_cents=overage_cents,
            overage_events=overage_events,
            period=period,
            plan=plan,
            retention_days=retention_days,
            seats=seats,
            subscription_status=subscription_status,
            trial_ends_at=trial_ends_at,
            used=used,
            schema=schema,
            workflow_cases=workflow_cases,
        )

        return usage_dto
