from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_status import TraceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineRuleFiltersDto")


@_attrs_define
class OnlineRuleFiltersDto:
    """
    Attributes:
        app_id (str | Unset):
        environment_id (str | Unset):
        maximum_duration_ms (float | Unset):
        minimum_duration_ms (float | Unset):
        models (list[str] | Unset):
        releases (list[str] | Unset):
        semantic_kinds (list[str] | Unset):
        services (list[str] | Unset):
        status (TraceStatus | Unset):
    """

    app_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    maximum_duration_ms: float | Unset = UNSET
    minimum_duration_ms: float | Unset = UNSET
    models: list[str] | Unset = UNSET
    releases: list[str] | Unset = UNSET
    semantic_kinds: list[str] | Unset = UNSET
    services: list[str] | Unset = UNSET
    status: TraceStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        environment_id = self.environment_id

        maximum_duration_ms = self.maximum_duration_ms

        minimum_duration_ms = self.minimum_duration_ms

        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models

        releases: list[str] | Unset = UNSET
        if not isinstance(self.releases, Unset):
            releases = self.releases

        semantic_kinds: list[str] | Unset = UNSET
        if not isinstance(self.semantic_kinds, Unset):
            semantic_kinds = self.semantic_kinds

        services: list[str] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if maximum_duration_ms is not UNSET:
            field_dict["maximumDurationMs"] = maximum_duration_ms
        if minimum_duration_ms is not UNSET:
            field_dict["minimumDurationMs"] = minimum_duration_ms
        if models is not UNSET:
            field_dict["models"] = models
        if releases is not UNSET:
            field_dict["releases"] = releases
        if semantic_kinds is not UNSET:
            field_dict["semanticKinds"] = semantic_kinds
        if services is not UNSET:
            field_dict["services"] = services
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        maximum_duration_ms = d.pop("maximumDurationMs", UNSET)

        minimum_duration_ms = d.pop("minimumDurationMs", UNSET)

        models = cast(list[str], d.pop("models", UNSET))

        releases = cast(list[str], d.pop("releases", UNSET))

        semantic_kinds = cast(list[str], d.pop("semanticKinds", UNSET))

        services = cast(list[str], d.pop("services", UNSET))

        _status = d.pop("status", UNSET)
        status: TraceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TraceStatus(_status)

        online_rule_filters_dto = cls(
            app_id=app_id,
            environment_id=environment_id,
            maximum_duration_ms=maximum_duration_ms,
            minimum_duration_ms=minimum_duration_ms,
            models=models,
            releases=releases,
            semantic_kinds=semantic_kinds,
            services=services,
            status=status,
        )

        online_rule_filters_dto.additional_properties = d
        return online_rule_filters_dto

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
