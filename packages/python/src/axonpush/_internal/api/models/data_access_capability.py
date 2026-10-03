from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataAccessCapability")


@_attrs_define
class DataAccessCapability:
    """
    Attributes:
        aggregate_retention_days (int):
        description (str):
        identifiable_retention_days (int):
        refused_for_scoped (list[str] | None):
        scoped_grants (bool):
    """

    aggregate_retention_days: int
    description: str
    identifiable_retention_days: int
    refused_for_scoped: list[str] | None
    scoped_grants: bool

    def to_dict(self) -> dict[str, Any]:
        aggregate_retention_days = self.aggregate_retention_days

        description = self.description

        identifiable_retention_days = self.identifiable_retention_days

        refused_for_scoped: list[str] | None
        if isinstance(self.refused_for_scoped, list):
            refused_for_scoped = self.refused_for_scoped

        else:
            refused_for_scoped = self.refused_for_scoped

        scoped_grants = self.scoped_grants

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "aggregateRetentionDays": aggregate_retention_days,
                "description": description,
                "identifiableRetentionDays": identifiable_retention_days,
                "refusedForScoped": refused_for_scoped,
                "scopedGrants": scoped_grants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aggregate_retention_days = d.pop("aggregateRetentionDays")

        description = d.pop("description")

        identifiable_retention_days = d.pop("identifiableRetentionDays")

        def _parse_refused_for_scoped(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refused_for_scoped_type_0 = cast(list[str], data)

                return refused_for_scoped_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        refused_for_scoped = _parse_refused_for_scoped(d.pop("refusedForScoped"))

        scoped_grants = d.pop("scopedGrants")

        data_access_capability = cls(
            aggregate_retention_days=aggregate_retention_days,
            description=description,
            identifiable_retention_days=identifiable_retention_days,
            refused_for_scoped=refused_for_scoped,
            scoped_grants=scoped_grants,
        )

        return data_access_capability
