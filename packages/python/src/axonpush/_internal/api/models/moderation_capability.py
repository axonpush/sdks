from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModerationCapability")


@_attrs_define
class ModerationCapability:
    """
    Attributes:
        actions (list[str] | None):
        detectors (list[str] | None):
        enabled (bool):
        targets (list[str] | None):
    """

    actions: list[str] | None
    detectors: list[str] | None
    enabled: bool
    targets: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        actions: list[str] | None
        if isinstance(self.actions, list):
            actions = self.actions

        else:
            actions = self.actions

        detectors: list[str] | None
        if isinstance(self.detectors, list):
            detectors = self.detectors

        else:
            detectors = self.detectors

        enabled = self.enabled

        targets: list[str] | None
        if isinstance(self.targets, list):
            targets = self.targets

        else:
            targets = self.targets

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actions": actions,
                "detectors": detectors,
                "enabled": enabled,
                "targets": targets,
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

        def _parse_detectors(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detectors_type_0 = cast(list[str], data)

                return detectors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        detectors = _parse_detectors(d.pop("detectors"))

        enabled = d.pop("enabled")

        def _parse_targets(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                targets_type_0 = cast(list[str], data)

                return targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        targets = _parse_targets(d.pop("targets"))

        moderation_capability = cls(
            actions=actions,
            detectors=detectors,
            enabled=enabled,
            targets=targets,
        )

        return moderation_capability
