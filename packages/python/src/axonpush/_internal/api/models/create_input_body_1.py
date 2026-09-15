from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_input_body_1_headers import CreateInputBody1Headers


T = TypeVar("T", bound="CreateInputBody1")


@_attrs_define
class CreateInputBody1:
    """
    Attributes:
        endpoint_url (str):
        env_slug (str):
        name (str):
        signals (list[str] | None): OTLP signals: logs and/or traces
        schema (str | Unset): A URL to the JSON Schema for this object.
        event_type_filter (list[str] | None | Unset):
        headers (CreateInputBody1Headers | Unset): Header name -> value map. Stored server-side, never returned.
        service_name (str | Unset):
    """

    endpoint_url: str
    env_slug: str
    name: str
    signals: list[str] | None
    schema: str | Unset = UNSET
    event_type_filter: list[str] | None | Unset = UNSET
    headers: CreateInputBody1Headers | Unset = UNSET
    service_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_input_body_1_headers import CreateInputBody1Headers

        endpoint_url = self.endpoint_url

        env_slug = self.env_slug

        name = self.name

        signals: list[str] | None
        if isinstance(self.signals, list):
            signals = self.signals

        else:
            signals = self.signals

        schema = self.schema

        event_type_filter: list[str] | None | Unset
        if isinstance(self.event_type_filter, Unset):
            event_type_filter = UNSET
        elif isinstance(self.event_type_filter, list):
            event_type_filter = self.event_type_filter

        else:
            event_type_filter = self.event_type_filter

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        service_name = self.service_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpointUrl": endpoint_url,
                "envSlug": env_slug,
                "name": name,
                "signals": signals,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if event_type_filter is not UNSET:
            field_dict["eventTypeFilter"] = event_type_filter
        if headers is not UNSET:
            field_dict["headers"] = headers
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_input_body_1_headers import CreateInputBody1Headers

        d = dict(src_dict)
        endpoint_url = d.pop("endpointUrl")

        env_slug = d.pop("envSlug")

        name = d.pop("name")

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

        def _parse_event_type_filter(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_type_filter_type_0 = cast(list[str], data)

                return event_type_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_type_filter = _parse_event_type_filter(d.pop("eventTypeFilter", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: CreateInputBody1Headers | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CreateInputBody1Headers.from_dict(_headers)

        service_name = d.pop("serviceName", UNSET)

        create_input_body_1 = cls(
            endpoint_url=endpoint_url,
            env_slug=env_slug,
            name=name,
            signals=signals,
            schema=schema,
            event_type_filter=event_type_filter,
            headers=headers,
            service_name=service_name,
        )

        return create_input_body_1
