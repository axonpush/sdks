from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_incident import ActivityIncident


T = TypeVar("T", bound="WorkspaceIncidentsOutputBody")


@_attrs_define
class WorkspaceIncidentsOutputBody:
    """
    Attributes:
        incidents (list[ActivityIncident] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    incidents: list[ActivityIncident] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_incident import ActivityIncident

        incidents: list[dict[str, Any]] | None
        if isinstance(self.incidents, list):
            incidents = []
            for incidents_type_0_item_data in self.incidents:
                incidents_type_0_item = incidents_type_0_item_data.to_dict()
                incidents.append(incidents_type_0_item)

        else:
            incidents = self.incidents

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incidents": incidents,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_incident import ActivityIncident

        d = dict(src_dict)

        def _parse_incidents(data: object) -> list[ActivityIncident] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incidents_type_0 = []
                _incidents_type_0 = data
                for incidents_type_0_item_data in _incidents_type_0:
                    incidents_type_0_item = ActivityIncident.from_dict(incidents_type_0_item_data)

                    incidents_type_0.append(incidents_type_0_item)

                return incidents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityIncident] | None, data)

        incidents = _parse_incidents(d.pop("incidents"))

        schema = d.pop("$schema", UNSET)

        workspace_incidents_output_body = cls(
            incidents=incidents,
            schema=schema,
        )

        return workspace_incidents_output_body
