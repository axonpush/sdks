from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_experiment_result_dto_output import LocalExperimentResultDtoOutput


T = TypeVar("T", bound="LocalExperimentResultDto")


@_attrs_define
class LocalExperimentResultDto:
    """
    Attributes:
        item_id (str):
        output (LocalExperimentResultDtoOutput):
        cost_usd (float | Unset):
        error (str | Unset):
        latency_ms (float | Unset):
        total_tokens (float | Unset):
        trace_id (str | Unset):
    """

    item_id: str
    output: LocalExperimentResultDtoOutput
    cost_usd: float | Unset = UNSET
    error: str | Unset = UNSET
    latency_ms: float | Unset = UNSET
    total_tokens: float | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.local_experiment_result_dto_output import LocalExperimentResultDtoOutput

        item_id = self.item_id

        output = self.output.to_dict()

        cost_usd = self.cost_usd

        error = self.error

        latency_ms = self.latency_ms

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemId": item_id,
                "output": output,
            }
        )
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if error is not UNSET:
            field_dict["error"] = error
        if latency_ms is not UNSET:
            field_dict["latencyMs"] = latency_ms
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.local_experiment_result_dto_output import LocalExperimentResultDtoOutput

        d = dict(src_dict)
        item_id = d.pop("itemId")

        output = LocalExperimentResultDtoOutput.from_dict(d.pop("output"))

        cost_usd = d.pop("costUsd", UNSET)

        error = d.pop("error", UNSET)

        latency_ms = d.pop("latencyMs", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        trace_id = d.pop("traceId", UNSET)

        local_experiment_result_dto = cls(
            item_id=item_id,
            output=output,
            cost_usd=cost_usd,
            error=error,
            latency_ms=latency_ms,
            total_tokens=total_tokens,
            trace_id=trace_id,
        )

        local_experiment_result_dto.additional_properties = d
        return local_experiment_result_dto

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
