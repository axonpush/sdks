from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_widget_point import ActivityWidgetPoint


T = TypeVar("T", bound="ActivityWidgetSeries")


@_attrs_define
class ActivityWidgetSeries:
    """
    Attributes:
        entity (str):
        field (str):
        points (list[ActivityWidgetPoint] | None):
        title (str):
        type_ (str):
    """

    entity: str
    field: str
    points: list[ActivityWidgetPoint] | None
    title: str
    type_: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_widget_point import ActivityWidgetPoint

        entity = self.entity

        field = self.field

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entity": entity,
                "field": field,
                "points": points,
                "title": title,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_widget_point import ActivityWidgetPoint

        d = dict(src_dict)
        entity = d.pop("entity")

        field = d.pop("field")

        def _parse_points(data: object) -> list[ActivityWidgetPoint] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = ActivityWidgetPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityWidgetPoint] | None, data)

        points = _parse_points(d.pop("points"))

        title = d.pop("title")

        type_ = d.pop("type")

        activity_widget_series = cls(
            entity=entity,
            field=field,
            points=points,
            title=title,
            type_=type_,
        )

        return activity_widget_series
