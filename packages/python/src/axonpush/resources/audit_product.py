"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    AccessLogOutputBody,
    ChangesOutputBody,
    ComplianceActionBody,
    ComplianceOverview,
    ComplianceRecord,
    ImportInputBody,
    ImportOutputBody,
    ListOutputBody,
    ListOutputBody3,
    NdaInputBody,
    ObligationsOutputBody,
    PatchInputBody,
    PolicyCheckInputBody,
    PolicyOutputBody,
    PublicInputBody,
    PublicWriteOutputBody,
    ShareOutputBody,
    TasksOutputBody,
    TrustOutputBody,
    TrustWriteInputBody,
    UnregisteredOutputBody,
    WriteInputBody,
    WriteOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.audit_product import audit_product_access_log as _access_log_op
from axonpush._internal.api.api.audit_product import audit_product_agents_list as _agents_list_op
from axonpush._internal.api.api.audit_product import (
    audit_product_agents_create as _agents_create_op,
)
from axonpush._internal.api.api.audit_product import audit_product_agents_get as _agents_get_op
from axonpush._internal.api.api.audit_product import (
    audit_product_agents_update as _agents_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_agents_changes as _agents_changes_op,
)
from axonpush._internal.api.api.audit_product import audit_product_agent_policy as _agent_policy_op
from axonpush._internal.api.api.audit_product import (
    audit_product_agent_policy_check as _agent_policy_check_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_agents_resume as _agents_resume_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_agents_suspend as _agents_suspend_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_assessments_list as _assessments_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_assessments_create as _assessments_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_assessments_get as _assessments_get_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_assessments_update as _assessments_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_assessments_approve as _assessments_approve_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_auditor_grants_list as _auditor_grants_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_auditor_grants_create as _auditor_grants_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_auditor_grants_get as _auditor_grants_get_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_auditor_grants_update as _auditor_grants_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_destinations_list as _destinations_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_destinations_create as _destinations_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_destinations_get as _destinations_get_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_destinations_update as _destinations_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_destinations_deliver as _destinations_deliver_op,
)
from axonpush._internal.api.api.audit_product import audit_product_grants_list as _grants_list_op
from axonpush._internal.api.api.audit_product import (
    audit_product_grants_create as _grants_create_op,
)
from axonpush._internal.api.api.audit_product import audit_product_grants_get as _grants_get_op
from axonpush._internal.api.api.audit_product import (
    audit_product_grants_update as _grants_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_incidents_list as _incidents_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_incidents_create as _incidents_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_incidents_get as _incidents_get_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_incidents_update as _incidents_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_incidents_file as _incidents_file_op,
)
from axonpush._internal.api.api.audit_product import audit_product_notices_list as _notices_list_op
from axonpush._internal.api.api.audit_product import (
    audit_product_notices_create as _notices_create_op,
)
from axonpush._internal.api.api.audit_product import audit_product_notices_get as _notices_get_op
from axonpush._internal.api.api.audit_product import (
    audit_product_notices_update as _notices_update_op,
)
from axonpush._internal.api.api.audit_product import audit_product_obligations as _obligations_op
from axonpush._internal.api.api.audit_product import (
    audit_product_oversight_tasks as _oversight_tasks_op,
)
from axonpush._internal.api.api.audit_product import audit_product_overview as _overview_op
from axonpush._internal.api.api.audit_product import audit_product_packs_list as _packs_list_op
from axonpush._internal.api.api.audit_product import audit_product_packs_create as _packs_create_op
from axonpush._internal.api.api.audit_product import audit_product_packs_get as _packs_get_op
from axonpush._internal.api.api.audit_product import audit_product_packs_update as _packs_update_op
from axonpush._internal.api.api.audit_product import audit_product_packs_build as _packs_build_op
from axonpush._internal.api.api.audit_product import (
    audit_product_packs_download as _packs_download_op,
)
from axonpush._internal.api.api.audit_product import audit_product_people_list as _people_list_op
from axonpush._internal.api.api.audit_product import (
    audit_product_people_create as _people_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_people_observed as _people_observed_op,
)
from axonpush._internal.api.api.audit_product import audit_product_people_get as _people_get_op
from axonpush._internal.api.api.audit_product import (
    audit_product_people_update as _people_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_providers_list as _providers_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_providers_create as _providers_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_providers_get as _providers_get_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_providers_update as _providers_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_requests_list as _requests_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_requests_create as _requests_create_op,
)
from axonpush._internal.api.api.audit_product import audit_product_requests_get as _requests_get_op
from axonpush._internal.api.api.audit_product import (
    audit_product_requests_update as _requests_update_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_requests_extend as _requests_extend_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_requests_fulfill as _requests_fulfill_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_requests_send as _requests_send_op,
)
from axonpush._internal.api.api.audit_product import audit_product_share_get as _share_get_op
from axonpush._internal.api.api.audit_product import audit_product_share_nda as _share_nda_op
from axonpush._internal.api.api.audit_product import (
    audit_product_share_download as _share_download_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_training_list as _training_list_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_training_create as _training_create_op,
)
from axonpush._internal.api.api.audit_product import (
    audit_product_training_import as _training_import_op,
)
from axonpush._internal.api.api.audit_product import audit_product_training_get as _training_get_op
from axonpush._internal.api.api.audit_product import (
    audit_product_training_update as _training_update_op,
)
from axonpush._internal.api.api.audit_product import audit_product_trust_get as _trust_get_op
from axonpush._internal.api.api.audit_product import audit_product_trust_update as _trust_update_op
from axonpush._internal.api.api.audit_product import audit_product_unregistered as _unregistered_op
from axonpush._internal.api.api.audit_product import audit_product_public_trust as _public_trust_op
from axonpush._internal.api.api.audit_product import (
    audit_product_public_request as _public_request_op,
)


