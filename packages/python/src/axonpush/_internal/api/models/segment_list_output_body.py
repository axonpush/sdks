from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_segment import LedgerSegment


T = TypeVar("T", bound="SegmentListOutputBody")


@_attrs_define
class SegmentListOutputBody:
    """
    Attributes:
        segments (list[LedgerSegment] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_cursor (str | Unset):
    """

    segments: list[LedgerSegment] | None
    schema: str | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.ledger_segment import LedgerSegment

        segments: list[dict[str, Any]] | None
        if isinstance(self.segments, list):
            segments = []
            for segments_type_0_item_data in self.segments:
                segments_type_0_item = segments_type_0_item_data.to_dict()
                segments.append(segments_type_0_item)

        else:
            segments = self.segments

        schema = self.schema

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segments": segments,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_segment import LedgerSegment

        d = dict(src_dict)

        def _parse_segments(data: object) -> list[LedgerSegment] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                segments_type_0 = []
                _segments_type_0 = data
                for segments_type_0_item_data in _segments_type_0:
                    segments_type_0_item = LedgerSegment.from_dict(segments_type_0_item_data)

                    segments_type_0.append(segments_type_0_item)

                return segments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LedgerSegment] | None, data)

        segments = _parse_segments(d.pop("segments"))

        schema = d.pop("$schema", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        segment_list_output_body = cls(
            segments=segments,
            schema=schema,
            next_cursor=next_cursor,
        )

        return segment_list_output_body
