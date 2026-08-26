from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_severity import IssueSeverity
from ..models.issue_status import IssueStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIssueDto")


@_attrs_define
class UpdateIssueDto:
    """
    Attributes:
        dataset_id (str | Unset):
        evaluator_id (str | Unset):
        experiment_id (str | Unset):
        owner_id (str | Unset):
        review_queue_id (str | Unset):
        severity (IssueSeverity | Unset):
        status (IssueStatus | Unset):
    """

    dataset_id: str | Unset = UNSET
    evaluator_id: str | Unset = UNSET
    experiment_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    review_queue_id: str | Unset = UNSET
    severity: IssueSeverity | Unset = UNSET
    status: IssueStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        evaluator_id = self.evaluator_id

        experiment_id = self.experiment_id

        owner_id = self.owner_id

        review_queue_id = self.review_queue_id

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if evaluator_id is not UNSET:
            field_dict["evaluatorId"] = evaluator_id
        if experiment_id is not UNSET:
            field_dict["experimentId"] = experiment_id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if review_queue_id is not UNSET:
            field_dict["reviewQueueId"] = review_queue_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId", UNSET)

        evaluator_id = d.pop("evaluatorId", UNSET)

        experiment_id = d.pop("experimentId", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        review_queue_id = d.pop("reviewQueueId", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: IssueSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = IssueSeverity(_severity)

        _status = d.pop("status", UNSET)
        status: IssueStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IssueStatus(_status)

        update_issue_dto = cls(
            dataset_id=dataset_id,
            evaluator_id=evaluator_id,
            experiment_id=experiment_id,
            owner_id=owner_id,
            review_queue_id=review_queue_id,
            severity=severity,
            status=status,
        )

        update_issue_dto.additional_properties = d
        return update_issue_dto

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
