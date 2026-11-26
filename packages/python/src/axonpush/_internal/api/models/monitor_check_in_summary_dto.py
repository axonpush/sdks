from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_check_in_summary_dto_status import MonitorCheckInSummaryDTOStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorCheckInSummaryDTO")


@_attrs_define
class MonitorCheckInSummaryDTO:
    """
    Attributes:
        started_at (str):
        status (MonitorCheckInSummaryDTOStatus):
        duration_ms (float | Unset):
    """

    started_at: str
    status: MonitorCheckInSummaryDTOStatus
    duration_ms: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        started_at = self.started_at

        status = self.status.value

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startedAt": started_at,
                "status": status,
            }
        )
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        started_at = d.pop("startedAt")

        status = MonitorCheckInSummaryDTOStatus(d.pop("status"))

        duration_ms = d.pop("durationMs", UNSET)

        monitor_check_in_summary_dto = cls(
            started_at=started_at,
            status=status,
            duration_ms=duration_ms,
        )

        return monitor_check_in_summary_dto
