from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_view_point import ActivityViewPoint


T = TypeVar("T", bound="ActivityViewSeries")


@_attrs_define
class ActivityViewSeries:
    """
    Attributes:
        key (str): Split value
        points (list[ActivityViewPoint] | None): One point per UTC day, zero-filled
    """

    key: str
    points: list[ActivityViewPoint] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_view_point import ActivityViewPoint

        key = self.key

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
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_view_point import ActivityViewPoint

        d = dict(src_dict)
        key = d.pop("key")

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

        activity_view_series = cls(
            key=key,
            points=points,
        )

        return activity_view_series
