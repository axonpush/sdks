from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_dto import EventDTO


T = TypeVar("T", bound="GetTraceOutputBody")


@_attrs_define
class GetTraceOutputBody:
    """
    Attributes:
        spans (list[EventDTO] | None):
        trace_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    spans: list[EventDTO] | None
    trace_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_dto import EventDTO

        spans: list[dict[str, Any]] | None
        if isinstance(self.spans, list):
            spans = []
            for spans_type_0_item_data in self.spans:
                spans_type_0_item = spans_type_0_item_data.to_dict()
                spans.append(spans_type_0_item)

        else:
            spans = self.spans

        trace_id = self.trace_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spans": spans,
                "traceId": trace_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_dto import EventDTO

        d = dict(src_dict)

        def _parse_spans(data: object) -> list[EventDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                spans_type_0 = []
                _spans_type_0 = data
                for spans_type_0_item_data in _spans_type_0:
                    spans_type_0_item = EventDTO.from_dict(spans_type_0_item_data)

                    spans_type_0.append(spans_type_0_item)

                return spans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventDTO] | None, data)

        spans = _parse_spans(d.pop("spans"))

        trace_id = d.pop("traceId")

        schema = d.pop("$schema", UNSET)

        get_trace_output_body = cls(
            spans=spans,
            trace_id=trace_id,
            schema=schema,
        )

        return get_trace_output_body
