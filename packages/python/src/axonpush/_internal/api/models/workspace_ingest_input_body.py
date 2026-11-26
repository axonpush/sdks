from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_observation import ActivityObservation


T = TypeVar("T", bound="WorkspaceIngestInputBody")


@_attrs_define
class WorkspaceIngestInputBody:
    """
    Attributes:
        observations (list[ActivityObservation] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        environment (str | Unset): Environment slug or id; defaults to each observation's environment
    """

    observations: list[ActivityObservation] | None
    schema: str | Unset = UNSET
    environment: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_observation import ActivityObservation

        observations: list[dict[str, Any]] | None
        if isinstance(self.observations, list):
            observations = []
            for observations_type_0_item_data in self.observations:
                observations_type_0_item = observations_type_0_item_data.to_dict()
                observations.append(observations_type_0_item)

        else:
            observations = self.observations

        schema = self.schema

        environment = self.environment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "observations": observations,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_observation import ActivityObservation

        d = dict(src_dict)

        def _parse_observations(data: object) -> list[ActivityObservation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                observations_type_0 = []
                _observations_type_0 = data
                for observations_type_0_item_data in _observations_type_0:
                    observations_type_0_item = ActivityObservation.from_dict(
                        observations_type_0_item_data
                    )

                    observations_type_0.append(observations_type_0_item)

                return observations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityObservation] | None, data)

        observations = _parse_observations(d.pop("observations"))

        schema = d.pop("$schema", UNSET)

        environment = d.pop("environment", UNSET)

        workspace_ingest_input_body = cls(
            observations=observations,
            schema=schema,
            environment=environment,
        )

        return workspace_ingest_input_body
