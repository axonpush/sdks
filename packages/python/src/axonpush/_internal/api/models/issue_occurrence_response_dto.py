from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_occurrence_response_dto_evidence import IssueOccurrenceResponseDtoEvidence


T = TypeVar("T", bound="IssueOccurrenceResponseDto")


@_attrs_define
class IssueOccurrenceResponseDto:
    """
    Attributes:
        created_at (datetime.datetime):
        event_id (str):
        evidence (IssueOccurrenceResponseDtoEvidence):
        fingerprint (str):
        issue_id (str):
        occurred_at (datetime.datetime):
        occurrence_id (str):
        org_id (str):
        trace_id (str):
        model (str | Unset):
        release (str | Unset):
        service (str | Unset):
        span_id (str | Unset):
    """

    created_at: datetime.datetime
    event_id: str
    evidence: IssueOccurrenceResponseDtoEvidence
    fingerprint: str
    issue_id: str
    occurred_at: datetime.datetime
    occurrence_id: str
    org_id: str
    trace_id: str
    model: str | Unset = UNSET
    release: str | Unset = UNSET
    service: str | Unset = UNSET
    span_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_occurrence_response_dto_evidence import (
            IssueOccurrenceResponseDtoEvidence,
        )

        created_at = self.created_at.isoformat()

        event_id = self.event_id

        evidence = self.evidence.to_dict()

        fingerprint = self.fingerprint

        issue_id = self.issue_id

        occurred_at = self.occurred_at.isoformat()

        occurrence_id = self.occurrence_id

        org_id = self.org_id

        trace_id = self.trace_id

        model = self.model

        release = self.release

        service = self.service

        span_id = self.span_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "eventId": event_id,
                "evidence": evidence,
                "fingerprint": fingerprint,
                "issueId": issue_id,
                "occurredAt": occurred_at,
                "occurrenceId": occurrence_id,
                "orgId": org_id,
                "traceId": trace_id,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if release is not UNSET:
            field_dict["release"] = release
        if service is not UNSET:
            field_dict["service"] = service
        if span_id is not UNSET:
            field_dict["spanId"] = span_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_occurrence_response_dto_evidence import (
            IssueOccurrenceResponseDtoEvidence,
        )

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        event_id = d.pop("eventId")

        evidence = IssueOccurrenceResponseDtoEvidence.from_dict(d.pop("evidence"))

        fingerprint = d.pop("fingerprint")

        issue_id = d.pop("issueId")

        occurred_at = isoparse(d.pop("occurredAt"))

        occurrence_id = d.pop("occurrenceId")

        org_id = d.pop("orgId")

        trace_id = d.pop("traceId")

        model = d.pop("model", UNSET)

        release = d.pop("release", UNSET)

        service = d.pop("service", UNSET)

        span_id = d.pop("spanId", UNSET)

        issue_occurrence_response_dto = cls(
            created_at=created_at,
            event_id=event_id,
            evidence=evidence,
            fingerprint=fingerprint,
            issue_id=issue_id,
            occurred_at=occurred_at,
            occurrence_id=occurrence_id,
            org_id=org_id,
            trace_id=trace_id,
            model=model,
            release=release,
            service=service,
            span_id=span_id,
        )

        issue_occurrence_response_dto.additional_properties = d
        return issue_occurrence_response_dto

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
