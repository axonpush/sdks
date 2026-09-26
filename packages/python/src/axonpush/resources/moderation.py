"""Moderation resource — rules CRUD and violation listing. ``/moderation``."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.moderation import (
    moderation_efficacy as _efficacy_op,
    moderation_rules_create as _create_op,
    moderation_rules_delete as _delete_op,
    moderation_rules_list as _list_op,
    moderation_violations_list as _violations_op,
)
from axonpush._internal.api.models import (
    CreateRuleInputBody,
    CreateRuleInputBodyAction,
    EfficacyOutputBody,
    ListRulesOutputBody,
    ListViolationsOutputBody,
    OkOutputBody,
    RuleDTO,
    ViolationDTO,
)
from axonpush._internal.api.types import UNSET

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap_rules(result: ListRulesOutputBody | None) -> List[RuleDTO] | None:
    if result is None:
        return None
    return list(result.rules or [])


def _unwrap_violations(result: ListViolationsOutputBody | None) -> List[ViolationDTO] | None:
    if result is None:
        return None
    return list(result.violations or [])


def _build_rule_dto(
    *,
    name: str,
    detector: str,
    action: CreateRuleInputBodyAction | str,
    pattern: str | None,
) -> CreateRuleInputBody:
    resolved = (
        action if isinstance(action, CreateRuleInputBodyAction) else CreateRuleInputBodyAction(action)
    )
    return CreateRuleInputBody(
        name=name,
        detector=detector,
        action=resolved,
        pattern=pattern if pattern is not None else UNSET,
    )


class Moderation:
    """Moderation rules and violations."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list_rules(self) -> List[RuleDTO] | None:
        """List moderation rules (envelope unwrapped). ``GET /moderation/rules``"""
        return self._client._invoke(_list_op, _coerce=_unwrap_rules)

    def create_rule(
        self,
        *,
        name: str,
        detector: str,
        action: CreateRuleInputBodyAction | str,
        pattern: str | None = None,
    ) -> RuleDTO | None:
        """Create a moderation rule. ``POST /moderation/rules``"""
        body = _build_rule_dto(name=name, detector=detector, action=action, pattern=pattern)
        return self._client._invoke(_create_op, body=body)

    def delete_rule(self, rule_id: str) -> OkOutputBody | None:
        """Delete a moderation rule. ``DELETE /moderation/rules/{ruleId}``"""
        return self._client._invoke(_delete_op, rule_id=rule_id)

    def list_violations(self, *, limit: int | None = None) -> List[ViolationDTO] | None:
        """List moderation violations (envelope unwrapped). ``GET /moderation/violations``"""
        kwargs = {} if limit is None else {"limit": limit}
        return self._client._invoke(_violations_op, _coerce=_unwrap_violations, **kwargs)

    def efficacy(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
    ) -> EfficacyOutputBody | None:
        """Rule efficacy metrics. ``GET /moderation/efficacy``"""
        kwargs = {
            k: v for k, v in {"since": since, "until": until}.items() if v is not None
        }
        return self._client._invoke(_efficacy_op, **kwargs)


class AsyncModeration:
    """Async sibling of :class:`Moderation`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list_rules(self) -> List[RuleDTO] | None:
        """See :meth:`Moderation.list_rules`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap_rules)

    async def create_rule(
        self,
        *,
        name: str,
        detector: str,
        action: CreateRuleInputBodyAction | str,
        pattern: str | None = None,
    ) -> RuleDTO | None:
        """See :meth:`Moderation.create_rule`."""
        body = _build_rule_dto(name=name, detector=detector, action=action, pattern=pattern)
        return await self._client._invoke(_create_op, body=body)

    async def delete_rule(self, rule_id: str) -> OkOutputBody | None:
        """See :meth:`Moderation.delete_rule`."""
        return await self._client._invoke(_delete_op, rule_id=rule_id)

    async def list_violations(self, *, limit: int | None = None) -> List[ViolationDTO] | None:
        """See :meth:`Moderation.list_violations`."""
        kwargs = {} if limit is None else {"limit": limit}
        return await self._client._invoke(_violations_op, _coerce=_unwrap_violations, **kwargs)

    async def efficacy(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
    ) -> EfficacyOutputBody | None:
        """See :meth:`Moderation.efficacy`."""
        kwargs = {
            k: v for k, v in {"since": since, "until": until}.items() if v is not None
        }
        return await self._client._invoke(_efficacy_op, **kwargs)
