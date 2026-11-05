import { describe, expect, it } from "vitest";
import { EvidenceRecorder } from "../evidence.js";
import type { ResourceClient } from "../resources/_client.js";
import { EventsResource } from "../resources/events.js";

function fixture() {
  const bodies: Array<Record<string, unknown>> = [];
  const client: ResourceClient = {
    environment: undefined,
    getOrCreateTrace: () => ({ traceId: "trace", nextSpanId: () => "span" }),
    invoke: async (_op, args) => {
      bodies.push((args as { body: Record<string, unknown> }).body);
      return null;
    },
  };
  const events = new EventsResource(client);
  return { bodies, events, recorder: new EvidenceRecorder(events, "channel", "agent") };
}

describe("evidence task context", () => {
  it("propagates to normal events, nests, and restores context", async () => {
    const { bodies, events, recorder } = fixture();
    let outer = "";
    await recorder.task("Review a case", async (id) => {
      outer = id;
      await recorder.task("Check a reference", async (childId) => {
        await events.publish({ identifier: "ordinary", channelId: "channel", payload: {} });
        const body = bodies.at(-1)!;
        expect(body.metadata).toMatchObject({
          "axonpush.task_id": childId,
          "axonpush.parent_task_id": id,
        });
      });
      await recorder.noticeShown("notice", "customer", "web");
      expect(bodies.at(-1)!.metadata).toMatchObject({ "axonpush.task_id": outer });
    });
    await events.publish({ identifier: "outside", channelId: "channel", payload: {} });
    expect(bodies.at(-1)!.metadata).toBeUndefined();
  });

  it("preserves application errors and never records the exception text", async () => {
    const { bodies, recorder } = fixture();
    const failure = new Error("private application error");
    await expect(
      recorder.task("Process a case", async () => {
        throw failure;
      }),
    ).rejects.toBe(failure);
    expect(bodies.at(-1)!.payload).toEqual({ outcome: "failed" });
    expect(JSON.stringify(bodies)).not.toContain(failure.message);
  });

  it("isolates concurrent tasks", async () => {
    const { bodies, recorder } = fixture();
    const ids = await Promise.all(
      [1, 2].map((n) =>
        recorder.task(`Case ${n}`, async (id) => {
          await new Promise((resolve) => setTimeout(resolve, n));
          await recorder.denied(`rule-${n}`, "tool", "shadow");
          return id;
        }),
      ),
    );
    expect(new Set(ids).size).toBe(2);
    const denials = bodies.filter((body) => body.identifier === "policy.denied");
    expect(
      denials.map((body) => (body.metadata as Record<string, unknown>)["axonpush.task_id"]).sort(),
    ).toEqual(ids.sort());
  });
});
