from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_client_confidence import ActivityClientConfidence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_client_evidence import ActivityClientEvidence


T = TypeVar("T", bound="ActivityClient")


@_attrs_define
class ActivityClient:
    """
    Attributes:
        confidence (ActivityClientConfidence):
        family (str):
        attribution_source (str | Unset):
        conflict (bool | Unset):
        evidence (list[ActivityClientEvidence] | None | Unset):
        reported_name (str | Unset):
        version (str | Unset):
    """

    confidence: ActivityClientConfidence
    family: str
    attribution_source: str | Unset = UNSET
    conflict: bool | Unset = UNSET
    evidence: list[ActivityClientEvidence] | None | Unset = UNSET
    reported_name: str | Unset = UNSET
    version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_client_evidence import ActivityClientEvidence

        confidence = self.confidence.value

        family = self.family

        attribution_source = self.attribution_source

        conflict = self.conflict

        evidence: list[dict[str, Any]] | None | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, list):
            evidence = []
            for evidence_type_0_item_data in self.evidence:
                evidence_type_0_item = evidence_type_0_item_data.to_dict()
                evidence.append(evidence_type_0_item)

        else:
            evidence = self.evidence

        reported_name = self.reported_name

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confidence": confidence,
                "family": family,
            }
        )
        if attribution_source is not UNSET:
            field_dict["attribution_source"] = attribution_source
        if conflict is not UNSET:
            field_dict["conflict"] = conflict
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if reported_name is not UNSET:
            field_dict["reported_name"] = reported_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_client_evidence import ActivityClientEvidence

        d = dict(src_dict)
        confidence = ActivityClientConfidence(d.pop("confidence"))

        family = d.pop("family")

        attribution_source = d.pop("attribution_source", UNSET)

        conflict = d.pop("conflict", UNSET)

        def _parse_evidence(data: object) -> list[ActivityClientEvidence] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_type_0 = []
                _evidence_type_0 = data
                for evidence_type_0_item_data in _evidence_type_0:
                    evidence_type_0_item = ActivityClientEvidence.from_dict(
                        evidence_type_0_item_data
                    )

                    evidence_type_0.append(evidence_type_0_item)

                return evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityClientEvidence] | None | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

        reported_name = d.pop("reported_name", UNSET)

        version = d.pop("version", UNSET)

        activity_client = cls(
            confidence=confidence,
            family=family,
            attribution_source=attribution_source,
            conflict=conflict,
            evidence=evidence,
            reported_name=reported_name,
            version=version,
        )

        return activity_client
