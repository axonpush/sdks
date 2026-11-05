# Evidence events, version 1

The audit-platform feature release adds passive evidence helpers. These APIs
are not available in older published packages. They use the existing publisher,
redaction, retry and fail-open behavior; no gateway is introduced.

| Language | Recorder | Task boundary |
| --- | --- | --- |
| TypeScript | `EvidenceRecorder(client.events, channelId, agentId)` | `task(goal, async taskId => ...)` |
| Python | `EvidenceRecorder(client.events, channel_id, agent_id)` | `with recorder.task(goal)` |
| Async Python | `AsyncEvidenceRecorder(client.events, channel_id, agent_id)` | `async with recorder.task(goal)` |
| .NET | `AxonPush.Evidence.EvidenceRecorder(client.Events, channelId, agentId)` | `TaskAsync(goal, async (taskId, ct) => ...)` |

Wire format uses `eventType=custom`, with the event name as `identifier` (the
server's canonical `operation_name`). This preserves existing ingest contracts.

- `agent.task.start`: payload `goal`.
- `agent.task.end`: payload `outcome` (`succeeded` or `failed`).
- `oversight.decision`: payload `decision`, `target_span_id`, `actor`, `reason`.
- `policy.denied`: payload `rule`, `tool`, `mode` (`shadow` or `enforce`), `reason`.
- `notice.shown`: payload `notice_id`, `audience`, `channel`.

Metadata includes `axonpush.evidence.version=1`, `axonpush.evidence.kind` equal
to the identifier, and `axonpush.evidence.origin=sdk_reported`. Within a task,
all ordinary events published through the SDK events resource inherit
`axonpush.task_id`; nested tasks also carry `axonpush.parent_task_id`. Context
is local to the async flow and restored on exit. Across processes or independent
OTLP exporters, callers must propagate IDs explicitly.

Goals, reasons and actors are customer content. Capture policy may omit them;
these helpers do not increase capture permissions. Metadata-only capture keeps
task linkage, not proof that explanatory content was retained. Exceptions are
not copied into task-end events. A failure recording task end cannot replace the
application's original exception.

`sdk_reported` distinguishes asserted decisions from decisions authenticated in
the dashboard. Publishing an approval does not verify a human's identity or
enforce a rule. Framework lifecycle adapters and typed audit management
resources remain separate work; this document describes only these helpers.
