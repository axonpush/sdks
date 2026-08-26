from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceIntelligenceProviderTestResponseDto")


@_attrs_define
class TraceIntelligenceProviderTestResponseDto:
    """
    Attributes:
        chat_model (str):
        dimensions (float):
        embedding_model (str):
        ok (bool):
    """

    chat_model: str
    dimensions: float
    embedding_model: str
    ok: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_model = self.chat_model

        dimensions = self.dimensions

        embedding_model = self.embedding_model

        ok = self.ok

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatModel": chat_model,
                "dimensions": dimensions,
                "embeddingModel": embedding_model,
                "ok": ok,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_model = d.pop("chatModel")

        dimensions = d.pop("dimensions")

        embedding_model = d.pop("embeddingModel")

        ok = d.pop("ok")

        trace_intelligence_provider_test_response_dto = cls(
            chat_model=chat_model,
            dimensions=dimensions,
            embedding_model=embedding_model,
            ok=ok,
        )

        trace_intelligence_provider_test_response_dto.additional_properties = d
        return trace_intelligence_provider_test_response_dto

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
