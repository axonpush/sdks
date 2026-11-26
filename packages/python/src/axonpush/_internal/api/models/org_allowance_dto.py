from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgAllowanceDTO")


@_attrs_define
class OrgAllowanceDTO:
    """
    Attributes:
        allowed (int): Free organisations the user may own; -1 when unlimited
        billing_enabled (bool): When true, organisations beyond the allowance are created unpaid instead of refused
        free_owned (int): Owned organisations not on an active paid subscription
        owned (int): Live organisations the user owns
        unlimited (bool):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    allowed: int
    billing_enabled: bool
    free_owned: int
    owned: int
    unlimited: bool
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed = self.allowed

        billing_enabled = self.billing_enabled

        free_owned = self.free_owned

        owned = self.owned

        unlimited = self.unlimited

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "allowed": allowed,
                "billingEnabled": billing_enabled,
                "freeOwned": free_owned,
                "owned": owned,
                "unlimited": unlimited,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = d.pop("allowed")

        billing_enabled = d.pop("billingEnabled")

        free_owned = d.pop("freeOwned")

        owned = d.pop("owned")

        unlimited = d.pop("unlimited")

        schema = d.pop("$schema", UNSET)

        org_allowance_dto = cls(
            allowed=allowed,
            billing_enabled=billing_enabled,
            free_owned=free_owned,
            owned=owned,
            unlimited=unlimited,
            schema=schema,
        )

        return org_allowance_dto
