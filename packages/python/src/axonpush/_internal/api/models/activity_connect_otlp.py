from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityConnectOTLP")


@_attrs_define
class ActivityConnectOTLP:
    """
    Attributes:
        endpoint (str): OTEL_EXPORTER_OTLP_ENDPOINT; exporters append /v1/traces and /v1/logs
        header (str): OTEL_EXPORTER_OTLP_HEADERS value; contains the key
        logs_endpoint (str):
        traces_endpoint (str):
    """

    endpoint: str
    header: str
    logs_endpoint: str
    traces_endpoint: str

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        header = self.header

        logs_endpoint = self.logs_endpoint

        traces_endpoint = self.traces_endpoint

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
                "header": header,
                "logsEndpoint": logs_endpoint,
                "tracesEndpoint": traces_endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        header = d.pop("header")

        logs_endpoint = d.pop("logsEndpoint")

        traces_endpoint = d.pop("tracesEndpoint")

        activity_connect_otlp = cls(
            endpoint=endpoint,
            header=header,
            logs_endpoint=logs_endpoint,
            traces_endpoint=traces_endpoint,
        )

        return activity_connect_otlp
