from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assessment_source import AssessmentSource
from ..models.assessment_target_type import AssessmentTargetType
from ..models.assessment_value_type import AssessmentValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_assessment_dto_correction import CreateAssessmentDtoCorrection
    from ..models.create_assessment_dto_metadata import CreateAssessmentDtoMetadata


T = TypeVar("T", bound="CreateAssessmentDto")


@_attrs_define
class CreateAssessmentDto:
    """
    Attributes:
        name (str):
        source (AssessmentSource):
        target_type (AssessmentTargetType):
        value (bool | float | str):
        value_type (AssessmentValueType):
        correction (CreateAssessmentDtoCorrection | Unset):
        evaluator_version_id (str | Unset):
        explanation (str | Unset):
        idempotency_key (str | Unset):
        metadata (CreateAssessmentDtoMetadata | Unset):
        target_id (str | Unset):
    """

    name: str
    source: AssessmentSource
    target_type: AssessmentTargetType
    value: bool | float | str
    value_type: AssessmentValueType
    correction: CreateAssessmentDtoCorrection | Unset = UNSET
    evaluator_version_id: str | Unset = UNSET
    explanation: str | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    metadata: CreateAssessmentDtoMetadata | Unset = UNSET
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_assessment_dto_correction import CreateAssessmentDtoCorrection
        from ..models.create_assessment_dto_metadata import CreateAssessmentDtoMetadata

        name = self.name

        source = self.source.value

        target_type = self.target_type.value

        value: bool | float | str
        value = self.value

        value_type = self.value_type.value

        correction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.correction, Unset):
            correction = self.correction.to_dict()

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
                "name": name,
                "source": source,
                "targetType": target_type,
                "value": value,
                "valueType": value_type,
            }
        )
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
        from ..models.create_assessment_dto_correction import CreateAssessmentDtoCorrection
        from ..models.create_assessment_dto_metadata import CreateAssessmentDtoMetadata

        d = dict(src_dict)
        name = d.pop("name")

        source = AssessmentSource(d.pop("source"))

        target_type = AssessmentTargetType(d.pop("targetType"))

        def _parse_value(data: object) -> bool | float | str:
            return cast(bool | float | str, data)

        value = _parse_value(d.pop("value"))

        value_type = AssessmentValueType(d.pop("valueType"))

        _correction = d.pop("correction", UNSET)
        correction: CreateAssessmentDtoCorrection | Unset
        if isinstance(_correction, Unset):
            correction = UNSET
        else:
            correction = CreateAssessmentDtoCorrection.from_dict(_correction)

        evaluator_version_id = d.pop("evaluatorVersionId", UNSET)

        explanation = d.pop("explanation", UNSET)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateAssessmentDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateAssessmentDtoMetadata.from_dict(_metadata)

        target_id = d.pop("targetId", UNSET)

        create_assessment_dto = cls(
            name=name,
            source=source,
            target_type=target_type,
            value=value,
            value_type=value_type,
            correction=correction,
            evaluator_version_id=evaluator_version_id,
            explanation=explanation,
            idempotency_key=idempotency_key,
            metadata=metadata,
            target_id=target_id,
        )

        create_assessment_dto.additional_properties = d
        return create_assessment_dto

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
