from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_dto import EnvironmentDTO


T = TypeVar("T", bound="ListEnvironmentsOutputBody")


@_attrs_define
class ListEnvironmentsOutputBody:
    """
    Attributes:
        environments (list[EnvironmentDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    environments: list[EnvironmentDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_dto import EnvironmentDTO

        environments: list[dict[str, Any]] | None
        if isinstance(self.environments, list):
            environments = []
            for environments_type_0_item_data in self.environments:
                environments_type_0_item = environments_type_0_item_data.to_dict()
                environments.append(environments_type_0_item)

        else:
            environments = self.environments

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "environments": environments,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_dto import EnvironmentDTO

        d = dict(src_dict)

        def _parse_environments(data: object) -> list[EnvironmentDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environments_type_0 = []
                _environments_type_0 = data
                for environments_type_0_item_data in _environments_type_0:
                    environments_type_0_item = EnvironmentDTO.from_dict(
                        environments_type_0_item_data
                    )

                    environments_type_0.append(environments_type_0_item)

                return environments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EnvironmentDTO] | None, data)

        environments = _parse_environments(d.pop("environments"))

        schema = d.pop("$schema", UNSET)

        list_environments_output_body = cls(
            environments=environments,
            schema=schema,
        )

        return list_environments_output_body
