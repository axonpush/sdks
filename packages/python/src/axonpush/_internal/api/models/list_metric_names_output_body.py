from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_name_dto import MetricNameDTO


T = TypeVar("T", bound="ListMetricNamesOutputBody")


@_attrs_define
class ListMetricNamesOutputBody:
    """
    Attributes:
        metrics (list[MetricNameDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    metrics: list[MetricNameDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_name_dto import MetricNameDTO

        metrics: list[dict[str, Any]] | None
        if isinstance(self.metrics, list):
            metrics = []
            for metrics_type_0_item_data in self.metrics:
                metrics_type_0_item = metrics_type_0_item_data.to_dict()
                metrics.append(metrics_type_0_item)

        else:
            metrics = self.metrics

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metrics": metrics,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_name_dto import MetricNameDTO

        d = dict(src_dict)

        def _parse_metrics(data: object) -> list[MetricNameDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metrics_type_0 = []
                _metrics_type_0 = data
                for metrics_type_0_item_data in _metrics_type_0:
                    metrics_type_0_item = MetricNameDTO.from_dict(metrics_type_0_item_data)

                    metrics_type_0.append(metrics_type_0_item)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MetricNameDTO] | None, data)

        metrics = _parse_metrics(d.pop("metrics"))

        schema = d.pop("$schema", UNSET)

        list_metric_names_output_body = cls(
            metrics=metrics,
            schema=schema,
        )

        return list_metric_names_output_body
