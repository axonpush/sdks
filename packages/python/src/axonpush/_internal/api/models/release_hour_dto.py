from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="ReleaseHourDTO")


@_attrs_define
class ReleaseHourDTO:
    """
    Attributes:
        abnormal (int):
        crashed (int):
        errored (int):
        exited (int):
        hour (str):
        started (int):
        unhandled (int):
    """

    abnormal: int
    crashed: int
    errored: int
    exited: int
    hour: str
    started: int
    unhandled: int

    def to_dict(self) -> dict[str, Any]:
        abnormal = self.abnormal

        crashed = self.crashed

        errored = self.errored

        exited = self.exited

        hour = self.hour

        started = self.started

        unhandled = self.unhandled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "abnormal": abnormal,
                "crashed": crashed,
                "errored": errored,
                "exited": exited,
                "hour": hour,
                "started": started,
                "unhandled": unhandled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abnormal = d.pop("abnormal")

        crashed = d.pop("crashed")

        errored = d.pop("errored")

        exited = d.pop("exited")

        hour = d.pop("hour")

        started = d.pop("started")

        unhandled = d.pop("unhandled")

        release_hour_dto = cls(
            abnormal=abnormal,
            crashed=crashed,
            errored=errored,
            exited=exited,
            hour=hour,
            started=started,
            unhandled=unhandled,
        )

        return release_hour_dto
