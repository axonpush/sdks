from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inclusion import Inclusion
    from ..models.manifest import Manifest


T = TypeVar("T", bound="ProofOutputBody")


@_attrs_define
class ProofOutputBody:
    """
    Attributes:
        event_id (str):
        manifest (Manifest):
        proof (Inclusion):
        segment_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    event_id: str
    manifest: Manifest
    proof: Inclusion
    segment_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.inclusion import Inclusion
        from ..models.manifest import Manifest

        event_id = self.event_id

        manifest = self.manifest.to_dict()

        proof = self.proof.to_dict()

        segment_id = self.segment_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eventId": event_id,
                "manifest": manifest,
                "proof": proof,
                "segmentId": segment_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inclusion import Inclusion
        from ..models.manifest import Manifest

        d = dict(src_dict)
        event_id = d.pop("eventId")

        manifest = Manifest.from_dict(d.pop("manifest"))

        proof = Inclusion.from_dict(d.pop("proof"))

        segment_id = d.pop("segmentId")

        schema = d.pop("$schema", UNSET)

        proof_output_body = cls(
            event_id=event_id,
            manifest=manifest,
            proof=proof,
            segment_id=segment_id,
            schema=schema,
        )

        return proof_output_body
