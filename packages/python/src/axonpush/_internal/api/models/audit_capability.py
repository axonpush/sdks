from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditCapability")


@_attrs_define
class AuditCapability:
    """
    Attributes:
        enabled (bool):
        formats (list[str] | None):
    """

    enabled: bool
    formats: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        formats: list[str] | None
        if isinstance(self.formats, list):
            formats = self.formats

        else:
            formats = self.formats

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "formats": formats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_formats(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                formats_type_0 = cast(list[str], data)

                return formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        formats = _parse_formats(d.pop("formats"))

        audit_capability = cls(
            enabled=enabled,
            formats=formats,
        )

        return audit_capability
