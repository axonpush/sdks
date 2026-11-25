from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.monitor_check_in_dto_status import MonitorCheckInDTOStatus
from ..types import UNSET, Unset


T = TypeVar("T", bound="MonitorCheckInDTO")


@_attrs_define
class MonitorCheckInDTO:
    """
    Attributes:
        check_in_id (str): The SDK's check-in id (missed runs get a synthetic id)
        id (str):
        started_at (str):
        status (MonitorCheckInDTOStatus):
        duration_ms (float | Unset):
        environment (str | Unset): The environment name the SDK reported
        finished_at (str | Unset):
        release (str | Unset):
        trace_id (str | Unset):
    """

    check_in_id: str
    id: str
    started_at: str
    status: MonitorCheckInDTOStatus
    duration_ms: float | Unset = UNSET
    environment: str | Unset = UNSET
    finished_at: str | Unset = UNSET
    release: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        check_in_id = self.check_in_id

        id = self.id

        started_at = self.started_at

        status = self.status.value

        duration_ms = self.duration_ms

        environment = self.environment

        finished_at = self.finished_at

        release = self.release

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "checkInId": check_in_id,
                "id": id,
                "startedAt": started_at,
                "status": status,
            }
        )
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if environment is not UNSET:
            field_dict["environment"] = environment
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if release is not UNSET:
            field_dict["release"] = release
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_in_id = d.pop("checkInId")

        id = d.pop("id")

        started_at = d.pop("startedAt")

        status = MonitorCheckInDTOStatus(d.pop("status"))

        duration_ms = d.pop("durationMs", UNSET)

        environment = d.pop("environment", UNSET)

        finished_at = d.pop("finishedAt", UNSET)

        release = d.pop("release", UNSET)

        trace_id = d.pop("traceId", UNSET)

        monitor_check_in_dto = cls(
            check_in_id=check_in_id,
            id=id,
            started_at=started_at,
            status=status,
            duration_ms=duration_ms,
            environment=environment,
            finished_at=finished_at,
            release=release,
            trace_id=trace_id,
        )

        return monitor_check_in_dto
