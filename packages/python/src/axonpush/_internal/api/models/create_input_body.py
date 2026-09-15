from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_input_body_destination_type import CreateInputBodyDestinationType
from ..models.create_input_body_metric import CreateInputBodyMetric
from ..models.create_input_body_operator import CreateInputBodyOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInputBody")


@_attrs_define
class CreateInputBody:
    """
    Attributes:
        destination (str):
        destination_type (CreateInputBodyDestinationType):
        metric (CreateInputBodyMetric):
        name (str): Alert rule display name
        operator (CreateInputBodyOperator):
        threshold (float):
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset):
        enabled (bool | Unset):
        environment_id (str | Unset):
        model (str | Unset):
        release (str | Unset):
        service (str | Unset):
    """

    destination: str
    destination_type: CreateInputBodyDestinationType
    metric: CreateInputBodyMetric
    name: str
    operator: CreateInputBodyOperator
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

        destination_type = CreateInputBodyDestinationType(d.pop("destinationType"))

        metric = CreateInputBodyMetric(d.pop("metric"))

        name = d.pop("name")

        operator = CreateInputBodyOperator(d.pop("operator"))

        threshold = d.pop("threshold")

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        enabled = d.pop("enabled", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        model = d.pop("model", UNSET)

        release = d.pop("release", UNSET)

        service = d.pop("service", UNSET)

        create_input_body = cls(
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

        return create_input_body
