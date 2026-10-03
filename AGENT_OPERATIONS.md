# Agent operations SDK contract

axonpush adapts per installation. A workspace spec declares, as data, what one application stores: a data dictionary of attributes, the entities being tracked and the events that update them, plus funnels, views and alerts. Nothing about any one business is hardcoded. The coding agent usually drafts the spec over MCP and a person reviews and activates it.

The public resources are `workspaces`, `templates`, `observations` and `activity` in Python/TypeScript, and `Workspaces`, `Templates`, `Observations` and `Activity` in .NET. Python offers synchronous and asynchronous siblings. Generated DTOs and methods come from the server's `contract/openapi.sdk.json`; never edit the generated layers to invent a capability.

## Send observations and profiles

The Python and TypeScript clients add three hand-written helpers on the client itself. Nothing is sent unless they are called.

- `observe(workspaceId, {event, refs, attributes, occurredAt?, sourceEventId?, traceId?, spanId?, environment?})` builds the core envelope `{schema_version: 1, source_event_id, event, occurred_at, environment?, refs, trace_id?, span_id?, snapshot?, source?, attributes}` and posts it to `POST /workspaces/{id}/observations` (`events:publish`). A missing `source_event_id` becomes a UUID, a missing `occurred_at` becomes now, and the bound SDK trace id is attached when there is one. TypeScript takes an array; Python has `observe_many`. Both send batches of at most 100. The response is `{receipts, dropped, dropCount}`: attribute keys the workspace has not declared are dropped and counted.
- `identify(workspaceId, {entity, id, traits})` posts to `POST /workspaces/{id}/identify` (`events:publish`) and returns `{profile, dropped}`. Traits must be keys in the entity's `profile`; they merge with what is stored and `null` deletes a key.
- `group(...)` is the same call as `identify`, named for organisation-like entities such as `company` or `team`.

All three apply the client's redaction policy and respect `failOpen`: on a connection failure they return `null`/`None` instead of throwing. Authentication and validation errors still surface.

Keep `source_event_id` stable across retries of the same fact; a reused ID with changed content is rejected. Poll `observations.receipt` to tell stored from projected.

## Author a workspace

1. Read `workspaces.describe`. It summarises the current spec in plain language and returns the format reference, the role list and the op catalogue.
2. Read the shared draft with `workspaces.draft`, then send typed edits with `workspaces.applyDraftOps` and the draft's `version`. A version mismatch returns 409 with the current draft; re-read and reapply.
3. Check `workspaces.catalog` for the events and attribute keys the app really sends, and `workspaces.draftChanges` for a plain-language change list.
4. Ask a person to review, then `workspaces.activateDraft`. Projections rebuild in the background.
5. Call `workspaces.connect` to get the application's credentials: a publish-only key bound to the workspace's app and one environment (shown once), the API URL, OTLP settings, a Sentry DSN when available, an `env` map and SDK snippets. Write `env` to a git-ignored file. A repeat call returns the existing key without its secret; `rotate: true` replaces it.

`workspaces.replaceDraft` replaces the whole draft for JSON editors; `workspaces.discardDraft` throws it away. Reflected MCP tool names replace operation ID dots with underscores, for example `workspaces_applyDraftOps`.

## Access and privacy

Ingestion and identify need `events:publish`; reads need `observe:read`; spec edits need `workspaces:manage` (or a session owner/admin); template publication needs `templates:publish`. Attributes marked `personal` are masked on read unless the caller is an owner/admin session or holds `profiles:read`.

Only declared keys are stored. Values are scanned for credentials, and non-personal text may not contain email addresses. Do not send prompts, messages, documents, credentials, full URLs or raw exception text. Client redaction is a second layer, not a replacement for a source allowlist.

`activity.deleteEntity` erases an entity, what is linked to it and its profile, and installs a replay tombstone.
