# Observe business activity

Business observations describe confirmed source transitions across traces. They use a workspace installed from a versioned spec. Framework spans are supporting technical evidence. See the [shared operations contract](../../../../AGENT_OPERATIONS.md) for authoring, access and privacy.

The exporter reads an already allowlisted batch from its durable journal. This synthetic file has the same structure as `contract/fixtures/activity-observation.json`; preserve its event ID, original occurrence time and content on every retry.

```python
import json
from pathlib import Path
from axonpush import AxonPush
from axonpush._internal.api.models import WorkspaceIngestInputBody

batch = json.loads(Path("allowlisted-observation-batch.json").read_text())
body = WorkspaceIngestInputBody.from_dict(batch)
with AxonPush() as client:
    stored = client.observations.accept("workspace-id", body)
    if stored is not None:
        for receipt in stored.receipts or []:
            status = client.observations.receipt(
                "workspace-id", receipt.source_event_id,
                {"environment": body.environment},
            )
            print(status.status if status is not None else "export unavailable")
```

The input batch contains `environment` and up to 100 `observations`. A receipt with `stored` status confirms durable acceptance; `projected` plus `projected_at` confirms projection. Poll from the exporter with bounded backoff. Authorize publishing with `events:publish`; that credential may read narrow status receipts without gaining operational read access.

An operator with `observe:read` can query an exact opaque agent reference:

```python
with AxonPush() as operator:
    page = operator.activity.entities(
        "workspace-id", {"environment": "dev", "agent_id": "opaque-agent-id", "limit": 50}
    )
```

Keep `.next_cursor` when paging. Counts come from `activity.summary`, not the length of a table page. Unidentified attempts stay unlinked until the source confirms identity. Snapshots restore current state without creating historical activity.
