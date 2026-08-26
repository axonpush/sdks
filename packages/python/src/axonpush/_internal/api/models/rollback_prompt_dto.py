from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RollbackPromptDto")


@_attrs_define
class RollbackPromptDto:
    """
    Attributes:
        approved (bool):
        environment (str):
        release (str | Unset):
        version (float | Unset): Defaults to the immediately previous promoted version.
        webhook_endpoint_id (str | Unset):
    """

    approved: bool
    environment: str
    release: str | Unset = UNSET
    version: float | Unset = UNSET
    webhook_endpoint_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved = self.approved

        environment = self.environment

        release = self.release

        version = self.version

        webhook_endpoint_id = self.webhook_endpoint_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approved": approved,
                "environment": environment,
            }
        )
        if release is not UNSET:
            field_dict["release"] = release
        if version is not UNSET:
            field_dict["version"] = version
        if webhook_endpoint_id is not UNSET:
            field_dict["webhookEndpointId"] = webhook_endpoint_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approved = d.pop("approved")

        environment = d.pop("environment")

        release = d.pop("release", UNSET)

        version = d.pop("version", UNSET)

        webhook_endpoint_id = d.pop("webhookEndpointId", UNSET)

        rollback_prompt_dto = cls(
            approved=approved,
            environment=environment,
            release=release,
            version=version,
            webhook_endpoint_id=webhook_endpoint_id,
        )

        rollback_prompt_dto.additional_properties = d
        return rollback_prompt_dto

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
