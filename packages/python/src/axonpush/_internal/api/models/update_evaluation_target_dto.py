from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.evaluation_target_type import EvaluationTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_evaluation_target_dto_config import UpdateEvaluationTargetDtoConfig


T = TypeVar("T", bound="UpdateEvaluationTargetDto")


@_attrs_define
class UpdateEvaluationTargetDto:
    """
    Attributes:
        config (UpdateEvaluationTargetDtoConfig | Unset):
        enabled (bool | Unset):  Default: True.
        endpoint (str | Unset):
        name (str | Unset):
        secret_ref (str | Unset): Reference to a separately managed secret. Raw credentials are never accepted.
        type_ (EvaluationTargetType | Unset):
    """

    config: UpdateEvaluationTargetDtoConfig | Unset = UNSET
    enabled: bool | Unset = True
    endpoint: str | Unset = UNSET
    name: str | Unset = UNSET
    secret_ref: str | Unset = UNSET
    type_: EvaluationTargetType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_evaluation_target_dto_config import UpdateEvaluationTargetDtoConfig

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        enabled = self.enabled

        endpoint = self.endpoint

        name = self.name

        secret_ref = self.secret_ref

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if name is not UNSET:
            field_dict["name"] = name
        if secret_ref is not UNSET:
            field_dict["secretRef"] = secret_ref
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_evaluation_target_dto_config import UpdateEvaluationTargetDtoConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: UpdateEvaluationTargetDtoConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = UpdateEvaluationTargetDtoConfig.from_dict(_config)

        enabled = d.pop("enabled", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        name = d.pop("name", UNSET)

        secret_ref = d.pop("secretRef", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EvaluationTargetType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EvaluationTargetType(_type_)

        update_evaluation_target_dto = cls(
            config=config,
            enabled=enabled,
            endpoint=endpoint,
            name=name,
            secret_ref=secret_ref,
            type_=type_,
        )

        update_evaluation_target_dto.additional_properties = d
        return update_evaluation_target_dto

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
