from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_view_result import ActivityViewResult


T = TypeVar("T", bound="ViewsOutputBody")


@_attrs_define
class ViewsOutputBody:
    """
    Attributes:
        views (list[ActivityViewResult] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    views: list[ActivityViewResult] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_view_result import ActivityViewResult

        views: list[dict[str, Any]] | None
        if isinstance(self.views, list):
            views = []
            for views_type_0_item_data in self.views:
                views_type_0_item = views_type_0_item_data.to_dict()
                views.append(views_type_0_item)

        else:
            views = self.views

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "views": views,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_view_result import ActivityViewResult

        d = dict(src_dict)

        def _parse_views(data: object) -> list[ActivityViewResult] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                views_type_0 = []
                _views_type_0 = data
                for views_type_0_item_data in _views_type_0:
                    views_type_0_item = ActivityViewResult.from_dict(views_type_0_item_data)

                    views_type_0.append(views_type_0_item)

                return views_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityViewResult] | None, data)

        views = _parse_views(d.pop("views"))

        schema = d.pop("$schema", UNSET)

        views_output_body = cls(
            views=views,
            schema=schema,
        )

        return views_output_body
