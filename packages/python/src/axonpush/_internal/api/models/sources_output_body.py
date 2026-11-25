from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.source_binding import SourceBinding


T = TypeVar("T", bound="SourcesOutputBody")


@_attrs_define
class SourcesOutputBody:
    """
    Attributes:
        sources (list[SourceBinding] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    sources: list[SourceBinding] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.source_binding import SourceBinding

        sources: list[dict[str, Any]] | None
        if isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sources": sources,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_binding import SourceBinding

        d = dict(src_dict)

        def _parse_sources(data: object) -> list[SourceBinding] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = SourceBinding.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SourceBinding] | None, data)

        sources = _parse_sources(d.pop("sources"))

        schema = d.pop("$schema", UNSET)

        sources_output_body = cls(
            sources=sources,
            schema=schema,
        )

        return sources_output_body
