from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activation_output_body_versions import ActivationOutputBodyVersions


T = TypeVar("T", bound="ActivationOutputBody")


@_attrs_define
class ActivationOutputBody:
    """
    Attributes:
        versions (ActivationOutputBodyVersions):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    versions: ActivationOutputBodyVersions
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activation_output_body_versions import ActivationOutputBodyVersions

        versions = self.versions.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "versions": versions,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activation_output_body_versions import ActivationOutputBodyVersions

        d = dict(src_dict)
        versions = ActivationOutputBodyVersions.from_dict(d.pop("versions"))

        schema = d.pop("$schema", UNSET)

        activation_output_body = cls(
            versions=versions,
            schema=schema,
        )

        return activation_output_body
