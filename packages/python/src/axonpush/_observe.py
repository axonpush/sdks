"""Envelope builders behind ``observe``, ``identify`` and ``group``."""

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from datetime import datetime, timezone
from typing import Any, TypedDict

from axonpush._internal.api.models import (
    ActivityIngestReport,
    IdentifyInputBody,
    WorkspaceIngestInputBody,
)
from axonpush._tracing import current_trace

MAX_OBSERVATION_BATCH = 100


class ObserveParams(TypedDict, total=False):
    """One observation. Only ``event`` is required."""

    event: str
    refs: Mapping[str, str]
    attributes: Mapping[str, Any]
    occurred_at: str | datetime
    source_event_id: str
    trace_id: str
    span_id: str
    environment: str
    snapshot: bool
    source: Mapping[str, Any]


def _iso(value: str | datetime | None) -> str:
    if value is None:
        return datetime.now(timezone.utc).isoformat()
    if isinstance(value, datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value.isoformat()
    return value


def build_observation(
    params: Mapping[str, Any],
    *,
    environment: str | None,
    redact: Callable[[Any], Any],
) -> dict[str, Any]:
    trace = current_trace()
    trace_id = params.get("trace_id") or (trace.w3c_trace_id() if trace else None)
    env = params.get("environment") or environment
    obs: dict[str, Any] = {
        "schema_version": 1,
        "source_event_id": params.get("source_event_id") or str(uuid.uuid4()),
        "event": params["event"],
        "occurred_at": _iso(params.get("occurred_at")),
        "refs": dict(params.get("refs") or {}),
        "attributes": redact(dict(params.get("attributes") or {})),
    }
    if env:
        obs["environment"] = env
    if trace_id:
        obs["trace_id"] = trace_id
    for key in ("span_id", "snapshot", "source"):
        if params.get(key) is not None:
            obs[key] = params[key]
    return obs


def observation_batches(
    observations: Mapping[str, Any] | list[Mapping[str, Any]],
    *,
    environment: str | None,
    redact: Callable[[Any], Any],
) -> list[WorkspaceIngestInputBody]:
    items = [observations] if isinstance(observations, Mapping) else list(observations)
    built = [build_observation(o, environment=environment, redact=redact) for o in items]
    return [
        WorkspaceIngestInputBody.from_dict({"observations": built[i : i + MAX_OBSERVATION_BATCH]})
        for i in range(0, len(built), MAX_OBSERVATION_BATCH)
    ]


def merge_reports(reports: list[ActivityIngestReport]) -> ActivityIngestReport | None:
    if not reports:
        return None
    if len(reports) == 1:
        return reports[0]
    receipts: list[Any] = []
    dropped: list[str] = []
    drop_count = 0
    for report in reports:
        receipts.extend(report.receipts or [])
        for key in report.dropped or []:
            if key not in dropped:
                dropped.append(key)
        count = report.drop_count
        drop_count += count if isinstance(count, int) else 0
    return ActivityIngestReport(receipts=receipts, dropped=dropped, drop_count=drop_count)


def identify_body(
    entity: str, id: str, traits: Mapping[str, Any], *, redact: Callable[[Any], Any]
) -> IdentifyInputBody:
    return IdentifyInputBody.from_dict({"entity": entity, "id": id, "traits": redact(dict(traits))})
