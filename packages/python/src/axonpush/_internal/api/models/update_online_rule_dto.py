from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.online_rule_filters_dto import OnlineRuleFiltersDto


T = TypeVar("T", bound="UpdateOnlineRuleDto")


@_attrs_define
class UpdateOnlineRuleDto:
    """
    Attributes:
        assessment_name (str | Unset):
        daily_budget (float | Unset):
        enabled (bool | Unset):
        evaluator_id (str | Unset):
        evaluator_version (float | Unset):
        filters (OnlineRuleFiltersDto | Unset):
        name (str | Unset):
        per_org_concurrency (float | Unset):
        sample_rate (float | Unset):
        timeout_ms (float | Unset):
    """

    assessment_name: str | Unset = UNSET
    daily_budget: float | Unset = UNSET
    enabled: bool | Unset = UNSET
    evaluator_id: str | Unset = UNSET
    evaluator_version: float | Unset = UNSET
    filters: OnlineRuleFiltersDto | Unset = UNSET
    name: str | Unset = UNSET
    per_org_concurrency: float | Unset = UNSET
    sample_rate: float | Unset = UNSET
    timeout_ms: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.online_rule_filters_dto import OnlineRuleFiltersDto

        assessment_name = self.assessment_name

        daily_budget = self.daily_budget

        enabled = self.enabled

        evaluator_id = self.evaluator_id

        evaluator_version = self.evaluator_version

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        name = self.name

        per_org_concurrency = self.per_org_concurrency

        sample_rate = self.sample_rate

        timeout_ms = self.timeout_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assessment_name is not UNSET:
            field_dict["assessmentName"] = assessment_name
        if daily_budget is not UNSET:
            field_dict["dailyBudget"] = daily_budget
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if evaluator_id is not UNSET:
            field_dict["evaluatorId"] = evaluator_id
        if evaluator_version is not UNSET:
            field_dict["evaluatorVersion"] = evaluator_version
        if filters is not UNSET:
            field_dict["filters"] = filters
        if name is not UNSET:
            field_dict["name"] = name
        if per_org_concurrency is not UNSET:
            field_dict["perOrgConcurrency"] = per_org_concurrency
        if sample_rate is not UNSET:
            field_dict["sampleRate"] = sample_rate
        if timeout_ms is not UNSET:
            field_dict["timeoutMs"] = timeout_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.online_rule_filters_dto import OnlineRuleFiltersDto

        d = dict(src_dict)
        assessment_name = d.pop("assessmentName", UNSET)

        daily_budget = d.pop("dailyBudget", UNSET)

        enabled = d.pop("enabled", UNSET)

        evaluator_id = d.pop("evaluatorId", UNSET)

        evaluator_version = d.pop("evaluatorVersion", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: OnlineRuleFiltersDto | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = OnlineRuleFiltersDto.from_dict(_filters)

        name = d.pop("name", UNSET)

        per_org_concurrency = d.pop("perOrgConcurrency", UNSET)

        sample_rate = d.pop("sampleRate", UNSET)

        timeout_ms = d.pop("timeoutMs", UNSET)

        update_online_rule_dto = cls(
            assessment_name=assessment_name,
            daily_budget=daily_budget,
            enabled=enabled,
            evaluator_id=evaluator_id,
            evaluator_version=evaluator_version,
            filters=filters,
            name=name,
            per_org_concurrency=per_org_concurrency,
            sample_rate=sample_rate,
            timeout_ms=timeout_ms,
        )

        update_online_rule_dto.additional_properties = d
        return update_online_rule_dto

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
