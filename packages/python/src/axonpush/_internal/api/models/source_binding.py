from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="SourceBinding")


@_attrs_define
class SourceBinding:
    """
    Attributes:
        id (str):
        publisher (str):
    """

    id: str
    publisher: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        publisher = self.publisher

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "publisher": publisher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        publisher = d.pop("publisher")

        source_binding = cls(
            id=id,
            publisher=publisher,
        )

        return source_binding
