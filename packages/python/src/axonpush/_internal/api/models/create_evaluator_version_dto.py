from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evaluator_kind import EvaluatorKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_evaluator_version_dto_config import CreateEvaluatorVersionDtoConfig
    from ..models.create_evaluator_version_dto_output_schema import (
        CreateEvaluatorVersionDtoOutputSchema,
    )


T = TypeVar("T", bound="CreateEvaluatorVersionDto")


@_attrs_define
class CreateEvaluatorVersionDto:
    """
    Attributes:
        config (CreateEvaluatorVersionDtoConfig):
        kind (EvaluatorKind):
        model (str | Unset):
        output_schema (CreateEvaluatorVersionDtoOutputSchema | Unset):
        provider (str | Unset):
        rubric (str | Unset):
    """

    config: CreateEvaluatorVersionDtoConfig
    kind: EvaluatorKind
    model: str | Unset = UNSET
    output_schema: CreateEvaluatorVersionDtoOutputSchema | Unset = UNSET
    provider: str | Unset = UNSET
    rubric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_evaluator_version_dto_config import CreateEvaluatorVersionDtoConfig
        from ..models.create_evaluator_version_dto_output_schema import (
            CreateEvaluatorVersionDtoOutputSchema,
        )

        config = self.config.to_dict()

        kind = self.kind.value

        model = self.model

        output_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_schema, Unset):
            output_schema = self.output_schema.to_dict()

        provider = self.provider

        rubric = self.rubric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "kind": kind,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if output_schema is not UNSET:
            field_dict["outputSchema"] = output_schema
        if provider is not UNSET:
            field_dict["provider"] = provider
        if rubric is not UNSET:
            field_dict["rubric"] = rubric

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_evaluator_version_dto_config import CreateEvaluatorVersionDtoConfig
        from ..models.create_evaluator_version_dto_output_schema import (
            CreateEvaluatorVersionDtoOutputSchema,
        )

        d = dict(src_dict)
        config = CreateEvaluatorVersionDtoConfig.from_dict(d.pop("config"))

        kind = EvaluatorKind(d.pop("kind"))

        model = d.pop("model", UNSET)

        _output_schema = d.pop("outputSchema", UNSET)
        output_schema: CreateEvaluatorVersionDtoOutputSchema | Unset
        if isinstance(_output_schema, Unset):
            output_schema = UNSET
        else:
            output_schema = CreateEvaluatorVersionDtoOutputSchema.from_dict(_output_schema)

        provider = d.pop("provider", UNSET)

        rubric = d.pop("rubric", UNSET)

        create_evaluator_version_dto = cls(
            config=config,
            kind=kind,
            model=model,
            output_schema=output_schema,
            provider=provider,
            rubric=rubric,
        )

        create_evaluator_version_dto.additional_properties = d
        return create_evaluator_version_dto

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
