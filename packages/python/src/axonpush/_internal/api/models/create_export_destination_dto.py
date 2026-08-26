from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_signal import ExportSignal
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_export_destination_dto_headers import CreateExportDestinationDtoHeaders


T = TypeVar("T", bound="CreateExportDestinationDto")


@_attrs_define
class CreateExportDestinationDto:
    """
    Attributes:
        endpoint_url (str): OTLP/HTTP base URL (v1/logs and v1/traces are appended)
        env_slug (str): Environment slug this destination is scoped to (e.g. "prod")
        name (str):
        signals (list[ExportSignal]):
        active (bool | Unset):  Default: True.
        event_type_filter (list[str] | Unset): Allow-list of event types to export (empty = all types)
        headers (CreateExportDestinationDtoHeaders | Unset): Header name -> value map (e.g. DD-API-KEY). Stored server-
            side, never returned.
        service_name (str | Unset): service.name attribute stamped on exported resources
    """

    endpoint_url: str
    env_slug: str
    name: str
    signals: list[ExportSignal]
    active: bool | Unset = True
    event_type_filter: list[str] | Unset = UNSET
    headers: CreateExportDestinationDtoHeaders | Unset = UNSET
    service_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_export_destination_dto_headers import CreateExportDestinationDtoHeaders

        endpoint_url = self.endpoint_url

        env_slug = self.env_slug

        name = self.name

        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.value
            signals.append(signals_item)

        active = self.active

        event_type_filter: list[str] | Unset = UNSET
        if not isinstance(self.event_type_filter, Unset):
            event_type_filter = self.event_type_filter

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        service_name = self.service_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointUrl": endpoint_url,
                "envSlug": env_slug,
                "name": name,
                "signals": signals,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if event_type_filter is not UNSET:
            field_dict["eventTypeFilter"] = event_type_filter
        if headers is not UNSET:
            field_dict["headers"] = headers
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_export_destination_dto_headers import CreateExportDestinationDtoHeaders

        d = dict(src_dict)
        endpoint_url = d.pop("endpointUrl")

        env_slug = d.pop("envSlug")

        name = d.pop("name")

        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = ExportSignal(signals_item_data)

            signals.append(signals_item)

        active = d.pop("active", UNSET)

        event_type_filter = cast(list[str], d.pop("eventTypeFilter", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: CreateExportDestinationDtoHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CreateExportDestinationDtoHeaders.from_dict(_headers)

        service_name = d.pop("serviceName", UNSET)

        create_export_destination_dto = cls(
            endpoint_url=endpoint_url,
            env_slug=env_slug,
            name=name,
            signals=signals,
            active=active,
            event_type_filter=event_type_filter,
            headers=headers,
            service_name=service_name,
        )

        create_export_destination_dto.additional_properties = d
        return create_export_destination_dto

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
