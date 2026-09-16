from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_input_body_1_destination_type import UpdateInputBody1DestinationType
from ..models.update_input_body_1_metric import UpdateInputBody1Metric
from ..models.update_input_body_1_operator import UpdateInputBody1Operator
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateInputBody1")


@_attrs_define
class UpdateInputBody1:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        destination (str | Unset):
        destination_type (UpdateInputBody1DestinationType | Unset):
        enabled (bool | Unset):
        metric (UpdateInputBody1Metric | Unset):
        name (str | Unset):
        operator (UpdateInputBody1Operator | Unset):
        threshold (float | Unset):
    """

    schema: str | Unset = UNSET
    destination: str | Unset = UNSET
    destination_type: UpdateInputBody1DestinationType | Unset = UNSET
    enabled: bool | Unset = UNSET
    metric: UpdateInputBody1Metric | Unset = UNSET
    name: str | Unset = UNSET
    operator: UpdateInputBody1Operator | Unset = UNSET
    threshold: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        destination = self.destination

        destination_type: str | Unset = UNSET
        if not isinstance(self.destination_type, Unset):
            destination_type = self.destination_type.value

        enabled = self.enabled

        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.value

        name = self.name

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        threshold = self.threshold

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if destination is not UNSET:
            field_dict["destination"] = destination
        if destination_type is not UNSET:
            field_dict["destinationType"] = destination_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if metric is not UNSET:
            field_dict["metric"] = metric
        if name is not UNSET:
            field_dict["name"] = name
        if operator is not UNSET:
            field_dict["operator"] = operator
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        destination = d.pop("destination", UNSET)

        _destination_type = d.pop("destinationType", UNSET)
        destination_type: UpdateInputBody1DestinationType | Unset
        if isinstance(_destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = UpdateInputBody1DestinationType(_destination_type)

        enabled = d.pop("enabled", UNSET)

        _metric = d.pop("metric", UNSET)
        metric: UpdateInputBody1Metric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = UpdateInputBody1Metric(_metric)

        name = d.pop("name", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: UpdateInputBody1Operator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = UpdateInputBody1Operator(_operator)

        threshold = d.pop("threshold", UNSET)

        update_input_body_1 = cls(
            schema=schema,
            destination=destination,
            destination_type=destination_type,
            enabled=enabled,
            metric=metric,
            name=name,
            operator=operator,
            threshold=threshold,
        )

        return update_input_body_1
