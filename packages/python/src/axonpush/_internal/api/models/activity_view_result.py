from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_activation_result import ActivityActivationResult
    from ..models.activity_graph_result import ActivityGraphResult
    from ..models.activity_interval_result import ActivityIntervalResult
    from ..models.activity_rate_result import ActivityRateResult
    from ..models.activity_view_point import ActivityViewPoint
    from ..models.activity_view_series import ActivityViewSeries
    from ..models.activity_view_split import ActivityViewSplit


T = TypeVar("T", bound="ActivityViewResult")


@_attrs_define
class ActivityViewResult:
    """
    Attributes:
        id (str):
        points (list[ActivityViewPoint] | None):
        title (str):
        type_ (str):
        activation (ActivityActivationResult | Unset):
        entity (str | Unset):
        graph (ActivityGraphResult | Unset):
        interval (ActivityIntervalResult | Unset):
        key (str | Unset): Attribute key the view resolved its role to
        rate (ActivityRateResult | Unset):
        reason (str | Unset): Why the view is empty, e.g. a role the dictionary does not declare
        series (list[ActivityViewSeries] | None | Unset):
        split_keys (list[str] | None | Unset): Attribute keys the splits resolved to
        splits (list[ActivityViewSplit] | None | Unset):
        value (int | Unset): KPI count
        window_seconds (int | Unset): The period measured, when the view has one
    """

    id: str
    points: list[ActivityViewPoint] | None
    title: str
    type_: str
    activation: ActivityActivationResult | Unset = UNSET
    entity: str | Unset = UNSET
    graph: ActivityGraphResult | Unset = UNSET
    interval: ActivityIntervalResult | Unset = UNSET
    key: str | Unset = UNSET
    rate: ActivityRateResult | Unset = UNSET
    reason: str | Unset = UNSET
    series: list[ActivityViewSeries] | None | Unset = UNSET
    split_keys: list[str] | None | Unset = UNSET
    splits: list[ActivityViewSplit] | None | Unset = UNSET
    value: int | Unset = UNSET
    window_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_activation_result import ActivityActivationResult
        from ..models.activity_graph_result import ActivityGraphResult
        from ..models.activity_interval_result import ActivityIntervalResult
        from ..models.activity_rate_result import ActivityRateResult
        from ..models.activity_view_point import ActivityViewPoint
        from ..models.activity_view_series import ActivityViewSeries
        from ..models.activity_view_split import ActivityViewSplit

        id = self.id

        points: list[dict[str, Any]] | None
        if isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        title = self.title

        type_ = self.type_

        activation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activation, Unset):
            activation = self.activation.to_dict()

        entity = self.entity

        graph: dict[str, Any] | Unset = UNSET
        if not isinstance(self.graph, Unset):
            graph = self.graph.to_dict()

        interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        key = self.key

        rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate, Unset):
            rate = self.rate.to_dict()

        reason = self.reason

        series: list[dict[str, Any]] | None | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        elif isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)

        else:
            series = self.series

        split_keys: list[str] | None | Unset
        if isinstance(self.split_keys, Unset):
            split_keys = UNSET
        elif isinstance(self.split_keys, list):
            split_keys = self.split_keys

        else:
            split_keys = self.split_keys

        splits: list[dict[str, Any]] | None | Unset
        if isinstance(self.splits, Unset):
            splits = UNSET
        elif isinstance(self.splits, list):
            splits = []
            for splits_type_0_item_data in self.splits:
                splits_type_0_item = splits_type_0_item_data.to_dict()
                splits.append(splits_type_0_item)

        else:
            splits = self.splits

        value = self.value

        window_seconds = self.window_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "points": points,
                "title": title,
                "type": type_,
            }
        )
        if activation is not UNSET:
            field_dict["activation"] = activation
        if entity is not UNSET:
            field_dict["entity"] = entity
        if graph is not UNSET:
            field_dict["graph"] = graph
        if interval is not UNSET:
            field_dict["interval"] = interval
        if key is not UNSET:
            field_dict["key"] = key
        if rate is not UNSET:
            field_dict["rate"] = rate
        if reason is not UNSET:
            field_dict["reason"] = reason
        if series is not UNSET:
            field_dict["series"] = series
        if split_keys is not UNSET:
            field_dict["splitKeys"] = split_keys
        if splits is not UNSET:
            field_dict["splits"] = splits
        if value is not UNSET:
            field_dict["value"] = value
        if window_seconds is not UNSET:
            field_dict["windowSeconds"] = window_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_activation_result import ActivityActivationResult
        from ..models.activity_graph_result import ActivityGraphResult
        from ..models.activity_interval_result import ActivityIntervalResult
        from ..models.activity_rate_result import ActivityRateResult
        from ..models.activity_view_point import ActivityViewPoint
        from ..models.activity_view_series import ActivityViewSeries
        from ..models.activity_view_split import ActivityViewSplit

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_points(data: object) -> list[ActivityViewPoint] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = ActivityViewPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityViewPoint] | None, data)

        points = _parse_points(d.pop("points"))

        title = d.pop("title")

        type_ = d.pop("type")

        _activation = d.pop("activation", UNSET)
        activation: ActivityActivationResult | Unset
        if isinstance(_activation, Unset):
            activation = UNSET
        else:
            activation = ActivityActivationResult.from_dict(_activation)

        entity = d.pop("entity", UNSET)

        _graph = d.pop("graph", UNSET)
        graph: ActivityGraphResult | Unset
        if isinstance(_graph, Unset):
            graph = UNSET
        else:
            graph = ActivityGraphResult.from_dict(_graph)

        _interval = d.pop("interval", UNSET)
        interval: ActivityIntervalResult | Unset
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = ActivityIntervalResult.from_dict(_interval)

        key = d.pop("key", UNSET)

        _rate = d.pop("rate", UNSET)
        rate: ActivityRateResult | Unset
        if isinstance(_rate, Unset):
            rate = UNSET
        else:
            rate = ActivityRateResult.from_dict(_rate)

        reason = d.pop("reason", UNSET)

        def _parse_series(data: object) -> list[ActivityViewSeries] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in _series_type_0:
                    series_type_0_item = ActivityViewSeries.from_dict(series_type_0_item_data)

                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityViewSeries] | None | Unset, data)

        series = _parse_series(d.pop("series", UNSET))

        def _parse_split_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                split_keys_type_0 = cast(list[str], data)

                return split_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        split_keys = _parse_split_keys(d.pop("splitKeys", UNSET))

        def _parse_splits(data: object) -> list[ActivityViewSplit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                splits_type_0 = []
                _splits_type_0 = data
                for splits_type_0_item_data in _splits_type_0:
                    splits_type_0_item = ActivityViewSplit.from_dict(splits_type_0_item_data)

                    splits_type_0.append(splits_type_0_item)

                return splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityViewSplit] | None | Unset, data)

        splits = _parse_splits(d.pop("splits", UNSET))

        value = d.pop("value", UNSET)

        window_seconds = d.pop("windowSeconds", UNSET)

        activity_view_result = cls(
            id=id,
            points=points,
            title=title,
            type_=type_,
            activation=activation,
            entity=entity,
            graph=graph,
            interval=interval,
            key=key,
            rate=rate,
            reason=reason,
            series=series,
            split_keys=split_keys,
            splits=splits,
            value=value,
            window_seconds=window_seconds,
        )

        return activity_view_result
