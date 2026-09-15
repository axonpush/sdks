from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliveryDTO")


@_attrs_define
class DeliveryDTO:
    """
    Attributes:
        created_at (str):
        delivery_id (str):
        endpoint_id (str):
        event_id (str):
        attempts (int | Unset):
        error (str | Unset):
        next_retry_at (str | Unset):
        status (str | Unset):
        status_code (int | Unset):
    """

    created_at: str
    delivery_id: str
    endpoint_id: str
    event_id: str
    attempts: int | Unset = UNSET
    error: str | Unset = UNSET
    next_retry_at: str | Unset = UNSET
    status: str | Unset = UNSET
    status_code: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        delivery_id = self.delivery_id

        endpoint_id = self.endpoint_id

        event_id = self.event_id

        attempts = self.attempts

        error = self.error

        next_retry_at = self.next_retry_at

        status = self.status

        status_code = self.status_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "deliveryId": delivery_id,
                "endpointId": endpoint_id,
                "eventId": event_id,
            }
        )
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if error is not UNSET:
            field_dict["error"] = error
        if next_retry_at is not UNSET:
            field_dict["nextRetryAt"] = next_retry_at
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        delivery_id = d.pop("deliveryId")

        endpoint_id = d.pop("endpointId")

        event_id = d.pop("eventId")

        attempts = d.pop("attempts", UNSET)

        error = d.pop("error", UNSET)

        next_retry_at = d.pop("nextRetryAt", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("statusCode", UNSET)

        delivery_dto = cls(
            created_at=created_at,
            delivery_id=delivery_id,
            endpoint_id=endpoint_id,
            event_id=event_id,
            attempts=attempts,
            error=error,
            next_retry_at=next_retry_at,
            status=status,
            status_code=status_code,
        )

        return delivery_dto
