from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="MonitorScheduleDTO")


@_attrs_define
class MonitorScheduleDTO:
    """
    Attributes:
        type_ (str): crontab, interval, or empty when the monitor has no schedule
        timezone (str | Unset):
        unit (str | Unset): Interval unit: minute, hour, day, week, month, year
        value (str | Unset): Crontab expression, or the interval count
    """

    type_: str
    timezone: str | Unset = UNSET
    unit: str | Unset = UNSET
    value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        timezone = self.timezone

        unit = self.unit

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if unit is not UNSET:
            field_dict["unit"] = unit
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        timezone = d.pop("timezone", UNSET)

        unit = d.pop("unit", UNSET)

        value = d.pop("value", UNSET)

        monitor_schedule_dto = cls(
            type_=type_,
            timezone=timezone,
            unit=unit,
            value=value,
        )

        return monitor_schedule_dto
