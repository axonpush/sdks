from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.fetch_status_output_body_state import FetchStatusOutputBodyState
from ..types import UNSET, Unset


T = TypeVar("T", bound="FetchStatusOutputBody")


@_attrs_define
class FetchStatusOutputBody:
    """
    Attributes:
        job_id (str):
        retry_after_ms (int): Suggested poll delay; 0 once finished
        segments (int):
        segments_done (int):
        state (FetchStatusOutputBodyState): gone means the history was erased or has expired
        schema (str | Unset): A URL to the JSON Schema for this object.
        error (str | Unset): Why a failed fetch failed
    """

    job_id: str
    retry_after_ms: int
    segments: int
    segments_done: int
    state: FetchStatusOutputBodyState
    schema: str | Unset = UNSET
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        retry_after_ms = self.retry_after_ms

        segments = self.segments

        segments_done = self.segments_done

        state = self.state.value

        schema = self.schema

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobId": job_id,
                "retryAfterMs": retry_after_ms,
                "segments": segments,
                "segmentsDone": segments_done,
                "state": state,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        retry_after_ms = d.pop("retryAfterMs")

        segments = d.pop("segments")

        segments_done = d.pop("segmentsDone")

        state = FetchStatusOutputBodyState(d.pop("state"))

        schema = d.pop("$schema", UNSET)

        error = d.pop("error", UNSET)

        fetch_status_output_body = cls(
            job_id=job_id,
            retry_after_ms=retry_after_ms,
            segments=segments,
            segments_done=segments_done,
            state=state,
            schema=schema,
            error=error,
        )

        return fetch_status_output_body
