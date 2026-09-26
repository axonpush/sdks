from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_count import KeyCount
    from ..models.overview_body_events_struct import OverviewBodyEventsStruct
    from ..models.overview_body_managed_llm_struct import OverviewBodyManagedLlmStruct
    from ..models.overview_body_mrr_struct import OverviewBodyMrrStruct
    from ..models.overview_body_totals_struct import OverviewBodyTotalsStruct


T = TypeVar("T", bound="OverviewBody")


@_attrs_define
class OverviewBody:
    """
    Attributes:
        events (OverviewBodyEventsStruct):
        managed_llm (OverviewBodyManagedLlmStruct):
        mrr (OverviewBodyMrrStruct):
        plan_distribution (list[KeyCount] | None):
        subscription_status_distribution (list[KeyCount] | None):
        totals (OverviewBodyTotalsStruct):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    events: OverviewBodyEventsStruct
    managed_llm: OverviewBodyManagedLlmStruct
    mrr: OverviewBodyMrrStruct
    plan_distribution: list[KeyCount] | None
    subscription_status_distribution: list[KeyCount] | None
    totals: OverviewBodyTotalsStruct
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.key_count import KeyCount
        from ..models.overview_body_events_struct import OverviewBodyEventsStruct
        from ..models.overview_body_managed_llm_struct import OverviewBodyManagedLlmStruct
        from ..models.overview_body_mrr_struct import OverviewBodyMrrStruct
        from ..models.overview_body_totals_struct import OverviewBodyTotalsStruct

        events = self.events.to_dict()

        managed_llm = self.managed_llm.to_dict()

        mrr = self.mrr.to_dict()

        plan_distribution: list[dict[str, Any]] | None
        if isinstance(self.plan_distribution, list):
            plan_distribution = []
            for plan_distribution_type_0_item_data in self.plan_distribution:
                plan_distribution_type_0_item = plan_distribution_type_0_item_data.to_dict()
                plan_distribution.append(plan_distribution_type_0_item)

        else:
            plan_distribution = self.plan_distribution

        subscription_status_distribution: list[dict[str, Any]] | None
        if isinstance(self.subscription_status_distribution, list):
            subscription_status_distribution = []
            for (
                subscription_status_distribution_type_0_item_data
            ) in self.subscription_status_distribution:
                subscription_status_distribution_type_0_item = (
                    subscription_status_distribution_type_0_item_data.to_dict()
                )
                subscription_status_distribution.append(
                    subscription_status_distribution_type_0_item
                )

        else:
            subscription_status_distribution = self.subscription_status_distribution

        totals = self.totals.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "managedLlm": managed_llm,
                "mrr": mrr,
                "planDistribution": plan_distribution,
                "subscriptionStatusDistribution": subscription_status_distribution,
                "totals": totals,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_count import KeyCount
        from ..models.overview_body_events_struct import OverviewBodyEventsStruct
        from ..models.overview_body_managed_llm_struct import OverviewBodyManagedLlmStruct
        from ..models.overview_body_mrr_struct import OverviewBodyMrrStruct
        from ..models.overview_body_totals_struct import OverviewBodyTotalsStruct

        d = dict(src_dict)
        events = OverviewBodyEventsStruct.from_dict(d.pop("events"))

        managed_llm = OverviewBodyManagedLlmStruct.from_dict(d.pop("managedLlm"))

        mrr = OverviewBodyMrrStruct.from_dict(d.pop("mrr"))

        def _parse_plan_distribution(data: object) -> list[KeyCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                plan_distribution_type_0 = []
                _plan_distribution_type_0 = data
                for plan_distribution_type_0_item_data in _plan_distribution_type_0:
                    plan_distribution_type_0_item = KeyCount.from_dict(
                        plan_distribution_type_0_item_data
                    )

                    plan_distribution_type_0.append(plan_distribution_type_0_item)

                return plan_distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeyCount] | None, data)

        plan_distribution = _parse_plan_distribution(d.pop("planDistribution"))

        def _parse_subscription_status_distribution(data: object) -> list[KeyCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscription_status_distribution_type_0 = []
                _subscription_status_distribution_type_0 = data
                for (
                    subscription_status_distribution_type_0_item_data
                ) in _subscription_status_distribution_type_0:
                    subscription_status_distribution_type_0_item = KeyCount.from_dict(
                        subscription_status_distribution_type_0_item_data
                    )

                    subscription_status_distribution_type_0.append(
                        subscription_status_distribution_type_0_item
                    )

                return subscription_status_distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KeyCount] | None, data)

        subscription_status_distribution = _parse_subscription_status_distribution(
            d.pop("subscriptionStatusDistribution")
        )

        totals = OverviewBodyTotalsStruct.from_dict(d.pop("totals"))

        schema = d.pop("$schema", UNSET)

        overview_body = cls(
            events=events,
            managed_llm=managed_llm,
            mrr=mrr,
            plan_distribution=plan_distribution,
            subscription_status_distribution=subscription_status_distribution,
            totals=totals,
            schema=schema,
        )

        return overview_body
