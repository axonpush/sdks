from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_breakdown import ActivityBreakdown
    from ..models.activity_cohort_count import ActivityCohortCount
    from ..models.activity_funnel_result import ActivityFunnelResult


T = TypeVar("T", bound="ActivityAnalytics")


@_attrs_define
class ActivityAnalytics:
    """
    Attributes:
        activations (list[ActivityCohortCount] | None):
        as_of (datetime.datetime):
        attempts (list[ActivityCohortCount] | None):
        clients (list[ActivityBreakdown] | None):
        funnels (list[ActivityFunnelResult] | None):
        window_days (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    activations: list[ActivityCohortCount] | None
    as_of: datetime.datetime
    attempts: list[ActivityCohortCount] | None
    clients: list[ActivityBreakdown] | None
    funnels: list[ActivityFunnelResult] | None
    window_days: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_breakdown import ActivityBreakdown
        from ..models.activity_cohort_count import ActivityCohortCount
        from ..models.activity_funnel_result import ActivityFunnelResult

        activations: list[dict[str, Any]] | None
        if isinstance(self.activations, list):
            activations = []
            for activations_type_0_item_data in self.activations:
                activations_type_0_item = activations_type_0_item_data.to_dict()
                activations.append(activations_type_0_item)

        else:
            activations = self.activations

        as_of = self.as_of.isoformat()

        attempts: list[dict[str, Any]] | None
        if isinstance(self.attempts, list):
            attempts = []
            for attempts_type_0_item_data in self.attempts:
                attempts_type_0_item = attempts_type_0_item_data.to_dict()
                attempts.append(attempts_type_0_item)

        else:
            attempts = self.attempts

        clients: list[dict[str, Any]] | None
        if isinstance(self.clients, list):
            clients = []
            for clients_type_0_item_data in self.clients:
                clients_type_0_item = clients_type_0_item_data.to_dict()
                clients.append(clients_type_0_item)

        else:
            clients = self.clients

        funnels: list[dict[str, Any]] | None
        if isinstance(self.funnels, list):
            funnels = []
            for funnels_type_0_item_data in self.funnels:
                funnels_type_0_item = funnels_type_0_item_data.to_dict()
                funnels.append(funnels_type_0_item)

        else:
            funnels = self.funnels

        window_days = self.window_days

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "activations": activations,
                "asOf": as_of,
                "attempts": attempts,
                "clients": clients,
                "funnels": funnels,
                "windowDays": window_days,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_breakdown import ActivityBreakdown
        from ..models.activity_cohort_count import ActivityCohortCount
        from ..models.activity_funnel_result import ActivityFunnelResult

        d = dict(src_dict)

        def _parse_activations(data: object) -> list[ActivityCohortCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                activations_type_0 = []
                _activations_type_0 = data
                for activations_type_0_item_data in _activations_type_0:
                    activations_type_0_item = ActivityCohortCount.from_dict(
                        activations_type_0_item_data
                    )

                    activations_type_0.append(activations_type_0_item)

                return activations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityCohortCount] | None, data)

        activations = _parse_activations(d.pop("activations"))

        as_of = isoparse(d.pop("asOf"))

        def _parse_attempts(data: object) -> list[ActivityCohortCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attempts_type_0 = []
                _attempts_type_0 = data
                for attempts_type_0_item_data in _attempts_type_0:
                    attempts_type_0_item = ActivityCohortCount.from_dict(attempts_type_0_item_data)

                    attempts_type_0.append(attempts_type_0_item)

                return attempts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityCohortCount] | None, data)

        attempts = _parse_attempts(d.pop("attempts"))

        def _parse_clients(data: object) -> list[ActivityBreakdown] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                clients_type_0 = []
                _clients_type_0 = data
                for clients_type_0_item_data in _clients_type_0:
                    clients_type_0_item = ActivityBreakdown.from_dict(clients_type_0_item_data)

                    clients_type_0.append(clients_type_0_item)

                return clients_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityBreakdown] | None, data)

        clients = _parse_clients(d.pop("clients"))

        def _parse_funnels(data: object) -> list[ActivityFunnelResult] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funnels_type_0 = []
                _funnels_type_0 = data
                for funnels_type_0_item_data in _funnels_type_0:
                    funnels_type_0_item = ActivityFunnelResult.from_dict(funnels_type_0_item_data)

                    funnels_type_0.append(funnels_type_0_item)

                return funnels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityFunnelResult] | None, data)

        funnels = _parse_funnels(d.pop("funnels"))

        window_days = d.pop("windowDays")

        schema = d.pop("$schema", UNSET)

        activity_analytics = cls(
            activations=activations,
            as_of=as_of,
            attempts=attempts,
            clients=clients,
            funnels=funnels,
            window_days=window_days,
            schema=schema,
        )

        return activity_analytics
