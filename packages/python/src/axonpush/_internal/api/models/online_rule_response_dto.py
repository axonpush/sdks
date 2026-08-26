from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.online_rule_filters_dto import OnlineRuleFiltersDto


T = TypeVar("T", bound="OnlineRuleResponseDto")


@_attrs_define
class OnlineRuleResponseDto:
    """
    Attributes:
        assessment_name (str):
        created_at (datetime.datetime):
        daily_budget (float):
        enabled (bool):
        evaluator_id (str):
        evaluator_version (float):
        filters (OnlineRuleFiltersDto):
        name (str):
        org_id (str):
        per_org_concurrency (float):
        rule_id (str):
        sample_rate (float):
        timeout_ms (float):
        updated_at (datetime.datetime):
        created_by (str | Unset):
    """

    assessment_name: str
    created_at: datetime.datetime
    daily_budget: float
    enabled: bool
    evaluator_id: str
    evaluator_version: float
    filters: OnlineRuleFiltersDto
    name: str
    org_id: str
    per_org_concurrency: float
    rule_id: str
    sample_rate: float
    timeout_ms: float
    updated_at: datetime.datetime
    created_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.online_rule_filters_dto import OnlineRuleFiltersDto

        assessment_name = self.assessment_name

        created_at = self.created_at.isoformat()

        daily_budget = self.daily_budget

        enabled = self.enabled

        evaluator_id = self.evaluator_id

        evaluator_version = self.evaluator_version

        filters = self.filters.to_dict()

        name = self.name

        org_id = self.org_id

        per_org_concurrency = self.per_org_concurrency

        rule_id = self.rule_id

        sample_rate = self.sample_rate

        timeout_ms = self.timeout_ms

        updated_at = self.updated_at.isoformat()

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessmentName": assessment_name,
                "createdAt": created_at,
                "dailyBudget": daily_budget,
                "enabled": enabled,
                "evaluatorId": evaluator_id,
                "evaluatorVersion": evaluator_version,
                "filters": filters,
                "name": name,
                "orgId": org_id,
                "perOrgConcurrency": per_org_concurrency,
                "ruleId": rule_id,
                "sampleRate": sample_rate,
                "timeoutMs": timeout_ms,
                "updatedAt": updated_at,
            }
        )
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.online_rule_filters_dto import OnlineRuleFiltersDto

        d = dict(src_dict)
        assessment_name = d.pop("assessmentName")

        created_at = isoparse(d.pop("createdAt"))

        daily_budget = d.pop("dailyBudget")

        enabled = d.pop("enabled")

        evaluator_id = d.pop("evaluatorId")

        evaluator_version = d.pop("evaluatorVersion")

        filters = OnlineRuleFiltersDto.from_dict(d.pop("filters"))

        name = d.pop("name")

        org_id = d.pop("orgId")

        per_org_concurrency = d.pop("perOrgConcurrency")

        rule_id = d.pop("ruleId")

        sample_rate = d.pop("sampleRate")

        timeout_ms = d.pop("timeoutMs")

        updated_at = isoparse(d.pop("updatedAt"))

        created_by = d.pop("createdBy", UNSET)

        online_rule_response_dto = cls(
            assessment_name=assessment_name,
            created_at=created_at,
            daily_budget=daily_budget,
            enabled=enabled,
            evaluator_id=evaluator_id,
            evaluator_version=evaluator_version,
            filters=filters,
            name=name,
            org_id=org_id,
            per_org_concurrency=per_org_concurrency,
            rule_id=rule_id,
            sample_rate=sample_rate,
            timeout_ms=timeout_ms,
            updated_at=updated_at,
            created_by=created_by,
        )

        online_rule_response_dto.additional_properties = d
        return online_rule_response_dto

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
