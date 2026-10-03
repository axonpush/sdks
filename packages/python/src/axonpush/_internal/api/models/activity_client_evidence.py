from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_client_evidence_confidence import ActivityClientEvidenceConfidence
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityClientEvidence")


@_attrs_define
class ActivityClientEvidence:
    """
    Attributes:
        confidence (ActivityClientEvidenceConfidence):
        family (str):
        source (str):
        name (str | Unset):
        version (str | Unset):
    """

    confidence: ActivityClientEvidenceConfidence
    family: str
    source: str
    name: str | Unset = UNSET
    version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        family = self.family

        source = self.source

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confidence": confidence,
                "family": family,
                "source": source,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence = ActivityClientEvidenceConfidence(d.pop("confidence"))

        family = d.pop("family")

        source = d.pop("source")

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        activity_client_evidence = cls(
            confidence=confidence,
            family=family,
            source=source,
            name=name,
            version=version,
        )

        return activity_client_evidence
