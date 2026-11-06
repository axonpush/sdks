from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_applicability import ComplianceApplicability
    from ..models.compliance_control import ComplianceControl
    from ..models.compliance_source import ComplianceSource
    from ..models.obligation_evidence_struct import ObligationEvidenceStruct


T = TypeVar("T", bound="ComplianceObligation")


@_attrs_define
class ComplianceObligation:
    """
    Attributes:
        agent_id (str):
        applies (ComplianceApplicability):
        clause (str):
        confidence (str):
        controls (list[ComplianceControl] | None):
        duty (str):
        effective_at (str):
        evidence (ObligationEvidenceStruct):
        evidence_count (int):
        evidence_disclaimer (str):
        id (str):
        law (str):
        notes (str):
        review_status (str):
        source_url (str):
        sources (list[ComplianceSource] | None):
        status (str):
        verified_at (str):
        watch (bool):
    """

    agent_id: str
    applies: ComplianceApplicability
    clause: str
    confidence: str
    controls: list[ComplianceControl] | None
    duty: str
    effective_at: str
    evidence: ObligationEvidenceStruct
    evidence_count: int
    evidence_disclaimer: str
    id: str
    law: str
    notes: str
    review_status: str
    source_url: str
    sources: list[ComplianceSource] | None
    status: str
    verified_at: str
    watch: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_applicability import ComplianceApplicability
        from ..models.compliance_control import ComplianceControl
        from ..models.compliance_source import ComplianceSource
        from ..models.obligation_evidence_struct import ObligationEvidenceStruct

        agent_id = self.agent_id

        applies = self.applies.to_dict()

        clause = self.clause

        confidence = self.confidence

        controls: list[dict[str, Any]] | None
        if isinstance(self.controls, list):
            controls = []
            for controls_type_0_item_data in self.controls:
                controls_type_0_item = controls_type_0_item_data.to_dict()
                controls.append(controls_type_0_item)

        else:
            controls = self.controls

        duty = self.duty

        effective_at = self.effective_at

        evidence = self.evidence.to_dict()

        evidence_count = self.evidence_count

        evidence_disclaimer = self.evidence_disclaimer

        id = self.id

        law = self.law

        notes = self.notes

        review_status = self.review_status

        source_url = self.source_url

        sources: list[dict[str, Any]] | None
        if isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        status = self.status

        verified_at = self.verified_at

        watch = self.watch

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agentId": agent_id,
                "applies": applies,
                "clause": clause,
                "confidence": confidence,
                "controls": controls,
                "duty": duty,
                "effectiveAt": effective_at,
                "evidence": evidence,
                "evidenceCount": evidence_count,
                "evidenceDisclaimer": evidence_disclaimer,
                "id": id,
                "law": law,
                "notes": notes,
                "reviewStatus": review_status,
                "sourceUrl": source_url,
                "sources": sources,
                "status": status,
                "verifiedAt": verified_at,
                "watch": watch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_applicability import ComplianceApplicability
        from ..models.compliance_control import ComplianceControl
        from ..models.compliance_source import ComplianceSource
        from ..models.obligation_evidence_struct import ObligationEvidenceStruct

        d = dict(src_dict)
        agent_id = d.pop("agentId")

        applies = ComplianceApplicability.from_dict(d.pop("applies"))

        clause = d.pop("clause")

        confidence = d.pop("confidence")

        def _parse_controls(data: object) -> list[ComplianceControl] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                controls_type_0 = []
                _controls_type_0 = data
                for controls_type_0_item_data in _controls_type_0:
                    controls_type_0_item = ComplianceControl.from_dict(controls_type_0_item_data)

                    controls_type_0.append(controls_type_0_item)

                return controls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceControl] | None, data)

        controls = _parse_controls(d.pop("controls"))

        duty = d.pop("duty")

        effective_at = d.pop("effectiveAt")

        evidence = ObligationEvidenceStruct.from_dict(d.pop("evidence"))

        evidence_count = d.pop("evidenceCount")

        evidence_disclaimer = d.pop("evidenceDisclaimer")

        id = d.pop("id")

        law = d.pop("law")

        notes = d.pop("notes")

        review_status = d.pop("reviewStatus")

        source_url = d.pop("sourceUrl")

        def _parse_sources(data: object) -> list[ComplianceSource] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = ComplianceSource.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceSource] | None, data)

        sources = _parse_sources(d.pop("sources"))

        status = d.pop("status")

        verified_at = d.pop("verifiedAt")

        watch = d.pop("watch")

        compliance_obligation = cls(
            agent_id=agent_id,
            applies=applies,
            clause=clause,
            confidence=confidence,
            controls=controls,
            duty=duty,
            effective_at=effective_at,
            evidence=evidence,
            evidence_count=evidence_count,
            evidence_disclaimer=evidence_disclaimer,
            id=id,
            law=law,
            notes=notes,
            review_status=review_status,
            source_url=source_url,
            sources=sources,
            status=status,
            verified_at=verified_at,
            watch=watch,
        )

        return compliance_obligation
