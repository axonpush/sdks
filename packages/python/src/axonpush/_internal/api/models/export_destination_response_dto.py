from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportDestinationResponseDto")


@_attrs_define
class ExportDestinationResponseDto:
    """
    Attributes:
        active (bool):
        created_at (datetime.datetime):
        destination_id (str):
        endpoint_url (str):
        env_slug (str):
        header_keys (list[str]): Configured header names (values are masked)
        id (str):
        name (str):
        org_id (str):
        signals (list[str]): OTLP signals: logs and/or traces
        event_type_filter (list[str] | Unset):
        service_name (str | Unset):
        updated_at (datetime.datetime | Unset):
    """

    active: bool
    created_at: datetime.datetime
    destination_id: str
    endpoint_url: str
    env_slug: str
    header_keys: list[str]
    id: str
    name: str
    org_id: str
    signals: list[str]
    event_type_filter: list[str] | Unset = UNSET
    service_name: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        created_at = self.created_at.isoformat()

        destination_id = self.destination_id

        endpoint_url = self.endpoint_url

        env_slug = self.env_slug

        header_keys = self.header_keys

        id = self.id

        name = self.name

        org_id = self.org_id

        signals = self.signals

        event_type_filter: list[str] | Unset = UNSET
        if not isinstance(self.event_type_filter, Unset):
            event_type_filter = self.event_type_filter

        service_name = self.service_name

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "createdAt": created_at,
                "destinationId": destination_id,
                "endpointUrl": endpoint_url,
                "envSlug": env_slug,
                "headerKeys": header_keys,
                "id": id,
                "name": name,
                "orgId": org_id,
                "signals": signals,
            }
        )
        if event_type_filter is not UNSET:
            field_dict["eventTypeFilter"] = event_type_filter
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        created_at = isoparse(d.pop("createdAt"))

        destination_id = d.pop("destinationId")

        endpoint_url = d.pop("endpointUrl")

        env_slug = d.pop("envSlug")

        header_keys = cast(list[str], d.pop("headerKeys"))

        id = d.pop("id")

        name = d.pop("name")

        org_id = d.pop("orgId")

        signals = cast(list[str], d.pop("signals"))

        event_type_filter = cast(list[str], d.pop("eventTypeFilter", UNSET))

        service_name = d.pop("serviceName", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        export_destination_response_dto = cls(
            active=active,
            created_at=created_at,
            destination_id=destination_id,
            endpoint_url=endpoint_url,
            env_slug=env_slug,
            header_keys=header_keys,
            id=id,
            name=name,
            org_id=org_id,
            signals=signals,
            event_type_filter=event_type_filter,
            service_name=service_name,
            updated_at=updated_at,
        )

        export_destination_response_dto.additional_properties = d
        return export_destination_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
