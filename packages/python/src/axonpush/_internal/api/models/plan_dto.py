from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.features import Features
    from ..models.plan_dto_lemonsqueezy_variants import PlanDTOLemonsqueezyVariants
    from ..models.top_up import TopUp


T = TypeVar("T", bound="PlanDTO")


@_attrs_define
class PlanDTO:
    """
    Attributes:
        archive_days (int):
        events_monthly (int | None):
        features (Features):
        hot_days (int):
        id (str):
        max_archive_days (int):
        name (str):
        price_annual_usd (int | None):
        price_monthly_usd (int | None):
        quota_ceiling_percent (int):
        sales_led (bool):
        seats (int | None):
        top_up_available (bool):
        workflow_cases_monthly (int | None):
        workflow_history_days (int):
        lemonsqueezy_variants (PlanDTOLemonsqueezyVariants | Unset):
        top_up (TopUp | Unset):
    """

    archive_days: int
    events_monthly: int | None
    features: Features
    hot_days: int
    id: str
    max_archive_days: int
    name: str
    price_annual_usd: int | None
    price_monthly_usd: int | None
    quota_ceiling_percent: int
    sales_led: bool
    seats: int | None
    top_up_available: bool
    workflow_cases_monthly: int | None
    workflow_history_days: int
    lemonsqueezy_variants: PlanDTOLemonsqueezyVariants | Unset = UNSET
    top_up: TopUp | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.features import Features
        from ..models.plan_dto_lemonsqueezy_variants import PlanDTOLemonsqueezyVariants
        from ..models.top_up import TopUp

        archive_days = self.archive_days

        events_monthly: int | None
        events_monthly = self.events_monthly

        features = self.features.to_dict()

        hot_days = self.hot_days

        id = self.id

        max_archive_days = self.max_archive_days

        name = self.name

        price_annual_usd: int | None
        price_annual_usd = self.price_annual_usd

        price_monthly_usd: int | None
        price_monthly_usd = self.price_monthly_usd

        quota_ceiling_percent = self.quota_ceiling_percent

        sales_led = self.sales_led

        seats: int | None
        seats = self.seats

        top_up_available = self.top_up_available

        workflow_cases_monthly: int | None
        workflow_cases_monthly = self.workflow_cases_monthly

        workflow_history_days = self.workflow_history_days

        lemonsqueezy_variants: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lemonsqueezy_variants, Unset):
            lemonsqueezy_variants = self.lemonsqueezy_variants.to_dict()

        top_up: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_up, Unset):
            top_up = self.top_up.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "archiveDays": archive_days,
                "eventsMonthly": events_monthly,
                "features": features,
                "hotDays": hot_days,
                "id": id,
                "maxArchiveDays": max_archive_days,
                "name": name,
                "priceAnnualUsd": price_annual_usd,
                "priceMonthlyUsd": price_monthly_usd,
                "quotaCeilingPercent": quota_ceiling_percent,
                "salesLed": sales_led,
                "seats": seats,
                "topUpAvailable": top_up_available,
                "workflowCasesMonthly": workflow_cases_monthly,
                "workflowHistoryDays": workflow_history_days,
            }
        )
        if lemonsqueezy_variants is not UNSET:
            field_dict["lemonsqueezyVariants"] = lemonsqueezy_variants
        if top_up is not UNSET:
            field_dict["topUp"] = top_up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.features import Features
        from ..models.plan_dto_lemonsqueezy_variants import PlanDTOLemonsqueezyVariants
        from ..models.top_up import TopUp

        d = dict(src_dict)
        archive_days = d.pop("archiveDays")

        def _parse_events_monthly(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        events_monthly = _parse_events_monthly(d.pop("eventsMonthly"))

        features = Features.from_dict(d.pop("features"))

        hot_days = d.pop("hotDays")

        id = d.pop("id")

        max_archive_days = d.pop("maxArchiveDays")

        name = d.pop("name")

        def _parse_price_annual_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        price_annual_usd = _parse_price_annual_usd(d.pop("priceAnnualUsd"))

        def _parse_price_monthly_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        price_monthly_usd = _parse_price_monthly_usd(d.pop("priceMonthlyUsd"))

        quota_ceiling_percent = d.pop("quotaCeilingPercent")

        sales_led = d.pop("salesLed")

        def _parse_seats(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        seats = _parse_seats(d.pop("seats"))

        top_up_available = d.pop("topUpAvailable")

        def _parse_workflow_cases_monthly(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        workflow_cases_monthly = _parse_workflow_cases_monthly(
            d.pop("workflowCasesMonthly")
        )

        workflow_history_days = d.pop("workflowHistoryDays")

        _lemonsqueezy_variants = d.pop("lemonsqueezyVariants", UNSET)
        lemonsqueezy_variants: PlanDTOLemonsqueezyVariants | Unset
        if isinstance(_lemonsqueezy_variants, Unset):
            lemonsqueezy_variants = UNSET
        else:
            lemonsqueezy_variants = PlanDTOLemonsqueezyVariants.from_dict(
                _lemonsqueezy_variants
            )

        _top_up = d.pop("topUp", UNSET)
        top_up: TopUp | Unset
        if isinstance(_top_up, Unset):
            top_up = UNSET
        else:
            top_up = TopUp.from_dict(_top_up)

        plan_dto = cls(
            archive_days=archive_days,
            events_monthly=events_monthly,
            features=features,
            hot_days=hot_days,
            id=id,
            max_archive_days=max_archive_days,
            name=name,
            price_annual_usd=price_annual_usd,
            price_monthly_usd=price_monthly_usd,
            quota_ceiling_percent=quota_ceiling_percent,
            sales_led=sales_led,
            seats=seats,
            top_up_available=top_up_available,
            workflow_cases_monthly=workflow_cases_monthly,
            workflow_history_days=workflow_history_days,
            lemonsqueezy_variants=lemonsqueezy_variants,
            top_up=top_up,
        )

        return plan_dto
