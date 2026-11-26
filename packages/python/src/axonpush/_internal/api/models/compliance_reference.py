from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceReference")


@_attrs_define
class ComplianceReference:
    """
    Attributes:
        available (bool):
        description (str):
        id (str):
        kind (str):
        label (str):
        state (str):
        app_id (str | Unset):
        email (str | Unset):
        environment_id (str | Unset):
        is_default (bool | Unset):
        name (str | Unset):
        role (str | Unset):
    """

    available: bool
    description: str
    id: str
    kind: str
    label: str
    state: str
    app_id: str | Unset = UNSET
    email: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    role: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        description = self.description

        id = self.id

        kind = self.kind

        label = self.label

        state = self.state

        app_id = self.app_id

        email = self.email

        environment_id = self.environment_id

        is_default = self.is_default

        name = self.name

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available": available,
                "description": description,
                "id": id,
                "kind": kind,
                "label": label,
                "state": state,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if email is not UNSET:
            field_dict["email"] = email
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available")

        description = d.pop("description")

        id = d.pop("id")

        kind = d.pop("kind")

        label = d.pop("label")

        state = d.pop("state")

        app_id = d.pop("appId", UNSET)

        email = d.pop("email", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        is_default = d.pop("isDefault", UNSET)

        name = d.pop("name", UNSET)

        role = d.pop("role", UNSET)

        compliance_reference = cls(
            available=available,
            description=description,
            id=id,
            kind=kind,
            label=label,
            state=state,
            app_id=app_id,
            email=email,
            environment_id=environment_id,
            is_default=is_default,
            name=name,
            role=role,
        )

        return compliance_reference
