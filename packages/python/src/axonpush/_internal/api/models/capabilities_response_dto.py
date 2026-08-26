from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_mode import DeploymentMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capability_flags_dto import CapabilityFlagsDto
    from ..models.license_state_dto import LicenseStateDto


T = TypeVar("T", bound="CapabilitiesResponseDto")


@_attrs_define
class CapabilitiesResponseDto:
    """
    Attributes:
        capabilities (CapabilityFlagsDto):
        deployment_mode (DeploymentMode):
        git_sha (str): Commit this build was made from.
        license_ (LicenseStateDto):
        server_version (str):
        version (float): Shape version of this document.
    """

    capabilities: CapabilityFlagsDto
    deployment_mode: DeploymentMode
    git_sha: str
    license_: LicenseStateDto
    server_version: str
    version: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.capability_flags_dto import CapabilityFlagsDto
        from ..models.license_state_dto import LicenseStateDto

        capabilities = self.capabilities.to_dict()

        deployment_mode = self.deployment_mode.value

        git_sha = self.git_sha

        license_ = self.license_.to_dict()

        server_version = self.server_version

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capabilities": capabilities,
                "deploymentMode": deployment_mode,
                "gitSha": git_sha,
                "license": license_,
                "serverVersion": server_version,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_flags_dto import CapabilityFlagsDto
        from ..models.license_state_dto import LicenseStateDto

        d = dict(src_dict)
        capabilities = CapabilityFlagsDto.from_dict(d.pop("capabilities"))

        deployment_mode = DeploymentMode(d.pop("deploymentMode"))

        git_sha = d.pop("gitSha")

        license_ = LicenseStateDto.from_dict(d.pop("license"))

        server_version = d.pop("serverVersion")

        version = d.pop("version")

        capabilities_response_dto = cls(
            capabilities=capabilities,
            deployment_mode=deployment_mode,
            git_sha=git_sha,
            license_=license_,
            server_version=server_version,
            version=version,
        )

        capabilities_response_dto.additional_properties = d
        return capabilities_response_dto

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
