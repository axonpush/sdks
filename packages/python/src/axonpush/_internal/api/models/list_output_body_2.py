from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_view import DashboardView


T = TypeVar("T", bound="ListOutputBody2")


@_attrs_define
class ListOutputBody2:
    """
    Attributes:
        dashboards (list[DashboardView] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    dashboards: list[DashboardView] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_view import DashboardView

        dashboards: list[dict[str, Any]] | None
        if isinstance(self.dashboards, list):
            dashboards = []
            for dashboards_type_0_item_data in self.dashboards:
                dashboards_type_0_item = dashboards_type_0_item_data.to_dict()
                dashboards.append(dashboards_type_0_item)

        else:
            dashboards = self.dashboards

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dashboards": dashboards,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_view import DashboardView

        d = dict(src_dict)

        def _parse_dashboards(data: object) -> list[DashboardView] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dashboards_type_0 = []
                _dashboards_type_0 = data
                for dashboards_type_0_item_data in _dashboards_type_0:
                    dashboards_type_0_item = DashboardView.from_dict(dashboards_type_0_item_data)

                    dashboards_type_0.append(dashboards_type_0_item)

                return dashboards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DashboardView] | None, data)

        dashboards = _parse_dashboards(d.pop("dashboards"))

        schema = d.pop("$schema", UNSET)

        list_output_body_2 = cls(
            dashboards=dashboards,
            schema=schema,
        )

        return list_output_body_2
