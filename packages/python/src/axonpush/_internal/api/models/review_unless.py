from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="ReviewUnless")


@_attrs_define
class ReviewUnless:
    """
    Attributes:
        case (str):
        input_ (str):
        op (str):
        timezone (str | Unset):
    """

    case: str
    input_: str
    op: str
    timezone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        case = self.case

        input_ = self.input_

        op = self.op

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "case": case,
                "input": input_,
                "op": op,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        case = d.pop("case")

        input_ = d.pop("input")

        op = d.pop("op")

        timezone = d.pop("timezone", UNSET)

        review_unless = cls(
            case=case,
            input_=input_,
            op=op,
            timezone=timezone,
        )

        return review_unless
