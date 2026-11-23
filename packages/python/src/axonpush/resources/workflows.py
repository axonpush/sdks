"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    ActionDecision,
    ActionReceipt,
    ActionRecord,
    ActionsPage,
    ActivateInputBody1,
    ActivationOutputBody,
    Bundle,
    Case,
    CasesOutputBody,
    ClaimRequestBody,
    ClaimResponseBody,
    Definition,
    DefinitionListBody,
    DiffInputBody1,
    DiffOutputBody1,
    Disposition,
    FactsInputBody,
    Proposal,
    RegisterSourceInputBody,
    ReplayInputBody,
    Result,
    SimulationInputBody,
    SourceInputBody,
    SourcesOutputBody,
    StatusOutputBody,
    WorkflowSetupGuide,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.workflows import workflows_actions as _actions_op
from axonpush._internal.api.api.workflows import workflows_activation as _activation_op
from axonpush._internal.api.api.workflows import workflows_activate as _activate_op
from axonpush._internal.api.api.workflows import workflows_cases as _cases_op
from axonpush._internal.api.api.workflows import workflows_case as _case_op
from axonpush._internal.api.api.workflows import workflows_propose_action as _propose_action_op
from axonpush._internal.api.api.workflows import workflows_decide_action as _decide_action_op
from axonpush._internal.api.api.workflows import workflows_action_receipt as _action_receipt_op
from axonpush._internal.api.api.workflows import workflows_close as _close_op
from axonpush._internal.api.api.workflows import workflows_disposition as _disposition_op
from axonpush._internal.api.api.workflows import workflows_replay as _replay_op
from axonpush._internal.api.api.workflows import workflows_compile as _compile_op
from axonpush._internal.api.api.workflows import workflows_definitions as _definitions_op
from axonpush._internal.api.api.workflows import workflows_publish as _publish_op
from axonpush._internal.api.api.workflows import workflows_describe as _describe_op
from axonpush._internal.api.api.workflows import workflows_diff as _diff_op
from axonpush._internal.api.api.workflows import workflows_facts as _facts_op
from axonpush._internal.api.api.workflows import workflows_simulate as _simulate_op
from axonpush._internal.api.api.workflows import workflows_sources as _sources_op
from axonpush._internal.api.api.workflows import workflows_register_source as _register_source_op
from axonpush._internal.api.api.workflows import workflows_claim_action as _claim_action_op


