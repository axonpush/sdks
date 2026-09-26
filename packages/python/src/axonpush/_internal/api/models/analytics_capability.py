from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsCapability")


@_attrs_define
class AnalyticsCapability:
    """
    Attributes:
        breakdown_dimensions (list[str] | None):
        custom_dimensions (bool):
        dashboards (bool):
        enabled (bool):
        tag_filter (bool):
    """

    breakdown_dimensions: list[str] | None
    custom_dimensions: bool
    dashboards: bool
    enabled: bool
    tag_filter: bool

    def to_dict(self) -> dict[str, Any]:
        breakdown_dimensions: list[str] | None
        if isinstance(self.breakdown_dimensions, list):
            breakdown_dimensions = self.breakdown_dimensions

        else:
            breakdown_dimensions = self.breakdown_dimensions

        custom_dimensions = self.custom_dimensions

        dashboards = self.dashboards

        enabled = self.enabled

        tag_filter = self.tag_filter

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "breakdownDimensions": breakdown_dimensions,
                "customDimensions": custom_dimensions,
                "dashboards": dashboards,
                "enabled": enabled,
                "tagFilter": tag_filter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_breakdown_dimensions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdown_dimensions_type_0 = cast(list[str], data)

                return breakdown_dimensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        breakdown_dimensions = _parse_breakdown_dimensions(d.pop("breakdownDimensions"))

        custom_dimensions = d.pop("customDimensions")

        dashboards = d.pop("dashboards")

        enabled = d.pop("enabled")

        tag_filter = d.pop("tagFilter")

        analytics_capability = cls(
            breakdown_dimensions=breakdown_dimensions,
            custom_dimensions=custom_dimensions,
            dashboards=dashboards,
            enabled=enabled,
            tag_filter=tag_filter,
        )

        return analytics_capability
