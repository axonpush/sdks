from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.experiment_result_status import ExperimentResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_result_dto_evaluator_results import ExperimentResultDtoEvaluatorResults
    from ..models.experiment_result_dto_output import ExperimentResultDtoOutput


T = TypeVar("T", bound="ExperimentResultDto")


@_attrs_define
class ExperimentResultDto:
    """
    Attributes:
        attempts (float):
        created_at (datetime.datetime):
        item_id (str):
        output (ExperimentResultDtoOutput):
        status (ExperimentResultStatus):
        updated_at (datetime.datetime):
        cost_usd (float | Unset):
        error (str | Unset):
        evaluator_results (ExperimentResultDtoEvaluatorResults | Unset):
        explanation (str | Unset):
        latency_ms (float | Unset):
        score (float | Unset):
        total_tokens (float | Unset):
        trace_id (str | Unset):
    """

    attempts: float
    created_at: datetime.datetime
    item_id: str
    output: ExperimentResultDtoOutput
    status: ExperimentResultStatus
    updated_at: datetime.datetime
    cost_usd: float | Unset = UNSET
    error: str | Unset = UNSET
    evaluator_results: ExperimentResultDtoEvaluatorResults | Unset = UNSET
    explanation: str | Unset = UNSET
    latency_ms: float | Unset = UNSET
    score: float | Unset = UNSET
    total_tokens: float | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_result_dto_evaluator_results import (
            ExperimentResultDtoEvaluatorResults,
        )
        from ..models.experiment_result_dto_output import ExperimentResultDtoOutput

        attempts = self.attempts

        created_at = self.created_at.isoformat()

        item_id = self.item_id

        output = self.output.to_dict()

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        cost_usd = self.cost_usd

        error = self.error

        evaluator_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.evaluator_results, Unset):
            evaluator_results = self.evaluator_results.to_dict()

        explanation = self.explanation

        latency_ms = self.latency_ms

        score = self.score

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "createdAt": created_at,
                "itemId": item_id,
                "output": output,
                "status": status,
                "updatedAt": updated_at,
            }
        )
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if error is not UNSET:
            field_dict["error"] = error
        if evaluator_results is not UNSET:
            field_dict["evaluatorResults"] = evaluator_results
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if latency_ms is not UNSET:
            field_dict["latencyMs"] = latency_ms
        if score is not UNSET:
            field_dict["score"] = score
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_result_dto_evaluator_results import (
            ExperimentResultDtoEvaluatorResults,
        )
        from ..models.experiment_result_dto_output import ExperimentResultDtoOutput

        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = isoparse(d.pop("createdAt"))

        item_id = d.pop("itemId")

        output = ExperimentResultDtoOutput.from_dict(d.pop("output"))

        status = ExperimentResultStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updatedAt"))

        cost_usd = d.pop("costUsd", UNSET)

        error = d.pop("error", UNSET)

        _evaluator_results = d.pop("evaluatorResults", UNSET)
        evaluator_results: ExperimentResultDtoEvaluatorResults | Unset
        if isinstance(_evaluator_results, Unset):
            evaluator_results = UNSET
        else:
            evaluator_results = ExperimentResultDtoEvaluatorResults.from_dict(_evaluator_results)

        explanation = d.pop("explanation", UNSET)

        latency_ms = d.pop("latencyMs", UNSET)

        score = d.pop("score", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        trace_id = d.pop("traceId", UNSET)

        experiment_result_dto = cls(
            attempts=attempts,
            created_at=created_at,
            item_id=item_id,
            output=output,
            status=status,
            updated_at=updated_at,
            cost_usd=cost_usd,
            error=error,
            evaluator_results=evaluator_results,
            explanation=explanation,
            latency_ms=latency_ms,
            score=score,
            total_tokens=total_tokens,
            trace_id=trace_id,
        )

        experiment_result_dto.additional_properties = d
        return experiment_result_dto

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
