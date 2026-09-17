from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.policy_body_destination_type import PolicyBodyDestinationType
from ..models.policy_body_window_type import PolicyBodyWindowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rung import Rung


T = TypeVar("T", bound="PolicyBody")


@_attrs_define
class PolicyBody:
    """
    Attributes:
        limit_usd (float): the 100% amount in USD
        name (str):
        rungs (list[Rung] | None): ordered ladder: each rung is {atPercent, action, blockMode?, fallbackModel?}
        window_type (PolicyBodyWindowType):
        schema (str | Unset): A URL to the JSON Schema for this object.
        api_key_id (str | Unset):
        app_id (str | Unset):
        cooldown_mins (int | Unset):
        destination (str | Unset):
        destination_type (PolicyBodyDestinationType | Unset):
        enabled (bool | Unset):
        environment_id (str | Unset):
        model (str | Unset): model prefix; empty = all models
        provider (str | Unset):
        tag_key (str | Unset):
        tag_value (str | Unset):
        user_id (str | Unset):
    """

    limit_usd: float
    name: str
    rungs: list[Rung] | None
    window_type: PolicyBodyWindowType
    schema: str | Unset = UNSET
    api_key_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    cooldown_mins: int | Unset = UNSET
    destination: str | Unset = UNSET
    destination_type: PolicyBodyDestinationType | Unset = UNSET
    enabled: bool | Unset = UNSET
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    provider: str | Unset = UNSET
    tag_key: str | Unset = UNSET
    tag_value: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.rung import Rung

        limit_usd = self.limit_usd

        name = self.name

        rungs: list[dict[str, Any]] | None
        if isinstance(self.rungs, list):
            rungs = []
            for rungs_type_0_item_data in self.rungs:
                rungs_type_0_item = rungs_type_0_item_data.to_dict()
                rungs.append(rungs_type_0_item)

        else:
            rungs = self.rungs

        window_type = self.window_type.value

        schema = self.schema

        api_key_id = self.api_key_id

        app_id = self.app_id

        cooldown_mins = self.cooldown_mins

        destination = self.destination

        destination_type: str | Unset = UNSET
        if not isinstance(self.destination_type, Unset):
            destination_type = self.destination_type.value

        enabled = self.enabled

        environment_id = self.environment_id

        model = self.model

        provider = self.provider

        tag_key = self.tag_key

        tag_value = self.tag_value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "limitUsd": limit_usd,
                "name": name,
                "rungs": rungs,
                "windowType": window_type,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if api_key_id is not UNSET:
            field_dict["apiKeyId"] = api_key_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if cooldown_mins is not UNSET:
            field_dict["cooldownMins"] = cooldown_mins
        if destination is not UNSET:
            field_dict["destination"] = destination
        if destination_type is not UNSET:
            field_dict["destinationType"] = destination_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
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
        limit_usd = d.pop("limitUsd")

        name = d.pop("name")

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

        window_type = PolicyBodyWindowType(d.pop("windowType"))

        schema = d.pop("$schema", UNSET)

        api_key_id = d.pop("apiKeyId", UNSET)

        app_id = d.pop("appId", UNSET)

        cooldown_mins = d.pop("cooldownMins", UNSET)

        destination = d.pop("destination", UNSET)

        _destination_type = d.pop("destinationType", UNSET)
        destination_type: PolicyBodyDestinationType | Unset
        if isinstance(_destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = PolicyBodyDestinationType(_destination_type)

        enabled = d.pop("enabled", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        provider = d.pop("provider", UNSET)

        tag_key = d.pop("tagKey", UNSET)

        tag_value = d.pop("tagValue", UNSET)

        user_id = d.pop("userId", UNSET)

        policy_body = cls(
            limit_usd=limit_usd,
            name=name,
            rungs=rungs,
            window_type=window_type,
            schema=schema,
            api_key_id=api_key_id,
            app_id=app_id,
            cooldown_mins=cooldown_mins,
            destination=destination,
            destination_type=destination_type,
            enabled=enabled,
            environment_id=environment_id,
            model=model,
            provider=provider,
            tag_key=tag_key,
            tag_value=tag_value,
            user_id=user_id,
        )

        return policy_body
