from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_delivery_status import WebhookDeliveryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDeliveryResponseDto")


@_attrs_define
class WebhookDeliveryResponseDto:
    """
    Attributes:
        attempts (float):
        created_at (datetime.datetime):
        delivery_id (str):
        endpoint_id (str):
        event_id (str):
        id (str):
        status (WebhookDeliveryStatus):
        error (str | Unset):
        last_attempt_at (datetime.datetime | Unset):
        next_attempt_at (datetime.datetime | Unset):
        response_body (str | Unset):
        status_code (float | Unset):
    """

    attempts: float
    created_at: datetime.datetime
    delivery_id: str
    endpoint_id: str
    event_id: str
    id: str
    status: WebhookDeliveryStatus
    error: str | Unset = UNSET
    last_attempt_at: datetime.datetime | Unset = UNSET
    next_attempt_at: datetime.datetime | Unset = UNSET
    response_body: str | Unset = UNSET
    status_code: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        created_at = self.created_at.isoformat()

        delivery_id = self.delivery_id

        endpoint_id = self.endpoint_id

        event_id = self.event_id

        id = self.id

        status = self.status.value

        error = self.error

        last_attempt_at: str | Unset = UNSET
        if not isinstance(self.last_attempt_at, Unset):
            last_attempt_at = self.last_attempt_at.isoformat()

        next_attempt_at: str | Unset = UNSET
        if not isinstance(self.next_attempt_at, Unset):
            next_attempt_at = self.next_attempt_at.isoformat()

        response_body = self.response_body

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempts": attempts,
                "createdAt": created_at,
                "deliveryId": delivery_id,
                "endpointId": endpoint_id,
                "eventId": event_id,
                "id": id,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if last_attempt_at is not UNSET:
            field_dict["lastAttemptAt"] = last_attempt_at
        if next_attempt_at is not UNSET:
            field_dict["nextAttemptAt"] = next_attempt_at
        if response_body is not UNSET:
            field_dict["responseBody"] = response_body
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        created_at = isoparse(d.pop("createdAt"))

        delivery_id = d.pop("deliveryId")

        endpoint_id = d.pop("endpointId")

        event_id = d.pop("eventId")

        id = d.pop("id")

        status = WebhookDeliveryStatus(d.pop("status"))

        error = d.pop("error", UNSET)

        _last_attempt_at = d.pop("lastAttemptAt", UNSET)
        last_attempt_at: datetime.datetime | Unset
        if isinstance(_last_attempt_at, Unset):
            last_attempt_at = UNSET
        else:
            last_attempt_at = isoparse(_last_attempt_at)

        _next_attempt_at = d.pop("nextAttemptAt", UNSET)
        next_attempt_at: datetime.datetime | Unset
        if isinstance(_next_attempt_at, Unset):
            next_attempt_at = UNSET
        else:
            next_attempt_at = isoparse(_next_attempt_at)

        response_body = d.pop("responseBody", UNSET)

        status_code = d.pop("statusCode", UNSET)

        webhook_delivery_response_dto = cls(
            attempts=attempts,
            created_at=created_at,
            delivery_id=delivery_id,
            endpoint_id=endpoint_id,
            event_id=event_id,
            id=id,
            status=status,
            error=error,
            last_attempt_at=last_attempt_at,
            next_attempt_at=next_attempt_at,
            response_body=response_body,
            status_code=status_code,
        )

        webhook_delivery_response_dto.additional_properties = d
        return webhook_delivery_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
