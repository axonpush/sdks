from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_workspace_series_bucket import ActivityWorkspaceSeriesBucket
from ..models.activity_workspace_series_metric import ActivityWorkspaceSeriesMetric
from ..models.activity_workspace_series_source import ActivityWorkspaceSeriesSource
from ..models.activity_workspace_series_window import ActivityWorkspaceSeriesWindow
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_metric_series import ActivityMetricSeries


T = TypeVar("T", bound="ActivityWorkspaceSeries")


@_attrs_define
class ActivityWorkspaceSeries:
    """
    Attributes:
        bucket (ActivityWorkspaceSeriesBucket):
        from_ (datetime.datetime):
        metric (ActivityWorkspaceSeriesMetric):
        series (list[ActivityMetricSeries] | None):
        to (datetime.datetime):
        window (ActivityWorkspaceSeriesWindow):
        schema (str | Unset): A URL to the JSON Schema for this object.
        reason (str | Unset): Why the series is empty when the spec lacks a needed role or funnel
        source (ActivityWorkspaceSeriesSource | Unset): rollup: de-identified daily aggregates (90d window); the funnel
            metric then counts entities reaching each stage per day rather than furthest stage
    """

    bucket: ActivityWorkspaceSeriesBucket
    from_: datetime.datetime
    metric: ActivityWorkspaceSeriesMetric
    series: list[ActivityMetricSeries] | None
    to: datetime.datetime
    window: ActivityWorkspaceSeriesWindow
    schema: str | Unset = UNSET
    reason: str | Unset = UNSET
    source: ActivityWorkspaceSeriesSource | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_metric_series import ActivityMetricSeries

        bucket = self.bucket.value

        from_ = self.from_.isoformat()

        metric = self.metric.value

        series: list[dict[str, Any]] | None
        if isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)

        else:
            series = self.series

        to = self.to.isoformat()

        window = self.window.value

        schema = self.schema

        reason = self.reason

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bucket": bucket,
                "from": from_,
                "metric": metric,
                "series": series,
                "to": to,
                "window": window,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if reason is not UNSET:
            field_dict["reason"] = reason
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_metric_series import ActivityMetricSeries

        d = dict(src_dict)
        bucket = ActivityWorkspaceSeriesBucket(d.pop("bucket"))

        from_ = isoparse(d.pop("from"))

        metric = ActivityWorkspaceSeriesMetric(d.pop("metric"))

        def _parse_series(data: object) -> list[ActivityMetricSeries] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in _series_type_0:
                    series_type_0_item = ActivityMetricSeries.from_dict(series_type_0_item_data)

                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityMetricSeries] | None, data)

        series = _parse_series(d.pop("series"))

        to = isoparse(d.pop("to"))

        window = ActivityWorkspaceSeriesWindow(d.pop("window"))

        schema = d.pop("$schema", UNSET)

        reason = d.pop("reason", UNSET)

        _source = d.pop("source", UNSET)
        source: ActivityWorkspaceSeriesSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ActivityWorkspaceSeriesSource(_source)

        activity_workspace_series = cls(
            bucket=bucket,
            from_=from_,
            metric=metric,
            series=series,
            to=to,
            window=window,
            schema=schema,
            reason=reason,
            source=source,
        )

        return activity_workspace_series
