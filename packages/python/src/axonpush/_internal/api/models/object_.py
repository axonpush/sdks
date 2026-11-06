from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Object")


@_attrs_define
class Object:
    """
    Attributes:
        bytes_ (int):
        key (str):
        sha256 (str):
        version (str):
    """

    bytes_: int
    key: str
    sha256: str
    version: str

    def to_dict(self) -> dict[str, Any]:
        bytes_ = self.bytes_

        key = self.key

        sha256 = self.sha256

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bytes": bytes_,
                "key": key,
                "sha256": sha256,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_ = d.pop("bytes")

        key = d.pop("key")

        sha256 = d.pop("sha256")

        version = d.pop("version")

        object_ = cls(
            bytes_=bytes_,
            key=key,
            sha256=sha256,
            version=version,
        )

        return object_
