from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_check_dto import ActionCheckDto
    from ..models.observe_action_dto_observed_fields import ObserveActionDtoObservedFields


T = TypeVar("T", bound="ObserveActionDto")


@_attrs_define
class ObserveActionDto:
    """
    Attributes:
        checks (list[ActionCheckDto]):
        object_ref (str):
        observation_id (str):
        observed_at (datetime.datetime):
        observed_fields (ObserveActionDtoObservedFields):
        provider (str):
        provider_account_ref (str):
        sequence (float):
        verifier_version (str):
    """

    checks: list[ActionCheckDto]
    object_ref: str
    observation_id: str
    observed_at: datetime.datetime
    observed_fields: ObserveActionDtoObservedFields
    provider: str
    provider_account_ref: str
    sequence: float
    verifier_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_check_dto import ActionCheckDto
        from ..models.observe_action_dto_observed_fields import ObserveActionDtoObservedFields

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)

        object_ref = self.object_ref

        observation_id = self.observation_id

        observed_at = self.observed_at.isoformat()

        observed_fields = self.observed_fields.to_dict()

        provider = self.provider

        provider_account_ref = self.provider_account_ref

        sequence = self.sequence

        verifier_version = self.verifier_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checks": checks,
                "objectRef": object_ref,
                "observationId": observation_id,
                "observedAt": observed_at,
                "observedFields": observed_fields,
                "provider": provider,
                "providerAccountRef": provider_account_ref,
                "sequence": sequence,
                "verifierVersion": verifier_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_check_dto import ActionCheckDto
        from ..models.observe_action_dto_observed_fields import ObserveActionDtoObservedFields

        d = dict(src_dict)
        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = ActionCheckDto.from_dict(checks_item_data)

            checks.append(checks_item)

        object_ref = d.pop("objectRef")

        observation_id = d.pop("observationId")

        observed_at = isoparse(d.pop("observedAt"))

        observed_fields = ObserveActionDtoObservedFields.from_dict(d.pop("observedFields"))

        provider = d.pop("provider")

        provider_account_ref = d.pop("providerAccountRef")

        sequence = d.pop("sequence")

        verifier_version = d.pop("verifierVersion")

        observe_action_dto = cls(
            checks=checks,
            object_ref=object_ref,
            observation_id=observation_id,
            observed_at=observed_at,
            observed_fields=observed_fields,
            provider=provider,
            provider_account_ref=provider_account_ref,
            sequence=sequence,
            verifier_version=verifier_version,
        )

        observe_action_dto.additional_properties = d
        return observe_action_dto

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
