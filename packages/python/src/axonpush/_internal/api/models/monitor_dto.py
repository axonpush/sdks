from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_dto_status import MonitorDTOStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_check_in_summary_dto import MonitorCheckInSummaryDTO
    from ..models.monitor_schedule_dto import MonitorScheduleDTO


T = TypeVar("T", bound="MonitorDTO")


@_attrs_define
class MonitorDTO:
    """
    Attributes:
        checkin_margin_min (int):
        consecutive_failures (int):
        created_at (str):
        failure_threshold (int):
        max_runtime_min (int):
        monitor_id (str):
        muted (bool):
        recent_check_ins (list[MonitorCheckInSummaryDTO] | None): Up to the 30 newest check-ins, newest first
        recovery_threshold (int):
        schedule (MonitorScheduleDTO):
        slug (str):
        status (MonitorDTOStatus):
        updated_at (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset):
        channel_id (str | Unset):
        environment_id (str | Unset):
        last_check_in_at (str | Unset):
        last_status (str | Unset):
        next_due_at (str | Unset):
    """

    checkin_margin_min: int
    consecutive_failures: int
    created_at: str
    failure_threshold: int
    max_runtime_min: int
    monitor_id: str
    muted: bool
    recent_check_ins: list[MonitorCheckInSummaryDTO] | None
    recovery_threshold: int
    schedule: MonitorScheduleDTO
    slug: str
    status: MonitorDTOStatus
    updated_at: str
    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    last_check_in_at: str | Unset = UNSET
    last_status: str | Unset = UNSET
    next_due_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_check_in_summary_dto import MonitorCheckInSummaryDTO
        from ..models.monitor_schedule_dto import MonitorScheduleDTO

        checkin_margin_min = self.checkin_margin_min

        consecutive_failures = self.consecutive_failures

        created_at = self.created_at

        failure_threshold = self.failure_threshold

        max_runtime_min = self.max_runtime_min

        monitor_id = self.monitor_id

        muted = self.muted

        recent_check_ins: list[dict[str, Any]] | None
        if isinstance(self.recent_check_ins, list):
            recent_check_ins = []
            for recent_check_ins_type_0_item_data in self.recent_check_ins:
                recent_check_ins_type_0_item = recent_check_ins_type_0_item_data.to_dict()
                recent_check_ins.append(recent_check_ins_type_0_item)

        else:
            recent_check_ins = self.recent_check_ins

        recovery_threshold = self.recovery_threshold

        schedule = self.schedule.to_dict()

        slug = self.slug

        status = self.status.value

        updated_at = self.updated_at

        schema = self.schema

        app_id = self.app_id

        channel_id = self.channel_id

        environment_id = self.environment_id

        last_check_in_at = self.last_check_in_at

        last_status = self.last_status

        next_due_at = self.next_due_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "checkinMarginMin": checkin_margin_min,
                "consecutiveFailures": consecutive_failures,
                "createdAt": created_at,
                "failureThreshold": failure_threshold,
                "maxRuntimeMin": max_runtime_min,
                "monitorId": monitor_id,
                "muted": muted,
                "recentCheckIns": recent_check_ins,
                "recoveryThreshold": recovery_threshold,
                "schedule": schedule,
                "slug": slug,
                "status": status,
                "updatedAt": updated_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if last_check_in_at is not UNSET:
            field_dict["lastCheckInAt"] = last_check_in_at
        if last_status is not UNSET:
            field_dict["lastStatus"] = last_status
        if next_due_at is not UNSET:
            field_dict["nextDueAt"] = next_due_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_check_in_summary_dto import MonitorCheckInSummaryDTO
        from ..models.monitor_schedule_dto import MonitorScheduleDTO

        d = dict(src_dict)
        checkin_margin_min = d.pop("checkinMarginMin")

        consecutive_failures = d.pop("consecutiveFailures")

        created_at = d.pop("createdAt")

        failure_threshold = d.pop("failureThreshold")

        max_runtime_min = d.pop("maxRuntimeMin")

        monitor_id = d.pop("monitorId")

        muted = d.pop("muted")

        def _parse_recent_check_ins(data: object) -> list[MonitorCheckInSummaryDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recent_check_ins_type_0 = []
                _recent_check_ins_type_0 = data
                for recent_check_ins_type_0_item_data in _recent_check_ins_type_0:
                    recent_check_ins_type_0_item = MonitorCheckInSummaryDTO.from_dict(
                        recent_check_ins_type_0_item_data
                    )

                    recent_check_ins_type_0.append(recent_check_ins_type_0_item)

                return recent_check_ins_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorCheckInSummaryDTO] | None, data)

        recent_check_ins = _parse_recent_check_ins(d.pop("recentCheckIns"))

        recovery_threshold = d.pop("recoveryThreshold")

        schedule = MonitorScheduleDTO.from_dict(d.pop("schedule"))

        slug = d.pop("slug")

        status = MonitorDTOStatus(d.pop("status"))

        updated_at = d.pop("updatedAt")

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        channel_id = d.pop("channelId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        last_check_in_at = d.pop("lastCheckInAt", UNSET)

        last_status = d.pop("lastStatus", UNSET)

        next_due_at = d.pop("nextDueAt", UNSET)

        monitor_dto = cls(
            checkin_margin_min=checkin_margin_min,
            consecutive_failures=consecutive_failures,
            created_at=created_at,
            failure_threshold=failure_threshold,
            max_runtime_min=max_runtime_min,
            monitor_id=monitor_id,
            muted=muted,
            recent_check_ins=recent_check_ins,
            recovery_threshold=recovery_threshold,
            schedule=schedule,
            slug=slug,
            status=status,
            updated_at=updated_at,
            schema=schema,
            app_id=app_id,
            channel_id=channel_id,
            environment_id=environment_id,
            last_check_in_at=last_check_in_at,
            last_status=last_status,
            next_due_at=next_due_at,
        )

        return monitor_dto
