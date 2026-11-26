from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_dto import MonitorDTO


T = TypeVar("T", bound="ListMonitorsOutputBody")


@_attrs_define
class ListMonitorsOutputBody:
    """
    Attributes:
        monitors (list[MonitorDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    monitors: list[MonitorDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_dto import MonitorDTO

        monitors: list[dict[str, Any]] | None
        if isinstance(self.monitors, list):
            monitors = []
            for monitors_type_0_item_data in self.monitors:
                monitors_type_0_item = monitors_type_0_item_data.to_dict()
                monitors.append(monitors_type_0_item)

        else:
            monitors = self.monitors

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitors": monitors,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_dto import MonitorDTO

        d = dict(src_dict)

        def _parse_monitors(data: object) -> list[MonitorDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                monitors_type_0 = []
                _monitors_type_0 = data
                for monitors_type_0_item_data in _monitors_type_0:
                    monitors_type_0_item = MonitorDTO.from_dict(
                        monitors_type_0_item_data
                    )

                    monitors_type_0.append(monitors_type_0_item)

                return monitors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorDTO] | None, data)

        monitors = _parse_monitors(d.pop("monitors"))

        schema = d.pop("$schema", UNSET)

        list_monitors_output_body = cls(
            monitors=monitors,
            schema=schema,
        )

        return list_monitors_output_body
