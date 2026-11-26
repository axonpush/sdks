from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_observation import ActivityObservation
    from ..models.activity_workspace_spec import ActivityWorkspaceSpec


T = TypeVar("T", bound="WorkspacePreviewInputBody")


@_attrs_define
class WorkspacePreviewInputBody:
    """
    Attributes:
        observations (list[ActivityObservation] | None):
        spec (ActivityWorkspaceSpec):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    observations: list[ActivityObservation] | None
    spec: ActivityWorkspaceSpec
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_observation import ActivityObservation
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        observations: list[dict[str, Any]] | None
        if isinstance(self.observations, list):
            observations = []
            for observations_type_0_item_data in self.observations:
                observations_type_0_item = observations_type_0_item_data.to_dict()
                observations.append(observations_type_0_item)

        else:
            observations = self.observations

        spec = self.spec.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "observations": observations,
                "spec": spec,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_observation import ActivityObservation
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

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

        spec = ActivityWorkspaceSpec.from_dict(d.pop("spec"))

        schema = d.pop("$schema", UNSET)

        workspace_preview_input_body = cls(
            observations=observations,
            spec=spec,
            schema=schema,
        )

        return workspace_preview_input_body
