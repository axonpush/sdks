from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.govern_rules import GovernRules


T = TypeVar("T", bound="GovernPolicyView")


@_attrs_define
class GovernPolicyView:
    """
    Attributes:
        created_at (str):
        enabled (bool):
        enforcement (str):
        name (str):
        policy_id (str):
        rules (GovernRules):
        updated_at (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        api_key_id (str | Unset):
        app_id (str | Unset):
        environment_id (str | Unset):
        model (str | Unset):
        provider (str | Unset):
        user_id (str | Unset):
    """

    created_at: str
    enabled: bool
    enforcement: str
    name: str
    policy_id: str
    rules: GovernRules
    updated_at: str
    schema: str | Unset = UNSET
    api_key_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    provider: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.govern_rules import GovernRules

        created_at = self.created_at

        enabled = self.enabled

        enforcement = self.enforcement

        name = self.name

        policy_id = self.policy_id

        rules = self.rules.to_dict()

        updated_at = self.updated_at

        schema = self.schema

        api_key_id = self.api_key_id

        app_id = self.app_id

        environment_id = self.environment_id

        model = self.model

        provider = self.provider

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "enabled": enabled,
                "enforcement": enforcement,
                "name": name,
                "policyId": policy_id,
                "rules": rules,
                "updatedAt": updated_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if api_key_id is not UNSET:
            field_dict["apiKeyId"] = api_key_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
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
        created_at = d.pop("createdAt")

        enabled = d.pop("enabled")

        enforcement = d.pop("enforcement")

        name = d.pop("name")

        policy_id = d.pop("policyId")

        rules = GovernRules.from_dict(d.pop("rules"))

        updated_at = d.pop("updatedAt")

        schema = d.pop("$schema", UNSET)

        api_key_id = d.pop("apiKeyId", UNSET)

        app_id = d.pop("appId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        provider = d.pop("provider", UNSET)

        user_id = d.pop("userId", UNSET)

        govern_policy_view = cls(
            created_at=created_at,
            enabled=enabled,
            enforcement=enforcement,
            name=name,
            policy_id=policy_id,
            rules=rules,
            updated_at=updated_at,
            schema=schema,
            api_key_id=api_key_id,
            app_id=app_id,
            environment_id=environment_id,
            model=model,
            provider=provider,
            user_id=user_id,
        )

        return govern_policy_view
