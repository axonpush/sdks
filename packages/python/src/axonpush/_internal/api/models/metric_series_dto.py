from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.metric_point_dto import MetricPointDTO


T = TypeVar("T", bound="MetricSeriesDTO")


@_attrs_define
class MetricSeriesDTO:
    """
    Attributes:
        group (str):
        points (list[MetricPointDTO] | None):
    """

    group: str
    points: list[MetricPointDTO] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_point_dto import MetricPointDTO

        group = self.group

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
                "group": group,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_point_dto import MetricPointDTO

        d = dict(src_dict)
        group = d.pop("group")

        def _parse_points(data: object) -> list[MetricPointDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = MetricPointDTO.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MetricPointDTO] | None, data)

        points = _parse_points(d.pop("points"))

        metric_series_dto = cls(
            group=group,
            points=points,
        )

        return metric_series_dto
