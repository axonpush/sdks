from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.ingest_category_total_dto import IngestCategoryTotalDTO
    from ..models.ingest_outcome_dto import IngestOutcomeDTO


T = TypeVar("T", bound="ListOutcomesOutputBody")


@_attrs_define
class ListOutcomesOutputBody:
    """
    Attributes:
        outcomes (list[IngestOutcomeDTO] | None):
        totals (list[IngestCategoryTotalDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    outcomes: list[IngestOutcomeDTO] | None
    totals: list[IngestCategoryTotalDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.ingest_category_total_dto import IngestCategoryTotalDTO
        from ..models.ingest_outcome_dto import IngestOutcomeDTO

        outcomes: list[dict[str, Any]] | None
        if isinstance(self.outcomes, list):
            outcomes = []
            for outcomes_type_0_item_data in self.outcomes:
                outcomes_type_0_item = outcomes_type_0_item_data.to_dict()
                outcomes.append(outcomes_type_0_item)

        else:
            outcomes = self.outcomes

        totals: list[dict[str, Any]] | None
        if isinstance(self.totals, list):
            totals = []
            for totals_type_0_item_data in self.totals:
                totals_type_0_item = totals_type_0_item_data.to_dict()
                totals.append(totals_type_0_item)

        else:
            totals = self.totals

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "outcomes": outcomes,
                "totals": totals,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingest_category_total_dto import IngestCategoryTotalDTO
        from ..models.ingest_outcome_dto import IngestOutcomeDTO

        d = dict(src_dict)

        def _parse_outcomes(data: object) -> list[IngestOutcomeDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outcomes_type_0 = []
                _outcomes_type_0 = data
                for outcomes_type_0_item_data in _outcomes_type_0:
                    outcomes_type_0_item = IngestOutcomeDTO.from_dict(outcomes_type_0_item_data)

                    outcomes_type_0.append(outcomes_type_0_item)

                return outcomes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IngestOutcomeDTO] | None, data)

        outcomes = _parse_outcomes(d.pop("outcomes"))

        def _parse_totals(data: object) -> list[IngestCategoryTotalDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                totals_type_0 = []
                _totals_type_0 = data
                for totals_type_0_item_data in _totals_type_0:
                    totals_type_0_item = IngestCategoryTotalDTO.from_dict(totals_type_0_item_data)

                    totals_type_0.append(totals_type_0_item)

                return totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IngestCategoryTotalDTO] | None, data)

        totals = _parse_totals(d.pop("totals"))

        schema = d.pop("$schema", UNSET)

        list_outcomes_output_body = cls(
            outcomes=outcomes,
            totals=totals,
            schema=schema,
        )

        return list_outcomes_output_body
