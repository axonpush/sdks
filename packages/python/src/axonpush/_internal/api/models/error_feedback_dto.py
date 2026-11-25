from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="ErrorFeedbackDTO")


@_attrs_define
class ErrorFeedbackDTO:
    """
    Attributes:
        content_state (str): available | not_loaded
        event_id (str):
        matched_by (str): event (associated Sentry event id) | trace (shared trace)
        occurred_at (str):
        associated_event_id (str | Unset):
        email (str | Unset):
        message (str | Unset):
        name (str | Unset):
        trace_id (str | Unset):
        url (str | Unset):
    """

    content_state: str
    event_id: str
    matched_by: str
    occurred_at: str
    associated_event_id: str | Unset = UNSET
    email: str | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content_state = self.content_state

        event_id = self.event_id

        matched_by = self.matched_by

        occurred_at = self.occurred_at

        associated_event_id = self.associated_event_id

        email = self.email

        message = self.message

        name = self.name

        trace_id = self.trace_id

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contentState": content_state,
                "eventId": event_id,
                "matchedBy": matched_by,
                "occurredAt": occurred_at,
            }
        )
        if associated_event_id is not UNSET:
            field_dict["associatedEventId"] = associated_event_id
        if email is not UNSET:
            field_dict["email"] = email
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_state = d.pop("contentState")

        event_id = d.pop("eventId")

        matched_by = d.pop("matchedBy")

        occurred_at = d.pop("occurredAt")

        associated_event_id = d.pop("associatedEventId", UNSET)

        email = d.pop("email", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        trace_id = d.pop("traceId", UNSET)

        url = d.pop("url", UNSET)

        error_feedback_dto = cls(
            content_state=content_state,
            event_id=event_id,
            matched_by=matched_by,
            occurred_at=occurred_at,
            associated_event_id=associated_event_id,
            email=email,
            message=message,
            name=name,
            trace_id=trace_id,
            url=url,
        )

        return error_feedback_dto
