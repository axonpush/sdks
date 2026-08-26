from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceSignalValueResponseDto")


@_attrs_define
class TraceIntelligenceSignalValueResponseDto:
    """
    Attributes:
        confidence (float):
        description (str):
        label (str):
        polarity (float | Unset):
        success (bool | Unset):
    """

    confidence: float
    description: str
    label: str
    polarity: float | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        description = self.description

        label = self.label

        polarity = self.polarity

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "description": description,
                "label": label,
            }
        )
        if polarity is not UNSET:
            field_dict["polarity"] = polarity
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence = d.pop("confidence")

        description = d.pop("description")

        label = d.pop("label")

        polarity = d.pop("polarity", UNSET)

        success = d.pop("success", UNSET)

        trace_intelligence_signal_value_response_dto = cls(
            confidence=confidence,
            description=description,
            label=label,
            polarity=polarity,
            success=success,
        )

        trace_intelligence_signal_value_response_dto.additional_properties = d
        return trace_intelligence_signal_value_response_dto

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
