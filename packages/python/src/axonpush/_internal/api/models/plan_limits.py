from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_features import PlanFeatures
    from ..models.plan_limits_lemonsqueezy_variants import PlanLimitsLemonsqueezyVariants


T = TypeVar("T", bound="PlanLimits")


@_attrs_define
class PlanLimits:
    """
    Attributes:
        events (int | None):
        experiments_monthly (int | None):
        features (PlanFeatures):
        hot_retention_days (int | None):
        price_annual_usd (int | None):
        price_monthly_usd (int | None):
        retention_days (int | None):
        seats (int | None):
        lemonsqueezy_variants (PlanLimitsLemonsqueezyVariants | Unset):
    """

    events: int | None
    experiments_monthly: int | None
    features: PlanFeatures
    hot_retention_days: int | None
    price_annual_usd: int | None
    price_monthly_usd: int | None
    retention_days: int | None
    seats: int | None
    lemonsqueezy_variants: PlanLimitsLemonsqueezyVariants | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.plan_features import PlanFeatures
        from ..models.plan_limits_lemonsqueezy_variants import PlanLimitsLemonsqueezyVariants

        events: int | None
        events = self.events

        experiments_monthly: int | None
        experiments_monthly = self.experiments_monthly

        features = self.features.to_dict()

        hot_retention_days: int | None
        hot_retention_days = self.hot_retention_days

        price_annual_usd: int | None
        price_annual_usd = self.price_annual_usd

        price_monthly_usd: int | None
        price_monthly_usd = self.price_monthly_usd

        retention_days: int | None
        retention_days = self.retention_days

        seats: int | None
        seats = self.seats

        lemonsqueezy_variants: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lemonsqueezy_variants, Unset):
            lemonsqueezy_variants = self.lemonsqueezy_variants.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "experimentsMonthly": experiments_monthly,
                "features": features,
                "hotRetentionDays": hot_retention_days,
                "priceAnnualUsd": price_annual_usd,
                "priceMonthlyUsd": price_monthly_usd,
                "retentionDays": retention_days,
                "seats": seats,
            }
        )
        if lemonsqueezy_variants is not UNSET:
            field_dict["lemonsqueezyVariants"] = lemonsqueezy_variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_features import PlanFeatures
        from ..models.plan_limits_lemonsqueezy_variants import PlanLimitsLemonsqueezyVariants

        d = dict(src_dict)

        def _parse_events(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        events = _parse_events(d.pop("events"))

        def _parse_experiments_monthly(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        experiments_monthly = _parse_experiments_monthly(d.pop("experimentsMonthly"))

        features = PlanFeatures.from_dict(d.pop("features"))

        def _parse_hot_retention_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        hot_retention_days = _parse_hot_retention_days(d.pop("hotRetentionDays"))

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

        _lemonsqueezy_variants = d.pop("lemonsqueezyVariants", UNSET)
        lemonsqueezy_variants: PlanLimitsLemonsqueezyVariants | Unset
        if isinstance(_lemonsqueezy_variants, Unset):
            lemonsqueezy_variants = UNSET
        else:
            lemonsqueezy_variants = PlanLimitsLemonsqueezyVariants.from_dict(_lemonsqueezy_variants)

        plan_limits = cls(
            events=events,
            experiments_monthly=experiments_monthly,
            features=features,
            hot_retention_days=hot_retention_days,
            price_annual_usd=price_annual_usd,
            price_monthly_usd=price_monthly_usd,
            retention_days=retention_days,
            seats=seats,
            lemonsqueezy_variants=lemonsqueezy_variants,
        )

        return plan_limits
