import { HttpResponse, http } from "msw";
import { setupServer } from "msw/node";
import { afterAll, afterEach, beforeAll, describe, expect, it } from "vitest";
import { AxonPush } from "../client.js";
import { ValidationError } from "../errors.js";
import { withTrace } from "../tracing.js";

const BASE = "http://observe.example.test";
const WS = "ws_support";
const server = setupServer();
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterAll(() => server.close());
afterEach(() => server.resetHandlers());

const client = (overrides: Partial<ConstructorParameters<typeof AxonPush>[0]> = {}) =>
  new AxonPush({
    baseUrl: BASE,
    apiKey: "ak_synthetic",
    tenantId: "synthetic-org",
    environment: "dev",
    maxRetries: 0,
    ...overrides,
  });

type Body = { observations: Record<string, unknown>[] };

const captureObservations = (bodies: Body[], report: Record<string, unknown> = {}) =>
  http.post(`${BASE}/workspaces/${WS}/observations`, async ({ request }) => {
    const body = (await request.json()) as Body;
    bodies.push(body);
    return HttpResponse.json({
      receipts: body.observations.map((o) => ({
        sourceEventId: o.source_event_id,
        status: "stored",
        receivedAt: "2026-10-03T00:00:01Z",
        projectedAt: null,
      })),
      dropped: [],
      dropCount: 0,
      ...report,
    });
  });

describe("observe", () => {
  it("builds the core envelope with defaults", async () => {
    const bodies: Body[] = [];
    server.use(captureObservations(bodies, { dropped: ["plan_tier"], dropCount: 1 }));
    const report = await client().observe(WS, {
      event: "ticket.escalated",
      refs: { ticket: "t_42", agent: "a_7" },
      attributes: { priority: "high", plan_tier: "pro" },
    });
    const sent = bodies[0]?.observations[0] ?? {};
    expect(sent.schema_version).toBe(1);
    expect(sent.event).toBe("ticket.escalated");
    expect(sent.refs).toEqual({ ticket: "t_42", agent: "a_7" });
    expect(sent.attributes).toEqual({ priority: "high", plan_tier: "pro" });
    expect(sent.environment).toBe("dev");
    expect(sent.source_event_id).toMatch(/^[0-9a-f-]{36}$/);
    expect(Number.isNaN(Date.parse(String(sent.occurred_at)))).toBe(false);
    expect(sent).not.toHaveProperty("trace_id");
    expect(report?.dropped).toEqual(["plan_tier"]);
    expect(report?.dropCount).toBe(1);
  });

  it("keeps caller-supplied identity, time and trace fields", async () => {
    const bodies: Body[] = [];
    server.use(captureObservations(bodies));
    await client().observe(WS, {
      event: "ticket.resolved",
      sourceEventId: "evt-1",
      occurredAt: new Date("2026-10-01T10:00:00Z"),
      traceId: "abc",
      spanId: "def",
      environment: "prod",
      refs: { ticket: "t_42" },
    });
    const sent = bodies[0]?.observations[0] ?? {};
    expect(sent.source_event_id).toBe("evt-1");
    expect(sent.occurred_at).toBe("2026-10-01T10:00:00.000Z");
    expect(sent.trace_id).toBe("abc");
    expect(sent.span_id).toBe("def");
    expect(sent.environment).toBe("prod");
  });

  it("attaches the bound trace context", async () => {
    const bodies: Body[] = [];
    server.use(captureObservations(bodies));
    const traceId = "0123456789abcdef0123456789abcdef";
    await withTrace(traceId, () => client().observe(WS, { event: "ticket.opened" }));
    expect(bodies[0]?.observations[0]?.trace_id).toBe(traceId);
  });

  it("redacts secret-looking attribute keys before sending", async () => {
    const bodies: Body[] = [];
    server.use(captureObservations(bodies));
    await client().observe(WS, { event: "ticket.opened", attributes: { api_key: "sk-123" } });
    expect(bodies[0]?.observations[0]?.attributes).toEqual({ api_key: "[REDACTED]" });
  });

  it("splits large arrays into batches of 100 and merges the reports", async () => {
    const bodies: Body[] = [];
    server.use(captureObservations(bodies, { dropped: ["x"], dropCount: 2 }));
    const many = Array.from({ length: 150 }, (_, i) => ({
      event: "ticket.opened",
      sourceEventId: `e${i}`,
    }));
    const report = await client().observe(WS, many);
    expect(bodies.map((b) => b.observations.length)).toEqual([100, 50]);
    expect(report?.receipts).toHaveLength(150);
    expect(report?.dropped).toEqual(["x"]);
    expect(report?.dropCount).toBe(4);
  });

  it("returns null instead of throwing on network failure when fail-open", async () => {
    server.use(http.post(`${BASE}/workspaces/${WS}/observations`, () => HttpResponse.error()));
    await expect(client().observe(WS, { event: "ticket.opened" })).resolves.toBeNull();
  });

  it("throws on network failure when fail-open is off", async () => {
    server.use(http.post(`${BASE}/workspaces/${WS}/observations`, () => HttpResponse.error()));
    await expect(
      client({ failOpen: false }).observe(WS, { event: "ticket.opened" }),
    ).rejects.toBeDefined();
  });
});

describe("identify and group", () => {
  const profile = (entity: string, id: string, traits: Record<string, unknown>) => ({
    profile: { entity, id, traits, updatedAt: "2026-10-03T00:00:00Z" },
    dropped: ["unknown_key"],
  });

  it("posts entity, id and traits, including null deletes", async () => {
    let sent: unknown;
    server.use(
      http.post(`${BASE}/workspaces/${WS}/identify`, async ({ request }) => {
        sent = await request.json();
        return HttpResponse.json(profile("agent", "a_7", { display_name: "Triage bot" }));
      }),
    );
    const result = await client().identify(WS, {
      entity: "agent",
      id: "a_7",
      traits: { display_name: "Triage bot", team: null, unknown_key: 1 },
    });
    expect(sent).toEqual({
      entity: "agent",
      id: "a_7",
      traits: { display_name: "Triage bot", team: null, unknown_key: 1 },
    });
    expect(result?.profile.traits).toEqual({ display_name: "Triage bot" });
    expect(result?.dropped).toEqual(["unknown_key"]);
  });

  it("group is identify under another name", async () => {
    let sent: unknown;
    server.use(
      http.post(`${BASE}/workspaces/${WS}/identify`, async ({ request }) => {
        sent = await request.json();
        return HttpResponse.json(profile("company", "c_1", { name: "Acme" }));
      }),
    );
    const result = await client().group(WS, {
      entity: "company",
      id: "c_1",
      traits: { name: "Acme" },
    });
    expect(sent).toEqual({ entity: "company", id: "c_1", traits: { name: "Acme" } });
    expect(result?.profile.entity).toBe("company");
  });

  it("fails open on network errors and surfaces validation errors", async () => {
    server.use(http.post(`${BASE}/workspaces/${WS}/identify`, () => HttpResponse.error()));
    await expect(
      client().identify(WS, { entity: "agent", id: "a", traits: {} }),
    ).resolves.toBeNull();
    server.use(
      http.post(`${BASE}/workspaces/${WS}/identify`, () =>
        HttpResponse.json({ title: "Unprocessable", status: 422 }, { status: 422 }),
      ),
    );
    await expect(
      client().identify(WS, { entity: "nope", id: "a", traits: {} }),
    ).rejects.toBeInstanceOf(ValidationError);
  });
});
