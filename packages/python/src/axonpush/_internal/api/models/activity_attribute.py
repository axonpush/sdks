from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_attribute_role import ActivityAttributeRole
from ..models.activity_attribute_type import ActivityAttributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityAttribute")


@_attrs_define
class ActivityAttribute:
    """
    Attributes:
        key (str): Stable attribute key sent in observation attributes and stored on entities
        type_ (ActivityAttributeType): duration is milliseconds; time is RFC 3339; ref is an opaque identifier
        description (str | Unset):
        entity (str | Unset): For a ref: the entity type it points at (used for linking and erasure)
        failure (list[str] | None | Unset): Outcome values that count as failures
        label (str | Unset):
        max_length (int | Unset): For text: maximum length, default 200
        multiple (bool | Unset): For a ref: the value is a list of up to 20 identifiers
        pending (list[str] | None | Unset): Outcome values that mean the work is still in progress
        personal (bool | Unset): Personal data: masked unless the caller is an owner/admin or holds profiles:read
        role (ActivityAttributeRole | Unset): Product meaning that generic views, analytics and alerts read through.
            expected_duration is in seconds.
        values (list[str] | None | Unset): Allowed values for an enum
    """

    key: str
    type_: ActivityAttributeType
    description: str | Unset = UNSET
    entity: str | Unset = UNSET
    failure: list[str] | None | Unset = UNSET
    label: str | Unset = UNSET
    max_length: int | Unset = UNSET
    multiple: bool | Unset = UNSET
    pending: list[str] | None | Unset = UNSET
    personal: bool | Unset = UNSET
    role: ActivityAttributeRole | Unset = UNSET
    values: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_.value

        description = self.description

        entity = self.entity

        failure: list[str] | None | Unset
        if isinstance(self.failure, Unset):
            failure = UNSET
        elif isinstance(self.failure, list):
            failure = self.failure

        else:
            failure = self.failure

        label = self.label

        max_length = self.max_length

        multiple = self.multiple

        pending: list[str] | None | Unset
        if isinstance(self.pending, Unset):
            pending = UNSET
        elif isinstance(self.pending, list):
            pending = self.pending

        else:
            pending = self.pending

        personal = self.personal

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        values: list[str] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entity is not UNSET:
            field_dict["entity"] = entity
        if failure is not UNSET:
            field_dict["failure"] = failure
        if label is not UNSET:
            field_dict["label"] = label
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if pending is not UNSET:
            field_dict["pending"] = pending
        if personal is not UNSET:
            field_dict["personal"] = personal
        if role is not UNSET:
            field_dict["role"] = role
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = ActivityAttributeType(d.pop("type"))

        description = d.pop("description", UNSET)

        entity = d.pop("entity", UNSET)

        def _parse_failure(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                failure_type_0 = cast(list[str], data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        failure = _parse_failure(d.pop("failure", UNSET))

        label = d.pop("label", UNSET)

        max_length = d.pop("maxLength", UNSET)

        multiple = d.pop("multiple", UNSET)

        def _parse_pending(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pending_type_0 = cast(list[str], data)

                return pending_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        pending = _parse_pending(d.pop("pending", UNSET))

        personal = d.pop("personal", UNSET)

        _role = d.pop("role", UNSET)
        role: ActivityAttributeRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ActivityAttributeRole(_role)

        def _parse_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        activity_attribute = cls(
            key=key,
            type_=type_,
            description=description,
            entity=entity,
            failure=failure,
            label=label,
            max_length=max_length,
            multiple=multiple,
            pending=pending,
            personal=personal,
            role=role,
            values=values,
        )

        return activity_attribute
