from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backfill_status import BackfillStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceBackfillResponseDto")


@_attrs_define
class TraceIntelligenceBackfillResponseDto:
    """
    Attributes:
        app_id (str):
        created_at (datetime.datetime):
        environment_id (str):
        failed_count (float):
        from_ (datetime.datetime):
        job_id (str):
        max_traces (float):
        processed_count (float):
        queued_count (float):
        status (BackfillStatus):
        to (datetime.datetime):
        updated_at (datetime.datetime):
        completed_at (datetime.datetime | Unset):
        error (str | Unset):
    """

    app_id: str
    created_at: datetime.datetime
    environment_id: str
    failed_count: float
    from_: datetime.datetime
    job_id: str
    max_traces: float
    processed_count: float
    queued_count: float
    status: BackfillStatus
    to: datetime.datetime
    updated_at: datetime.datetime
    completed_at: datetime.datetime | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        created_at = self.created_at.isoformat()

        environment_id = self.environment_id

        failed_count = self.failed_count

        from_ = self.from_.isoformat()

        job_id = self.job_id

        max_traces = self.max_traces

        processed_count = self.processed_count

        queued_count = self.queued_count

        status = self.status.value

        to = self.to.isoformat()

        updated_at = self.updated_at.isoformat()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "createdAt": created_at,
                "environmentId": environment_id,
                "failedCount": failed_count,
                "from": from_,
                "jobId": job_id,
                "maxTraces": max_traces,
                "processedCount": processed_count,
                "queuedCount": queued_count,
                "status": status,
                "to": to,
                "updatedAt": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId")

        created_at = isoparse(d.pop("createdAt"))

        environment_id = d.pop("environmentId")

        failed_count = d.pop("failedCount")

        from_ = isoparse(d.pop("from"))

        job_id = d.pop("jobId")

        max_traces = d.pop("maxTraces")

        processed_count = d.pop("processedCount")

        queued_count = d.pop("queuedCount")

        status = BackfillStatus(d.pop("status"))

        to = isoparse(d.pop("to"))

        updated_at = isoparse(d.pop("updatedAt"))

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        error = d.pop("error", UNSET)

        trace_intelligence_backfill_response_dto = cls(
            app_id=app_id,
            created_at=created_at,
            environment_id=environment_id,
            failed_count=failed_count,
            from_=from_,
            job_id=job_id,
            max_traces=max_traces,
            processed_count=processed_count,
            queued_count=queued_count,
            status=status,
            to=to,
            updated_at=updated_at,
            completed_at=completed_at,
            error=error,
        )

        trace_intelligence_backfill_response_dto.additional_properties = d
        return trace_intelligence_backfill_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
