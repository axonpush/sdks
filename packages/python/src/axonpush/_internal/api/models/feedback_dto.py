from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackDTO")


@_attrs_define
class FeedbackDTO:
    """
    Attributes:
        created_at (str):
        feedback_id (str):
        message (str):
        status (str):
        category (str | Unset):
        context (Any | Unset):
        email (str | Unset):
        org_id (str | Unset):
        reviewed_at (str | Unset):
        reviewed_by (str | Unset):
        user_id (str | Unset):
    """

    created_at: str
    feedback_id: str
    message: str
    status: str
    category: str | Unset = UNSET
    context: Any | Unset = UNSET
    email: str | Unset = UNSET
    org_id: str | Unset = UNSET
    reviewed_at: str | Unset = UNSET
    reviewed_by: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        feedback_id = self.feedback_id

        message = self.message

        status = self.status

        category = self.category

        context = self.context

        email = self.email

        org_id = self.org_id

        reviewed_at = self.reviewed_at

        reviewed_by = self.reviewed_by

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "feedbackId": feedback_id,
                "message": message,
                "status": status,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if context is not UNSET:
            field_dict["context"] = context
        if email is not UNSET:
            field_dict["email"] = email
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if reviewed_by is not UNSET:
            field_dict["reviewedBy"] = reviewed_by
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        feedback_id = d.pop("feedbackId")

        message = d.pop("message")

        status = d.pop("status")

        category = d.pop("category", UNSET)

        context = d.pop("context", UNSET)

        email = d.pop("email", UNSET)

        org_id = d.pop("orgId", UNSET)

        reviewed_at = d.pop("reviewedAt", UNSET)

        reviewed_by = d.pop("reviewedBy", UNSET)

        user_id = d.pop("userId", UNSET)

        feedback_dto = cls(
            created_at=created_at,
            feedback_id=feedback_id,
            message=message,
            status=status,
            category=category,
            context=context,
            email=email,
            org_id=org_id,
            reviewed_at=reviewed_at,
            reviewed_by=reviewed_by,
            user_id=user_id,
        )

        return feedback_dto
