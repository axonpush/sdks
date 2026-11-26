from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityEdgeEvidence")


@_attrs_define
class ActivityEdgeEvidence:
    """
    Attributes:
        ref (str): Timeline ref
        with_ (str): Timeline with
    """

    ref: str
    with_: str

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        with_ = self.with_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ref": ref,
                "with": with_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref = d.pop("ref")

        with_ = d.pop("with")

        activity_edge_evidence = cls(
            ref=ref,
            with_=with_,
        )

        return activity_edge_evidence
