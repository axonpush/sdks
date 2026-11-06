from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceActionBody")


@_attrs_define
class ComplianceActionBody:
    """
    Attributes:
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        identity_verified (bool | Unset):
        reason (str | Unset):
        reply (str | Unset):
        report (str | Unset):
        report_kind (str | Unset):
    """

    version: int
    schema: str | Unset = UNSET
    identity_verified: bool | Unset = UNSET
    reason: str | Unset = UNSET
    reply: str | Unset = UNSET
    report: str | Unset = UNSET
    report_kind: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        schema = self.schema

        identity_verified = self.identity_verified

        reason = self.reason

        reply = self.reply

        report = self.report

        report_kind = self.report_kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if identity_verified is not UNSET:
            field_dict["identityVerified"] = identity_verified
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reply is not UNSET:
            field_dict["reply"] = reply
        if report is not UNSET:
            field_dict["report"] = report
        if report_kind is not UNSET:
            field_dict["reportKind"] = report_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        identity_verified = d.pop("identityVerified", UNSET)

        reason = d.pop("reason", UNSET)

        reply = d.pop("reply", UNSET)

        report = d.pop("report", UNSET)

        report_kind = d.pop("reportKind", UNSET)

        compliance_action_body = cls(
            version=version,
            schema=schema,
            identity_verified=identity_verified,
            reason=reason,
            reply=reply,
            report=report,
            report_kind=report_kind,
        )

        return compliance_action_body