class AuditProduct:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def access_log(self, params: Mapping[str, Any] | None = None) -> AccessLogOutputBody | None:
        """Read scoped auditor access records."""
        return self._client._invoke(
            _access_log_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def agents_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody3 | None:
        """List agents."""
        return self._client._invoke(
            _agents_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def agents_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create agents resource."""
        return self._client._invoke(_agents_create_op, body=body)

    def agents_get(self, id: str) -> ComplianceRecord | None:
        """Read agents resource."""
        return self._client._invoke(_agents_get_op, id=id)

    def agents_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update agents resource with optimistic version."""
        return self._client._invoke(_agents_update_op, id=id, body=body)

    def agents_changes(
        self, id: str, params: Mapping[str, Any] | None = None
    ) -> ChangesOutputBody | None:
        """Read agent revision history."""
        return self._client._invoke(
            _agents_changes_op, id=id, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def agent_policy(self, id: str) -> PolicyOutputBody | None:
        """Read the declared policy for a bound agent."""
        return self._client._invoke(_agent_policy_op, id=id)

    def agent_policy_check(self, id: str, body: PolicyCheckInputBody) -> PolicyOutputBody | None:
        """Check a declared subject opt-out without putting identifiers in URLs."""
        return self._client._invoke(_agent_policy_check_op, id=id, body=body)

    def agents_resume(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply resume workflow."""
        return self._client._invoke(_agents_resume_op, id=id, body=body)

    def agents_suspend(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply suspend workflow."""
        return self._client._invoke(_agents_suspend_op, id=id, body=body)

    def assessments_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List assessments."""
        return self._client._invoke(
            _assessments_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def assessments_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create assessments resource."""
        return self._client._invoke(_assessments_create_op, body=body)

    def assessments_get(self, id: str) -> ComplianceRecord | None:
        """Read assessments resource."""
        return self._client._invoke(_assessments_get_op, id=id)

    def assessments_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update assessments resource with optimistic version."""
        return self._client._invoke(_assessments_update_op, id=id, body=body)

    def assessments_approve(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply approve workflow."""
        return self._client._invoke(_assessments_approve_op, id=id, body=body)

    def auditor_grants_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List auditor-grants."""
        return self._client._invoke(
            _auditor_grants_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def auditor_grants_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create auditor-grants resource."""
        return self._client._invoke(_auditor_grants_create_op, body=body)

    def auditor_grants_get(self, id: str) -> ComplianceRecord | None:
        """Read auditor-grants resource."""
        return self._client._invoke(_auditor_grants_get_op, id=id)

    def auditor_grants_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update auditor-grants resource with optimistic version."""
        return self._client._invoke(_auditor_grants_update_op, id=id, body=body)

    def destinations_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List destinations."""
        return self._client._invoke(
            _destinations_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def destinations_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create destinations resource."""
        return self._client._invoke(_destinations_create_op, body=body)

    def destinations_get(self, id: str) -> ComplianceRecord | None:
        """Read destinations resource."""
        return self._client._invoke(_destinations_get_op, id=id)

    def destinations_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update destinations resource with optimistic version."""
        return self._client._invoke(_destinations_update_op, id=id, body=body)

    def destinations_deliver(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply deliver workflow."""
        return self._client._invoke(_destinations_deliver_op, id=id, body=body)

    def grants_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List grants."""
        return self._client._invoke(
            _grants_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def grants_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create grants resource."""
        return self._client._invoke(_grants_create_op, body=body)

    def grants_get(self, id: str) -> ComplianceRecord | None:
        """Read grants resource."""
        return self._client._invoke(_grants_get_op, id=id)

    def grants_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update grants resource with optimistic version."""
        return self._client._invoke(_grants_update_op, id=id, body=body)

    def incidents_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List incidents."""
        return self._client._invoke(
            _incidents_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def incidents_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create incidents resource."""
        return self._client._invoke(_incidents_create_op, body=body)

    def incidents_get(self, id: str) -> ComplianceRecord | None:
        """Read incidents resource."""
        return self._client._invoke(_incidents_get_op, id=id)

    def incidents_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update incidents resource with optimistic version."""
        return self._client._invoke(_incidents_update_op, id=id, body=body)

    def incidents_file(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply file workflow."""
        return self._client._invoke(_incidents_file_op, id=id, body=body)

    def notices_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List notices."""
        return self._client._invoke(
            _notices_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def notices_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create notices resource."""
        return self._client._invoke(_notices_create_op, body=body)

    def notices_get(self, id: str) -> ComplianceRecord | None:
        """Read notices resource."""
        return self._client._invoke(_notices_get_op, id=id)

    def notices_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update notices resource with optimistic version."""
        return self._client._invoke(_notices_update_op, id=id, body=body)

    def obligations(self, params: Mapping[str, Any] | None = None) -> ObligationsOutputBody | None:
        """Evaluate recorded evidence against the versioned catalogue."""
        return self._client._invoke(
            _obligations_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def oversight_tasks(self, params: Mapping[str, Any] | None = None) -> TasksOutputBody | None:
        """Read task-scoped oversight and drift evidence."""
        return self._client._invoke(
            _oversight_tasks_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def overview(self) -> ComplianceOverview | None:
        """Read audit evidence overview."""
        return self._client._invoke(_overview_op)

    def packs_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List packs."""
        return self._client._invoke(
            _packs_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def packs_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create packs resource."""
        return self._client._invoke(_packs_create_op, body=body)

    def packs_get(self, id: str) -> ComplianceRecord | None:
        """Read packs resource."""
        return self._client._invoke(_packs_get_op, id=id)

    def packs_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update packs resource with optimistic version."""
        return self._client._invoke(_packs_update_op, id=id, body=body)

    def packs_build(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply build workflow."""
        return self._client._invoke(_packs_build_op, id=id, body=body)

    def packs_download(self, id: str, params: Mapping[str, Any] | None = None) -> Any | None:
        """Download a signed evidence pack."""
        return self._client._invoke(
            _packs_download_op, id=id, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def people_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List people."""
        return self._client._invoke(
            _people_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def people_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create people resource."""
        return self._client._invoke(_people_create_op, body=body)

    def people_observed(self) -> UnregisteredOutputBody | None:
        """List reported decision actors."""
        return self._client._invoke(_people_observed_op)

    def people_get(self, id: str) -> ComplianceRecord | None:
        """Read people resource."""
        return self._client._invoke(_people_get_op, id=id)

    def people_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update people resource with optimistic version."""
        return self._client._invoke(_people_update_op, id=id, body=body)

    def providers_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List providers."""
        return self._client._invoke(
            _providers_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def providers_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create providers resource."""
        return self._client._invoke(_providers_create_op, body=body)

    def providers_get(self, id: str) -> ComplianceRecord | None:
        """Read providers resource."""
        return self._client._invoke(_providers_get_op, id=id)

    def providers_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update providers resource with optimistic version."""
        return self._client._invoke(_providers_update_op, id=id, body=body)

    def requests_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List requests."""
        return self._client._invoke(
            _requests_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def requests_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create requests resource."""
        return self._client._invoke(_requests_create_op, body=body)

    def requests_get(self, id: str) -> ComplianceRecord | None:
        """Read requests resource."""
        return self._client._invoke(_requests_get_op, id=id)

    def requests_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update requests resource with optimistic version."""
        return self._client._invoke(_requests_update_op, id=id, body=body)

    def requests_extend(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply extend workflow."""
        return self._client._invoke(_requests_extend_op, id=id, body=body)

    def requests_fulfill(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply fulfill workflow."""
        return self._client._invoke(_requests_fulfill_op, id=id, body=body)

    def requests_send(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply send workflow."""
        return self._client._invoke(_requests_send_op, id=id, body=body)

    def share_get(self, token: str) -> ShareOutputBody | None:
        """Read expiring pack-scoped auditor access."""
        return self._client._invoke(_share_get_op, token=token)

    def share_nda(self, token: str, body: NdaInputBody) -> PublicWriteOutputBody | None:
        """Accept configured NDA terms for an auditor access link."""
        return self._client._invoke(_share_nda_op, token=token, body=body)

    def share_download(
        self, token: str, pack_id: str, params: Mapping[str, Any] | None = None
    ) -> Any | None:
        """Download a pack within live auditor scope."""
        return self._client._invoke(
            _share_download_op,
            token=token,
            pack_id=pack_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def training_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List training."""
        return self._client._invoke(
            _training_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def training_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create training resource."""
        return self._client._invoke(_training_create_op, body=body)

    def training_import(self, body: ImportInputBody) -> ImportOutputBody | None:
        """Atomically import training completion CSV."""
        return self._client._invoke(_training_import_op, body=body)

    def training_get(self, id: str) -> ComplianceRecord | None:
        """Read training resource."""
        return self._client._invoke(_training_get_op, id=id)

    def training_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update training resource with optimistic version."""
        return self._client._invoke(_training_update_op, id=id, body=body)

    def trust_get(self) -> ComplianceRecord | None:
        """Read trust-page publication settings."""
        return self._client._invoke(_trust_get_op)

    def trust_update(self, body: TrustWriteInputBody) -> ComplianceRecord | None:
        """Publish explicitly selected trust-page sections."""
        return self._client._invoke(_trust_update_op, body=body)

    def unregistered(self) -> UnregisteredOutputBody | None:
        """List observed unregistered agents."""
        return self._client._invoke(_unregistered_op)

    def public_trust(self, slug: str) -> TrustOutputBody | None:
        """Read explicitly published trust evidence."""
        return self._client._invoke(_public_trust_op, slug=slug)

    def public_request(self, slug: str, body: PublicInputBody) -> PublicWriteOutputBody | None:
        """Submit a rate-limited concern or evidence access request."""
        return self._client._invoke(_public_request_op, slug=slug, body=body)


class AsyncAuditProduct:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def access_log(
        self, params: Mapping[str, Any] | None = None
    ) -> AccessLogOutputBody | None:
        """Read scoped auditor access records."""
        return await self._client._invoke(
            _access_log_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def agents_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody3 | None:
        """List agents."""
        return await self._client._invoke(
            _agents_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def agents_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create agents resource."""
        return await self._client._invoke(_agents_create_op, body=body)

    async def agents_get(self, id: str) -> ComplianceRecord | None:
        """Read agents resource."""
        return await self._client._invoke(_agents_get_op, id=id)

    async def agents_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update agents resource with optimistic version."""
        return await self._client._invoke(_agents_update_op, id=id, body=body)

    async def agents_changes(
        self, id: str, params: Mapping[str, Any] | None = None
    ) -> ChangesOutputBody | None:
        """Read agent revision history."""
        return await self._client._invoke(
            _agents_changes_op, id=id, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def agent_policy(self, id: str) -> PolicyOutputBody | None:
        """Read the declared policy for a bound agent."""
        return await self._client._invoke(_agent_policy_op, id=id)

    async def agent_policy_check(
        self, id: str, body: PolicyCheckInputBody
    ) -> PolicyOutputBody | None:
        """Check a declared subject opt-out without putting identifiers in URLs."""
        return await self._client._invoke(_agent_policy_check_op, id=id, body=body)

    async def agents_resume(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply resume workflow."""
        return await self._client._invoke(_agents_resume_op, id=id, body=body)

    async def agents_suspend(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply suspend workflow."""
        return await self._client._invoke(_agents_suspend_op, id=id, body=body)

    async def assessments_list(
        self, params: Mapping[str, Any] | None = None
    ) -> ListOutputBody | None:
        """List assessments."""
        return await self._client._invoke(
            _assessments_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def assessments_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create assessments resource."""
        return await self._client._invoke(_assessments_create_op, body=body)

    async def assessments_get(self, id: str) -> ComplianceRecord | None:
        """Read assessments resource."""
        return await self._client._invoke(_assessments_get_op, id=id)

    async def assessments_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update assessments resource with optimistic version."""
        return await self._client._invoke(_assessments_update_op, id=id, body=body)

    async def assessments_approve(
        self, id: str, body: ComplianceActionBody
    ) -> ComplianceRecord | None:
        """Apply approve workflow."""
        return await self._client._invoke(_assessments_approve_op, id=id, body=body)

    async def auditor_grants_list(
        self, params: Mapping[str, Any] | None = None
    ) -> ListOutputBody | None:
        """List auditor-grants."""
        return await self._client._invoke(
            _auditor_grants_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def auditor_grants_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create auditor-grants resource."""
        return await self._client._invoke(_auditor_grants_create_op, body=body)

    async def auditor_grants_get(self, id: str) -> ComplianceRecord | None:
        """Read auditor-grants resource."""
        return await self._client._invoke(_auditor_grants_get_op, id=id)

    async def auditor_grants_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update auditor-grants resource with optimistic version."""
        return await self._client._invoke(_auditor_grants_update_op, id=id, body=body)

    async def destinations_list(
        self, params: Mapping[str, Any] | None = None
    ) -> ListOutputBody | None:
        """List destinations."""
        return await self._client._invoke(
            _destinations_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def destinations_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create destinations resource."""
        return await self._client._invoke(_destinations_create_op, body=body)

    async def destinations_get(self, id: str) -> ComplianceRecord | None:
        """Read destinations resource."""
        return await self._client._invoke(_destinations_get_op, id=id)

    async def destinations_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update destinations resource with optimistic version."""
        return await self._client._invoke(_destinations_update_op, id=id, body=body)

    async def destinations_deliver(
        self, id: str, body: ComplianceActionBody
    ) -> ComplianceRecord | None:
        """Apply deliver workflow."""
        return await self._client._invoke(_destinations_deliver_op, id=id, body=body)

    async def grants_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List grants."""
        return await self._client._invoke(
            _grants_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def grants_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create grants resource."""
        return await self._client._invoke(_grants_create_op, body=body)

    async def grants_get(self, id: str) -> ComplianceRecord | None:
        """Read grants resource."""
        return await self._client._invoke(_grants_get_op, id=id)

    async def grants_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update grants resource with optimistic version."""
        return await self._client._invoke(_grants_update_op, id=id, body=body)

    async def incidents_list(
        self, params: Mapping[str, Any] | None = None
    ) -> ListOutputBody | None:
        """List incidents."""
        return await self._client._invoke(
            _incidents_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def incidents_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create incidents resource."""
        return await self._client._invoke(_incidents_create_op, body=body)

    async def incidents_get(self, id: str) -> ComplianceRecord | None:
        """Read incidents resource."""
        return await self._client._invoke(_incidents_get_op, id=id)

    async def incidents_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update incidents resource with optimistic version."""
        return await self._client._invoke(_incidents_update_op, id=id, body=body)

    async def incidents_file(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply file workflow."""
        return await self._client._invoke(_incidents_file_op, id=id, body=body)

    async def notices_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List notices."""
        return await self._client._invoke(
            _notices_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def notices_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create notices resource."""
        return await self._client._invoke(_notices_create_op, body=body)

    async def notices_get(self, id: str) -> ComplianceRecord | None:
        """Read notices resource."""
        return await self._client._invoke(_notices_get_op, id=id)

    async def notices_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update notices resource with optimistic version."""
        return await self._client._invoke(_notices_update_op, id=id, body=body)

    async def obligations(
        self, params: Mapping[str, Any] | None = None
    ) -> ObligationsOutputBody | None:
        """Evaluate recorded evidence against the versioned catalogue."""
        return await self._client._invoke(
            _obligations_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def oversight_tasks(
        self, params: Mapping[str, Any] | None = None
    ) -> TasksOutputBody | None:
        """Read task-scoped oversight and drift evidence."""
        return await self._client._invoke(
            _oversight_tasks_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def overview(self) -> ComplianceOverview | None:
        """Read audit evidence overview."""
        return await self._client._invoke(_overview_op)

    async def packs_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List packs."""
        return await self._client._invoke(
            _packs_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def packs_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create packs resource."""
        return await self._client._invoke(_packs_create_op, body=body)

    async def packs_get(self, id: str) -> ComplianceRecord | None:
        """Read packs resource."""
        return await self._client._invoke(_packs_get_op, id=id)

    async def packs_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update packs resource with optimistic version."""
        return await self._client._invoke(_packs_update_op, id=id, body=body)

    async def packs_build(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply build workflow."""
        return await self._client._invoke(_packs_build_op, id=id, body=body)

    async def packs_download(self, id: str, params: Mapping[str, Any] | None = None) -> Any | None:
        """Download a signed evidence pack."""
        return await self._client._invoke(
            _packs_download_op, id=id, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def people_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List people."""
        return await self._client._invoke(
            _people_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def people_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create people resource."""
        return await self._client._invoke(_people_create_op, body=body)

    async def people_observed(self) -> UnregisteredOutputBody | None:
        """List reported decision actors."""
        return await self._client._invoke(_people_observed_op)

    async def people_get(self, id: str) -> ComplianceRecord | None:
        """Read people resource."""
        return await self._client._invoke(_people_get_op, id=id)

    async def people_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update people resource with optimistic version."""
        return await self._client._invoke(_people_update_op, id=id, body=body)

    async def providers_list(
        self, params: Mapping[str, Any] | None = None
    ) -> ListOutputBody | None:
        """List providers."""
        return await self._client._invoke(
            _providers_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def providers_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create providers resource."""
        return await self._client._invoke(_providers_create_op, body=body)

    async def providers_get(self, id: str) -> ComplianceRecord | None:
        """Read providers resource."""
        return await self._client._invoke(_providers_get_op, id=id)

    async def providers_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update providers resource with optimistic version."""
        return await self._client._invoke(_providers_update_op, id=id, body=body)

    async def requests_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List requests."""
        return await self._client._invoke(
            _requests_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def requests_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create requests resource."""
        return await self._client._invoke(_requests_create_op, body=body)

    async def requests_get(self, id: str) -> ComplianceRecord | None:
        """Read requests resource."""
        return await self._client._invoke(_requests_get_op, id=id)

    async def requests_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update requests resource with optimistic version."""
        return await self._client._invoke(_requests_update_op, id=id, body=body)

    async def requests_extend(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply extend workflow."""
        return await self._client._invoke(_requests_extend_op, id=id, body=body)

    async def requests_fulfill(
        self, id: str, body: ComplianceActionBody
    ) -> ComplianceRecord | None:
        """Apply fulfill workflow."""
        return await self._client._invoke(_requests_fulfill_op, id=id, body=body)

    async def requests_send(self, id: str, body: ComplianceActionBody) -> ComplianceRecord | None:
        """Apply send workflow."""
        return await self._client._invoke(_requests_send_op, id=id, body=body)

    async def share_get(self, token: str) -> ShareOutputBody | None:
        """Read expiring pack-scoped auditor access."""
        return await self._client._invoke(_share_get_op, token=token)

    async def share_nda(self, token: str, body: NdaInputBody) -> PublicWriteOutputBody | None:
        """Accept configured NDA terms for an auditor access link."""
        return await self._client._invoke(_share_nda_op, token=token, body=body)

    async def share_download(
        self, token: str, pack_id: str, params: Mapping[str, Any] | None = None
    ) -> Any | None:
        """Download a pack within live auditor scope."""
        return await self._client._invoke(
            _share_download_op,
            token=token,
            pack_id=pack_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def training_list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody | None:
        """List training."""
        return await self._client._invoke(
            _training_list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def training_create(self, body: WriteInputBody) -> WriteOutputBody | None:
        """Create training resource."""
        return await self._client._invoke(_training_create_op, body=body)

    async def training_import(self, body: ImportInputBody) -> ImportOutputBody | None:
        """Atomically import training completion CSV."""
        return await self._client._invoke(_training_import_op, body=body)

    async def training_get(self, id: str) -> ComplianceRecord | None:
        """Read training resource."""
        return await self._client._invoke(_training_get_op, id=id)

    async def training_update(self, id: str, body: PatchInputBody) -> ComplianceRecord | None:
        """Update training resource with optimistic version."""
        return await self._client._invoke(_training_update_op, id=id, body=body)

    async def trust_get(self) -> ComplianceRecord | None:
        """Read trust-page publication settings."""
        return await self._client._invoke(_trust_get_op)

    async def trust_update(self, body: TrustWriteInputBody) -> ComplianceRecord | None:
        """Publish explicitly selected trust-page sections."""
        return await self._client._invoke(_trust_update_op, body=body)

    async def unregistered(self) -> UnregisteredOutputBody | None:
        """List observed unregistered agents."""
        return await self._client._invoke(_unregistered_op)

    async def public_trust(self, slug: str) -> TrustOutputBody | None:
        """Read explicitly published trust evidence."""
        return await self._client._invoke(_public_trust_op, slug=slug)

    async def public_request(
        self, slug: str, body: PublicInputBody
    ) -> PublicWriteOutputBody | None:
        """Submit a rate-limited concern or evidence access request."""
        return await self._client._invoke(_public_request_op, slug=slug, body=body)
