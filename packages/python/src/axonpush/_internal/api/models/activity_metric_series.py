from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_series_point import ActivitySeriesPoint


T = TypeVar("T", bound="ActivityMetricSeries")


@_attrs_define
class ActivityMetricSeries:
    """
    Attributes:
        key (str):
        label (str):
        points (list[ActivitySeriesPoint] | None):
    """

    key: str
    label: str
    points: list[ActivitySeriesPoint] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_series_point import ActivitySeriesPoint

        key = self.key

        label = self.label

        points: list[dict[str, Any]] | None
        if isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label": label,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_series_point import ActivitySeriesPoint

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_points(data: object) -> list[ActivitySeriesPoint] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = ActivitySeriesPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivitySeriesPoint] | None, data)

        points = _parse_points(d.pop("points"))

        activity_metric_series = cls(
            key=key,
            label=label,
            points=points,
        )

        return activity_metric_series