class Workflows:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def actions(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActionsPage | None:
        """Discover typed actions available on a case or list review and recovery tasks."""
        return self._client._invoke(
            _actions_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def activation(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivationOutputBody | None:
        """Read active workflow versions for this environment."""
        return self._client._invoke(
            _activation_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def activate(
        self, workspace_id: str, body: ActivateInputBody1, params: Mapping[str, Any] | None = None
    ) -> StatusOutputBody | None:
        """Activate a published version for new cases in this environment."""
        return self._client._invoke(
            _activate_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def cases(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> CasesOutputBody | None:
        """List business cases; cursor pagination is scoped to workspace and environment."""
        return self._client._invoke(
            _cases_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def case(
        self, workspace_id: str, case_key: str, params: Mapping[str, Any] | None = None
    ) -> Case | None:
        """Inspect a case, pinned contract, evidence and verification."""
        return self._client._invoke(
            _case_op,
            workspace_id=workspace_id,
            case_key=case_key,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def propose_action(
        self,
        workspace_id: str,
        case_key: str,
        body: Proposal,
        params: Mapping[str, Any] | None = None,
    ) -> ActionRecord | None:
        """Propose a typed action against the current case state."""
        return self._client._invoke(
            _propose_action_op,
            workspace_id=workspace_id,
            case_key=case_key,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def decide_action(
        self,
        workspace_id: str,
        case_key: str,
        action_id: str,
        body: ActionDecision,
        params: Mapping[str, Any] | None = None,
    ) -> ActionRecord | None:
        """Review a specific proposal revision or request recovery."""
        return self._client._invoke(
            _decide_action_op,
            workspace_id=workspace_id,
            case_key=case_key,
            action_id=action_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def action_receipt(
        self,
        workspace_id: str,
        case_key: str,
        action_id: str,
        body: ActionReceipt,
        params: Mapping[str, Any] | None = None,
    ) -> ActionRecord | None:
        """Record an execution receipt or authoritative lookup for a lease."""
        return self._client._invoke(
            _action_receipt_op,
            workspace_id=workspace_id,
            case_key=case_key,
            action_id=action_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def close(
        self, workspace_id: str, case_key: str, params: Mapping[str, Any] | None = None
    ) -> StatusOutputBody | None:
        """Close case ingestion and retain its history for 90 days; this does not verify completion."""
        return self._client._invoke(
            _close_op,
            workspace_id=workspace_id,
            case_key=case_key,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def disposition(
        self,
        workspace_id: str,
        case_key: str,
        obligation_id: str,
        body: Disposition,
        params: Mapping[str, Any] | None = None,
    ) -> StatusOutputBody | None:
        """Record an audited human disposition; acknowledgement does not verify completion."""
        return self._client._invoke(
            _disposition_op,
            workspace_id=workspace_id,
            case_key=case_key,
            obligation_id=obligation_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def replay(
        self,
        workspace_id: str,
        case_key: str,
        body: ReplayInputBody,
        params: Mapping[str, Any] | None = None,
    ) -> Result | None:
        """Preview a version against one case; apply only queues a replay of its pinned version."""
        return self._client._invoke(
            _replay_op,
            workspace_id=workspace_id,
            case_key=case_key,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def compile(
        self, workspace_id: str, body: SourceInputBody, params: Mapping[str, Any] | None = None
    ) -> Bundle | None:
        """Compile an explicit workflow contract without saving."""
        return self._client._invoke(
            _compile_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def definitions(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> DefinitionListBody | None:
        """List up to 100 immutable workflow definitions."""
        return self._client._invoke(
            _definitions_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def publish(
        self, workspace_id: str, body: SourceInputBody, params: Mapping[str, Any] | None = None
    ) -> Definition | None:
        """Publish an immutable workflow definition; activation is separate."""
        return self._client._invoke(
            _publish_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def describe(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkflowSetupGuide | None:
        """Start here: guided workflow setup questions, exact tool sequence and a deterministic booking example; read-only."""
        return self._client._invoke(
            _describe_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def diff(
        self, workspace_id: str, body: DiffInputBody1, params: Mapping[str, Any] | None = None
    ) -> DiffOutputBody1 | None:
        """Compare semantic and source identities without changing deployed definitions."""
        return self._client._invoke(
            _diff_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def facts(
        self, workspace_id: str, body: FactsInputBody, params: Mapping[str, Any] | None = None
    ) -> StatusOutputBody | None:
        """Persist case facts and queue verification; receipt means stored, not verified."""
        return self._client._invoke(
            _facts_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def simulate(
        self, workspace_id: str, body: SimulationInputBody, params: Mapping[str, Any] | None = None
    ) -> Result | None:
        """Evaluate supplied evidence with an explicit clock; no state is saved."""
        return self._client._invoke(
            _simulate_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def sources(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> SourcesOutputBody | None:
        """Read configured source bindings; configuration alone does not establish coverage."""
        return self._client._invoke(
            _sources_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def register_source(
        self,
        workspace_id: str,
        body: RegisterSourceInputBody,
        params: Mapping[str, Any] | None = None,
    ) -> StatusOutputBody | None:
        """Bind an evidence source to an explicit publisher identity."""
        return self._client._invoke(
            _register_source_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def claim_action(
        self, workspace_id: str, body: ClaimRequestBody, params: Mapping[str, Any] | None = None
    ) -> ClaimResponseBody | None:
        """Lease one command for this outbound worker."""
        return self._client._invoke(
            _claim_action_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )


class AsyncWorkflows:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def actions(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActionsPage | None:
        """Discover typed actions available on a case or list review and recovery tasks."""
        return await self._client._invoke(
            _actions_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def activation(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivationOutputBody | None:
        """Read active workflow versions for this environment."""
        return await self._client._invoke(
            _activation_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def activate(
        self, workspace_id: str, body: ActivateInputBody1, params: Mapping[str, Any] | None = None
    ) -> StatusOutputBody | None:
        """Activate a published version for new cases in this environment."""
        return await self._client._invoke(
            _activate_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def cases(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> CasesOutputBody | None:
        """List business cases; cursor pagination is scoped to workspace and environment."""
        return await self._client._invoke(
            _cases_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def case(
        self, workspace_id: str, case_key: str, params: Mapping[str, Any] | None = None
    ) -> Case | None:
        """Inspect a case, pinned contract, evidence and verification."""
        return await self._client._invoke(
            _case_op,
            workspace_id=workspace_id,
            case_key=case_key,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def propose_action(
        self,
        workspace_id: str,
        case_key: str,
        body: Proposal,
        params: Mapping[str, Any] | None = None,
    ) -> ActionRecord | None:
        """Propose a typed action against the current case state."""
        return await self._client._invoke(
            _propose_action_op,
            workspace_id=workspace_id,
            case_key=case_key,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def decide_action(
        self,
        workspace_id: str,
        case_key: str,
        action_id: str,
        body: ActionDecision,
        params: Mapping[str, Any] | None = None,
    ) -> ActionRecord | None:
        """Review a specific proposal revision or request recovery."""
        return await self._client._invoke(
            _decide_action_op,
            workspace_id=workspace_id,
            case_key=case_key,
            action_id=action_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def action_receipt(
        self,
        workspace_id: str,
        case_key: str,
        action_id: str,
        body: ActionReceipt,
        params: Mapping[str, Any] | None = None,
    ) -> ActionRecord | None:
        """Record an execution receipt or authoritative lookup for a lease."""
        return await self._client._invoke(
            _action_receipt_op,
            workspace_id=workspace_id,
            case_key=case_key,
            action_id=action_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def close(
        self, workspace_id: str, case_key: str, params: Mapping[str, Any] | None = None
    ) -> StatusOutputBody | None:
        """Close case ingestion and retain its history for 90 days; this does not verify completion."""
        return await self._client._invoke(
            _close_op,
            workspace_id=workspace_id,
            case_key=case_key,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def disposition(
        self,
        workspace_id: str,
        case_key: str,
        obligation_id: str,
        body: Disposition,
        params: Mapping[str, Any] | None = None,
    ) -> StatusOutputBody | None:
        """Record an audited human disposition; acknowledgement does not verify completion."""
        return await self._client._invoke(
            _disposition_op,
            workspace_id=workspace_id,
            case_key=case_key,
            obligation_id=obligation_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def replay(
        self,
        workspace_id: str,
        case_key: str,
        body: ReplayInputBody,
        params: Mapping[str, Any] | None = None,
    ) -> Result | None:
        """Preview a version against one case; apply only queues a replay of its pinned version."""
        return await self._client._invoke(
            _replay_op,
            workspace_id=workspace_id,
            case_key=case_key,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def compile(
        self, workspace_id: str, body: SourceInputBody, params: Mapping[str, Any] | None = None
    ) -> Bundle | None:
        """Compile an explicit workflow contract without saving."""
        return await self._client._invoke(
            _compile_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def definitions(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> DefinitionListBody | None:
        """List up to 100 immutable workflow definitions."""
        return await self._client._invoke(
            _definitions_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def publish(
        self, workspace_id: str, body: SourceInputBody, params: Mapping[str, Any] | None = None
    ) -> Definition | None:
        """Publish an immutable workflow definition; activation is separate."""
        return await self._client._invoke(
            _publish_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def describe(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkflowSetupGuide | None:
        """Start here: guided workflow setup questions, exact tool sequence and a deterministic booking example; read-only."""
        return await self._client._invoke(
            _describe_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def diff(
        self, workspace_id: str, body: DiffInputBody1, params: Mapping[str, Any] | None = None
    ) -> DiffOutputBody1 | None:
        """Compare semantic and source identities without changing deployed definitions."""
        return await self._client._invoke(
            _diff_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def facts(
        self, workspace_id: str, body: FactsInputBody, params: Mapping[str, Any] | None = None
    ) -> StatusOutputBody | None:
        """Persist case facts and queue verification; receipt means stored, not verified."""
        return await self._client._invoke(
            _facts_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def simulate(
        self, workspace_id: str, body: SimulationInputBody, params: Mapping[str, Any] | None = None
    ) -> Result | None:
        """Evaluate supplied evidence with an explicit clock; no state is saved."""
        return await self._client._invoke(
            _simulate_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def sources(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> SourcesOutputBody | None:
        """Read configured source bindings; configuration alone does not establish coverage."""
        return await self._client._invoke(
            _sources_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def register_source(
        self,
        workspace_id: str,
        body: RegisterSourceInputBody,
        params: Mapping[str, Any] | None = None,
    ) -> StatusOutputBody | None:
        """Bind an evidence source to an explicit publisher identity."""
        return await self._client._invoke(
            _register_source_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def claim_action(
        self, workspace_id: str, body: ClaimRequestBody, params: Mapping[str, Any] | None = None
    ) -> ClaimResponseBody | None:
        """Lease one command for this outbound worker."""
        return await self._client._invoke(
            _claim_action_op,
            workspace_id=workspace_id,
            body=body,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )
