from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_capability import AuditCapability
    from ..models.moderation_capability import ModerationCapability
    from ..models.spend_policy_capability import SpendPolicyCapability


T = TypeVar("T", bound="Controls")


@_attrs_define
class Controls:
    """
    Attributes:
        audit_trail (AuditCapability):
        inline_moderation (ModerationCapability):
        spend_policies (SpendPolicyCapability):
    """

    audit_trail: AuditCapability
    inline_moderation: ModerationCapability
    spend_policies: SpendPolicyCapability

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_capability import AuditCapability
        from ..models.moderation_capability import ModerationCapability
        from ..models.spend_policy_capability import SpendPolicyCapability

        audit_trail = self.audit_trail.to_dict()

        inline_moderation = self.inline_moderation.to_dict()

        spend_policies = self.spend_policies.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "auditTrail": audit_trail,
                "inlineModeration": inline_moderation,
                "spendPolicies": spend_policies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_capability import AuditCapability
        from ..models.moderation_capability import ModerationCapability
        from ..models.spend_policy_capability import SpendPolicyCapability

        d = dict(src_dict)
        audit_trail = AuditCapability.from_dict(d.pop("auditTrail"))

        inline_moderation = ModerationCapability.from_dict(d.pop("inlineModeration"))

        spend_policies = SpendPolicyCapability.from_dict(d.pop("spendPolicies"))

        controls = cls(
            audit_trail=audit_trail,
            inline_moderation=inline_moderation,
            spend_policies=spend_policies,
        )

        return controls
