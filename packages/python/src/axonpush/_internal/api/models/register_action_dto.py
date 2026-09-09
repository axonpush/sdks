from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.register_action_dto_intended_fields import RegisterActionDtoIntendedFields


T = TypeVar("T", bound="RegisterActionDto")


@_attrs_define
class RegisterActionDto:
    """
    Attributes:
        action_id (str):
        app_id (str):
        contract_id (str):
        contract_version (float):
        environment_id (str):
        intended_fields (RegisterActionDtoIntendedFields):
        intent_source (str):
        object_ref (str):
        provider (str):
        provider_account_ref (str):
        span_id (str | Unset):
        trace_id (str | Unset):
    """

    action_id: str
    app_id: str
    contract_id: str
    contract_version: float
    environment_id: str
    intended_fields: RegisterActionDtoIntendedFields
    intent_source: str
    object_ref: str
    provider: str
    provider_account_ref: str
    span_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.register_action_dto_intended_fields import RegisterActionDtoIntendedFields

        action_id = self.action_id

        app_id = self.app_id

        contract_id = self.contract_id

        contract_version = self.contract_version

        environment_id = self.environment_id

        intended_fields = self.intended_fields.to_dict()

        intent_source = self.intent_source

        object_ref = self.object_ref

        provider = self.provider

        provider_account_ref = self.provider_account_ref

        span_id = self.span_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionId": action_id,
                "appId": app_id,
                "contractId": contract_id,
                "contractVersion": contract_version,
                "environmentId": environment_id,
                "intendedFields": intended_fields,
                "intentSource": intent_source,
                "objectRef": object_ref,
                "provider": provider,
                "providerAccountRef": provider_account_ref,
            }
        )
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_action_dto_intended_fields import RegisterActionDtoIntendedFields

        d = dict(src_dict)
        action_id = d.pop("actionId")

        app_id = d.pop("appId")

        contract_id = d.pop("contractId")

        contract_version = d.pop("contractVersion")

        environment_id = d.pop("environmentId")

        intended_fields = RegisterActionDtoIntendedFields.from_dict(d.pop("intendedFields"))

        intent_source = d.pop("intentSource")

        object_ref = d.pop("objectRef")

        provider = d.pop("provider")

        provider_account_ref = d.pop("providerAccountRef")

        span_id = d.pop("spanId", UNSET)

        trace_id = d.pop("traceId", UNSET)

        register_action_dto = cls(
            action_id=action_id,
            app_id=app_id,
            contract_id=contract_id,
            contract_version=contract_version,
            environment_id=environment_id,
            intended_fields=intended_fields,
            intent_source=intent_source,
            object_ref=object_ref,
            provider=provider,
            provider_account_ref=provider_account_ref,
            span_id=span_id,
            trace_id=trace_id,
        )

        register_action_dto.additional_properties = d
        return register_action_dto

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
