from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.govern_policy_body_enforcement import GovernPolicyBodyEnforcement
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.govern_rules import GovernRules


T = TypeVar("T", bound="GovernPolicyBody")


@_attrs_define
class GovernPolicyBody:
    """
    Attributes:
        name (str):
        rules (GovernRules):
        schema (str | Unset): A URL to the JSON Schema for this object.
        api_key_id (str | Unset):
        app_id (str | Unset):
        enabled (bool | Unset):
        enforcement (GovernPolicyBodyEnforcement | Unset): enforce (mutate to comply, default) | block (reject 422) |
            warn (record only)
        environment_id (str | Unset):
        model (str | Unset): model prefix; empty = all models
        provider (str | Unset): openai | anthropic; empty = all providers
        user_id (str | Unset):
    """

    name: str
    rules: GovernRules
    schema: str | Unset = UNSET
    api_key_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    enforcement: GovernPolicyBodyEnforcement | Unset = UNSET
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    provider: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.govern_rules import GovernRules

        name = self.name

        rules = self.rules.to_dict()

        schema = self.schema

        api_key_id = self.api_key_id

        app_id = self.app_id

        enabled = self.enabled

        enforcement: str | Unset = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement.value

        environment_id = self.environment_id

        model = self.model

        provider = self.provider

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "rules": rules,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if api_key_id is not UNSET:
            field_dict["apiKeyId"] = api_key_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if model is not UNSET:
            field_dict["model"] = model
        if provider is not UNSET:
            field_dict["provider"] = provider
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.govern_rules import GovernRules

        d = dict(src_dict)
        name = d.pop("name")

        rules = GovernRules.from_dict(d.pop("rules"))

        schema = d.pop("$schema", UNSET)

        api_key_id = d.pop("apiKeyId", UNSET)

        app_id = d.pop("appId", UNSET)

        enabled = d.pop("enabled", UNSET)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: GovernPolicyBodyEnforcement | Unset
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = GovernPolicyBodyEnforcement(_enforcement)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        provider = d.pop("provider", UNSET)

        user_id = d.pop("userId", UNSET)

        govern_policy_body = cls(
            name=name,
            rules=rules,
            schema=schema,
            api_key_id=api_key_id,
            app_id=app_id,
            enabled=enabled,
            enforcement=enforcement,
            environment_id=environment_id,
            model=model,
            provider=provider,
            user_id=user_id,
        )

        return govern_policy_body
