from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection import Connection


T = TypeVar("T", bound="ConnectionsOutputBody")


@_attrs_define
class ConnectionsOutputBody:
    """
    Attributes:
        connections (list[Connection] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    connections: list[Connection] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection import Connection

        connections: list[dict[str, Any]] | None
        if isinstance(self.connections, list):
            connections = []
            for connections_type_0_item_data in self.connections:
                connections_type_0_item = connections_type_0_item_data.to_dict()
                connections.append(connections_type_0_item)

        else:
            connections = self.connections

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connections": connections,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection import Connection

        d = dict(src_dict)

        def _parse_connections(data: object) -> list[Connection] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                connections_type_0 = []
                _connections_type_0 = data
                for connections_type_0_item_data in _connections_type_0:
                    connections_type_0_item = Connection.from_dict(connections_type_0_item_data)

                    connections_type_0.append(connections_type_0_item)

                return connections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Connection] | None, data)

        connections = _parse_connections(d.pop("connections"))

        schema = d.pop("$schema", UNSET)

        connections_output_body = cls(
            connections=connections,
            schema=schema,
        )

        return connections_output_body
