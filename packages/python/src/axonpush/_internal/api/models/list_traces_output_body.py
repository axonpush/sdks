from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_summary_dto import TraceSummaryDTO


T = TypeVar("T", bound="ListTracesOutputBody")


@_attrs_define
class ListTracesOutputBody:
    """
    Attributes:
        traces (list[TraceSummaryDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    traces: list[TraceSummaryDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_summary_dto import TraceSummaryDTO

        traces: list[dict[str, Any]] | None
        if isinstance(self.traces, list):
            traces = []
            for traces_type_0_item_data in self.traces:
                traces_type_0_item = traces_type_0_item_data.to_dict()
                traces.append(traces_type_0_item)

        else:
            traces = self.traces

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "traces": traces,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_summary_dto import TraceSummaryDTO

        d = dict(src_dict)

        def _parse_traces(data: object) -> list[TraceSummaryDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                traces_type_0 = []
                _traces_type_0 = data
                for traces_type_0_item_data in _traces_type_0:
                    traces_type_0_item = TraceSummaryDTO.from_dict(traces_type_0_item_data)

                    traces_type_0.append(traces_type_0_item)

                return traces_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TraceSummaryDTO] | None, data)

        traces = _parse_traces(d.pop("traces"))

        schema = d.pop("$schema", UNSET)

        list_traces_output_body = cls(
            traces=traces,
            schema=schema,
        )

        return list_traces_output_body
