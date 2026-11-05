from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_job import LedgerJob


T = TypeVar("T", bound="ListJobsOutputBody")


@_attrs_define
class ListJobsOutputBody:
    """
    Attributes:
        jobs (list[LedgerJob] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_cursor (str | Unset):
    """

    jobs: list[LedgerJob] | None
    schema: str | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.ledger_job import LedgerJob

        jobs: list[dict[str, Any]] | None
        if isinstance(self.jobs, list):
            jobs = []
            for jobs_type_0_item_data in self.jobs:
                jobs_type_0_item = jobs_type_0_item_data.to_dict()
                jobs.append(jobs_type_0_item)

        else:
            jobs = self.jobs

        schema = self.schema

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobs": jobs,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_job import LedgerJob

        d = dict(src_dict)

        def _parse_jobs(data: object) -> list[LedgerJob] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                jobs_type_0 = []
                _jobs_type_0 = data
                for jobs_type_0_item_data in _jobs_type_0:
                    jobs_type_0_item = LedgerJob.from_dict(jobs_type_0_item_data)

                    jobs_type_0.append(jobs_type_0_item)

                return jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LedgerJob] | None, data)

        jobs = _parse_jobs(d.pop("jobs"))

        schema = d.pop("$schema", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        list_jobs_output_body = cls(
            jobs=jobs,
            schema=schema,
            next_cursor=next_cursor,
        )

        return list_jobs_output_body
