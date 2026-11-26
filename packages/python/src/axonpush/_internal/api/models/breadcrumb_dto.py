from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BreadcrumbDTO")


@_attrs_define
class BreadcrumbDTO:
    """
    Attributes:
        synthesized (bool):
        category (str | Unset):
        level (str | Unset):
        message (str | Unset):
        timestamp (str | Unset):
        type_ (str | Unset):
    """

    synthesized: bool
    category: str | Unset = UNSET
    level: str | Unset = UNSET
    message: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        synthesized = self.synthesized

        category = self.category

        level = self.level

        message = self.message

        timestamp = self.timestamp

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "synthesized": synthesized,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if level is not UNSET:
            field_dict["level"] = level
        if message is not UNSET:
            field_dict["message"] = message
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        synthesized = d.pop("synthesized")

        category = d.pop("category", UNSET)

        level = d.pop("level", UNSET)

        message = d.pop("message", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        type_ = d.pop("type", UNSET)

        breadcrumb_dto = cls(
            synthesized=synthesized,
            category=category,
            level=level,
            message=message,
            timestamp=timestamp,
            type_=type_,
        )

        return breadcrumb_dto
