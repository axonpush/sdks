from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evaluation_target_type import EvaluationTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_evaluation_target_dto_config import CreateEvaluationTargetDtoConfig


T = TypeVar("T", bound="CreateEvaluationTargetDto")


@_attrs_define
class CreateEvaluationTargetDto:
    """
    Attributes:
        name (str):
        type_ (EvaluationTargetType):
        config (CreateEvaluationTargetDtoConfig | Unset):
        enabled (bool | Unset):  Default: True.
        endpoint (str | Unset):
        secret_ref (str | Unset): Reference to a separately managed secret. Raw credentials are never accepted.
    """

    name: str
    type_: EvaluationTargetType
    config: CreateEvaluationTargetDtoConfig | Unset = UNSET
    enabled: bool | Unset = True
    endpoint: str | Unset = UNSET
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_evaluation_target_dto_config import CreateEvaluationTargetDtoConfig

        name = self.name

        type_ = self.type_.value

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        enabled = self.enabled

        endpoint = self.endpoint

        secret_ref = self.secret_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if secret_ref is not UNSET:
            field_dict["secretRef"] = secret_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_evaluation_target_dto_config import CreateEvaluationTargetDtoConfig

        d = dict(src_dict)
        name = d.pop("name")

        type_ = EvaluationTargetType(d.pop("type"))

        _config = d.pop("config", UNSET)
        config: CreateEvaluationTargetDtoConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = CreateEvaluationTargetDtoConfig.from_dict(_config)

        enabled = d.pop("enabled", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        secret_ref = d.pop("secretRef", UNSET)

        create_evaluation_target_dto = cls(
            name=name,
            type_=type_,
            config=config,
            enabled=enabled,
            endpoint=endpoint,
            secret_ref=secret_ref,
        )

        create_evaluation_target_dto.additional_properties = d
        return create_evaluation_target_dto

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
