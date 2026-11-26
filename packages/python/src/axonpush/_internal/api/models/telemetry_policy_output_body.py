from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryPolicyOutputBody")


@_attrs_define
class TelemetryPolicyOutputBody:
    """
    Attributes:
        policy (Any):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    policy: Any
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "policy": policy,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy = d.pop("policy")

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        telemetry_policy_output_body = cls(
            policy=policy,
            version=version,
            schema=schema,
        )

        return telemetry_policy_output_body
