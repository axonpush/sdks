from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.intelligence_job_status import IntelligenceJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.intelligence_job_response_dto_clusters_item import (
        IntelligenceJobResponseDtoClustersItem,
    )


T = TypeVar("T", bound="IntelligenceJobResponseDto")


@_attrs_define
class IntelligenceJobResponseDto:
    """
    Attributes:
        algorithm (str):
        cluster_count (float):
        clusters (list[IntelligenceJobResponseDtoClustersItem]):
        cost_usd (float):
        created_at (datetime.datetime):
        issue_count (float):
        job_id (str):
        labelled_count (float):
        max_cost_usd (float):
        max_labels (float):
        minimum_cohort_size (float):
        org_id (str):
        status (IntelligenceJobStatus):
        updated_at (datetime.datetime):
        completed_at (datetime.datetime | Unset):
        created_by (str | Unset):
        error (str | Unset):
        evaluator_id (str | Unset):
        evaluator_version (float | Unset):
        model (str | Unset):
        provider (str | Unset):
    """

    algorithm: str
    cluster_count: float
    clusters: list[IntelligenceJobResponseDtoClustersItem]
    cost_usd: float
    created_at: datetime.datetime
    issue_count: float
    job_id: str
    labelled_count: float
    max_cost_usd: float
    max_labels: float
    minimum_cohort_size: float
    org_id: str
    status: IntelligenceJobStatus
    updated_at: datetime.datetime
    completed_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    error: str | Unset = UNSET
    evaluator_id: str | Unset = UNSET
    evaluator_version: float | Unset = UNSET
    model: str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.intelligence_job_response_dto_clusters_item import (
            IntelligenceJobResponseDtoClustersItem,
        )

        algorithm = self.algorithm

        cluster_count = self.cluster_count

        clusters = []
        for clusters_item_data in self.clusters:
            clusters_item = clusters_item_data.to_dict()
            clusters.append(clusters_item)

        cost_usd = self.cost_usd

        created_at = self.created_at.isoformat()

        issue_count = self.issue_count

        job_id = self.job_id

        labelled_count = self.labelled_count

        max_cost_usd = self.max_cost_usd

        max_labels = self.max_labels

        minimum_cohort_size = self.minimum_cohort_size

        org_id = self.org_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        created_by = self.created_by

        error = self.error

        evaluator_id = self.evaluator_id

        evaluator_version = self.evaluator_version

        model = self.model

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "clusterCount": cluster_count,
                "clusters": clusters,
                "costUsd": cost_usd,
                "createdAt": created_at,
                "issueCount": issue_count,
                "jobId": job_id,
                "labelledCount": labelled_count,
                "maxCostUsd": max_cost_usd,
                "maxLabels": max_labels,
                "minimumCohortSize": minimum_cohort_size,
                "orgId": org_id,
                "status": status,
                "updatedAt": updated_at,
            }
        )
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if error is not UNSET:
            field_dict["error"] = error
        if evaluator_id is not UNSET:
            field_dict["evaluatorId"] = evaluator_id
        if evaluator_version is not UNSET:
            field_dict["evaluatorVersion"] = evaluator_version
        if model is not UNSET:
            field_dict["model"] = model
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.intelligence_job_response_dto_clusters_item import (
            IntelligenceJobResponseDtoClustersItem,
        )

        d = dict(src_dict)
        algorithm = d.pop("algorithm")

        cluster_count = d.pop("clusterCount")

        clusters = []
        _clusters = d.pop("clusters")
        for clusters_item_data in _clusters:
            clusters_item = IntelligenceJobResponseDtoClustersItem.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        cost_usd = d.pop("costUsd")

        created_at = isoparse(d.pop("createdAt"))

        issue_count = d.pop("issueCount")

        job_id = d.pop("jobId")

        labelled_count = d.pop("labelledCount")

        max_cost_usd = d.pop("maxCostUsd")

        max_labels = d.pop("maxLabels")

        minimum_cohort_size = d.pop("minimumCohortSize")

        org_id = d.pop("orgId")

        status = IntelligenceJobStatus(d.pop("status"))

        updated_at = isoparse(d.pop("updatedAt"))

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        created_by = d.pop("createdBy", UNSET)

        error = d.pop("error", UNSET)

        evaluator_id = d.pop("evaluatorId", UNSET)

        evaluator_version = d.pop("evaluatorVersion", UNSET)

        model = d.pop("model", UNSET)

        provider = d.pop("provider", UNSET)

        intelligence_job_response_dto = cls(
            algorithm=algorithm,
            cluster_count=cluster_count,
            clusters=clusters,
            cost_usd=cost_usd,
            created_at=created_at,
            issue_count=issue_count,
            job_id=job_id,
            labelled_count=labelled_count,
            max_cost_usd=max_cost_usd,
            max_labels=max_labels,
            minimum_cohort_size=minimum_cohort_size,
            org_id=org_id,
            status=status,
            updated_at=updated_at,
            completed_at=completed_at,
            created_by=created_by,
            error=error,
            evaluator_id=evaluator_id,
            evaluator_version=evaluator_version,
            model=model,
            provider=provider,
        )

        intelligence_job_response_dto.additional_properties = d
        return intelligence_job_response_dto

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
