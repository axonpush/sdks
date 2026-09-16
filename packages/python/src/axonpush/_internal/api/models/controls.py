from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_capability import AuditCapability
    from ..models.budget_capability import BudgetCapability
    from ..models.moderation_capability import ModerationCapability


T = TypeVar("T", bound="Controls")


@_attrs_define
class Controls:
    """
    Attributes:
        audit_trail (AuditCapability):
        cost_budgets (BudgetCapability):
        inline_moderation (ModerationCapability):
    """

    audit_trail: AuditCapability
    cost_budgets: BudgetCapability
    inline_moderation: ModerationCapability

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_capability import AuditCapability
        from ..models.budget_capability import BudgetCapability
        from ..models.moderation_capability import ModerationCapability

        audit_trail = self.audit_trail.to_dict()

        cost_budgets = self.cost_budgets.to_dict()

        inline_moderation = self.inline_moderation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "auditTrail": audit_trail,
                "costBudgets": cost_budgets,
                "inlineModeration": inline_moderation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_capability import AuditCapability
        from ..models.budget_capability import BudgetCapability
        from ..models.moderation_capability import ModerationCapability

        d = dict(src_dict)
        audit_trail = AuditCapability.from_dict(d.pop("auditTrail"))

        cost_budgets = BudgetCapability.from_dict(d.pop("costBudgets"))

        inline_moderation = ModerationCapability.from_dict(d.pop("inlineModeration"))

        controls = cls(
            audit_trail=audit_trail,
            cost_budgets=cost_budgets,
            inline_moderation=inline_moderation,
        )

        return controls
