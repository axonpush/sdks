from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanFeatures")


@_attrs_define
class PlanFeatures:
    """
    Attributes:
        audit_log (bool | Unset):
        custom_retention (bool | Unset):
        rbac (bool | Unset):
        sso (bool | Unset):
    """

    audit_log: bool | Unset = UNSET
    custom_retention: bool | Unset = UNSET
    rbac: bool | Unset = UNSET
    sso: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audit_log = self.audit_log

        custom_retention = self.custom_retention

        rbac = self.rbac

        sso = self.sso

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audit_log is not UNSET:
            field_dict["auditLog"] = audit_log
        if custom_retention is not UNSET:
            field_dict["customRetention"] = custom_retention
        if rbac is not UNSET:
            field_dict["rbac"] = rbac
        if sso is not UNSET:
            field_dict["sso"] = sso

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audit_log = d.pop("auditLog", UNSET)

        custom_retention = d.pop("customRetention", UNSET)

        rbac = d.pop("rbac", UNSET)

        sso = d.pop("sso", UNSET)

        plan_features = cls(
            audit_log=audit_log,
            custom_retention=custom_retention,
            rbac=rbac,
            sso=sso,
        )

        return plan_features
