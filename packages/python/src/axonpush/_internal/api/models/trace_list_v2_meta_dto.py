from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceListV2MetaDto")


@_attrs_define
class TraceListV2MetaDto:
    """
    Attributes:
        has_more (bool):
        limit (float):
        truncated (bool): True when `total` is a floor rather than an exact count.
        cursor (None | str | Unset):
        total (float | None | Unset): Matching traces across the whole window, not just this page. Null when the store
            cannot count cheaply.
    """

    has_more: bool
    limit: float
    truncated: bool
    cursor: None | str | Unset = UNSET
    total: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        limit = self.limit

        truncated = self.truncated

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        total: float | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasMore": has_more,
                "limit": limit,
                "truncated": truncated,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("hasMore")

        limit = d.pop("limit")

        truncated = d.pop("truncated")

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        def _parse_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        trace_list_v2_meta_dto = cls(
            has_more=has_more,
            limit=limit,
            truncated=truncated,
            cursor=cursor,
            total=total,
        )

        trace_list_v2_meta_dto.additional_properties = d
        return trace_list_v2_meta_dto

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
