from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.signals_status import SignalsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_signals_payload_response_dto import (
        TraceIntelligenceSignalsPayloadResponseDto,
    )


T = TypeVar("T", bound="TraceIntelligenceSignalsResponseDto")


@_attrs_define
class TraceIntelligenceSignalsResponseDto:
    """
    Attributes:
        analyzed_at (datetime.datetime):
        extraction_version (str):
        status (SignalsStatus):
        trace_id (str):
        trace_revision (str):
        failure_reason (str | Unset):
        signals (TraceIntelligenceSignalsPayloadResponseDto | Unset):
        skip_reason (str | Unset):
    """

    analyzed_at: datetime.datetime
    extraction_version: str
    status: SignalsStatus
    trace_id: str
    trace_revision: str
    failure_reason: str | Unset = UNSET
    signals: TraceIntelligenceSignalsPayloadResponseDto | Unset = UNSET
    skip_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_signals_payload_response_dto import (
            TraceIntelligenceSignalsPayloadResponseDto,
        )

        analyzed_at = self.analyzed_at.isoformat()

        extraction_version = self.extraction_version

        status = self.status.value

        trace_id = self.trace_id

        trace_revision = self.trace_revision

        failure_reason = self.failure_reason

        signals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signals, Unset):
            signals = self.signals.to_dict()

        skip_reason = self.skip_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analyzedAt": analyzed_at,
                "extractionVersion": extraction_version,
                "status": status,
                "traceId": trace_id,
                "traceRevision": trace_revision,
            }
        )
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if signals is not UNSET:
            field_dict["signals"] = signals
        if skip_reason is not UNSET:
            field_dict["skipReason"] = skip_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_signals_payload_response_dto import (
            TraceIntelligenceSignalsPayloadResponseDto,
        )

        d = dict(src_dict)
        analyzed_at = isoparse(d.pop("analyzedAt"))

        extraction_version = d.pop("extractionVersion")

        status = SignalsStatus(d.pop("status"))

        trace_id = d.pop("traceId")

        trace_revision = d.pop("traceRevision")

        failure_reason = d.pop("failureReason", UNSET)

        _signals = d.pop("signals", UNSET)
        signals: TraceIntelligenceSignalsPayloadResponseDto | Unset
        if isinstance(_signals, Unset):
            signals = UNSET
        else:
            signals = TraceIntelligenceSignalsPayloadResponseDto.from_dict(_signals)

        skip_reason = d.pop("skipReason", UNSET)

        trace_intelligence_signals_response_dto = cls(
            analyzed_at=analyzed_at,
            extraction_version=extraction_version,
            status=status,
            trace_id=trace_id,
            trace_revision=trace_revision,
            failure_reason=failure_reason,
            signals=signals,
            skip_reason=skip_reason,
        )

        trace_intelligence_signals_response_dto.additional_properties = d
        return trace_intelligence_signals_response_dto

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
