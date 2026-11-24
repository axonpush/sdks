from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.features import Features
    from ..models.overage import Overage


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
        workflow_cases_monthly (int | None):
        workflow_history_days (int):
        cadences (list[str] | None | Unset):
        overage (Overage | Unset):
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
    workflow_cases_monthly: int | None
    workflow_history_days: int
    cadences: list[str] | None | Unset = UNSET
    overage: Overage | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.features import Features
        from ..models.overage import Overage

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

        workflow_cases_monthly: int | None
        workflow_cases_monthly = self.workflow_cases_monthly

        workflow_history_days = self.workflow_history_days

        cadences: list[str] | None | Unset
        if isinstance(self.cadences, Unset):
            cadences = UNSET
        elif isinstance(self.cadences, list):
            cadences = self.cadences

        else:
            cadences = self.cadences

        overage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overage, Unset):
            overage = self.overage.to_dict()

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
                "workflowCasesMonthly": workflow_cases_monthly,
                "workflowHistoryDays": workflow_history_days,
            }
        )
        if cadences is not UNSET:
            field_dict["cadences"] = cadences
        if overage is not UNSET:
            field_dict["overage"] = overage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.features import Features
        from ..models.overage import Overage

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

        def _parse_workflow_cases_monthly(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        workflow_cases_monthly = _parse_workflow_cases_monthly(
            d.pop("workflowCasesMonthly")
        )

        workflow_history_days = d.pop("workflowHistoryDays")

        def _parse_cadences(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cadences_type_0 = cast(list[str], data)

                return cadences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cadences = _parse_cadences(d.pop("cadences", UNSET))

        _overage = d.pop("overage", UNSET)
        overage: Overage | Unset
        if isinstance(_overage, Unset):
            overage = UNSET
        else:
            overage = Overage.from_dict(_overage)

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
            workflow_cases_monthly=workflow_cases_monthly,
            workflow_history_days=workflow_history_days,
            cadences=cadences,
            overage=overage,
        )

        return plan_dto
