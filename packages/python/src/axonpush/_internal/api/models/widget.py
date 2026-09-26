from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.widget_type import WidgetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_scope import WidgetScope


T = TypeVar("T", bound="Widget")


@_attrs_define
class Widget:
    """
    Attributes:
        type_ (WidgetType): kpi | timeseries | breakdown | latency
        dimension (str | Unset): breakdown dimension (model, provider, tag, ...)
        limit (int | Unset):
        metric (str | Unset): kpi/timeseries metric: calls|errors|cost|tokens|latency|ttft
        scope (WidgetScope | Unset):
        tag_key (str | Unset): attribute key to group by when dimension=tag
        title (str | Unset):
    """

    type_: WidgetType
    dimension: str | Unset = UNSET
    limit: int | Unset = UNSET
    metric: str | Unset = UNSET
    scope: WidgetScope | Unset = UNSET
    tag_key: str | Unset = UNSET
    title: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.widget_scope import WidgetScope

        type_ = self.type_.value

        dimension = self.dimension

        limit = self.limit

        metric = self.metric

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        tag_key = self.tag_key

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if limit is not UNSET:
            field_dict["limit"] = limit
        if metric is not UNSET:
            field_dict["metric"] = metric
        if scope is not UNSET:
            field_dict["scope"] = scope
        if tag_key is not UNSET:
            field_dict["tagKey"] = tag_key
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_scope import WidgetScope

        d = dict(src_dict)
        type_ = WidgetType(d.pop("type"))

        dimension = d.pop("dimension", UNSET)

        limit = d.pop("limit", UNSET)

        metric = d.pop("metric", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: WidgetScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = WidgetScope.from_dict(_scope)

        tag_key = d.pop("tagKey", UNSET)

        title = d.pop("title", UNSET)

        widget = cls(
            type_=type_,
            dimension=dimension,
            limit=limit,
            metric=metric,
            scope=scope,
            tag_key=tag_key,
            title=title,
        )

        return widget
