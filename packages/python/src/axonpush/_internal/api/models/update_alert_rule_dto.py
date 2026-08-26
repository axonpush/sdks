from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_destination_type import AlertDestinationType
from ..models.alert_metric import AlertMetric
from ..models.alert_operator import AlertOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertRuleDto")


@_attrs_define
class UpdateAlertRuleDto:
    """
    Attributes:
        app_id (str | Unset):
        destination (str | Unset): Email address or an existing webhook endpoint ID.
        destination_type (AlertDestinationType | Unset):
        enabled (bool | Unset):  Default: True.
        environment_id (str | Unset):
        metric (AlertMetric | Unset):
        model (str | Unset):
        name (str | Unset):
        operator (AlertOperator | Unset):
        release (str | Unset):
        service (str | Unset):
        threshold (float | Unset):
    """

    app_id: str | Unset = UNSET
    destination: str | Unset = UNSET
    destination_type: AlertDestinationType | Unset = UNSET
    enabled: bool | Unset = True
    environment_id: str | Unset = UNSET
    metric: AlertMetric | Unset = UNSET
    model: str | Unset = UNSET
    name: str | Unset = UNSET
    operator: AlertOperator | Unset = UNSET
    release: str | Unset = UNSET
    service: str | Unset = UNSET
    threshold: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        destination = self.destination

        destination_type: str | Unset = UNSET
        if not isinstance(self.destination_type, Unset):
            destination_type = self.destination_type.value

        enabled = self.enabled

        environment_id = self.environment_id

        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.value

        model = self.model

        name = self.name

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        release = self.release

        service = self.service

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if destination is not UNSET:
            field_dict["destination"] = destination
        if destination_type is not UNSET:
            field_dict["destinationType"] = destination_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if metric is not UNSET:
            field_dict["metric"] = metric
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if operator is not UNSET:
            field_dict["operator"] = operator
        if release is not UNSET:
            field_dict["release"] = release
        if service is not UNSET:
            field_dict["service"] = service
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId", UNSET)

        destination = d.pop("destination", UNSET)

        _destination_type = d.pop("destinationType", UNSET)
        destination_type: AlertDestinationType | Unset
        if isinstance(_destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = AlertDestinationType(_destination_type)

        enabled = d.pop("enabled", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        _metric = d.pop("metric", UNSET)
        metric: AlertMetric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = AlertMetric(_metric)

        model = d.pop("model", UNSET)

        name = d.pop("name", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: AlertOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = AlertOperator(_operator)

        release = d.pop("release", UNSET)

        service = d.pop("service", UNSET)

        threshold = d.pop("threshold", UNSET)

        update_alert_rule_dto = cls(
            app_id=app_id,
            destination=destination,
            destination_type=destination_type,
            enabled=enabled,
            environment_id=environment_id,
            metric=metric,
            model=model,
            name=name,
            operator=operator,
            release=release,
            service=service,
            threshold=threshold,
        )

        update_alert_rule_dto.additional_properties = d
        return update_alert_rule_dto

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
