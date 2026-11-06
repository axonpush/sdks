# Declared framework tasks

Framework integrations keep their existing event counts and behavior by default.
An agent, chain or workflow name is not a declared goal. Opt in only when your
application can state the intended root outcome; no model-generated goal is inferred.

The wire vocabulary matches `EvidenceRecorder`: `agent.task.start` carries `goal`,
then `agent.task.end` carries `outcome: succeeded|failed`. Both are `custom` events
with `axonpush.evidence.version=1`, `axonpush.evidence.kind`, SDK-reported origin,
and `axonpush.task_id`. A surrounding manual task becomes `axonpush.parent_task_id`.
Goals remain content subject to capture, retention and erasure policy. These events
are customer-reported observations, not authenticated approvals or enforcement.

## LangChain and LangGraph

Use the root chain callbacks, not individual model or tool calls. Nested chains,
LLMs and tools inherit the root task identity. Concurrent root run IDs stay separate.
A root chain error closes its own task as failed; a child error does not close the
root prematurely. Repeated terminal callbacks cannot emit a second completion.

```ts
const callbacks = new AxonPushCallbackHandler({
  client, channelId, agentId: "support-assistant",
  taskGoal: ({ metadata }) =>
    typeof metadata?.declaredGoal === "string" ? metadata.declaredGoal : undefined,
});
await chain.invoke(input, {
  callbacks: [callbacks], metadata: { declaredGoal: "Draft a reply to the verified support request" },
});
```

```python
handler = AxonPushCallbackHandler(
    client, channel_id, agent_id="support-assistant",
    task_goal=lambda context: (context.get("metadata") or {}).get("declared_goal"),
)
chain.invoke(input, config={"callbacks": [handler], "metadata": {
    "declared_goal": "Draft a reply to the verified support request",
}})
handler.flush()
handler.close()
```

The async Python handler accepts the same option; await `aflush()` / `aclose()`.
A static declared goal string is also accepted. Missing, empty or failing selectors
leave that run undeclared and do not disrupt the framework. Mappings and recent
completion deduplication are bounded at 10,000 IDs. Finished roots remove their
child mappings, so cleanup follows the completed run rather than scanning every
other active run. Long-running applications should still close their handlers.

## Mastra 1.x

The observability exporter listens to real `span_started` and `span_ended` events.
Only root agent/workflow spans with a declared goal open tasks. Internal spans,
child tool completions and externally nested traces do not become new root tasks.
The exporter does not fabricate a start when it only receives an ended span.
Root `errorInfo` determines failed completion; child errors remain observations.

```ts
new AxonPushMastraExporter({
  client, channelId,
  taskGoal: ({ metadata }) =>
    typeof metadata?.declaredGoal === "string" ? metadata.declaredGoal : undefined,
});
```

Supply the declared goal through the root span's metadata using your Mastra run
configuration. Configure observability to deliver both started and ended events.
The legacy Mastra hook bag offers `hooks.task(goal, async () => workflow.run(...))`
when its older callback surface does not expose a correlated root run ID.

## OpenAI Agents

Agent lifecycle hooks do not reliably describe completion of the whole Runner call:
handoffs and exceptions can occur outside a particular agent's successful end hook.
Wrap the complete runner with the integration's explicit task scope:

```ts
const result = await hooks.task("Resolve the verified support request", async () =>
  Runner.run(agent, input, { hooks }),
);
```

```python
async with hooks.task("Resolve the verified support request"):
    result = await Runner.run(agent, input, hooks=hooks)
await hooks.flush()
await hooks.close()
```

The scope records actual success, exception or cancellation while preserving the
application's original exception and restoring task context. Agent/tool/handoff
callbacks inside the scope retain its task ID. For streaming APIs, keep the scope
open until the stream has been fully consumed and its final result checked.
Do not wrap only stream creation, which would report completion too early.
See the [official lifecycle interface](https://openai.github.io/openai-agents-python/ref/lifecycle/).

## CrewAI

Existing step callbacks are unchanged. With a CrewAI release exposing correlated
kickoff lifecycle events, explicitly register a native event listener:

```python
stop = callbacks.listen_for_tasks(
    lambda context: (context.get("input") or {}).get("declared_goal"), crew=crew,
)
try:
    result = crew.kickoff(inputs={"declared_goal": "Investigate the submitted support case"})
finally:
    stop()
    callbacks.flush()
    callbacks.close()
```

The listener uses kickoff `event_id` and terminal `started_event_id`, matching
CrewAI's [event contracts](https://github.com/crewAIInc/crewAI/blob/main/lib/crewai/src/crewai/events/base_events.py).
It separates simultaneous executions, tolerates reordered start/end delivery,
ignores replay notifications when the event bus identifies them, and unregisters
on close. `crew=` limits collection to that Crew object. Events without correlation
IDs are left undeclared; old version names or object IDs are never guessed.
A missing kickoff start is not fabricated from its completion.

Older CrewAI versions can wrap the actual kickoff instead:

```python
with callbacks.task("Investigate the submitted support case"):
    result = crew.kickoff(inputs=inputs)
```

Do not enable native kickoff listeners and a wrapper for the same intended task:
choose the boundary that matches your integration. The wrapper propagates ambient
task identity in the calling async/thread context; unrelated worker threads need
the framework's own correlation or explicit context propagation.
