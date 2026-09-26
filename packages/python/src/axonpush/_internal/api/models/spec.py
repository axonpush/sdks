from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget import Widget


T = TypeVar("T", bound="Spec")


@_attrs_define
class Spec:
    """
    Attributes:
        widgets (list[Widget] | None):
    """

    widgets: list[Widget] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.widget import Widget

        widgets: list[dict[str, Any]] | None
        if isinstance(self.widgets, list):
            widgets = []
            for widgets_type_0_item_data in self.widgets:
                widgets_type_0_item = widgets_type_0_item_data.to_dict()
                widgets.append(widgets_type_0_item)

        else:
            widgets = self.widgets

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "widgets": widgets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget import Widget

        d = dict(src_dict)

        def _parse_widgets(data: object) -> list[Widget] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                widgets_type_0 = []
                _widgets_type_0 = data
                for widgets_type_0_item_data in _widgets_type_0:
                    widgets_type_0_item = Widget.from_dict(widgets_type_0_item_data)

                    widgets_type_0.append(widgets_type_0_item)

                return widgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Widget] | None, data)

        widgets = _parse_widgets(d.pop("widgets"))

        spec = cls(
            widgets=widgets,
        )

        return spec
