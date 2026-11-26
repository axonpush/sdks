from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceSource")


@_attrs_define
class ComplianceSource:
    """
    Attributes:
        label (str):
        url (str):
    """

    label: str
    url: str

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "label": label,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        url = d.pop("url")

        compliance_source = cls(
            label=label,
            url=url,
        )

        return compliance_source
