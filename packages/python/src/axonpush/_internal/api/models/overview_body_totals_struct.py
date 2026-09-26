from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverviewBodyTotalsStruct")


@_attrs_define
class OverviewBodyTotalsStruct:
    """
    Attributes:
        orgs (int):
        users (int):
    """

    orgs: int
    users: int

    def to_dict(self) -> dict[str, Any]:
        orgs = self.orgs

        users = self.users

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "orgs": orgs,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        orgs = d.pop("orgs")

        users = d.pop("users")

        overview_body_totals_struct = cls(
            orgs=orgs,
            users=users,
        )

        return overview_body_totals_struct
