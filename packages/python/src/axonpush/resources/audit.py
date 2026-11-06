"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    CreateHoldInputBody,
    GovernanceInputBody,
    HoldListOutputBody,
    LedgerHold,
    LedgerJob,
    LedgerPolicy,
    LedgerPolicyUpdate,
    ListJobsOutputBody,
    ListOutputBody2,
    ProofOutputBody,
    RecoverJobInputBody,
    ReleaseHoldInputBody,
    SegmentListOutputBody,
    SegmentOutputBody,
    StatusOutputBody,
    StorageOutputBody,
    VerifyOutputBody,
    VerifyResult,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.audit_logs import audit_list as _list_op
from axonpush._internal.api.api.audit_logs import audit_verify as _verify_op
from axonpush._internal.api.api.audit import audit_holds_list as _holds_list_op
from axonpush._internal.api.api.audit import audit_holds_create as _holds_create_op
from axonpush._internal.api.api.audit import audit_holds_release as _holds_release_op
from axonpush._internal.api.api.audit import audit_jobs as _jobs_op
from axonpush._internal.api.api.audit import audit_job as _job_op
from axonpush._internal.api.api.audit import audit_governance_receipt as _governance_receipt_op
from axonpush._internal.api.api.audit import audit_job_recover as _job_recover_op
from axonpush._internal.api.api.audit import audit_job_retry as _job_retry_op
from axonpush._internal.api.api.audit import audit_proof as _proof_op
from axonpush._internal.api.api.audit import audit_reconcile as _reconcile_op
from axonpush._internal.api.api.audit import audit_retention as _retention_op
from axonpush._internal.api.api.audit import audit_retention_update as _retention_update_op
from axonpush._internal.api.api.audit import audit_segments as _segments_op
from axonpush._internal.api.api.audit import audit_segment_get as _segment_get_op
from axonpush._internal.api.api.audit import audit_content as _content_op
from axonpush._internal.api.api.audit import audit_governance_lift as _governance_lift_op
from axonpush._internal.api.api.audit import audit_restore as _restore_op
from axonpush._internal.api.api.audit import audit_segment_verify as _segment_verify_op
from axonpush._internal.api.api.audit import audit_status as _status_op
from axonpush._internal.api.api.audit import audit_storage as _storage_op
from axonpush._internal.api.api.audit import audit_evidence_verify as _evidence_verify_op


