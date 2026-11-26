from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportDeliveryDTO")


@_attrs_define
class ExportDeliveryDTO:
    """
    Attributes:
        attempts (int):
        created_at (str):
        delivery_id (str):
        event_id (str):
        signal (str):
        status (str):
        error (str | Unset):
        status_code (int | Unset):
    """

    attempts: int
    created_at: str
    delivery_id: str
    event_id: str
    signal: str
    status: str
    error: str | Unset = UNSET
    status_code: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        created_at = self.created_at

        delivery_id = self.delivery_id

        event_id = self.event_id

        signal = self.signal

        status = self.status

        error = self.error

        status_code = self.status_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts": attempts,
                "createdAt": created_at,
                "deliveryId": delivery_id,
                "eventId": event_id,
                "signal": signal,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = d.pop("createdAt")

        delivery_id = d.pop("deliveryId")

        event_id = d.pop("eventId")

        signal = d.pop("signal")

        status = d.pop("status")

        error = d.pop("error", UNSET)

        status_code = d.pop("statusCode", UNSET)

        export_delivery_dto = cls(
            attempts=attempts,
            created_at=created_at,
            delivery_id=delivery_id,
            event_id=event_id,
            signal=signal,
            status=status,
            error=error,
            status_code=status_code,
        )

        return export_delivery_dto
