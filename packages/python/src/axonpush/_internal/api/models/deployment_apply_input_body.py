from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentApplyInputBody")


@_attrs_define
class DeploymentApplyInputBody:
    """
    Attributes:
        runtime_id (str):
        source (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        expected_active_version_id (str | Unset):
    """

    runtime_id: str
    source: str
    schema: str | Unset = UNSET
    expected_active_version_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        runtime_id = self.runtime_id

        source = self.source

        schema = self.schema

        expected_active_version_id = self.expected_active_version_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "runtime_id": runtime_id,
                "source": source,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if expected_active_version_id is not UNSET:
            field_dict["expected_active_version_id"] = expected_active_version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        runtime_id = d.pop("runtime_id")

        source = d.pop("source")

        schema = d.pop("$schema", UNSET)

        expected_active_version_id = d.pop("expected_active_version_id", UNSET)

        deployment_apply_input_body = cls(
            runtime_id=runtime_id,
            source=source,
            schema=schema,
            expected_active_version_id=expected_active_version_id,
        )

        return deployment_apply_input_body
