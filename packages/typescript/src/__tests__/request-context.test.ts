import { describe, expect, it, vi } from "vitest";
import { AxonPush } from "../client.js";
import { BackgroundPublisher } from "../integrations/_publisher.js";
import { currentRequestContext } from "../request-context.js";

const context = (id: string) => ({
  workspaceId: "ws",
  environment: "dev",
  subjects: { user: id, company: "acme" },
  bindings: { accepted: { attributes: { userId: "user" } } },
});
const make = () =>
  new AxonPush({
    apiKey: "synthetic",
    tenantId: "org",
    baseUrl: "http://local.test",
    environment: "dev",
    maxRetries: 0,
  });
describe("customer request context", () => {
  it("isolates concurrent flows, restores nested scopes and never crosses clients", async () => {
    const a = make(),
      b = make();
    await Promise.all(
      ["alice", "bob"].map((id) =>
        a.withContext(context(id), async (scope) => {
          await Promise.resolve();
          expect(currentRequestContext(a)?.subjects?.user).toBe(id);
          expect(currentRequestContext(b)).toBeUndefined();
          expect(() =>
            a.withContext(context("nested"), () => {
              throw Error("stop");
            }),
          ).toThrow("stop");
          expect(currentRequestContext(a)?.subjects?.user).toBe(id);
          expect(scope.capture().subjects?.user).toBe(id);
        }),
      ),
    );
    expect(currentRequestContext(a)).toBeUndefined();
  });
  it("maps only explicitly declared observation fields and links case subjects", async () => {
    const client = make();
    const invoke = vi.spyOn(client, "invoke").mockResolvedValue(null);
    await client.withContext(context("alice"), async (scope) => {
      await scope.observe({ event: "accepted", refs: { booking: "booking1" } });
      const observation = (
        invoke.mock.calls.at(-1)?.[1] as { body: { observations: Record<string, unknown>[] } }
      ).body.observations[0];
      expect(observation?.attributes).toEqual({ userId: "alice" });
      expect(observation?.refs).toEqual({ booking: "booking1" });
      await scope.facts("booking", { case_id: "b1", facts: [], coverage: [] });
      expect(
        (invoke.mock.calls.at(-1)?.[1] as { body: { input: { subjects: unknown } } }).body.input
          .subjects,
      ).toEqual({ user: "alice", company: "acme" });
      expect(() =>
        scope.facts("booking", {
          case_id: "b1",
          subjects: { user: "bob" },
          facts: [],
          coverage: [],
        }),
      ).toThrow("Conflicting subject");
      await expect(client.observe("other", { event: "accepted" })).rejects.toThrow("mismatch");
    });
  });
  it("captures customer identity before queued publication and clears the worker scope", async () => {
    const client = make();
    const invoke = vi.spyOn(client, "invoke").mockResolvedValue(null);
    const publisher = new BackgroundPublisher(client);
    await client.withContext(context("alice"), async () =>
      publisher.submit({ identifier: "accepted", channelId: "channel", payload: {} }),
    );
    await client.withContext(context("bob"), async () =>
      publisher.submit({ identifier: "accepted", channelId: "channel", payload: {} }),
    );
    await publisher.flush();
    await publisher.close();
    const users = invoke.mock.calls.map(
      (call) =>
        (call[1] as { body: { metadata: Record<string, unknown> } }).body.metadata["user.id"],
    );
    expect(users).toEqual(["alice", "bob"]);
    const traces = invoke.mock.calls.map(
      (call) => (call[1] as { body: { traceId: string } }).body.traceId,
    );
    expect(new Set(traces).size).toBe(2);
    expect(currentRequestContext(client)).toBeUndefined();
  });
  it("rejects conflicting event identity and snapshots the caller's inputs", async () => {
    const client = make();
    const invoke = vi.spyOn(client, "invoke").mockResolvedValue(null);
    const input = context("alice");
    await client.withContext(input, async (scope) => {
      input.subjects.user = "mutated";
      await scope.events.publish({ identifier: "event", channelId: "channel", payload: {} });
      expect(
        (invoke.mock.calls.at(-1)?.[1] as { body: { metadata: Record<string, unknown> } }).body
          .metadata["user.id"],
      ).toBe("alice");
      await expect(
        scope.events.publish({
          identifier: "event",
          channelId: "channel",
          payload: {},
          metadata: { "user.id": "bob" },
        }),
      ).rejects.toThrow("Conflicting");
    });
  });
});
