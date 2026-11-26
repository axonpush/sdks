from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityConnectSDK")


@_attrs_define
class ActivityConnectSDK:
    """
    Attributes:
        python (str):
        typescript (str):
    """

    python: str
    typescript: str

    def to_dict(self) -> dict[str, Any]:
        python = self.python

        typescript = self.typescript

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "python": python,
                "typescript": typescript,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        python = d.pop("python")

        typescript = d.pop("typescript")

        activity_connect_sdk = cls(
            python=python,
            typescript=typescript,
        )

        return activity_connect_sdk
