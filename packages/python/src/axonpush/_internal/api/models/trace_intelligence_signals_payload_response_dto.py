from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_signal_value_response_dto import (
        TraceIntelligenceSignalValueResponseDto,
    )


T = TypeVar("T", bound="TraceIntelligenceSignalsPayloadResponseDto")


@_attrs_define
class TraceIntelligenceSignalsPayloadResponseDto:
    """
    Attributes:
        behavior (TraceIntelligenceSignalValueResponseDto):
        goal (TraceIntelligenceSignalValueResponseDto):
        outcome (TraceIntelligenceSignalValueResponseDto):
        sentiment (TraceIntelligenceSignalValueResponseDto):
    """

    behavior: TraceIntelligenceSignalValueResponseDto
    goal: TraceIntelligenceSignalValueResponseDto
    outcome: TraceIntelligenceSignalValueResponseDto
    sentiment: TraceIntelligenceSignalValueResponseDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_signal_value_response_dto import (
            TraceIntelligenceSignalValueResponseDto,
        )

        behavior = self.behavior.to_dict()

        goal = self.goal.to_dict()

        outcome = self.outcome.to_dict()

        sentiment = self.sentiment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "behavior": behavior,
                "goal": goal,
                "outcome": outcome,
                "sentiment": sentiment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_signal_value_response_dto import (
            TraceIntelligenceSignalValueResponseDto,
        )

        d = dict(src_dict)
        behavior = TraceIntelligenceSignalValueResponseDto.from_dict(d.pop("behavior"))

        goal = TraceIntelligenceSignalValueResponseDto.from_dict(d.pop("goal"))

        outcome = TraceIntelligenceSignalValueResponseDto.from_dict(d.pop("outcome"))

        sentiment = TraceIntelligenceSignalValueResponseDto.from_dict(d.pop("sentiment"))

        trace_intelligence_signals_payload_response_dto = cls(
            behavior=behavior,
            goal=goal,
            outcome=outcome,
            sentiment=sentiment,
        )

        trace_intelligence_signals_payload_response_dto.additional_properties = d
        return trace_intelligence_signals_payload_response_dto

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
