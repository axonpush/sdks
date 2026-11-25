from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime


T = TypeVar("T", bound="ActivitySeriesPoint")


@_attrs_define
class ActivitySeriesPoint:
    """
    Attributes:
        t (datetime.datetime):
        v (float):
        n (int | Unset): Sample count behind a lag percentile; zero means the bucket had no evidence
    """

    t: datetime.datetime
    v: float
    n: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        t = self.t.isoformat()

        v = self.v

        n = self.n

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "t": t,
                "v": v,
            }
        )
        if n is not UNSET:
            field_dict["n"] = n

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        t = isoparse(d.pop("t"))

        v = d.pop("v")

        n = d.pop("n", UNSET)

        activity_series_point = cls(
            t=t,
            v=v,
            n=n,
        )

        return activity_series_point
