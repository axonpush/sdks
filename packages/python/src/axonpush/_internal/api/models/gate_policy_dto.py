from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.gate_policy_scope import GatePolicyScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatePolicyDto")


@_attrs_define
class GatePolicyDto:
    """
    Attributes:
        created_at (datetime.datetime):
        enabled (bool):
        org_id (str):
        scope_id (str):
        scope_type (GatePolicyScope):
        updated_at (datetime.datetime):
        created_by (str | Unset):
        description (str | Unset):
        max_cost_increase_percent (float | Unset): Maximum cost increase against the baseline, in percent.
        max_cost_usd (float | Unset): Maximum total run cost in USD.
        max_failure_rate (float | Unset): Maximum share of dataset items allowed to error, 0-1.
        max_latency_increase_percent (float | Unset): Maximum latency increase against the baseline, in percent.
        max_latency_ms (float | Unset): Maximum mean latency in milliseconds.
        min_score (float | Unset): Minimum absolute score the candidate must reach.
        min_score_delta (float | Unset): Smallest score change against the baseline that still passes. Usually negative.
        name (str | Unset):
    """

    created_at: datetime.datetime
    enabled: bool
    org_id: str
    scope_id: str
    scope_type: GatePolicyScope
    updated_at: datetime.datetime
    created_by: str | Unset = UNSET
    description: str | Unset = UNSET
    max_cost_increase_percent: float | Unset = UNSET
    max_cost_usd: float | Unset = UNSET
    max_failure_rate: float | Unset = UNSET
    max_latency_increase_percent: float | Unset = UNSET
    max_latency_ms: float | Unset = UNSET
    min_score: float | Unset = UNSET
    min_score_delta: float | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        enabled = self.enabled

        org_id = self.org_id

        scope_id = self.scope_id

        scope_type = self.scope_type.value

        updated_at = self.updated_at.isoformat()

        created_by = self.created_by

        description = self.description

        max_cost_increase_percent = self.max_cost_increase_percent

        max_cost_usd = self.max_cost_usd

        max_failure_rate = self.max_failure_rate

        max_latency_increase_percent = self.max_latency_increase_percent

        max_latency_ms = self.max_latency_ms

        min_score = self.min_score

        min_score_delta = self.min_score_delta

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "enabled": enabled,
                "orgId": org_id,
                "scopeId": scope_id,
                "scopeType": scope_type,
                "updatedAt": updated_at,
            }
        )
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if max_cost_increase_percent is not UNSET:
            field_dict["maxCostIncreasePercent"] = max_cost_increase_percent
        if max_cost_usd is not UNSET:
            field_dict["maxCostUsd"] = max_cost_usd
        if max_failure_rate is not UNSET:
            field_dict["maxFailureRate"] = max_failure_rate
        if max_latency_increase_percent is not UNSET:
            field_dict["maxLatencyIncreasePercent"] = max_latency_increase_percent
        if max_latency_ms is not UNSET:
            field_dict["maxLatencyMs"] = max_latency_ms
        if min_score is not UNSET:
            field_dict["minScore"] = min_score
        if min_score_delta is not UNSET:
            field_dict["minScoreDelta"] = min_score_delta
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        enabled = d.pop("enabled")

        org_id = d.pop("orgId")

        scope_id = d.pop("scopeId")

        scope_type = GatePolicyScope(d.pop("scopeType"))

        updated_at = isoparse(d.pop("updatedAt"))

        created_by = d.pop("createdBy", UNSET)

        description = d.pop("description", UNSET)

        max_cost_increase_percent = d.pop("maxCostIncreasePercent", UNSET)

        max_cost_usd = d.pop("maxCostUsd", UNSET)

        max_failure_rate = d.pop("maxFailureRate", UNSET)

        max_latency_increase_percent = d.pop("maxLatencyIncreasePercent", UNSET)

        max_latency_ms = d.pop("maxLatencyMs", UNSET)

        min_score = d.pop("minScore", UNSET)

        min_score_delta = d.pop("minScoreDelta", UNSET)

        name = d.pop("name", UNSET)

        gate_policy_dto = cls(
            created_at=created_at,
            enabled=enabled,
            org_id=org_id,
            scope_id=scope_id,
            scope_type=scope_type,
            updated_at=updated_at,
            created_by=created_by,
            description=description,
            max_cost_increase_percent=max_cost_increase_percent,
            max_cost_usd=max_cost_usd,
            max_failure_rate=max_failure_rate,
            max_latency_increase_percent=max_latency_increase_percent,
            max_latency_ms=max_latency_ms,
            min_score=min_score,
            min_score_delta=min_score_delta,
            name=name,
        )

        gate_policy_dto.additional_properties = d
        return gate_policy_dto

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
