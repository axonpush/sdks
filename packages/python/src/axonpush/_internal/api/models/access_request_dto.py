from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessRequestDTO")


@_attrs_define
class AccessRequestDTO:
    """
    Attributes:
        company (str):
        created_at (str):
        email (str):
        request_id (str):
        status (str):
        use_case (str):
        country (str | Unset):
        invitation_code (str | Unset):
        name (str | Unset):
        note (str | Unset):
        org_id (str | Unset):
        reviewed_at (str | Unset):
    """

    company: str
    created_at: str
    email: str
    request_id: str
    status: str
    use_case: str
    country: str | Unset = UNSET
    invitation_code: str | Unset = UNSET
    name: str | Unset = UNSET
    note: str | Unset = UNSET
    org_id: str | Unset = UNSET
    reviewed_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        created_at = self.created_at

        email = self.email

        request_id = self.request_id

        status = self.status

        use_case = self.use_case

        country = self.country

        invitation_code = self.invitation_code

        name = self.name

        note = self.note

        org_id = self.org_id

        reviewed_at = self.reviewed_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "company": company,
                "createdAt": created_at,
                "email": email,
                "requestId": request_id,
                "status": status,
                "useCase": use_case,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if invitation_code is not UNSET:
            field_dict["invitationCode"] = invitation_code
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company")

        created_at = d.pop("createdAt")

        email = d.pop("email")

        request_id = d.pop("requestId")

        status = d.pop("status")

        use_case = d.pop("useCase")

        country = d.pop("country", UNSET)

        invitation_code = d.pop("invitationCode", UNSET)

        name = d.pop("name", UNSET)

        note = d.pop("note", UNSET)

        org_id = d.pop("orgId", UNSET)

        reviewed_at = d.pop("reviewedAt", UNSET)

        access_request_dto = cls(
            company=company,
            created_at=created_at,
            email=email,
            request_id=request_id,
            status=status,
            use_case=use_case,
            country=country,
            invitation_code=invitation_code,
            name=name,
            note=note,
            org_id=org_id,
            reviewed_at=reviewed_at,
        )

        return access_request_dto
