from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentCounts")


@_attrs_define
class DeploymentCounts:
    """
    Attributes:
        confirmed (int):
        could_not_confirm (int):
        no_result (int):
        not_completed (int):
        pending (int):
    """

    confirmed: int
    could_not_confirm: int
    no_result: int
    not_completed: int
    pending: int

    def to_dict(self) -> dict[str, Any]:
        confirmed = self.confirmed

        could_not_confirm = self.could_not_confirm

        no_result = self.no_result

        not_completed = self.not_completed

        pending = self.pending

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confirmed": confirmed,
                "could_not_confirm": could_not_confirm,
                "no_result": no_result,
                "not_completed": not_completed,
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmed = d.pop("confirmed")

        could_not_confirm = d.pop("could_not_confirm")

        no_result = d.pop("no_result")

        not_completed = d.pop("not_completed")

        pending = d.pop("pending")

        deployment_counts = cls(
            confirmed=confirmed,
            could_not_confirm=could_not_confirm,
            no_result=no_result,
            not_completed=not_completed,
            pending=pending,
        )

        return deployment_counts
