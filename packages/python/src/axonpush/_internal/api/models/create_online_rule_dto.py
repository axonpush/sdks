from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.online_rule_filters_dto import OnlineRuleFiltersDto


T = TypeVar("T", bound="CreateOnlineRuleDto")


@_attrs_define
class CreateOnlineRuleDto:
    """
    Attributes:
        evaluator_id (str):
        evaluator_version (float):
        name (str):
        assessment_name (str | Unset):
        daily_budget (float | Unset):  Default: 1000.0.
        enabled (bool | Unset):  Default: True.
        filters (OnlineRuleFiltersDto | Unset):
        per_org_concurrency (float | Unset):  Default: 4.0.
        sample_rate (float | Unset):  Default: 1.0.
        timeout_ms (float | Unset):  Default: 15000.0.
    """

    evaluator_id: str
    evaluator_version: float
    name: str
    assessment_name: str | Unset = UNSET
    daily_budget: float | Unset = 1000.0
    enabled: bool | Unset = True
    filters: OnlineRuleFiltersDto | Unset = UNSET
    per_org_concurrency: float | Unset = 4.0
    sample_rate: float | Unset = 1.0
    timeout_ms: float | Unset = 15000.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.online_rule_filters_dto import OnlineRuleFiltersDto

        evaluator_id = self.evaluator_id

        evaluator_version = self.evaluator_version

        name = self.name

        assessment_name = self.assessment_name

        daily_budget = self.daily_budget

        enabled = self.enabled

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        per_org_concurrency = self.per_org_concurrency

        sample_rate = self.sample_rate

        timeout_ms = self.timeout_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "evaluatorId": evaluator_id,
                "evaluatorVersion": evaluator_version,
                "name": name,
            }
        )
        if assessment_name is not UNSET:
            field_dict["assessmentName"] = assessment_name
        if daily_budget is not UNSET:
            field_dict["dailyBudget"] = daily_budget
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filters is not UNSET:
            field_dict["filters"] = filters
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
        evaluator_id = d.pop("evaluatorId")

        evaluator_version = d.pop("evaluatorVersion")

        name = d.pop("name")

        assessment_name = d.pop("assessmentName", UNSET)

        daily_budget = d.pop("dailyBudget", UNSET)

        enabled = d.pop("enabled", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: OnlineRuleFiltersDto | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = OnlineRuleFiltersDto.from_dict(_filters)

        per_org_concurrency = d.pop("perOrgConcurrency", UNSET)

        sample_rate = d.pop("sampleRate", UNSET)

        timeout_ms = d.pop("timeoutMs", UNSET)

        create_online_rule_dto = cls(
            evaluator_id=evaluator_id,
            evaluator_version=evaluator_version,
            name=name,
            assessment_name=assessment_name,
            daily_budget=daily_budget,
            enabled=enabled,
            filters=filters,
            per_org_concurrency=per_org_concurrency,
            sample_rate=sample_rate,
            timeout_ms=timeout_ms,
        )

        create_online_rule_dto.additional_properties = d
        return create_online_rule_dto

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
