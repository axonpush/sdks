from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_intelligence_cluster_list_meta_dto_cursor_type_0 import (
        TraceIntelligenceClusterListMetaDtoCursorType0,
    )


T = TypeVar("T", bound="TraceIntelligenceClusterListMetaDto")


@_attrs_define
class TraceIntelligenceClusterListMetaDto:
    """
    Attributes:
        has_more (bool):
        cursor (None | TraceIntelligenceClusterListMetaDtoCursorType0 | Unset):
    """

    has_more: bool
    cursor: None | TraceIntelligenceClusterListMetaDtoCursorType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_intelligence_cluster_list_meta_dto_cursor_type_0 import (
            TraceIntelligenceClusterListMetaDtoCursorType0,
        )

        has_more = self.has_more

        cursor: dict[str, Any] | None | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        elif isinstance(self.cursor, TraceIntelligenceClusterListMetaDtoCursorType0):
            cursor = self.cursor.to_dict()
        else:
            cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasMore": has_more,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_intelligence_cluster_list_meta_dto_cursor_type_0 import (
            TraceIntelligenceClusterListMetaDtoCursorType0,
        )

        d = dict(src_dict)
        has_more = d.pop("hasMore")

        def _parse_cursor(
            data: object,
        ) -> None | TraceIntelligenceClusterListMetaDtoCursorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cursor_type_0 = TraceIntelligenceClusterListMetaDtoCursorType0.from_dict(data)

                return cursor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceIntelligenceClusterListMetaDtoCursorType0 | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        trace_intelligence_cluster_list_meta_dto = cls(
            has_more=has_more,
            cursor=cursor,
        )

        trace_intelligence_cluster_list_meta_dto.additional_properties = d
        return trace_intelligence_cluster_list_meta_dto

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
