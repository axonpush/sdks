from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="SetExtraFreeOrgsInputBody")


@_attrs_define
class SetExtraFreeOrgsInputBody:
    """
    Attributes:
        extra_free_orgs (int): Free organisations beyond the one everybody gets; 0 resets, -1 is unlimited
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    extra_free_orgs: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        extra_free_orgs = self.extra_free_orgs

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "extraFreeOrgs": extra_free_orgs,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extra_free_orgs = d.pop("extraFreeOrgs")

        schema = d.pop("$schema", UNSET)

        set_extra_free_orgs_input_body = cls(
            extra_free_orgs=extra_free_orgs,
            schema=schema,
        )

        return set_extra_free_orgs_input_body
