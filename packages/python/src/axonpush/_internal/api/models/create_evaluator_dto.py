from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evaluator_kind import EvaluatorKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_evaluator_dto_config import CreateEvaluatorDtoConfig


T = TypeVar("T", bound="CreateEvaluatorDto")


@_attrs_define
class CreateEvaluatorDto:
    """
    Attributes:
        config (CreateEvaluatorDtoConfig):
        kind (EvaluatorKind):
        name (str):
        description (str | Unset):
        model (str | Unset):
        output_schema (Any | Unset):
        provider (str | Unset):
        rubric (str | Unset):
    """

    config: CreateEvaluatorDtoConfig
    kind: EvaluatorKind
    name: str
    description: str | Unset = UNSET
    model: str | Unset = UNSET
    output_schema: Any | Unset = UNSET
    provider: str | Unset = UNSET
    rubric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_evaluator_dto_config import CreateEvaluatorDtoConfig

        config = self.config.to_dict()

        kind = self.kind.value

        name = self.name

        description = self.description

        model = self.model

        output_schema = self.output_schema

        provider = self.provider

        rubric = self.rubric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "kind": kind,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.create_evaluator_dto_config import CreateEvaluatorDtoConfig

        d = dict(src_dict)
        config = CreateEvaluatorDtoConfig.from_dict(d.pop("config"))

        kind = EvaluatorKind(d.pop("kind"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        model = d.pop("model", UNSET)

        output_schema = d.pop("outputSchema", UNSET)

        provider = d.pop("provider", UNSET)

        rubric = d.pop("rubric", UNSET)

        create_evaluator_dto = cls(
            config=config,
            kind=kind,
            name=name,
            description=description,
            model=model,
            output_schema=output_schema,
            provider=provider,
            rubric=rubric,
        )

        create_evaluator_dto.additional_properties = d
        return create_evaluator_dto

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
