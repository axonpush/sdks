from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diff_cohort_dto import DiffCohortDTO


T = TypeVar("T", bound="DiffInputBody")


@_attrs_define
class DiffInputBody:
    """
    Attributes:
        baseline (DiffCohortDTO):
        selection (DiffCohortDTO):
        schema (str | Unset): A URL to the JSON Schema for this object.
        keys (list[str] | None | Unset): Attribute keys to diff; defaults to the top cataloged keys (capped)
        limit (int | Unset): Max ranked attributes to return (default and max 20)
    """

    baseline: DiffCohortDTO
    selection: DiffCohortDTO
    schema: str | Unset = UNSET
    keys: list[str] | None | Unset = UNSET
    limit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.diff_cohort_dto import DiffCohortDTO

        baseline = self.baseline.to_dict()

        selection = self.selection.to_dict()

        schema = self.schema

        keys: list[str] | None | Unset
        if isinstance(self.keys, Unset):
            keys = UNSET
        elif isinstance(self.keys, list):
            keys = self.keys

        else:
            keys = self.keys

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "baseline": baseline,
                "selection": selection,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if keys is not UNSET:
            field_dict["keys"] = keys
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diff_cohort_dto import DiffCohortDTO

        d = dict(src_dict)
        baseline = DiffCohortDTO.from_dict(d.pop("baseline"))

        selection = DiffCohortDTO.from_dict(d.pop("selection"))

        schema = d.pop("$schema", UNSET)

        def _parse_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = cast(list[str], data)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keys = _parse_keys(d.pop("keys", UNSET))

        limit = d.pop("limit", UNSET)

        diff_input_body = cls(
            baseline=baseline,
            selection=selection,
            schema=schema,
            keys=keys,
            limit=limit,
        )

        return diff_input_body
