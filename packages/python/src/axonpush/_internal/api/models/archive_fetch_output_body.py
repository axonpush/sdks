from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.archive_fetch_output_body_state import ArchiveFetchOutputBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveFetchOutputBody")


@_attrs_define
class ArchiveFetchOutputBody:
    """
    Attributes:
        job_id (str): Poll GET /archive-fetches/{jobId}
        segments (int): Archive parts the trace spans
        state (ArchiveFetchOutputBodyState):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    job_id: str
    segments: int
    state: ArchiveFetchOutputBodyState
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        segments = self.segments

        state = self.state.value

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobId": job_id,
                "segments": segments,
                "state": state,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId")

        segments = d.pop("segments")

        state = ArchiveFetchOutputBodyState(d.pop("state"))

        schema = d.pop("$schema", UNSET)

        archive_fetch_output_body = cls(
            job_id=job_id,
            segments=segments,
            state=state,
            schema=schema,
        )

        return archive_fetch_output_body
