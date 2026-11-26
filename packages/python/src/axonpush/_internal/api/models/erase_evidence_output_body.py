from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EraseEvidenceOutputBody")


@_attrs_define
class EraseEvidenceOutputBody:
    """
    Attributes:
        erased (int): Events scrubbed by this call (at most 500)
        more (bool): True when more events for the subject remain; call again until false. The subject is tombstoned on
            the first call, so remaining events are already hidden from reads.
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    erased: int
    more: bool
    status: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        erased = self.erased

        more = self.more

        status = self.status

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "erased": erased,
                "more": more,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        erased = d.pop("erased")

        more = d.pop("more")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        erase_evidence_output_body = cls(
            erased=erased,
            more=more,
            status=status,
            schema=schema,
        )

        return erase_evidence_output_body
