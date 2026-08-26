from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_capture_mode import ContentCaptureMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telemetry_regex_rule_dto import TelemetryRegexRuleDto


T = TypeVar("T", bound="TelemetryPolicyOverrideDto")


@_attrs_define
class TelemetryPolicyOverrideDto:
    """
    Attributes:
        content_capture_mode (ContentCaptureMode | Unset):
        max_string_length (float | Unset):
        redacted_paths (list[str] | Unset):
        regex_rules (list[TelemetryRegexRuleDto] | Unset):
    """

    content_capture_mode: ContentCaptureMode | Unset = UNSET
    max_string_length: float | Unset = UNSET
    redacted_paths: list[str] | Unset = UNSET
    regex_rules: list[TelemetryRegexRuleDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.telemetry_regex_rule_dto import TelemetryRegexRuleDto

        content_capture_mode: str | Unset = UNSET
        if not isinstance(self.content_capture_mode, Unset):
            content_capture_mode = self.content_capture_mode.value

        max_string_length = self.max_string_length

        redacted_paths: list[str] | Unset = UNSET
        if not isinstance(self.redacted_paths, Unset):
            redacted_paths = self.redacted_paths

        regex_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regex_rules, Unset):
            regex_rules = []
            for regex_rules_item_data in self.regex_rules:
                regex_rules_item = regex_rules_item_data.to_dict()
                regex_rules.append(regex_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_capture_mode is not UNSET:
            field_dict["contentCaptureMode"] = content_capture_mode
        if max_string_length is not UNSET:
            field_dict["maxStringLength"] = max_string_length
        if redacted_paths is not UNSET:
            field_dict["redactedPaths"] = redacted_paths
        if regex_rules is not UNSET:
            field_dict["regexRules"] = regex_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.telemetry_regex_rule_dto import TelemetryRegexRuleDto

        d = dict(src_dict)
        _content_capture_mode = d.pop("contentCaptureMode", UNSET)
        content_capture_mode: ContentCaptureMode | Unset
        if isinstance(_content_capture_mode, Unset):
            content_capture_mode = UNSET
        else:
            content_capture_mode = ContentCaptureMode(_content_capture_mode)

        max_string_length = d.pop("maxStringLength", UNSET)

        redacted_paths = cast(list[str], d.pop("redactedPaths", UNSET))

        _regex_rules = d.pop("regexRules", UNSET)
        regex_rules: list[TelemetryRegexRuleDto] | Unset = UNSET
        if _regex_rules is not UNSET:
            regex_rules = []
            for regex_rules_item_data in _regex_rules:
                regex_rules_item = TelemetryRegexRuleDto.from_dict(regex_rules_item_data)

                regex_rules.append(regex_rules_item)

        telemetry_policy_override_dto = cls(
            content_capture_mode=content_capture_mode,
            max_string_length=max_string_length,
            redacted_paths=redacted_paths,
            regex_rules=regex_rules,
        )

        telemetry_policy_override_dto.additional_properties = d
        return telemetry_policy_override_dto

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
