# Business operations SDK contract

AxonPush receives metadata-only source observations and builds an operational view from a versioned declarative workspace. Source applications own identities, permissions and decisions. Framework/OTLP spans supply technical evidence; lifecycle observations describe joining, committed domain transitions, concurrent operations and explicit workflow waits.

The public resources are `workspaces`, `templates`, `observations` and `activity` in Python/TypeScript, and `Workspaces`, `Templates`, `Observations` and `Activity` in .NET. Python offers synchronous and asynchronous siblings. Generated DTOs and methods come from the server's `contract/openapi.sdk.json`; never edit the generated layers to invent a capability.

## Author a workspace

1. Read `workspaces.schema` (`GET /workspaces/schema`). The same JSON Schema is used by HTTP, MCP and the dashboard editor.
2. Read `templates.list` or compose a spec from source semantics. Templates are immutable public or organization-private configuration. An installed copy belongs to the organization and pins `template: {id, version}`. Its edits do not modify the gallery; upgrades are explicit new revisions.
3. Validate the spec, preview it against clearly synthetic metadata-only observations and review a diff against the current revision.
4. Create a workspace for the authorized application, or save an immutable revision in an existing workspace.
5. Activate `{revision, generation}` using a freshly read workspace. Poll the workspace until rebuild completes and the revision is active. A generation conflict requires rereading and comparing before retrying. Rollback activates a previous revision with the current generation.

Use the deployed MCP tool catalog rather than assuming a remembered name is available. Reflected MCP names normally replace operation ID dots with underscores. Publication to a public or private gallery is a separate requested action and includes configuration only, never observations, personal data or production identifiers.

## Publish and verify observations

Ingestion accepts at most 100 typed observations per batch at `POST /workspaces/{workspaceId}/observations`, with an environment. Preserve `source_event_id`, original `occurred_at` and the exact allowlisted payload across retries. A reused ID with changed content is rejected. The receipt separates `stored` (durably accepted) from `projected` (queryable in derived activity); poll `observations.receipt` before claiming success.

Keep agent identity, initiating/delegated agent, per-action client attribution, trusted opaque correlations and source record/revision separate. Before identity is established, use an anonymous actor and an unlinked attempt. A snapshot reconstructs current state and creates no historical claim or action. Registration source differs from the current client; self-reported client names confer no authority.

Collect committed transitions through an isolated durable journal/outbox and transient starts/terminals through a bounded nonblocking buffer. Export in a separate worker with finite timeouts, retry/backoff, dead letters and independent health. Never synchronously export inside a business transaction. Semantic lifecycle events are unsampled in healthy operation; overload must expose loss rather than silently claim completeness.

Build an allowlist before buffering or logging. Do not include hidden reasoning, prompts, arguments/results, messages, CVs/documents, contacts, assessment answers, compensation terms, credentials, full URLs, headers or raw exception text. SDK/server redaction is a second layer and cannot replace a source-specific allowlist. Typed DTOs describe permitted metadata; they are not an authorization policy for arbitrary content.

## Query activity and health

`activity.entities` returns exact scoped entities and cursor pagination. `activity.timeline` preserves source evidence and occurrence/receipt/projection times. `activity.summary` returns total counts with a visible activity window; do not use a page length as a metric. `activity.analytics` exposes distinct lifecycle cohorts and unknown/unlinked attribution, and `activity.widgets` aggregates the active spec. Retain concurrent operations and threads; a terminal operation cannot clear unrelated work.

Running requires a current start within its expected runtime. Missing completion becomes overdue/unknown. Last observation time cannot prove offline or abandonment. Read `activity.health` and `activity.incidents` to distinguish exporter/backlog/projection problems from source state. Expected authentication challenges and ordinary human decisions are not automatic incidents.

Existing alert rules can notify on `metric: lifecycle_open` with `threshold >= 1`, app/environment scope and optional `service: operation | journey | pipeline` incident scope. Stateful incidents provide deduplication/recovery; notification rules retain their configured minimum sample/cooldown and email/webhook channel behavior. Alerts never take hiring actions or message candidates/companies.

## Access and retention

Service ingestion needs `events:publish`; reads need `observe:read`; workspace edits need `workspaces:manage`; template publication needs `templates:publish`. Session mutations require an organization owner/admin. Credentials remain bounded by organization, application and environment on the server. A publish-only credential can inspect its scoped acceptance/projection status receipt; it cannot read operational evidence or author configuration. Customer/company isolation requires equivalent server-side permissions across events, traces, exports and MCP; UI filtering does not provide isolation.

The current server retains diagnostic spans for seven days and identifiable operational evidence for 30 days. Live aggregate queries use the retained 30-day operational window. Source policies can be stricter. `activity.deleteAgent` removes retained evidence and derived state and installs a replay tombstone. Verify deletion across configured storage/index/export paths and replay; do not assume append-only storage means deletion is complete.

## Local release verification

Regenerate, run transport/serialization tests, compare Python/TypeScript/.NET operations surfaces and verify sensitive fixtures, deduplication, late delivery, capture-off/on/failing compatibility and scoped access. Measure source-to-view freshness and warm collection overhead at representative traffic. The proposed targets (p95 freshness <=15 seconds, p99 <=60 seconds, warm p95 collection <5 ms) are acceptance gates, not claims established by building the SDK.

Billing is dormant during the restricted pilot. This document does not authorize deployment, public template publication or expanded customer access.
