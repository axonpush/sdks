from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_capture_mode import ContentCaptureMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry_policy_dto_environment_overrides import (
        TelemetryPolicyDtoEnvironmentOverrides,
    )
    from ..models.telemetry_regex_rule_dto import TelemetryRegexRuleDto


T = TypeVar("T", bound="TelemetryPolicyDto")


@_attrs_define
class TelemetryPolicyDto:
    """
    Attributes:
        content_capture_mode (ContentCaptureMode):  Default: ContentCaptureMode.METADATA_ONLY.
        environment_overrides (TelemetryPolicyDtoEnvironmentOverrides): Per-environment overrides, keyed by environment
            slug.
        max_string_length (float):  Default: 4096.0.
        redacted_paths (list[str]):
        regex_rules (list[TelemetryRegexRuleDto]):
    """

    environment_overrides: TelemetryPolicyDtoEnvironmentOverrides
    redacted_paths: list[str]
    regex_rules: list[TelemetryRegexRuleDto]
    content_capture_mode: ContentCaptureMode = ContentCaptureMode.METADATA_ONLY
    max_string_length: float = 4096.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.telemetry_policy_dto_environment_overrides import (
            TelemetryPolicyDtoEnvironmentOverrides,
        )
        from ..models.telemetry_regex_rule_dto import TelemetryRegexRuleDto

        content_capture_mode = self.content_capture_mode.value

        environment_overrides = self.environment_overrides.to_dict()

        max_string_length = self.max_string_length

        redacted_paths = self.redacted_paths

        regex_rules = []
        for regex_rules_item_data in self.regex_rules:
            regex_rules_item = regex_rules_item_data.to_dict()
            regex_rules.append(regex_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentCaptureMode": content_capture_mode,
                "environmentOverrides": environment_overrides,
                "maxStringLength": max_string_length,
                "redactedPaths": redacted_paths,
                "regexRules": regex_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.telemetry_policy_dto_environment_overrides import (
            TelemetryPolicyDtoEnvironmentOverrides,
        )
        from ..models.telemetry_regex_rule_dto import TelemetryRegexRuleDto

        d = dict(src_dict)
        content_capture_mode = ContentCaptureMode(d.pop("contentCaptureMode"))

        environment_overrides = TelemetryPolicyDtoEnvironmentOverrides.from_dict(
            d.pop("environmentOverrides")
        )

        max_string_length = d.pop("maxStringLength")

        redacted_paths = cast(list[str], d.pop("redactedPaths"))

        regex_rules = []
        _regex_rules = d.pop("regexRules")
        for regex_rules_item_data in _regex_rules:
            regex_rules_item = TelemetryRegexRuleDto.from_dict(regex_rules_item_data)

            regex_rules.append(regex_rules_item)

        telemetry_policy_dto = cls(
            content_capture_mode=content_capture_mode,
            environment_overrides=environment_overrides,
            max_string_length=max_string_length,
            redacted_paths=redacted_paths,
            regex_rules=regex_rules,
        )

        telemetry_policy_dto.additional_properties = d
        return telemetry_policy_dto

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
