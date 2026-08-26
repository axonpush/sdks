from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_response_dto_flags import HealthResponseDtoFlags


T = TypeVar("T", bound="HealthResponseDto")


@_attrs_define
class HealthResponseDto:
    """
    Attributes:
        flags (HealthResponseDtoFlags):
        status (str):
        timestamp (str):
        version (str):
    """

    flags: HealthResponseDtoFlags
    status: str
    timestamp: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.health_response_dto_flags import HealthResponseDtoFlags

        flags = self.flags.to_dict()

        status = self.status

        timestamp = self.timestamp

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flags": flags,
                "status": status,
                "timestamp": timestamp,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_response_dto_flags import HealthResponseDtoFlags

        d = dict(src_dict)
        flags = HealthResponseDtoFlags.from_dict(d.pop("flags"))

        status = d.pop("status")

        timestamp = d.pop("timestamp")

        version = d.pop("version")

        health_response_dto = cls(
            flags=flags,
            status=status,
            timestamp=timestamp,
            version=version,
        )

        health_response_dto.additional_properties = d
        return health_response_dto

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
