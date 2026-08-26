from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_signal import ExportSignal
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_export_destination_dto_headers import UpdateExportDestinationDtoHeaders


T = TypeVar("T", bound="UpdateExportDestinationDto")


@_attrs_define
class UpdateExportDestinationDto:
    """
    Attributes:
        active (bool | Unset):
        endpoint_url (str | Unset):
        event_type_filter (list[str] | Unset):
        headers (UpdateExportDestinationDtoHeaders | Unset): Replaces the stored header map. Never returned by the API.
        name (str | Unset):
        service_name (str | Unset):
        signals (list[ExportSignal] | Unset):
    """

    active: bool | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    event_type_filter: list[str] | Unset = UNSET
    headers: UpdateExportDestinationDtoHeaders | Unset = UNSET
    name: str | Unset = UNSET
    service_name: str | Unset = UNSET
    signals: list[ExportSignal] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_export_destination_dto_headers import UpdateExportDestinationDtoHeaders

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
            signals = []
            for signals_item_data in self.signals:
                signals_item = signals_item_data.value
                signals.append(signals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        from ..models.update_export_destination_dto_headers import UpdateExportDestinationDtoHeaders

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        event_type_filter = cast(list[str], d.pop("eventTypeFilter", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: UpdateExportDestinationDtoHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = UpdateExportDestinationDtoHeaders.from_dict(_headers)

        name = d.pop("name", UNSET)

        service_name = d.pop("serviceName", UNSET)

        _signals = d.pop("signals", UNSET)
        signals: list[ExportSignal] | Unset = UNSET
        if _signals is not UNSET:
            signals = []
            for signals_item_data in _signals:
                signals_item = ExportSignal(signals_item_data)

                signals.append(signals_item)

        update_export_destination_dto = cls(
            active=active,
            endpoint_url=endpoint_url,
            event_type_filter=event_type_filter,
            headers=headers,
            name=name,
            service_name=service_name,
            signals=signals,
        )

        update_export_destination_dto.additional_properties = d
        return update_export_destination_dto

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
