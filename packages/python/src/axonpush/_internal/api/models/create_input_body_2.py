from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_input_body_2_destination_type import CreateInputBody2DestinationType
from ..models.create_input_body_2_metric import CreateInputBody2Metric
from ..models.create_input_body_2_operator import CreateInputBody2Operator
from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateInputBody2")


@_attrs_define
class CreateInputBody2:
    """
    Attributes:
        destination (str):
        destination_type (CreateInputBody2DestinationType):
        metric (CreateInputBody2Metric):
        name (str): Alert rule display name
        operator (CreateInputBody2Operator):
        threshold (float):
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset):
        enabled (bool | Unset):
        environment_id (str | Unset):
        model (str | Unset):
        release (str | Unset): Release scope; for crash_free_rate, the release whose sessions are measured (empty = all
            releases)
        service (str | Unset): Service name; the workflow stage for lifecycle_open; the monitor slug for monitor_failed
    """

    destination: str
    destination_type: CreateInputBody2DestinationType
    metric: CreateInputBody2Metric
    name: str
    operator: CreateInputBody2Operator
    threshold: float
    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    release: str | Unset = UNSET
    service: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        destination_type = self.destination_type.value

        metric = self.metric.value

        name = self.name

        operator = self.operator.value

        threshold = self.threshold

        schema = self.schema

        app_id = self.app_id

        enabled = self.enabled

        environment_id = self.environment_id

        model = self.model

        release = self.release

        service = self.service

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "destination": destination,
                "destinationType": destination_type,
                "metric": metric,
                "name": name,
                "operator": operator,
                "threshold": threshold,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
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
        destination = d.pop("destination")

        destination_type = CreateInputBody2DestinationType(d.pop("destinationType"))

        metric = CreateInputBody2Metric(d.pop("metric"))

        name = d.pop("name")

        operator = CreateInputBody2Operator(d.pop("operator"))

        threshold = d.pop("threshold")

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        enabled = d.pop("enabled", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        release = d.pop("release", UNSET)

        service = d.pop("service", UNSET)

        create_input_body_2 = cls(
            destination=destination,
            destination_type=destination_type,
            metric=metric,
            name=name,
            operator=operator,
            threshold=threshold,
            schema=schema,
            app_id=app_id,
            enabled=enabled,
            environment_id=environment_id,
            model=model,
            release=release,
            service=service,
        )

        return create_input_body_2
