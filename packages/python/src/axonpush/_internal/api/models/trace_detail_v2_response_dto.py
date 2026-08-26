from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_hierarchy_item_dto import TraceHierarchyItemDto
    from ..models.trace_summary_v2_dto import TraceSummaryV2Dto


T = TypeVar("T", bound="TraceDetailV2ResponseDto")


@_attrs_define
class TraceDetailV2ResponseDto:
    """
    Attributes:
        hierarchy (list[TraceHierarchyItemDto]):
        summary (TraceSummaryV2Dto):
    """

    hierarchy: list[TraceHierarchyItemDto]
    summary: TraceSummaryV2Dto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_hierarchy_item_dto import TraceHierarchyItemDto
        from ..models.trace_summary_v2_dto import TraceSummaryV2Dto

        hierarchy = []
        for hierarchy_item_data in self.hierarchy:
            hierarchy_item = hierarchy_item_data.to_dict()
            hierarchy.append(hierarchy_item)

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hierarchy": hierarchy,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_hierarchy_item_dto import TraceHierarchyItemDto
        from ..models.trace_summary_v2_dto import TraceSummaryV2Dto

        d = dict(src_dict)
        hierarchy = []
        _hierarchy = d.pop("hierarchy")
        for hierarchy_item_data in _hierarchy:
            hierarchy_item = TraceHierarchyItemDto.from_dict(hierarchy_item_data)

            hierarchy.append(hierarchy_item)

        summary = TraceSummaryV2Dto.from_dict(d.pop("summary"))

        trace_detail_v2_response_dto = cls(
            hierarchy=hierarchy,
            summary=summary,
        )

        trace_detail_v2_response_dto.additional_properties = d
        return trace_detail_v2_response_dto

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
