from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage import Coverage
    from ..models.fact import Fact
    from ..models.input_case_fields import InputCaseFields
    from ..models.input_subjects import InputSubjects
    from ..models.obligation import Obligation


T = TypeVar("T", bound="Input")


@_attrs_define
class Input:
    """
    Attributes:
        case_id (str):
        coverage (list[Coverage] | None):
        facts (list[Fact] | None):
        case_fields (InputCaseFields | Unset):
        now (datetime.datetime | Unset):
        previous (list[Obligation] | None | Unset):
        subjects (InputSubjects | Unset):
    """

    case_id: str
    coverage: list[Coverage] | None
    facts: list[Fact] | None
    case_fields: InputCaseFields | Unset = UNSET
    now: datetime.datetime | Unset = UNSET
    previous: list[Obligation] | None | Unset = UNSET
    subjects: InputSubjects | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.coverage import Coverage
        from ..models.fact import Fact
        from ..models.input_case_fields import InputCaseFields
        from ..models.input_subjects import InputSubjects
        from ..models.obligation import Obligation

        case_id = self.case_id

        coverage: list[dict[str, Any]] | None
        if isinstance(self.coverage, list):
            coverage = []
            for coverage_type_0_item_data in self.coverage:
                coverage_type_0_item = coverage_type_0_item_data.to_dict()
                coverage.append(coverage_type_0_item)

        else:
            coverage = self.coverage

        facts: list[dict[str, Any]] | None
        if isinstance(self.facts, list):
            facts = []
            for facts_type_0_item_data in self.facts:
                facts_type_0_item = facts_type_0_item_data.to_dict()
                facts.append(facts_type_0_item)

        else:
            facts = self.facts

        case_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.case_fields, Unset):
            case_fields = self.case_fields.to_dict()

        now: str | Unset = UNSET
        if not isinstance(self.now, Unset):
            now = self.now.isoformat()

        previous: list[dict[str, Any]] | None | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        elif isinstance(self.previous, list):
            previous = []
            for previous_type_0_item_data in self.previous:
                previous_type_0_item = previous_type_0_item_data.to_dict()
                previous.append(previous_type_0_item)

        else:
            previous = self.previous

        subjects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subjects, Unset):
            subjects = self.subjects.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "case_id": case_id,
                "coverage": coverage,
                "facts": facts,
            }
        )
        if case_fields is not UNSET:
            field_dict["case_fields"] = case_fields
        if now is not UNSET:
            field_dict["now"] = now
        if previous is not UNSET:
            field_dict["previous"] = previous
        if subjects is not UNSET:
            field_dict["subjects"] = subjects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage import Coverage
        from ..models.fact import Fact
        from ..models.input_case_fields import InputCaseFields
        from ..models.input_subjects import InputSubjects
        from ..models.obligation import Obligation

        d = dict(src_dict)
        case_id = d.pop("case_id")

        def _parse_coverage(data: object) -> list[Coverage] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                coverage_type_0 = []
                _coverage_type_0 = data
                for coverage_type_0_item_data in _coverage_type_0:
                    coverage_type_0_item = Coverage.from_dict(coverage_type_0_item_data)

                    coverage_type_0.append(coverage_type_0_item)

                return coverage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Coverage] | None, data)

        coverage = _parse_coverage(d.pop("coverage"))

        def _parse_facts(data: object) -> list[Fact] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facts_type_0 = []
                _facts_type_0 = data
                for facts_type_0_item_data in _facts_type_0:
                    facts_type_0_item = Fact.from_dict(facts_type_0_item_data)

                    facts_type_0.append(facts_type_0_item)

                return facts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Fact] | None, data)

        facts = _parse_facts(d.pop("facts"))

        _case_fields = d.pop("case_fields", UNSET)
        case_fields: InputCaseFields | Unset
        if isinstance(_case_fields, Unset):
            case_fields = UNSET
        else:
            case_fields = InputCaseFields.from_dict(_case_fields)

        _now = d.pop("now", UNSET)
        now: datetime.datetime | Unset
        if isinstance(_now, Unset):
            now = UNSET
        else:
            now = isoparse(_now)

        def _parse_previous(data: object) -> list[Obligation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                previous_type_0 = []
                _previous_type_0 = data
                for previous_type_0_item_data in _previous_type_0:
                    previous_type_0_item = Obligation.from_dict(
                        previous_type_0_item_data
                    )

                    previous_type_0.append(previous_type_0_item)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Obligation] | None | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        _subjects = d.pop("subjects", UNSET)
        subjects: InputSubjects | Unset
        if isinstance(_subjects, Unset):
            subjects = UNSET
        else:
            subjects = InputSubjects.from_dict(_subjects)

        input_ = cls(
            case_id=case_id,
            coverage=coverage,
            facts=facts,
            case_fields=case_fields,
            now=now,
            previous=previous,
            subjects=subjects,
        )

        return input_
