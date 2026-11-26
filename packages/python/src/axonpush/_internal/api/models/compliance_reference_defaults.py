from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceReferenceDefaults")


@_attrs_define
class ComplianceReferenceDefaults:
    """
    Attributes:
        app_id (str | Unset):
        environment_id (str | Unset):
        owner_user_id (str | Unset):
    """

    app_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    owner_user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        environment_id = self.environment_id

        owner_user_id = self.owner_user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if owner_user_id is not UNSET:
            field_dict["ownerUserId"] = owner_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        owner_user_id = d.pop("ownerUserId", UNSET)

        compliance_reference_defaults = cls(
            app_id=app_id,
            environment_id=environment_id,
            owner_user_id=owner_user_id,
        )

        return compliance_reference_defaults
