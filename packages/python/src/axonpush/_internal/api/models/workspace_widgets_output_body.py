from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_widget_series import ActivityWidgetSeries


T = TypeVar("T", bound="WorkspaceWidgetsOutputBody")


@_attrs_define
class WorkspaceWidgetsOutputBody:
    """
    Attributes:
        series (list[ActivityWidgetSeries] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    series: list[ActivityWidgetSeries] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_widget_series import ActivityWidgetSeries

        series: list[dict[str, Any]] | None
        if isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)

        else:
            series = self.series

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "series": series,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_widget_series import ActivityWidgetSeries

        d = dict(src_dict)

        def _parse_series(data: object) -> list[ActivityWidgetSeries] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in _series_type_0:
                    series_type_0_item = ActivityWidgetSeries.from_dict(series_type_0_item_data)

                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityWidgetSeries] | None, data)

        series = _parse_series(d.pop("series"))

        schema = d.pop("$schema", UNSET)

        workspace_widgets_output_body = cls(
            series=series,
            schema=schema,
        )

        return workspace_widgets_output_body
