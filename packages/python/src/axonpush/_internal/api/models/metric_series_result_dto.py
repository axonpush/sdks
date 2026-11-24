from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_series_dto import MetricSeriesDTO


T = TypeVar("T", bound="MetricSeriesResultDTO")


@_attrs_define
class MetricSeriesResultDTO:
    """
    Attributes:
        agg (str):
        interval (str):
        name (str):
        series (list[MetricSeriesDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        group_by (str | Unset):
    """

    agg: str
    interval: str
    name: str
    series: list[MetricSeriesDTO] | None
    schema: str | Unset = UNSET
    group_by: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_series_dto import MetricSeriesDTO

        agg = self.agg

        interval = self.interval

        name = self.name

        series: list[dict[str, Any]] | None
        if isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)

        else:
            series = self.series

        schema = self.schema

        group_by = self.group_by

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agg": agg,
                "interval": interval,
                "name": name,
                "series": series,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_series_dto import MetricSeriesDTO

        d = dict(src_dict)
        agg = d.pop("agg")

        interval = d.pop("interval")

        name = d.pop("name")

        def _parse_series(data: object) -> list[MetricSeriesDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in _series_type_0:
                    series_type_0_item = MetricSeriesDTO.from_dict(
                        series_type_0_item_data
                    )

                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MetricSeriesDTO] | None, data)

        series = _parse_series(d.pop("series"))

        schema = d.pop("$schema", UNSET)

        group_by = d.pop("groupBy", UNSET)

        metric_series_result_dto = cls(
            agg=agg,
            interval=interval,
            name=name,
            series=series,
            schema=schema,
            group_by=group_by,
        )

        return metric_series_result_dto
