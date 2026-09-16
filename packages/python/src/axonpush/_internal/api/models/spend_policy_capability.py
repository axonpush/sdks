from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendPolicyCapability")


@_attrs_define
class SpendPolicyCapability:
    """
    Attributes:
        actions (list[str] | None):
        dimensions (list[str] | None):
        enabled (bool):
        windows (list[str] | None):
    """

    actions: list[str] | None
    dimensions: list[str] | None
    enabled: bool
    windows: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        actions: list[str] | None
        if isinstance(self.actions, list):
            actions = self.actions

        else:
            actions = self.actions

        dimensions: list[str] | None
        if isinstance(self.dimensions, list):
            dimensions = self.dimensions

        else:
            dimensions = self.dimensions

        enabled = self.enabled

        windows: list[str] | None
        if isinstance(self.windows, list):
            windows = self.windows

        else:
            windows = self.windows

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actions": actions,
                "dimensions": dimensions,
                "enabled": enabled,
                "windows": windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_actions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_0 = cast(list[str], data)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        actions = _parse_actions(d.pop("actions"))

        def _parse_dimensions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dimensions_type_0 = cast(list[str], data)

                return dimensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        dimensions = _parse_dimensions(d.pop("dimensions"))

        enabled = d.pop("enabled")

        def _parse_windows(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                windows_type_0 = cast(list[str], data)

                return windows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        windows = _parse_windows(d.pop("windows"))

        spend_policy_capability = cls(
            actions=actions,
            dimensions=dimensions,
            enabled=enabled,
            windows=windows,
        )

        return spend_policy_capability
