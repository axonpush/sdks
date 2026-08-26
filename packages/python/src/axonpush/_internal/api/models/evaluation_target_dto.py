from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.evaluation_target_type import EvaluationTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluation_target_dto_config import EvaluationTargetDtoConfig


T = TypeVar("T", bound="EvaluationTargetDto")


@_attrs_define
class EvaluationTargetDto:
    """
    Attributes:
        created_at (datetime.datetime):
        name (str):
        org_id (str):
        target_id (str):
        type_ (EvaluationTargetType):
        updated_at (datetime.datetime):
        config (EvaluationTargetDtoConfig | Unset):
        enabled (bool | Unset):  Default: True.
        endpoint (str | Unset):
        secret_ref (str | Unset): Reference to a separately managed secret. Raw credentials are never accepted.
    """

    created_at: datetime.datetime
    name: str
    org_id: str
    target_id: str
    type_: EvaluationTargetType
    updated_at: datetime.datetime
    config: EvaluationTargetDtoConfig | Unset = UNSET
    enabled: bool | Unset = True
    endpoint: str | Unset = UNSET
    secret_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluation_target_dto_config import EvaluationTargetDtoConfig

        created_at = self.created_at.isoformat()

        name = self.name

        org_id = self.org_id

        target_id = self.target_id

        type_ = self.type_.value

        updated_at = self.updated_at.isoformat()

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
                "createdAt": created_at,
                "name": name,
                "orgId": org_id,
                "targetId": target_id,
                "type": type_,
                "updatedAt": updated_at,
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
        from ..models.evaluation_target_dto_config import EvaluationTargetDtoConfig

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        org_id = d.pop("orgId")

        target_id = d.pop("targetId")

        type_ = EvaluationTargetType(d.pop("type"))

        updated_at = isoparse(d.pop("updatedAt"))

        _config = d.pop("config", UNSET)
        config: EvaluationTargetDtoConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = EvaluationTargetDtoConfig.from_dict(_config)

        enabled = d.pop("enabled", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        secret_ref = d.pop("secretRef", UNSET)

        evaluation_target_dto = cls(
            created_at=created_at,
            name=name,
            org_id=org_id,
            target_id=target_id,
            type_=type_,
            updated_at=updated_at,
            config=config,
            enabled=enabled,
            endpoint=endpoint,
            secret_ref=secret_ref,
        )

        evaluation_target_dto.additional_properties = d
        return evaluation_target_dto

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
