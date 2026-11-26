from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentSource")


@_attrs_define
class DeploymentSource:
    """
    Attributes:
        bound (bool):
        id (str):
        publisher (str | Unset):
    """

    bound: bool
    id: str
    publisher: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bound = self.bound

        id = self.id

        publisher = self.publisher

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bound": bound,
                "id": id,
            }
        )
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bound = d.pop("bound")

        id = d.pop("id")

        publisher = d.pop("publisher", UNSET)

        deployment_source = cls(
            bound=bound,
            id=id,
            publisher=publisher,
        )

        return deployment_source
