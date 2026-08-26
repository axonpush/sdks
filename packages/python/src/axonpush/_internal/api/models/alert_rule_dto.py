from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.alert_destination_type import AlertDestinationType
from ..models.alert_metric import AlertMetric
from ..models.alert_operator import AlertOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertRuleDto")


@_attrs_define
class AlertRuleDto:
    """
    Attributes:
        alert_rule_id (str):
        created_at (datetime.datetime):
        destination (str): Email address or an existing webhook endpoint ID.
        destination_type (AlertDestinationType):
        metric (AlertMetric):
        name (str):
        operator (AlertOperator):
        org_id (str):
        threshold (float):
        updated_at (datetime.datetime):
        app_id (str | Unset):
        enabled (bool | Unset):  Default: True.
        environment_id (str | Unset):
        model (str | Unset):
        release (str | Unset):
        service (str | Unset):
    """

    alert_rule_id: str
    created_at: datetime.datetime
    destination: str
    destination_type: AlertDestinationType
    metric: AlertMetric
    name: str
    operator: AlertOperator
    org_id: str
    threshold: float
    updated_at: datetime.datetime
    app_id: str | Unset = UNSET
    enabled: bool | Unset = True
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    release: str | Unset = UNSET
    service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_rule_id = self.alert_rule_id

        created_at = self.created_at.isoformat()

        destination = self.destination

        destination_type = self.destination_type.value

        metric = self.metric.value

        name = self.name

        operator = self.operator.value

        org_id = self.org_id

        threshold = self.threshold

        updated_at = self.updated_at.isoformat()

        app_id = self.app_id

        enabled = self.enabled

        environment_id = self.environment_id

        model = self.model

        release = self.release

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alertRuleId": alert_rule_id,
                "createdAt": created_at,
                "destination": destination,
                "destinationType": destination_type,
                "metric": metric,
                "name": name,
                "operator": operator,
                "orgId": org_id,
                "threshold": threshold,
                "updatedAt": updated_at,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if model is not UNSET:
            field_dict["model"] = model
        if release is not UNSET:
            field_dict["release"] = release
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_rule_id = d.pop("alertRuleId")

        created_at = isoparse(d.pop("createdAt"))

        destination = d.pop("destination")

        destination_type = AlertDestinationType(d.pop("destinationType"))

        metric = AlertMetric(d.pop("metric"))

        name = d.pop("name")

        operator = AlertOperator(d.pop("operator"))

        org_id = d.pop("orgId")

        threshold = d.pop("threshold")

        updated_at = isoparse(d.pop("updatedAt"))

        app_id = d.pop("appId", UNSET)

        enabled = d.pop("enabled", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        release = d.pop("release", UNSET)

        service = d.pop("service", UNSET)

        alert_rule_dto = cls(
            alert_rule_id=alert_rule_id,
            created_at=created_at,
            destination=destination,
            destination_type=destination_type,
            metric=metric,
            name=name,
            operator=operator,
            org_id=org_id,
            threshold=threshold,
            updated_at=updated_at,
            app_id=app_id,
            enabled=enabled,
            environment_id=environment_id,
            model=model,
            release=release,
            service=service,
        )

        alert_rule_dto.additional_properties = d
        return alert_rule_dto

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
