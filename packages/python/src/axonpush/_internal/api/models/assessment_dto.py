from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.assessment_source import AssessmentSource
from ..models.assessment_target_type import AssessmentTargetType
from ..models.assessment_value_type import AssessmentValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assessment_dto_metadata import AssessmentDtoMetadata


T = TypeVar("T", bound="AssessmentDto")


@_attrs_define
class AssessmentDto:
    """
    Attributes:
        assessment_id (str):
        created_at (datetime.datetime):
        name (str):
        org_id (str):
        source (AssessmentSource):
        target_type (AssessmentTargetType):
        trace_id (str):
        updated_at (datetime.datetime):
        value (bool | float | str):
        value_type (AssessmentValueType):
        actor_id (str | Unset):
        correction (Any | Unset):
        evaluator_version_id (str | Unset):
        explanation (str | Unset):
        idempotency_key (str | Unset):
        metadata (AssessmentDtoMetadata | Unset):
        target_id (str | Unset):
    """

    assessment_id: str
    created_at: datetime.datetime
    name: str
    org_id: str
    source: AssessmentSource
    target_type: AssessmentTargetType
    trace_id: str
    updated_at: datetime.datetime
    value: bool | float | str
    value_type: AssessmentValueType
    actor_id: str | Unset = UNSET
    correction: Any | Unset = UNSET
    evaluator_version_id: str | Unset = UNSET
    explanation: str | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    metadata: AssessmentDtoMetadata | Unset = UNSET
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assessment_dto_metadata import AssessmentDtoMetadata

        assessment_id = self.assessment_id

        created_at = self.created_at.isoformat()

        name = self.name

        org_id = self.org_id

        source = self.source.value

        target_type = self.target_type.value

        trace_id = self.trace_id

        updated_at = self.updated_at.isoformat()

        value: bool | float | str
        value = self.value

        value_type = self.value_type.value

        actor_id = self.actor_id

        correction = self.correction

        evaluator_version_id = self.evaluator_version_id

        explanation = self.explanation

        idempotency_key = self.idempotency_key

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessmentId": assessment_id,
                "createdAt": created_at,
                "name": name,
                "orgId": org_id,
                "source": source,
                "targetType": target_type,
                "traceId": trace_id,
                "updatedAt": updated_at,
                "value": value,
                "valueType": value_type,
            }
        )
        if actor_id is not UNSET:
            field_dict["actorId"] = actor_id
        if correction is not UNSET:
            field_dict["correction"] = correction
        if evaluator_version_id is not UNSET:
            field_dict["evaluatorVersionId"] = evaluator_version_id
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assessment_dto_metadata import AssessmentDtoMetadata

        d = dict(src_dict)
        assessment_id = d.pop("assessmentId")

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        org_id = d.pop("orgId")

        source = AssessmentSource(d.pop("source"))

        target_type = AssessmentTargetType(d.pop("targetType"))

        trace_id = d.pop("traceId")

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_value(data: object) -> bool | float | str:
            return cast(bool | float | str, data)

        value = _parse_value(d.pop("value"))

        value_type = AssessmentValueType(d.pop("valueType"))

        actor_id = d.pop("actorId", UNSET)

        correction = d.pop("correction", UNSET)

        evaluator_version_id = d.pop("evaluatorVersionId", UNSET)

        explanation = d.pop("explanation", UNSET)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AssessmentDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AssessmentDtoMetadata.from_dict(_metadata)

        target_id = d.pop("targetId", UNSET)

        assessment_dto = cls(
            assessment_id=assessment_id,
            created_at=created_at,
            name=name,
            org_id=org_id,
            source=source,
            target_type=target_type,
            trace_id=trace_id,
            updated_at=updated_at,
            value=value,
            value_type=value_type,
            actor_id=actor_id,
            correction=correction,
            evaluator_version_id=evaluator_version_id,
            explanation=explanation,
            idempotency_key=idempotency_key,
            metadata=metadata,
            target_id=target_id,
        )

        assessment_dto.additional_properties = d
        return assessment_dto

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
