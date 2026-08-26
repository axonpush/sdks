from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceSnapshotResponseDto")


@_attrs_define
class TraceIntelligenceSnapshotResponseDto:
    """
    Attributes:
        analyzed_through (datetime.datetime):
        created_at (datetime.datetime):
        snapshot_id (str):
        source_trace_count (float):
    """

    analyzed_through: datetime.datetime
    created_at: datetime.datetime
    snapshot_id: str
    source_trace_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analyzed_through = self.analyzed_through.isoformat()

        created_at = self.created_at.isoformat()

        snapshot_id = self.snapshot_id

        source_trace_count = self.source_trace_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analyzedThrough": analyzed_through,
                "createdAt": created_at,
                "snapshotId": snapshot_id,
                "sourceTraceCount": source_trace_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        analyzed_through = isoparse(d.pop("analyzedThrough"))

        created_at = isoparse(d.pop("createdAt"))

        snapshot_id = d.pop("snapshotId")

        source_trace_count = d.pop("sourceTraceCount")

        trace_intelligence_snapshot_response_dto = cls(
            analyzed_through=analyzed_through,
            created_at=created_at,
            snapshot_id=snapshot_id,
            source_trace_count=source_trace_count,
        )

        trace_intelligence_snapshot_response_dto.additional_properties = d
        return trace_intelligence_snapshot_response_dto

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
