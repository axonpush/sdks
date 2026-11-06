import { randomUUID } from "node:crypto";
import { evidenceTasks } from "./evidence-context.js";
import type { EventsResource } from "./resources/events.js";

export type OversightDecision = "approved" | "overrode" | "stopped" | "escalated";

/** Passive, customer-reported evidence. Content obeys the capture policy;
 * recording an approval does not authenticate its actor or enforce a policy. */
export class EvidenceRecorder {
  constructor(
    private readonly events: Pick<EventsResource, "publish">,
    private readonly channelId: string,
    private readonly agentId: string,
  ) {}

  async task<T>(goal: string, action: (taskId: string) => Promise<T>): Promise<T> {
    if (!goal.trim()) throw new Error("A declared task requires a goal");
    const parent = evidenceTasks.getStore();
    const task = { id: randomUUID(), ...(parent ? { parentId: parent.id } : {}) };
    return evidenceTasks.run(task, async () => {
      await this.emit("agent.task.start", { goal });
      let value: T;
      try {
        value = await action(task.id);
      } catch (error) {
        try {
          await this.emit("agent.task.end", { outcome: "failed" });
        } catch {}
        throw error;
      }
      await this.emit("agent.task.end", { outcome: "succeeded" });
      return value;
    });
  }

  decision(decision: OversightDecision, targetSpanId: string, actor: string, reason?: string) {
    return this.emit("oversight.decision", {
      decision,
      target_span_id: targetSpanId,
      actor,
      reason,
    });
  }
  denied(rule: string, tool: string, mode: "shadow" | "enforce", reason?: string) {
    return this.emit("policy.denied", { rule, tool, mode, reason });
  }
  noticeShown(noticeId: string, audience: string, channel: string) {
    return this.emit("notice.shown", { notice_id: noticeId, audience, channel });
  }

  private emit(kind: string, payload: Record<string, unknown>) {
    return this.events.publish({
      channelId: this.channelId,
      agentId: this.agentId,
      identifier: kind,
      eventType: "custom",
      payload,
      metadata: {
        "axonpush.evidence.version": 1,
        "axonpush.evidence.kind": kind,
        "axonpush.evidence.origin": "sdk_reported",
      },
    });
  }
}
