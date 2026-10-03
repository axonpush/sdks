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
    from ..models.activity_funnel_result import ActivityFunnelResult
    from ..models.activity_funnel_split import ActivityFunnelSplit


T = TypeVar("T", bound="ActivityAnalytics")


@_attrs_define
class ActivityAnalytics:
    """
    Attributes:
        as_of (datetime.datetime):
        clients (list[ActivityBreakdown] | None): Entities by the client and actor_side roles; empty without a client
            role
        funnels (list[ActivityFunnelResult] | None):
        splits (list[ActivityFunnelSplit] | None):
        window_days (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    as_of: datetime.datetime
    clients: list[ActivityBreakdown] | None
    funnels: list[ActivityFunnelResult] | None
    splits: list[ActivityFunnelSplit] | None
    window_days: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_breakdown import ActivityBreakdown
        from ..models.activity_funnel_result import ActivityFunnelResult
        from ..models.activity_funnel_split import ActivityFunnelSplit

        as_of = self.as_of.isoformat()

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

        splits: list[dict[str, Any]] | None
        if isinstance(self.splits, list):
            splits = []
            for splits_type_0_item_data in self.splits:
                splits_type_0_item = splits_type_0_item_data.to_dict()
                splits.append(splits_type_0_item)

        else:
            splits = self.splits

        window_days = self.window_days

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asOf": as_of,
                "clients": clients,
                "funnels": funnels,
                "splits": splits,
                "windowDays": window_days,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_breakdown import ActivityBreakdown
        from ..models.activity_funnel_result import ActivityFunnelResult
        from ..models.activity_funnel_split import ActivityFunnelSplit

        d = dict(src_dict)
        as_of = isoparse(d.pop("asOf"))

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

        def _parse_splits(data: object) -> list[ActivityFunnelSplit] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = ActivityFunnelSplit.from_dict(splits_type_0_item_data)

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityFunnelSplit] | None, data)

        splits = _parse_splits(d.pop("splits"))

        window_days = d.pop("windowDays")

        schema = d.pop("$schema", UNSET)

        activity_analytics = cls(
            as_of=as_of,
            clients=clients,
            funnels=funnels,
            splits=splits,
            window_days=window_days,
            schema=schema,
        )

        return activity_analytics
