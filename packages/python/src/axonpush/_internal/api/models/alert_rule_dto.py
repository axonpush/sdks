from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertRuleDTO")


@_attrs_define
class AlertRuleDTO:
    """
    Attributes:
        alert_rule_id (str):
        created_at (str):
        destination (str):
        destination_type (str):
        enabled (bool):
        metric (str):
        name (str):
        operator (str):
        org_id (str):
        threshold (float):
        updated_at (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset):
        environment_id (str | Unset):
        model (str | Unset):
        release (str | Unset):
        service (str | Unset):
    """

    alert_rule_id: str
    created_at: str
    destination: str
    destination_type: str
    enabled: bool
    metric: str
    name: str
    operator: str
    org_id: str
    threshold: float
    updated_at: str
    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    release: str | Unset = UNSET
    service: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        alert_rule_id = self.alert_rule_id

        created_at = self.created_at

        destination = self.destination

        destination_type = self.destination_type

        enabled = self.enabled

        metric = self.metric

        name = self.name

        operator = self.operator

        org_id = self.org_id

        threshold = self.threshold

        updated_at = self.updated_at

        schema = self.schema

        app_id = self.app_id

        environment_id = self.environment_id

        model = self.model

        release = self.release

        service = self.service

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alertRuleId": alert_rule_id,
                "createdAt": created_at,
                "destination": destination,
                "destinationType": destination_type,
                "enabled": enabled,
                "metric": metric,
                "name": name,
                "operator": operator,
                "orgId": org_id,
                "threshold": threshold,
                "updatedAt": updated_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if app_id is not UNSET:
            field_dict["appId"] = app_id
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

        created_at = d.pop("createdAt")

        destination = d.pop("destination")

        destination_type = d.pop("destinationType")

        enabled = d.pop("enabled")

        metric = d.pop("metric")

        name = d.pop("name")

        operator = d.pop("operator")

        org_id = d.pop("orgId")

        threshold = d.pop("threshold")

        updated_at = d.pop("updatedAt")

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        release = d.pop("release", UNSET)

        service = d.pop("service", UNSET)

        alert_rule_dto = cls(
            alert_rule_id=alert_rule_id,
            created_at=created_at,
            destination=destination,
            destination_type=destination_type,
            enabled=enabled,
            metric=metric,
            name=name,
            operator=operator,
            org_id=org_id,
            threshold=threshold,
            updated_at=updated_at,
            schema=schema,
            app_id=app_id,
            environment_id=environment_id,
            model=model,
            release=release,
            service=service,
        )

        return alert_rule_dto
