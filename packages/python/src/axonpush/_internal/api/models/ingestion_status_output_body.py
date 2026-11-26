from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestionStatusOutputBody")


@_attrs_define
class IngestionStatusOutputBody:
    """
    Attributes:
        ever_ingested (bool):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    ever_ingested: bool
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ever_ingested = self.ever_ingested

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "everIngested": ever_ingested,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ever_ingested = d.pop("everIngested")

        schema = d.pop("$schema", UNSET)

        ingestion_status_output_body = cls(
            ever_ingested=ever_ingested,
            schema=schema,
        )

        return ingestion_status_output_body
