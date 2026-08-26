from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_intelligence_scope import TraceIntelligenceScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_provider_dto import TraceIntelligenceProviderDto


T = TypeVar("T", bound="UpdateTraceIntelligenceSettingsDto")


@_attrs_define
class UpdateTraceIntelligenceSettingsDto:
    """
    Attributes:
        content_consent (bool | Unset): Explicitly consent to sending captured content
        daily_trace_limit (float | Unset):  Default: 1000.0.
        enabled (bool | Unset):
        provider (TraceIntelligenceProviderDto | Unset):
        retention_days (float | Unset):  Default: 30.0.
        sampling_rate (float | Unset):  Default: 0.1.
        scope (TraceIntelligenceScope | Unset):  Default: TraceIntelligenceScope.APP_ENVIRONMENT.
    """

    content_consent: bool | Unset = UNSET
    daily_trace_limit: float | Unset = 1000.0
    enabled: bool | Unset = UNSET
    provider: TraceIntelligenceProviderDto | Unset = UNSET
    retention_days: float | Unset = 30.0
    sampling_rate: float | Unset = 0.1
    scope: TraceIntelligenceScope | Unset = TraceIntelligenceScope.APP_ENVIRONMENT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_provider_dto import TraceIntelligenceProviderDto

        content_consent = self.content_consent

        daily_trace_limit = self.daily_trace_limit

        enabled = self.enabled

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        retention_days = self.retention_days

        sampling_rate = self.sampling_rate

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_consent is not UNSET:
            field_dict["contentConsent"] = content_consent
        if daily_trace_limit is not UNSET:
            field_dict["dailyTraceLimit"] = daily_trace_limit
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if provider is not UNSET:
            field_dict["provider"] = provider
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days
        if sampling_rate is not UNSET:
            field_dict["samplingRate"] = sampling_rate
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_provider_dto import TraceIntelligenceProviderDto

        d = dict(src_dict)
        content_consent = d.pop("contentConsent", UNSET)

        daily_trace_limit = d.pop("dailyTraceLimit", UNSET)

        enabled = d.pop("enabled", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: TraceIntelligenceProviderDto | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = TraceIntelligenceProviderDto.from_dict(_provider)

        retention_days = d.pop("retentionDays", UNSET)

        sampling_rate = d.pop("samplingRate", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: TraceIntelligenceScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = TraceIntelligenceScope(_scope)

        update_trace_intelligence_settings_dto = cls(
            content_consent=content_consent,
            daily_trace_limit=daily_trace_limit,
            enabled=enabled,
            provider=provider,
            retention_days=retention_days,
            sampling_rate=sampling_rate,
            scope=scope,
        )

        update_trace_intelligence_settings_dto.additional_properties = d
        return update_trace_intelligence_settings_dto

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