class Audit:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody2 | None:
        """List audit log entries."""
        return self._client._invoke(
            _list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def verify(self) -> VerifyResult | None:
        """Verify the tamper-evident audit hash chain."""
        return self._client._invoke(_verify_op)

    def holds_list(self) -> HoldListOutputBody | None:
        """List legal holds."""
        return self._client._invoke(_holds_list_op)

    def holds_create(self, body: CreateHoldInputBody) -> LedgerHold | None:
        """Apply a recorded legal hold."""
        return self._client._invoke(_holds_create_op, body=body)

    def holds_release(self, hold_id: str, body: ReleaseHoldInputBody) -> LedgerHold | None:
        """Release a recorded legal hold."""
        return self._client._invoke(_holds_release_op, hold_id=hold_id, body=body)

    def jobs(self, params: Mapping[str, Any] | None = None) -> ListJobsOutputBody | None:
        """List recent archive operations."""
        return self._client._invoke(
            _jobs_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def job(self, job_id: str) -> LedgerJob | None:
        """Read verification or restoration progress."""
        return self._client._invoke(_job_op, job_id=job_id)

    def governance_receipt(self, job_id: str) -> Any | None:
        """Download and revalidate the immutable timestamped governance reason."""
        return self._client._invoke(_governance_receipt_op, job_id=job_id)

    def job_recover(self, job_id: str, body: RecoverJobInputBody) -> LedgerJob | None:
        """Recover an abandoned job after stopping its old worker."""
        return self._client._invoke(_job_recover_op, job_id=job_id, body=body)

    def job_retry(self, job_id: str) -> LedgerJob | None:
        """Retry a failed archive operation."""
        return self._client._invoke(_job_retry_op, job_id=job_id)

    def proof(self, event_id: str) -> ProofOutputBody | None:
        """Download an event inclusion proof."""
        return self._client._invoke(_proof_op, event_id=event_id)

    def reconcile(self) -> LedgerJob | None:
        """Reconcile restored hot copies with permanent erasures."""
        return self._client._invoke(_reconcile_op)

    def retention(self) -> LedgerPolicy | None:
        """Read regional retention policy."""
        return self._client._invoke(_retention_op)

    def retention_update(self, body: LedgerPolicyUpdate) -> LedgerPolicy | None:
        """Update regional retention policy."""
        return self._client._invoke(_retention_update_op, body=body)

    def segments(self, params: Mapping[str, Any] | None = None) -> SegmentListOutputBody | None:
        """List sealed archive parts."""
        return self._client._invoke(
            _segments_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def segment_get(self, segment_id: str) -> SegmentOutputBody | None:
        """Read a sealed manifest."""
        return self._client._invoke(_segment_get_op, segment_id=segment_id)

    def content(self, segment_id: str, event_id: str) -> Any | None:
        """Read restored authorized content."""
        return self._client._invoke(_content_op, segment_id=segment_id, event_id=event_id)

    def governance_lift(self, segment_id: str, body: GovernanceInputBody) -> LedgerJob | None:
        """Request separately authorized governance retention shortening with an immutable reason."""
        return self._client._invoke(_governance_lift_op, segment_id=segment_id, body=body)

    def restore(self, segment_id: str) -> LedgerJob | None:
        """Request cold archive restoration."""
        return self._client._invoke(_restore_op, segment_id=segment_id)

    def segment_verify(self, segment_id: str) -> VerifyOutputBody | None:
        """Verify immutable archive bytes."""
        return self._client._invoke(_segment_verify_op, segment_id=segment_id)

    def status(self) -> StatusOutputBody | None:
        """Read archive integrity and storage status."""
        return self._client._invoke(_status_op)

    def storage(self, params: Mapping[str, Any] | None = None) -> StorageOutputBody | None:
        """Read bounded projected storage tiers and configured price estimates."""
        return self._client._invoke(
            _storage_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    def evidence_verify(self) -> LedgerJob | None:
        """Start bounded seal-chain verification."""
        return self._client._invoke(_evidence_verify_op)


class AsyncAudit:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self, params: Mapping[str, Any] | None = None) -> ListOutputBody2 | None:
        """List audit log entries."""
        return await self._client._invoke(
            _list_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def verify(self) -> VerifyResult | None:
        """Verify the tamper-evident audit hash chain."""
        return await self._client._invoke(_verify_op)

    async def holds_list(self) -> HoldListOutputBody | None:
        """List legal holds."""
        return await self._client._invoke(_holds_list_op)

    async def holds_create(self, body: CreateHoldInputBody) -> LedgerHold | None:
        """Apply a recorded legal hold."""
        return await self._client._invoke(_holds_create_op, body=body)

    async def holds_release(self, hold_id: str, body: ReleaseHoldInputBody) -> LedgerHold | None:
        """Release a recorded legal hold."""
        return await self._client._invoke(_holds_release_op, hold_id=hold_id, body=body)

    async def jobs(self, params: Mapping[str, Any] | None = None) -> ListJobsOutputBody | None:
        """List recent archive operations."""
        return await self._client._invoke(
            _jobs_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def job(self, job_id: str) -> LedgerJob | None:
        """Read verification or restoration progress."""
        return await self._client._invoke(_job_op, job_id=job_id)

    async def governance_receipt(self, job_id: str) -> Any | None:
        """Download and revalidate the immutable timestamped governance reason."""
        return await self._client._invoke(_governance_receipt_op, job_id=job_id)

    async def job_recover(self, job_id: str, body: RecoverJobInputBody) -> LedgerJob | None:
        """Recover an abandoned job after stopping its old worker."""
        return await self._client._invoke(_job_recover_op, job_id=job_id, body=body)

    async def job_retry(self, job_id: str) -> LedgerJob | None:
        """Retry a failed archive operation."""
        return await self._client._invoke(_job_retry_op, job_id=job_id)

    async def proof(self, event_id: str) -> ProofOutputBody | None:
        """Download an event inclusion proof."""
        return await self._client._invoke(_proof_op, event_id=event_id)

    async def reconcile(self) -> LedgerJob | None:
        """Reconcile restored hot copies with permanent erasures."""
        return await self._client._invoke(_reconcile_op)

    async def retention(self) -> LedgerPolicy | None:
        """Read regional retention policy."""
        return await self._client._invoke(_retention_op)

    async def retention_update(self, body: LedgerPolicyUpdate) -> LedgerPolicy | None:
        """Update regional retention policy."""
        return await self._client._invoke(_retention_update_op, body=body)

    async def segments(
        self, params: Mapping[str, Any] | None = None
    ) -> SegmentListOutputBody | None:
        """List sealed archive parts."""
        return await self._client._invoke(
            _segments_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def segment_get(self, segment_id: str) -> SegmentOutputBody | None:
        """Read a sealed manifest."""
        return await self._client._invoke(_segment_get_op, segment_id=segment_id)

    async def content(self, segment_id: str, event_id: str) -> Any | None:
        """Read restored authorized content."""
        return await self._client._invoke(_content_op, segment_id=segment_id, event_id=event_id)

    async def governance_lift(self, segment_id: str, body: GovernanceInputBody) -> LedgerJob | None:
        """Request separately authorized governance retention shortening with an immutable reason."""
        return await self._client._invoke(_governance_lift_op, segment_id=segment_id, body=body)

    async def restore(self, segment_id: str) -> LedgerJob | None:
        """Request cold archive restoration."""
        return await self._client._invoke(_restore_op, segment_id=segment_id)

    async def segment_verify(self, segment_id: str) -> VerifyOutputBody | None:
        """Verify immutable archive bytes."""
        return await self._client._invoke(_segment_verify_op, segment_id=segment_id)

    async def status(self) -> StatusOutputBody | None:
        """Read archive integrity and storage status."""
        return await self._client._invoke(_status_op)

    async def storage(self, params: Mapping[str, Any] | None = None) -> StorageOutputBody | None:
        """Read bounded projected storage tiers and configured price estimates."""
        return await self._client._invoke(
            _storage_op, **{k: v for k, v in (params or {}).items() if v is not None}
        )

    async def evidence_verify(self) -> LedgerJob | None:
        """Start bounded seal-chain verification."""
        return await self._client._invoke(_evidence_verify_op)
