from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeseries_point_dto import TimeseriesPointDTO


T = TypeVar("T", bound="TimeseriesOutputBody")


@_attrs_define
class TimeseriesOutputBody:
    """
    Attributes:
        bucket (str):
        points (list[TimeseriesPointDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    bucket: str
    points: list[TimeseriesPointDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.timeseries_point_dto import TimeseriesPointDTO

        bucket = self.bucket

        points: list[dict[str, Any]] | None
        if isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)

        else:
            points = self.points

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bucket": bucket,
                "points": points,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeseries_point_dto import TimeseriesPointDTO

        d = dict(src_dict)
        bucket = d.pop("bucket")

        def _parse_points(data: object) -> list[TimeseriesPointDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = TimeseriesPointDTO.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TimeseriesPointDTO] | None, data)

        points = _parse_points(d.pop("points"))

        schema = d.pop("$schema", UNSET)

        timeseries_output_body = cls(
            bucket=bucket,
            points=points,
            schema=schema,
        )

        return timeseries_output_body
