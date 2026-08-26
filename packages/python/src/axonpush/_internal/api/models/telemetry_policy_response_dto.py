from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry_policy_dto import TelemetryPolicyDto


T = TypeVar("T", bound="TelemetryPolicyResponseDto")


@_attrs_define
class TelemetryPolicyResponseDto:
    """
    Attributes:
        policy (TelemetryPolicyDto):
        version (float):
    """

    policy: TelemetryPolicyDto
    version: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.telemetry_policy_dto import TelemetryPolicyDto

        policy = self.policy.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.telemetry_policy_dto import TelemetryPolicyDto

        d = dict(src_dict)
        policy = TelemetryPolicyDto.from_dict(d.pop("policy"))

        version = d.pop("version")

        telemetry_policy_response_dto = cls(
            policy=policy,
            version=version,
        )

        telemetry_policy_response_dto.additional_properties = d
        return telemetry_policy_response_dto

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
