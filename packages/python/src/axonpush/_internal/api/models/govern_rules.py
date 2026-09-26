from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GovernRules")


@_attrs_define
class GovernRules:
    """
    Attributes:
        allowed_models (list[str] | None | Unset):
        allowed_tools (list[str] | None | Unset):
        default_model (str | Unset):
        denied_tools (list[str] | None | Unset):
        max_tokens (int | Unset):
        reasoning_effort_cap (str | Unset):
        reasoning_tokens_cap (int | Unset):
        require_safety_identifier (bool | Unset):
        require_structured_output (bool | Unset):
        service_tier (str | Unset):
        temperature_max (float | Unset):
    """

    allowed_models: list[str] | None | Unset = UNSET
    allowed_tools: list[str] | None | Unset = UNSET
    default_model: str | Unset = UNSET
    denied_tools: list[str] | None | Unset = UNSET
    max_tokens: int | Unset = UNSET
    reasoning_effort_cap: str | Unset = UNSET
    reasoning_tokens_cap: int | Unset = UNSET
    require_safety_identifier: bool | Unset = UNSET
    require_structured_output: bool | Unset = UNSET
    service_tier: str | Unset = UNSET
    temperature_max: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_models: list[str] | None | Unset
        if isinstance(self.allowed_models, Unset):
            allowed_models = UNSET
        elif isinstance(self.allowed_models, list):
            allowed_models = self.allowed_models

        else:
            allowed_models = self.allowed_models

        allowed_tools: list[str] | None | Unset
        if isinstance(self.allowed_tools, Unset):
            allowed_tools = UNSET
        elif isinstance(self.allowed_tools, list):
            allowed_tools = self.allowed_tools

        else:
            allowed_tools = self.allowed_tools

        default_model = self.default_model

        denied_tools: list[str] | None | Unset
        if isinstance(self.denied_tools, Unset):
            denied_tools = UNSET
        elif isinstance(self.denied_tools, list):
            denied_tools = self.denied_tools

        else:
            denied_tools = self.denied_tools

        max_tokens = self.max_tokens

        reasoning_effort_cap = self.reasoning_effort_cap

        reasoning_tokens_cap = self.reasoning_tokens_cap

        require_safety_identifier = self.require_safety_identifier

        require_structured_output = self.require_structured_output

        service_tier = self.service_tier

        temperature_max = self.temperature_max

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_models is not UNSET:
            field_dict["allowedModels"] = allowed_models
        if allowed_tools is not UNSET:
            field_dict["allowedTools"] = allowed_tools
        if default_model is not UNSET:
            field_dict["defaultModel"] = default_model
        if denied_tools is not UNSET:
            field_dict["deniedTools"] = denied_tools
        if max_tokens is not UNSET:
            field_dict["maxTokens"] = max_tokens
        if reasoning_effort_cap is not UNSET:
            field_dict["reasoningEffortCap"] = reasoning_effort_cap
        if reasoning_tokens_cap is not UNSET:
            field_dict["reasoningTokensCap"] = reasoning_tokens_cap
        if require_safety_identifier is not UNSET:
            field_dict["requireSafetyIdentifier"] = require_safety_identifier
        if require_structured_output is not UNSET:
            field_dict["requireStructuredOutput"] = require_structured_output
        if service_tier is not UNSET:
            field_dict["serviceTier"] = service_tier
        if temperature_max is not UNSET:
            field_dict["temperatureMax"] = temperature_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_allowed_models(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_models_type_0 = cast(list[str], data)

                return allowed_models_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_models = _parse_allowed_models(d.pop("allowedModels", UNSET))

        def _parse_allowed_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_tools_type_0 = cast(list[str], data)

                return allowed_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_tools = _parse_allowed_tools(d.pop("allowedTools", UNSET))

        default_model = d.pop("defaultModel", UNSET)

        def _parse_denied_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                denied_tools_type_0 = cast(list[str], data)

                return denied_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        denied_tools = _parse_denied_tools(d.pop("deniedTools", UNSET))

        max_tokens = d.pop("maxTokens", UNSET)

        reasoning_effort_cap = d.pop("reasoningEffortCap", UNSET)

        reasoning_tokens_cap = d.pop("reasoningTokensCap", UNSET)

        require_safety_identifier = d.pop("requireSafetyIdentifier", UNSET)

        require_structured_output = d.pop("requireStructuredOutput", UNSET)

        service_tier = d.pop("serviceTier", UNSET)

        temperature_max = d.pop("temperatureMax", UNSET)

        govern_rules = cls(
            allowed_models=allowed_models,
            allowed_tools=allowed_tools,
            default_model=default_model,
            denied_tools=denied_tools,
            max_tokens=max_tokens,
            reasoning_effort_cap=reasoning_effort_cap,
            reasoning_tokens_cap=reasoning_tokens_cap,
            require_safety_identifier=require_safety_identifier,
            require_structured_output=require_structured_output,
            service_tier=service_tier,
            temperature_max=temperature_max,
        )

        return govern_rules
