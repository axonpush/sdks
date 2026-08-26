from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_compare_side_dto import AnalyticsCompareSideDto


T = TypeVar("T", bound="AnalyticsCompareResponseDto")


@_attrs_define
class AnalyticsCompareResponseDto:
    """
    Attributes:
        baseline (AnalyticsCompareSideDto):
        candidate (AnalyticsCompareSideDto):
        dimension (str):
        measure (str):
        delta (float | None | Unset):
        percent_delta (float | None | Unset):
    """

    baseline: AnalyticsCompareSideDto
    candidate: AnalyticsCompareSideDto
    dimension: str
    measure: str
    delta: float | None | Unset = UNSET
    percent_delta: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_compare_side_dto import AnalyticsCompareSideDto

        baseline = self.baseline.to_dict()

        candidate = self.candidate.to_dict()

        dimension = self.dimension

        measure = self.measure

        delta: float | None | Unset
        if isinstance(self.delta, Unset):
            delta = UNSET
        else:
            delta = self.delta

        percent_delta: float | None | Unset
        if isinstance(self.percent_delta, Unset):
            percent_delta = UNSET
        else:
            percent_delta = self.percent_delta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseline": baseline,
                "candidate": candidate,
                "dimension": dimension,
                "measure": measure,
            }
        )
        if delta is not UNSET:
            field_dict["delta"] = delta
        if percent_delta is not UNSET:
            field_dict["percentDelta"] = percent_delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_compare_side_dto import AnalyticsCompareSideDto

        d = dict(src_dict)
        baseline = AnalyticsCompareSideDto.from_dict(d.pop("baseline"))

        candidate = AnalyticsCompareSideDto.from_dict(d.pop("candidate"))

        dimension = d.pop("dimension")

        measure = d.pop("measure")

        def _parse_delta(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        delta = _parse_delta(d.pop("delta", UNSET))

        def _parse_percent_delta(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent_delta = _parse_percent_delta(d.pop("percentDelta", UNSET))

        analytics_compare_response_dto = cls(
            baseline=baseline,
            candidate=candidate,
            dimension=dimension,
            measure=measure,
            delta=delta,
            percent_delta=percent_delta,
        )

        analytics_compare_response_dto.additional_properties = d
        return analytics_compare_response_dto

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
