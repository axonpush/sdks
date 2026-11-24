from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.case_schema import CaseSchema
    from ..models.contract_actions import ContractActions
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
        actions (ContractActions | Unset):
        initial_state (str | Unset):
    """

    case: CaseSchema
    facts: ContractFacts
    presentation: Presentation
    requirements: ContractRequirements
    schema_version: int
    workflow: str
    actions: ContractActions | Unset = UNSET
    initial_state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.case_schema import CaseSchema
        from ..models.contract_actions import ContractActions
        from ..models.contract_facts import ContractFacts
        from ..models.contract_requirements import ContractRequirements
        from ..models.presentation import Presentation

        case = self.case.to_dict()

        facts = self.facts.to_dict()

        presentation = self.presentation.to_dict()

        requirements = self.requirements.to_dict()

        schema_version = self.schema_version

        workflow = self.workflow

        actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        initial_state = self.initial_state

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
        if actions is not UNSET:
            field_dict["actions"] = actions
        if initial_state is not UNSET:
            field_dict["initial_state"] = initial_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.case_schema import CaseSchema
        from ..models.contract_actions import ContractActions
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

        _actions = d.pop("actions", UNSET)
        actions: ContractActions | Unset
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = ContractActions.from_dict(_actions)

        initial_state = d.pop("initial_state", UNSET)

        contract = cls(
            case=case,
            facts=facts,
            presentation=presentation,
            requirements=requirements,
            schema_version=schema_version,
            workflow=workflow,
            actions=actions,
            initial_state=initial_state,
        )

        return contract
