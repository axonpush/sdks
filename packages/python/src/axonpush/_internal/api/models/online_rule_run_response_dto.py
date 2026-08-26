from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.online_rule_run_status import OnlineRuleRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineRuleRunResponseDto")


@_attrs_define
class OnlineRuleRunResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        evaluator_version (float):
        org_id (str):
        rule_id (str):
        run_id (str):
        status (OnlineRuleRunStatus):
        trace_id (str):
        trace_revision (str):
        updated_at (datetime.datetime):
        assessment_id (str | Unset):
        completed_at (datetime.datetime | Unset):
        cost_usd (float | Unset):
        error (str | Unset):
        model (str | Unset):
        passed (bool | Unset):
        provider (str | Unset):
        reason (str | Unset):
        score (float | Unset):
        total_tokens (float | Unset):
    """

    created_at: datetime.datetime
    evaluator_version: float
    org_id: str
    rule_id: str
    run_id: str
    status: OnlineRuleRunStatus
    trace_id: str
    trace_revision: str
    updated_at: datetime.datetime
    assessment_id: str | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    cost_usd: float | Unset = UNSET
    error: str | Unset = UNSET
    model: str | Unset = UNSET
    passed: bool | Unset = UNSET
    provider: str | Unset = UNSET
    reason: str | Unset = UNSET
    score: float | Unset = UNSET
    total_tokens: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        evaluator_version = self.evaluator_version

        org_id = self.org_id

        rule_id = self.rule_id

        run_id = self.run_id

        status = self.status.value

        trace_id = self.trace_id

        trace_revision = self.trace_revision

        updated_at = self.updated_at.isoformat()

        assessment_id = self.assessment_id

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        cost_usd = self.cost_usd

        error = self.error

        model = self.model

        passed = self.passed

        provider = self.provider

        reason = self.reason

        score = self.score

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "evaluatorVersion": evaluator_version,
                "orgId": org_id,
                "ruleId": rule_id,
                "runId": run_id,
                "status": status,
                "traceId": trace_id,
                "traceRevision": trace_revision,
                "updatedAt": updated_at,
            }
        )
        if assessment_id is not UNSET:
            field_dict["assessmentId"] = assessment_id
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if error is not UNSET:
            field_dict["error"] = error
        if model is not UNSET:
            field_dict["model"] = model
        if passed is not UNSET:
            field_dict["passed"] = passed
        if provider is not UNSET:
            field_dict["provider"] = provider
        if reason is not UNSET:
            field_dict["reason"] = reason
        if score is not UNSET:
            field_dict["score"] = score
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        evaluator_version = d.pop("evaluatorVersion")

        org_id = d.pop("orgId")

        rule_id = d.pop("ruleId")

        run_id = d.pop("runId")

        status = OnlineRuleRunStatus(d.pop("status"))

        trace_id = d.pop("traceId")

        trace_revision = d.pop("traceRevision")

        updated_at = isoparse(d.pop("updatedAt"))

        assessment_id = d.pop("assessmentId", UNSET)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        cost_usd = d.pop("costUsd", UNSET)

        error = d.pop("error", UNSET)

        model = d.pop("model", UNSET)

        passed = d.pop("passed", UNSET)

        provider = d.pop("provider", UNSET)

        reason = d.pop("reason", UNSET)

        score = d.pop("score", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        online_rule_run_response_dto = cls(
            created_at=created_at,
            evaluator_version=evaluator_version,
            org_id=org_id,
            rule_id=rule_id,
            run_id=run_id,
            status=status,
            trace_id=trace_id,
            trace_revision=trace_revision,
            updated_at=updated_at,
            assessment_id=assessment_id,
            completed_at=completed_at,
            cost_usd=cost_usd,
            error=error,
            model=model,
            passed=passed,
            provider=provider,
            reason=reason,
            score=score,
            total_tokens=total_tokens,
        )

        online_rule_run_response_dto.additional_properties = d
        return online_rule_run_response_dto

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
