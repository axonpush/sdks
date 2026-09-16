from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_input_body_2_headers import UpdateInputBody2Headers


T = TypeVar("T", bound="UpdateInputBody2")


@_attrs_define
class UpdateInputBody2:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        active (bool | Unset):
        endpoint_url (str | Unset):
        event_type_filter (list[str] | Unset):
        headers (UpdateInputBody2Headers | Unset): Replaces the stored header map. Never returned.
        name (str | Unset):
        service_name (str | Unset):
        signals (list[str] | Unset):
    """

    schema: str | Unset = UNSET
    active: bool | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    event_type_filter: list[str] | Unset = UNSET
    headers: UpdateInputBody2Headers | Unset = UNSET
    name: str | Unset = UNSET
    service_name: str | Unset = UNSET
    signals: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_input_body_2_headers import UpdateInputBody2Headers

        schema = self.schema

        active = self.active

        endpoint_url = self.endpoint_url

        event_type_filter: list[str] | Unset = UNSET
        if not isinstance(self.event_type_filter, Unset):
            event_type_filter = self.event_type_filter

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        name = self.name

        service_name = self.service_name

        signals: list[str] | Unset = UNSET
        if not isinstance(self.signals, Unset):
            signals = self.signals

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if active is not UNSET:
            field_dict["active"] = active
        if endpoint_url is not UNSET:
            field_dict["endpointUrl"] = endpoint_url
        if event_type_filter is not UNSET:
            field_dict["eventTypeFilter"] = event_type_filter
        if headers is not UNSET:
            field_dict["headers"] = headers
        if name is not UNSET:
            field_dict["name"] = name
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if signals is not UNSET:
            field_dict["signals"] = signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_input_body_2_headers import UpdateInputBody2Headers

        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        active = d.pop("active", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        event_type_filter = cast(list[str], d.pop("eventTypeFilter", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: UpdateInputBody2Headers | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = UpdateInputBody2Headers.from_dict(_headers)

        name = d.pop("name", UNSET)

        service_name = d.pop("serviceName", UNSET)

        signals = cast(list[str], d.pop("signals", UNSET))

        update_input_body_2 = cls(
            schema=schema,
            active=active,
            endpoint_url=endpoint_url,
            event_type_filter=event_type_filter,
            headers=headers,
            name=name,
            service_name=service_name,
            signals=signals,
        )

        return update_input_body_2
