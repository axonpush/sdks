from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_widget_type import ActivityWidgetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityWidget")


@_attrs_define
class ActivityWidget:
    """
    Attributes:
        title (str):
        type_ (ActivityWidgetType):
        entity (str | Unset):
        field (str | Unset):
    """

    title: str
    type_: ActivityWidgetType
    entity: str | Unset = UNSET
    field: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_.value

        entity = self.entity

        field = self.field

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "type": type_,
            }
        )
        if entity is not UNSET:
            field_dict["entity"] = entity
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        type_ = ActivityWidgetType(d.pop("type"))

        entity = d.pop("entity", UNSET)

        field = d.pop("field", UNSET)

        activity_widget = cls(
            title=title,
            type_=type_,
            entity=entity,
            field=field,
        )

        return activity_widget
