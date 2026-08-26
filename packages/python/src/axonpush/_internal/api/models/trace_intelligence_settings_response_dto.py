from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trace_intelligence_scope import TraceIntelligenceScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_provider_response_dto import (
        TraceIntelligenceProviderResponseDto,
    )


T = TypeVar("T", bound="TraceIntelligenceSettingsResponseDto")


@_attrs_define
class TraceIntelligenceSettingsResponseDto:
    """
    Attributes:
        algorithm_version (str):
        daily_trace_limit (float):
        enabled (bool):
        extraction_version (str):
        provider (TraceIntelligenceProviderResponseDto):
        retention_days (float):
        sampling_rate (float):
        scope (TraceIntelligenceScope):
        content_consent_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    algorithm_version: str
    daily_trace_limit: float
    enabled: bool
    extraction_version: str
    provider: TraceIntelligenceProviderResponseDto
    retention_days: float
    sampling_rate: float
    scope: TraceIntelligenceScope
    content_consent_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_provider_response_dto import (
            TraceIntelligenceProviderResponseDto,
        )

        algorithm_version = self.algorithm_version

        daily_trace_limit = self.daily_trace_limit

        enabled = self.enabled

        extraction_version = self.extraction_version

        provider = self.provider.to_dict()

        retention_days = self.retention_days

        sampling_rate = self.sampling_rate

        scope = self.scope.value

        content_consent_at: str | Unset = UNSET
        if not isinstance(self.content_consent_at, Unset):
            content_consent_at = self.content_consent_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithmVersion": algorithm_version,
                "dailyTraceLimit": daily_trace_limit,
                "enabled": enabled,
                "extractionVersion": extraction_version,
                "provider": provider,
                "retentionDays": retention_days,
                "samplingRate": sampling_rate,
                "scope": scope,
            }
        )
        if content_consent_at is not UNSET:
            field_dict["contentConsentAt"] = content_consent_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_provider_response_dto import (
            TraceIntelligenceProviderResponseDto,
        )

        d = dict(src_dict)
        algorithm_version = d.pop("algorithmVersion")

        daily_trace_limit = d.pop("dailyTraceLimit")

        enabled = d.pop("enabled")

        extraction_version = d.pop("extractionVersion")

        provider = TraceIntelligenceProviderResponseDto.from_dict(d.pop("provider"))

        retention_days = d.pop("retentionDays")

        sampling_rate = d.pop("samplingRate")

        scope = TraceIntelligenceScope(d.pop("scope"))

        _content_consent_at = d.pop("contentConsentAt", UNSET)
        content_consent_at: datetime.datetime | Unset
        if isinstance(_content_consent_at, Unset):
            content_consent_at = UNSET
        else:
            content_consent_at = isoparse(_content_consent_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        trace_intelligence_settings_response_dto = cls(
            algorithm_version=algorithm_version,
            daily_trace_limit=daily_trace_limit,
            enabled=enabled,
            extraction_version=extraction_version,
            provider=provider,
            retention_days=retention_days,
            sampling_rate=sampling_rate,
            scope=scope,
            content_consent_at=content_consent_at,
            updated_at=updated_at,
        )

        trace_intelligence_settings_response_dto.additional_properties = d
        return trace_intelligence_settings_response_dto

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
