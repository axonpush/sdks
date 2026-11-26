from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchResult")


@_attrs_define
class BatchResult:
    """
    Attributes:
        index (int):
        status (str):
        error_code (str | Unset):
        event_id (str | Unset):
    """

    index: int
    status: str
    error_code: str | Unset = UNSET
    event_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        status = self.status

        error_code = self.error_code

        event_id = self.event_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "index": index,
                "status": status,
            }
        )
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if event_id is not UNSET:
            field_dict["eventId"] = event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        status = d.pop("status")

        error_code = d.pop("errorCode", UNSET)

        event_id = d.pop("eventId", UNSET)

        batch_result = cls(
            index=index,
            status=status,
            error_code=error_code,
            event_id=event_id,
        )

        return batch_result
