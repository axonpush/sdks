from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingEventDTO")


@_attrs_define
class BillingEventDTO:
    """
    Attributes:
        created_at (str):
        event_name (str):
        external_id (str):
        org_id (str):
        error (str | Unset):
        payload (Any | Unset):
        processed_at (str | Unset):
    """

    created_at: str
    event_name: str
    external_id: str
    org_id: str
    error: str | Unset = UNSET
    payload: Any | Unset = UNSET
    processed_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        event_name = self.event_name

        external_id = self.external_id

        org_id = self.org_id

        error = self.error

        payload = self.payload

        processed_at = self.processed_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "eventName": event_name,
                "externalId": external_id,
                "orgId": org_id,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if payload is not UNSET:
            field_dict["payload"] = payload
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        event_name = d.pop("eventName")

        external_id = d.pop("externalId")

        org_id = d.pop("orgId")

        error = d.pop("error", UNSET)

        payload = d.pop("payload", UNSET)

        processed_at = d.pop("processedAt", UNSET)

        billing_event_dto = cls(
            created_at=created_at,
            event_name=event_name,
            external_id=external_id,
            org_id=org_id,
            error=error,
            payload=payload,
            processed_at=processed_at,
        )

        return billing_event_dto
