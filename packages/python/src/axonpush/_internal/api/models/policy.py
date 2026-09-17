from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rung import Rung


T = TypeVar("T", bound="Policy")


@_attrs_define
class Policy:
    """
    Attributes:
        cooldown_mins (int):
        created_at (str):
        enabled (bool):
        limit_usd (float):
        name (str):
        policy_id (str):
        rungs (list[Rung] | None):
        updated_at (str):
        window_type (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        api_key_id (str | Unset):
        app_id (str | Unset):
        current_spend_usd (float | Unset):
        destination (str | Unset):
        destination_type (str | Unset):
        environment_id (str | Unset):
        model (str | Unset):
        provider (str | Unset):
        tag_key (str | Unset):
        tag_value (str | Unset):
        user_id (str | Unset):
    """

    cooldown_mins: int
    created_at: str
    enabled: bool
    limit_usd: float
    name: str
    policy_id: str
    rungs: list[Rung] | None
    updated_at: str
    window_type: str
    schema: str | Unset = UNSET
    api_key_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    current_spend_usd: float | Unset = UNSET
    destination: str | Unset = UNSET
    destination_type: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    provider: str | Unset = UNSET
    tag_key: str | Unset = UNSET
    tag_value: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.rung import Rung

        cooldown_mins = self.cooldown_mins

        created_at = self.created_at

        enabled = self.enabled

        limit_usd = self.limit_usd

        name = self.name

        policy_id = self.policy_id

        rungs: list[dict[str, Any]] | None
        if isinstance(self.rungs, list):
            rungs = []
            for rungs_type_0_item_data in self.rungs:
                rungs_type_0_item = rungs_type_0_item_data.to_dict()
                rungs.append(rungs_type_0_item)

        else:
            rungs = self.rungs

        updated_at = self.updated_at

        window_type = self.window_type

        schema = self.schema

        api_key_id = self.api_key_id

        app_id = self.app_id

        current_spend_usd = self.current_spend_usd

        destination = self.destination

        destination_type = self.destination_type

        environment_id = self.environment_id

        model = self.model

        provider = self.provider

        tag_key = self.tag_key

        tag_value = self.tag_value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cooldownMins": cooldown_mins,
                "createdAt": created_at,
                "enabled": enabled,
                "limitUsd": limit_usd,
                "name": name,
                "policyId": policy_id,
                "rungs": rungs,
                "updatedAt": updated_at,
                "windowType": window_type,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if api_key_id is not UNSET:
            field_dict["apiKeyId"] = api_key_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if current_spend_usd is not UNSET:
            field_dict["currentSpendUsd"] = current_spend_usd
        if destination is not UNSET:
            field_dict["destination"] = destination
        if destination_type is not UNSET:
            field_dict["destinationType"] = destination_type
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if model is not UNSET:
            field_dict["model"] = model
        if provider is not UNSET:
            field_dict["provider"] = provider
        if tag_key is not UNSET:
            field_dict["tagKey"] = tag_key
        if tag_value is not UNSET:
            field_dict["tagValue"] = tag_value
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rung import Rung

        d = dict(src_dict)
        cooldown_mins = d.pop("cooldownMins")

        created_at = d.pop("createdAt")

        enabled = d.pop("enabled")

        limit_usd = d.pop("limitUsd")

        name = d.pop("name")

        policy_id = d.pop("policyId")

        def _parse_rungs(data: object) -> list[Rung] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rungs_type_0 = []
                _rungs_type_0 = data
                for rungs_type_0_item_data in _rungs_type_0:
                    rungs_type_0_item = Rung.from_dict(rungs_type_0_item_data)

                    rungs_type_0.append(rungs_type_0_item)

                return rungs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Rung] | None, data)

        rungs = _parse_rungs(d.pop("rungs"))

        updated_at = d.pop("updatedAt")

        window_type = d.pop("windowType")

        schema = d.pop("$schema", UNSET)

        api_key_id = d.pop("apiKeyId", UNSET)

        app_id = d.pop("appId", UNSET)

        current_spend_usd = d.pop("currentSpendUsd", UNSET)

        destination = d.pop("destination", UNSET)

        destination_type = d.pop("destinationType", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        provider = d.pop("provider", UNSET)

        tag_key = d.pop("tagKey", UNSET)

        tag_value = d.pop("tagValue", UNSET)

        user_id = d.pop("userId", UNSET)

        policy = cls(
            cooldown_mins=cooldown_mins,
            created_at=created_at,
            enabled=enabled,
            limit_usd=limit_usd,
            name=name,
            policy_id=policy_id,
            rungs=rungs,
            updated_at=updated_at,
            window_type=window_type,
            schema=schema,
            api_key_id=api_key_id,
            app_id=app_id,
            current_spend_usd=current_spend_usd,
            destination=destination,
            destination_type=destination_type,
            environment_id=environment_id,
            model=model,
            provider=provider,
            tag_key=tag_key,
            tag_value=tag_value,
            user_id=user_id,
        )

        return policy
