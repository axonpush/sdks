from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.case_schema import CaseSchema
    from ..models.contract_facts import ContractFacts
    from ..models.contract_requirements import ContractRequirements
    from ..models.presentation import Presentation


T = TypeVar("T", bound="Contract")


@_attrs_define
class Contract:
    """
    Attributes:
        case (CaseSchema):
        facts (ContractFacts):
        presentation (Presentation):
        requirements (ContractRequirements):
        schema_version (int):
        workflow (str):
    """

    case: CaseSchema
    facts: ContractFacts
    presentation: Presentation
    requirements: ContractRequirements
    schema_version: int
    workflow: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.case_schema import CaseSchema
        from ..models.contract_facts import ContractFacts
        from ..models.contract_requirements import ContractRequirements
        from ..models.presentation import Presentation

        case = self.case.to_dict()

        facts = self.facts.to_dict()

        presentation = self.presentation.to_dict()

        requirements = self.requirements.to_dict()

        schema_version = self.schema_version

        workflow = self.workflow

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "case": case,
                "facts": facts,
                "presentation": presentation,
                "requirements": requirements,
                "schema_version": schema_version,
                "workflow": workflow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.case_schema import CaseSchema
        from ..models.contract_facts import ContractFacts
        from ..models.contract_requirements import ContractRequirements
        from ..models.presentation import Presentation

        d = dict(src_dict)
        case = CaseSchema.from_dict(d.pop("case"))

        facts = ContractFacts.from_dict(d.pop("facts"))

        presentation = Presentation.from_dict(d.pop("presentation"))

        requirements = ContractRequirements.from_dict(d.pop("requirements"))

        schema_version = d.pop("schema_version")

        workflow = d.pop("workflow")

        contract = cls(
            case=case,
            facts=facts,
            presentation=presentation,
            requirements=requirements,
            schema_version=schema_version,
            workflow=workflow,
        )

        return contract
