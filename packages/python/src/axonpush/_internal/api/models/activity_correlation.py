from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityCorrelation")


@_attrs_define
class ActivityCorrelation:
    """
    Attributes:
        application_id (str | Unset):
        causation_id (str | Unset):
        connection_ref (str | Unset):
        job_id (str | Unset):
        join_attempt_id (str | Unset):
        operation_id (str | Unset):
        request_id (str | Unset):
        role_id (str | Unset):
        span_id (str | Unset):
        thread_id (str | Unset):
        trace_id (str | Unset):
    """

    application_id: str | Unset = UNSET
    causation_id: str | Unset = UNSET
    connection_ref: str | Unset = UNSET
    job_id: str | Unset = UNSET
    join_attempt_id: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    request_id: str | Unset = UNSET
    role_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        causation_id = self.causation_id

        connection_ref = self.connection_ref

        job_id = self.job_id

        join_attempt_id = self.join_attempt_id

        operation_id = self.operation_id

        request_id = self.request_id

        role_id = self.role_id

        span_id = self.span_id

        thread_id = self.thread_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if causation_id is not UNSET:
            field_dict["causation_id"] = causation_id
        if connection_ref is not UNSET:
            field_dict["connection_ref"] = connection_ref
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if join_attempt_id is not UNSET:
            field_dict["join_attempt_id"] = join_attempt_id
        if operation_id is not UNSET:
            field_dict["operation_id"] = operation_id
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_id = d.pop("application_id", UNSET)

        causation_id = d.pop("causation_id", UNSET)

        connection_ref = d.pop("connection_ref", UNSET)

        job_id = d.pop("job_id", UNSET)

        join_attempt_id = d.pop("join_attempt_id", UNSET)

        operation_id = d.pop("operation_id", UNSET)

        request_id = d.pop("request_id", UNSET)

        role_id = d.pop("role_id", UNSET)

        span_id = d.pop("span_id", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        activity_correlation = cls(
            application_id=application_id,
            causation_id=causation_id,
            connection_ref=connection_ref,
            job_id=job_id,
            join_attempt_id=join_attempt_id,
            operation_id=operation_id,
            request_id=request_id,
            role_id=role_id,
            span_id=span_id,
            thread_id=thread_id,
            trace_id=trace_id,
        )

        return activity_correlation
