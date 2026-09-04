from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.evaluator_kind import EvaluatorKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluator_version_dto_config import EvaluatorVersionDtoConfig


T = TypeVar("T", bound="EvaluatorVersionDto")


@_attrs_define
class EvaluatorVersionDto:
    """
    Attributes:
        config (EvaluatorVersionDtoConfig):
        created_at (datetime.datetime):
        evaluator_id (str):
        kind (EvaluatorKind):
        org_id (str):
        version (float):
        model (str | Unset):
        output_schema (Any | Unset):
        provider (str | Unset):
        rubric (str | Unset):
    """

    config: EvaluatorVersionDtoConfig
    created_at: datetime.datetime
    evaluator_id: str
    kind: EvaluatorKind
    org_id: str
    version: float
    model: str | Unset = UNSET
    output_schema: Any | Unset = UNSET
    provider: str | Unset = UNSET
    rubric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluator_version_dto_config import EvaluatorVersionDtoConfig

        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        evaluator_id = self.evaluator_id

        kind = self.kind.value

        org_id = self.org_id

        version = self.version

        model = self.model

        output_schema = self.output_schema

        provider = self.provider

        rubric = self.rubric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "createdAt": created_at,
                "evaluatorId": evaluator_id,
                "kind": kind,
                "orgId": org_id,
                "version": version,
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
        from ..models.evaluator_version_dto_config import EvaluatorVersionDtoConfig

        d = dict(src_dict)
        config = EvaluatorVersionDtoConfig.from_dict(d.pop("config"))

        created_at = isoparse(d.pop("createdAt"))

        evaluator_id = d.pop("evaluatorId")

        kind = EvaluatorKind(d.pop("kind"))

        org_id = d.pop("orgId")

        version = d.pop("version")

        model = d.pop("model", UNSET)

        output_schema = d.pop("outputSchema", UNSET)

        provider = d.pop("provider", UNSET)

        rubric = d.pop("rubric", UNSET)

        evaluator_version_dto = cls(
            config=config,
            created_at=created_at,
            evaluator_id=evaluator_id,
            kind=kind,
            org_id=org_id,
            version=version,
            model=model,
            output_schema=output_schema,
            provider=provider,
            rubric=rubric,
        )

        evaluator_version_dto.additional_properties = d
        return evaluator_version_dto

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
