import { describe, expect, it } from "vitest";
import type { AxonPush } from "../../client.js";
import { evidenceTasks } from "../../evidence-context.js";
import { FrameworkTaskLifecycle } from "../../integrations/_task_lifecycle.js";
import { AxonPushCallbackHandler } from "../../integrations/langchain.js";
import { AxonPushMastraExporter } from "../../integrations/mastra.js";
import { AxonPushRunHooks } from "../../integrations/openai-agents.js";
import type { PublishParams } from "../../resources/events.js";

function fake() {
  const events: PublishParams[] = [];
  const client = {
    events: {
      async publish(value: PublishParams) {
        events.push(value);
      },
    },
  } as unknown as AxonPush;
  return { client, events };
}
const boundaries = (events: PublishParams[]) =>
  events.filter((event) => event.identifier.startsWith("agent.task."));

describe("opt-in declared root tasks", () => {
  it("keeps default legacy counts and never infers a goal from a chain name", () => {
    const { client, events } = fake();
    const callback = new AxonPushCallbackHandler({ client, channelId: "ch" });
    callback.handleChainStart({ name: "This is a name, not a declared goal" }, {}, "root");
    callback.handleChainEnd({}, "root");
    expect(events.map((event) => event.identifier)).toEqual(["chain.start", "chain.end"]);
  });
  it("isolates overlapping roots, correlates descendants and closes failures exactly once", () => {
    const { client, events } = fake();
    const callback = new AxonPushCallbackHandler({
      client,
      channelId: "ch",
      taskGoal: ({ input }) => (input as { goal?: string }).goal,
    });
    callback.handleChainStart({}, { goal: "Declared A" }, "a");
    callback.handleChainStart({}, { goal: "Declared B" }, "b");
    callback.handleChainStart({}, {}, "child-a", "a");
    callback.handleToolStart({ name: "search" }, "", "tool-a", "child-a");
    callback.handleChainError(new Error("application failure"), "b");
    callback.handleChainEnd({}, "child-a", "a");
    callback.handleChainEnd({}, "a");
    callback.handleChainEnd({}, "a");
    const lifecycle = boundaries(events);
    expect(lifecycle).toHaveLength(4);
    const a = lifecycle.find((event) => (event.payload as { goal?: string }).goal === "Declared A")!
      .metadata!["axonpush.task_id"];
    const b = lifecycle.find((event) => (event.payload as { goal?: string }).goal === "Declared B")!
      .metadata!["axonpush.task_id"];
    expect(a).not.toEqual(b);
    expect(
      events.find((event) => event.identifier === "tool.search.start")!.metadata![
        "axonpush.task_id"
      ],
    ).toBe(a);
    expect(
      lifecycle
        .filter((event) => event.identifier === "agent.task.end")
        .map((event) => [event.metadata!["axonpush.task_id"], event.payload]),
    ).toEqual([
      [b, { outcome: "failed" }],
      [a, { outcome: "succeeded" }],
    ]);
    callback.handleToolStart({ name: "after" }, "", "after", "a");
    expect(events.at(-1)!.metadata).not.toHaveProperty("axonpush.task_id");
  });
  it("skips missing/blank/failing selectors and links an explicitly declared parent scope", () => {
    for (const taskGoal of [
      " ",
      () => undefined,
      () => {
        throw new Error("selector failure");
      },
    ]) {
      const tasks = new FrameworkTaskLifecycle(taskGoal, "langchain");
      expect(tasks.start("root", undefined, {})).toBeUndefined();
      expect(tasks.finish("root", "failed")).toBeUndefined();
    }
    evidenceTasks.run({ id: "declared-parent" }, () => {
      const tasks = new FrameworkTaskLifecycle("Child intent", "langchain");
      expect(tasks.start("root", undefined, {})!.metadata).toMatchObject({
        "axonpush.parent_task_id": "declared-parent",
      });
    });
  });
  it("uses actual Mastra root boundaries, ignores child failures as root completion, and never synthesizes missing starts", async () => {
    const { client, events } = fake();
    const exporter = new AxonPushMastraExporter({
      client,
      channelId: "ch",
      taskGoal: "Resolve the support case",
    });
    const root = {
      id: "root",
      traceId: "trace",
      name: "Support",
      type: "agent_run",
      startTime: new Date(),
    };
    await exporter.onTracingEvent({ type: "span_started", exportedSpan: root } as never);
    await exporter.onTracingEvent({
      type: "span_ended",
      exportedSpan: {
        ...root,
        id: "tool",
        parentSpanId: "root",
        type: "tool_call",
        errorInfo: { message: "retryable" },
      },
    } as never);
    expect(boundaries(events)).toHaveLength(1);
    await exporter.onTracingEvent({
      type: "span_ended",
      exportedSpan: { ...root, errorInfo: { message: "failed" } },
    } as never);
    expect(boundaries(events).map((event) => event.payload)).toEqual([
      { goal: "Resolve the support case" },
      { outcome: "failed" },
    ]);
    expect(events.find((event) => event.spanId === "tool")!.metadata!["axonpush.task_id"]).toBe(
      boundaries(events)[0]!.metadata!["axonpush.task_id"],
    );
    const count = events.length;
    await exporter.onTracingEvent({
      type: "span_ended",
      exportedSpan: { ...root, id: "missing" },
    } as never);
    expect(events).toHaveLength(count + 1);
  });
  it("records the entire OpenAI runner scope rather than closing tasks on handoffs", async () => {
    const { client, events } = fake();
    const hooks = new AxonPushRunHooks({ client, channelId: "ch" });
    await expect(
      hooks.task("Resolve the declared request", async () => {
        await hooks.onAgentStart({}, { name: "triage" });
        await hooks.onHandoff({}, { name: "triage" }, { name: "expert" });
        await hooks.onAgentEnd({}, { name: "triage" }, "handoff");
        expect(boundaries(events)).toHaveLength(1);
        throw new Error("runner failure");
      }),
    ).rejects.toThrow("runner failure");
    expect(boundaries(events).map((event) => event.payload)).toEqual([
      { goal: "Resolve the declared request" },
      { outcome: "failed" },
    ]);
    expect(
      events.find((event) => event.identifier === "agent.handoff")!.metadata!["axonpush.task_id"],
    ).toBe(boundaries(events)[0]!.metadata!["axonpush.task_id"]);
    expect(evidenceTasks.getStore()).toBeUndefined();
  });
});
