from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromptDeploymentDto")


@_attrs_define
class PromptDeploymentDto:
    """
    Attributes:
        environment (str):
        org_id (str):
        promoted_at (datetime.datetime):
        prompt_id (str):
        revision (float):
        version (float):
        previous_version (float | Unset):
        release (str | Unset):
    """

    environment: str
    org_id: str
    promoted_at: datetime.datetime
    prompt_id: str
    revision: float
    version: float
    previous_version: float | Unset = UNSET
    release: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment

        org_id = self.org_id

        promoted_at = self.promoted_at.isoformat()

        prompt_id = self.prompt_id

        revision = self.revision

        version = self.version

        previous_version = self.previous_version

        release = self.release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
                "orgId": org_id,
                "promotedAt": promoted_at,
                "promptId": prompt_id,
                "revision": revision,
                "version": version,
            }
        )
        if previous_version is not UNSET:
            field_dict["previousVersion"] = previous_version
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment = d.pop("environment")

        org_id = d.pop("orgId")

        promoted_at = isoparse(d.pop("promotedAt"))

        prompt_id = d.pop("promptId")

        revision = d.pop("revision")

        version = d.pop("version")

        previous_version = d.pop("previousVersion", UNSET)

        release = d.pop("release", UNSET)

        prompt_deployment_dto = cls(
            environment=environment,
            org_id=org_id,
            promoted_at=promoted_at,
            prompt_id=prompt_id,
            revision=revision,
            version=version,
            previous_version=previous_version,
            release=release,
        )

        prompt_deployment_dto.additional_properties = d
        return prompt_deployment_dto

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
