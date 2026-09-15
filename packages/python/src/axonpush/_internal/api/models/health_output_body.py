from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthOutputBody")


@_attrs_define
class HealthOutputBody:
    """
    Attributes:
        service (str): Entrypoint name
        status (str): Service health status
        version (str): Build version
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    service: str
    status: str
    version: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        status = self.status

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "service": service,
                "status": status,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service = d.pop("service")

        status = d.pop("status")

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        health_output_body = cls(
            service=service,
            status=status,
            version=version,
            schema=schema,
        )

        return health_output_body
