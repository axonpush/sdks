import { describe, expect, it, vi } from "vitest";

import { WorkflowRuntime } from "../workflow-worker.js";

const action = {
  id: "act_1",
  case_key: "case_1",
  case_id: "booking_1",
  handler: "calendar",
  mode: "execute",
  revision: 3,
};

describe("WorkflowRuntime", () => {
  it("settles a claimed action exactly once", async () => {
    const request = vi
      .fn<typeof fetch>()
      .mockResolvedValueOnce(Response.json({ action }))
      .mockResolvedValueOnce(Response.json({}));
    const execute = vi.fn(async () => ({ booking_id: "confirmed" }));
    const runtime = new WorkflowRuntime(
      {
        baseUrl: "https://api.example.test",
        workspace: "workspace",
        environment: "development",
        apiKey: "secret",
        handler: "calendar",
        fetch: request,
      },
      { execute, lookup: vi.fn() },
    );

    await expect(runtime.tick()).resolves.toBe(true);
    expect(execute).toHaveBeenCalledOnce();
    const receipt = JSON.parse(String(request.mock.calls[1]?.[1]?.body));
    expect(receipt).toEqual({
      result: "executed",
      output: { booking_id: "confirmed" },
      revision: 3,
    });
  });

  it("marks an uncertain execution ambiguous instead of retrying it", async () => {
    const request = vi
      .fn<typeof fetch>()
      .mockResolvedValueOnce(Response.json({ action }))
      .mockResolvedValueOnce(Response.json({}));
    const execute = vi.fn(async () => {
      throw new Error("connection disappeared after commit");
    });
    const runtime = new WorkflowRuntime(
      {
        baseUrl: "https://api.example.test",
        workspace: "workspace",
        environment: "development",
        apiKey: "secret",
        handler: "calendar",
        fetch: request,
      },
      { execute, lookup: vi.fn() },
    );

    await runtime.tick();
    expect(execute).toHaveBeenCalledOnce();
    expect(JSON.parse(String(request.mock.calls[1]?.[1]?.body))).toEqual({
      result: "ambiguous",
      revision: 3,
    });
  });

  it("treats a stale receipt as a lost lease", async () => {
    const events: string[] = [];
    const request = vi
      .fn<typeof fetch>()
      .mockResolvedValueOnce(Response.json({ action }))
      .mockResolvedValueOnce(new Response(null, { status: 409 }));
    const runtime = new WorkflowRuntime(
      {
        baseUrl: "https://api.example.test",
        workspace: "workspace",
        environment: "development",
        apiKey: "secret",
        handler: "calendar",
        fetch: request,
        onEvent: (event) => events.push(event.type),
      },
      { execute: vi.fn(async () => ({})), lookup: vi.fn() },
    );

    await expect(runtime.tick()).resolves.toBe(true);
    expect(events).toContain("lease_lost");
  });
});
