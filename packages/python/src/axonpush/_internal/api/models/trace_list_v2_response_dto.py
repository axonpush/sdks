from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_list_v2_meta_dto import TraceListV2MetaDto
    from ..models.trace_summary_v2_dto import TraceSummaryV2Dto


T = TypeVar("T", bound="TraceListV2ResponseDto")


@_attrs_define
class TraceListV2ResponseDto:
    """
    Attributes:
        data (list[TraceSummaryV2Dto]):
        meta (TraceListV2MetaDto):
    """

    data: list[TraceSummaryV2Dto]
    meta: TraceListV2MetaDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_list_v2_meta_dto import TraceListV2MetaDto
        from ..models.trace_summary_v2_dto import TraceSummaryV2Dto

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_list_v2_meta_dto import TraceListV2MetaDto
        from ..models.trace_summary_v2_dto import TraceSummaryV2Dto

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TraceSummaryV2Dto.from_dict(data_item_data)

            data.append(data_item)

        meta = TraceListV2MetaDto.from_dict(d.pop("meta"))

        trace_list_v2_response_dto = cls(
            data=data,
            meta=meta,
        )

        trace_list_v2_response_dto.additional_properties = d
        return trace_list_v2_response_dto

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
