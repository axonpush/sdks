from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.latency_percentiles_dto import LatencyPercentilesDTO
    from ..models.overview_breakdown_dto import OverviewBreakdownDTO
    from ..models.overview_timeseries_dto import OverviewTimeseriesDTO


T = TypeVar("T", bound="AnalyticsOverviewOutputBody")


@_attrs_define
class AnalyticsOverviewOutputBody:
    """
    Attributes:
        breakdowns (list[OverviewBreakdownDTO] | None):
        latency (LatencyPercentilesDTO):
        timeseries (OverviewTimeseriesDTO):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    breakdowns: list[OverviewBreakdownDTO] | None
    latency: LatencyPercentilesDTO
    timeseries: OverviewTimeseriesDTO
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.latency_percentiles_dto import LatencyPercentilesDTO
        from ..models.overview_breakdown_dto import OverviewBreakdownDTO
        from ..models.overview_timeseries_dto import OverviewTimeseriesDTO

        breakdowns: list[dict[str, Any]] | None
        if isinstance(self.breakdowns, list):
            breakdowns = []
            for breakdowns_type_0_item_data in self.breakdowns:
                breakdowns_type_0_item = breakdowns_type_0_item_data.to_dict()
                breakdowns.append(breakdowns_type_0_item)

        else:
            breakdowns = self.breakdowns

        latency = self.latency.to_dict()

        timeseries = self.timeseries.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "breakdowns": breakdowns,
                "latency": latency,
                "timeseries": timeseries,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latency_percentiles_dto import LatencyPercentilesDTO
        from ..models.overview_breakdown_dto import OverviewBreakdownDTO
        from ..models.overview_timeseries_dto import OverviewTimeseriesDTO

        d = dict(src_dict)

        def _parse_breakdowns(data: object) -> list[OverviewBreakdownDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdowns_type_0 = []
                _breakdowns_type_0 = data
                for breakdowns_type_0_item_data in _breakdowns_type_0:
                    breakdowns_type_0_item = OverviewBreakdownDTO.from_dict(
                        breakdowns_type_0_item_data
                    )

                    breakdowns_type_0.append(breakdowns_type_0_item)

                return breakdowns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OverviewBreakdownDTO] | None, data)

        breakdowns = _parse_breakdowns(d.pop("breakdowns"))

        latency = LatencyPercentilesDTO.from_dict(d.pop("latency"))

        timeseries = OverviewTimeseriesDTO.from_dict(d.pop("timeseries"))

        schema = d.pop("$schema", UNSET)

        analytics_overview_output_body = cls(
            breakdowns=breakdowns,
            latency=latency,
            timeseries=timeseries,
            schema=schema,
        )

        return analytics_overview_output_body
