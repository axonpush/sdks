from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.issue_severity import IssueSeverity
from ..models.issue_status import IssueStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_response_dto_label_provenance import IssueResponseDtoLabelProvenance


T = TypeVar("T", bound="IssueResponseDto")


@_attrs_define
class IssueResponseDto:
    """
    Attributes:
        affected_models (list[str]):
        affected_releases (list[str]):
        affected_services (list[str]):
        created_at (datetime.datetime):
        fingerprint (str):
        first_seen_at (datetime.datetime):
        issue_id (str):
        last_seen_at (datetime.datetime):
        occurrence_count (float):
        org_id (str):
        representative_trace_ids (list[str]):
        severity (IssueSeverity):
        status (IssueStatus):
        title (str):
        updated_at (datetime.datetime):
        dataset_id (str | Unset):
        description (str | Unset):
        error_template (str | Unset):
        error_type (str | Unset):
        evaluator_id (str | Unset):
        experiment_id (str | Unset):
        generated_label (str | Unset):
        label_provenance (IssueResponseDtoLabelProvenance | Unset):
        merged_into_issue_id (str | Unset):
        operation (str | Unset):
        owner_id (str | Unset):
        review_queue_id (str | Unset):
        semantic_kind (str | Unset):
    """

    affected_models: list[str]
    affected_releases: list[str]
    affected_services: list[str]
    created_at: datetime.datetime
    fingerprint: str
    first_seen_at: datetime.datetime
    issue_id: str
    last_seen_at: datetime.datetime
    occurrence_count: float
    org_id: str
    representative_trace_ids: list[str]
    severity: IssueSeverity
    status: IssueStatus
    title: str
    updated_at: datetime.datetime
    dataset_id: str | Unset = UNSET
    description: str | Unset = UNSET
    error_template: str | Unset = UNSET
    error_type: str | Unset = UNSET
    evaluator_id: str | Unset = UNSET
    experiment_id: str | Unset = UNSET
    generated_label: str | Unset = UNSET
    label_provenance: IssueResponseDtoLabelProvenance | Unset = UNSET
    merged_into_issue_id: str | Unset = UNSET
    operation: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    review_queue_id: str | Unset = UNSET
    semantic_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_response_dto_label_provenance import IssueResponseDtoLabelProvenance

        affected_models = self.affected_models

        affected_releases = self.affected_releases

        affected_services = self.affected_services

        created_at = self.created_at.isoformat()

        fingerprint = self.fingerprint

        first_seen_at = self.first_seen_at.isoformat()

        issue_id = self.issue_id

        last_seen_at = self.last_seen_at.isoformat()

        occurrence_count = self.occurrence_count

        org_id = self.org_id

        representative_trace_ids = self.representative_trace_ids

        severity = self.severity.value

        status = self.status.value

        title = self.title

        updated_at = self.updated_at.isoformat()

        dataset_id = self.dataset_id

        description = self.description

        error_template = self.error_template

        error_type = self.error_type

        evaluator_id = self.evaluator_id

        experiment_id = self.experiment_id

        generated_label = self.generated_label

        label_provenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_provenance, Unset):
            label_provenance = self.label_provenance.to_dict()

        merged_into_issue_id = self.merged_into_issue_id

        operation = self.operation

        owner_id = self.owner_id

        review_queue_id = self.review_queue_id

        semantic_kind = self.semantic_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affectedModels": affected_models,
                "affectedReleases": affected_releases,
                "affectedServices": affected_services,
                "createdAt": created_at,
                "fingerprint": fingerprint,
                "firstSeenAt": first_seen_at,
                "issueId": issue_id,
                "lastSeenAt": last_seen_at,
                "occurrenceCount": occurrence_count,
                "orgId": org_id,
                "representativeTraceIds": representative_trace_ids,
                "severity": severity,
                "status": status,
                "title": title,
                "updatedAt": updated_at,
            }
        )
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if description is not UNSET:
            field_dict["description"] = description
        if error_template is not UNSET:
            field_dict["errorTemplate"] = error_template
        if error_type is not UNSET:
            field_dict["errorType"] = error_type
        if evaluator_id is not UNSET:
            field_dict["evaluatorId"] = evaluator_id
        if experiment_id is not UNSET:
            field_dict["experimentId"] = experiment_id
        if generated_label is not UNSET:
            field_dict["generatedLabel"] = generated_label
        if label_provenance is not UNSET:
            field_dict["labelProvenance"] = label_provenance
        if merged_into_issue_id is not UNSET:
            field_dict["mergedIntoIssueId"] = merged_into_issue_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if review_queue_id is not UNSET:
            field_dict["reviewQueueId"] = review_queue_id
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_response_dto_label_provenance import IssueResponseDtoLabelProvenance

        d = dict(src_dict)
        affected_models = cast(list[str], d.pop("affectedModels"))

        affected_releases = cast(list[str], d.pop("affectedReleases"))

        affected_services = cast(list[str], d.pop("affectedServices"))

        created_at = isoparse(d.pop("createdAt"))

        fingerprint = d.pop("fingerprint")

        first_seen_at = isoparse(d.pop("firstSeenAt"))

        issue_id = d.pop("issueId")

        last_seen_at = isoparse(d.pop("lastSeenAt"))

        occurrence_count = d.pop("occurrenceCount")

        org_id = d.pop("orgId")

        representative_trace_ids = cast(list[str], d.pop("representativeTraceIds"))

        severity = IssueSeverity(d.pop("severity"))

        status = IssueStatus(d.pop("status"))

        title = d.pop("title")

        updated_at = isoparse(d.pop("updatedAt"))

        dataset_id = d.pop("datasetId", UNSET)

        description = d.pop("description", UNSET)

        error_template = d.pop("errorTemplate", UNSET)

        error_type = d.pop("errorType", UNSET)

        evaluator_id = d.pop("evaluatorId", UNSET)

        experiment_id = d.pop("experimentId", UNSET)

        generated_label = d.pop("generatedLabel", UNSET)

        _label_provenance = d.pop("labelProvenance", UNSET)
        label_provenance: IssueResponseDtoLabelProvenance | Unset
        if isinstance(_label_provenance, Unset):
            label_provenance = UNSET
        else:
            label_provenance = IssueResponseDtoLabelProvenance.from_dict(_label_provenance)

        merged_into_issue_id = d.pop("mergedIntoIssueId", UNSET)

        operation = d.pop("operation", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        review_queue_id = d.pop("reviewQueueId", UNSET)

        semantic_kind = d.pop("semanticKind", UNSET)

        issue_response_dto = cls(
            affected_models=affected_models,
            affected_releases=affected_releases,
            affected_services=affected_services,
            created_at=created_at,
            fingerprint=fingerprint,
            first_seen_at=first_seen_at,
            issue_id=issue_id,
            last_seen_at=last_seen_at,
            occurrence_count=occurrence_count,
            org_id=org_id,
            representative_trace_ids=representative_trace_ids,
            severity=severity,
            status=status,
            title=title,
            updated_at=updated_at,
            dataset_id=dataset_id,
            description=description,
            error_template=error_template,
            error_type=error_type,
            evaluator_id=evaluator_id,
            experiment_id=experiment_id,
            generated_label=generated_label,
            label_provenance=label_provenance,
            merged_into_issue_id=merged_into_issue_id,
            operation=operation,
            owner_id=owner_id,
            review_queue_id=review_queue_id,
            semantic_kind=semantic_kind,
        )

        issue_response_dto.additional_properties = d
        return issue_response_dto

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
