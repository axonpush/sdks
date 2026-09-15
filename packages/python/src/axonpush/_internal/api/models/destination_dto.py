from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DestinationDTO")


@_attrs_define
class DestinationDTO:
    """
    Attributes:
        active (bool):
        created_at (str):
        destination_id (str):
        endpoint_url (str):
        env_slug (str):
        event_type_filter (list[str] | None):
        header_keys (list[str] | None):
        name (str):
        org_id (str):
        signals (list[str] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        service_name (str | Unset):
        updated_at (str | Unset):
    """

    active: bool
    created_at: str
    destination_id: str
    endpoint_url: str
    env_slug: str
    event_type_filter: list[str] | None
    header_keys: list[str] | None
    name: str
    org_id: str
    signals: list[str] | None
    schema: str | Unset = UNSET
    service_name: str | Unset = UNSET
    updated_at: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        created_at = self.created_at

        destination_id = self.destination_id

        endpoint_url = self.endpoint_url

        env_slug = self.env_slug

        event_type_filter: list[str] | None
        if isinstance(self.event_type_filter, list):
            event_type_filter = self.event_type_filter

        else:
            event_type_filter = self.event_type_filter

        header_keys: list[str] | None
        if isinstance(self.header_keys, list):
            header_keys = self.header_keys

        else:
            header_keys = self.header_keys

        name = self.name

        org_id = self.org_id

        signals: list[str] | None
        if isinstance(self.signals, list):
            signals = self.signals

        else:
            signals = self.signals

        schema = self.schema

        service_name = self.service_name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
                "createdAt": created_at,
                "destinationId": destination_id,
                "endpointUrl": endpoint_url,
                "envSlug": env_slug,
                "eventTypeFilter": event_type_filter,
                "headerKeys": header_keys,
                "name": name,
                "orgId": org_id,
                "signals": signals,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        created_at = d.pop("createdAt")

        destination_id = d.pop("destinationId")

        endpoint_url = d.pop("endpointUrl")

        env_slug = d.pop("envSlug")

        def _parse_event_type_filter(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_type_filter_type_0 = cast(list[str], data)

                return event_type_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        event_type_filter = _parse_event_type_filter(d.pop("eventTypeFilter"))

        def _parse_header_keys(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                header_keys_type_0 = cast(list[str], data)

                return header_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        header_keys = _parse_header_keys(d.pop("headerKeys"))

        name = d.pop("name")

        org_id = d.pop("orgId")

        def _parse_signals(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                signals_type_0 = cast(list[str], data)

                return signals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        signals = _parse_signals(d.pop("signals"))

        schema = d.pop("$schema", UNSET)

        service_name = d.pop("serviceName", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        destination_dto = cls(
            active=active,
            created_at=created_at,
            destination_id=destination_id,
            endpoint_url=endpoint_url,
            env_slug=env_slug,
            event_type_filter=event_type_filter,
            header_keys=header_keys,
            name=name,
            org_id=org_id,
            signals=signals,
            schema=schema,
            service_name=service_name,
            updated_at=updated_at,
        )

        return destination_dto
