from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceSpanSearchMetaDto")


@_attrs_define
class TraceSpanSearchMetaDto:
    """
    Attributes:
        limit (float):
        query (str):
        scanned (float): Spans searched, matching or not.
        total (float): Matches found before the response cap.
    """

    limit: float
    query: str
    scanned: float
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        query = self.query

        scanned = self.scanned

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "query": query,
                "scanned": scanned,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        query = d.pop("query")

        scanned = d.pop("scanned")

        total = d.pop("total")

        trace_span_search_meta_dto = cls(
            limit=limit,
            query=query,
            scanned=scanned,
            total=total,
        )

        trace_span_search_meta_dto.additional_properties = d
        return trace_span_search_meta_dto

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
