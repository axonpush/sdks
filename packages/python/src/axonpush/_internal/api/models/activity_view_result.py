from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_view_point import ActivityViewPoint


T = TypeVar("T", bound="ActivityViewResult")


@_attrs_define
class ActivityViewResult:
    """
    Attributes:
        id (str):
        points (list[ActivityViewPoint] | None):
        title (str):
        type_ (str):
        entity (str | Unset):
        key (str | Unset): Attribute key the view resolved its role to
        reason (str | Unset): Why the view is empty, e.g. a role the dictionary does not declare
        value (int | Unset): KPI count
    """

    id: str
    points: list[ActivityViewPoint] | None
    title: str
    type_: str
    entity: str | Unset = UNSET
    key: str | Unset = UNSET
    reason: str | Unset = UNSET
    value: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_view_point import ActivityViewPoint

        id = self.id

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

        entity = self.entity

        key = self.key

        reason = self.reason

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "points": points,
                "title": title,
                "type": type_,
            }
        )
        if entity is not UNSET:
            field_dict["entity"] = entity
        if key is not UNSET:
            field_dict["key"] = key
        if reason is not UNSET:
            field_dict["reason"] = reason
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_view_point import ActivityViewPoint

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_points(data: object) -> list[ActivityViewPoint] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in _points_type_0:
                    points_type_0_item = ActivityViewPoint.from_dict(points_type_0_item_data)

                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityViewPoint] | None, data)

        points = _parse_points(d.pop("points"))

        title = d.pop("title")

        type_ = d.pop("type")

        entity = d.pop("entity", UNSET)

        key = d.pop("key", UNSET)

        reason = d.pop("reason", UNSET)

        value = d.pop("value", UNSET)

        activity_view_result = cls(
            id=id,
            points=points,
            title=title,
            type_=type_,
            entity=entity,
            key=key,
            reason=reason,
            value=value,
        )

        return activity_view_result
