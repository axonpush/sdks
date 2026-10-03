import { readFileSync } from "node:fs";
import { HttpResponse, http } from "msw";
import { setupServer } from "msw/node";
import { afterAll, afterEach, beforeAll, describe, expect, it } from "vitest";
import type { ActivityObservation } from "../_internal/api/types.gen.js";
import { AxonPush } from "../client.js";
import { AuthenticationError, NotFoundError } from "../errors.js";
import type { CreateAlertRuleInput } from "../resources/alerts.js";

const fixture = JSON.parse(
  readFileSync(
    new URL("../../../../contract/fixtures/activity-observation.json", import.meta.url),
    "utf8",
  ),
) as ActivityObservation;
const BASE = "http://operations.example.test";
const server = setupServer();
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterAll(() => server.close());
afterEach(() => server.resetHandlers());
const client = () =>
  new AxonPush({
    baseUrl: BASE,
    apiKey: "ak_synthetic",
    tenantId: "synthetic-org",
    environment: "dev",
    maxRetries: 0,
  });
const receipt = {
  sourceEventId: fixture.source_event_id,
  status: "stored",
  receivedAt: "2026-10-03T00:00:01Z",
  projectedAt: null,
};

describe("shared business operations contract", () => {
  it("preserves retry identity, original occurrence and stored/projected receipts", async () => {
    const bodies: unknown[] = [];
    let projected = false;
    server.use(
      http.post(`${BASE}/workspaces/synthetic-workspace/observations`, async ({ request }) => {
        bodies.push(await request.json());
        expect(request.headers.get("x-axonpush-environment")).toBe("dev");
        return HttpResponse.json({ receipts: [receipt] }, { status: 200 });
      }),
      http.get(
        `${BASE}/workspaces/synthetic-workspace/observations/${fixture.source_event_id}`,
        ({ request }) => {
          expect(new URL(request.url).searchParams.get("environment")).toBe("dev");
          return HttpResponse.json(
            projected
              ? { ...receipt, status: "projected", projectedAt: "2026-10-03T00:00:02Z" }
              : receipt,
          );
        },
      ),
    );
    const sdk = client();
    const body = { environment: "dev", observations: [fixture] };
    const first = await sdk.observations.accept("synthetic-workspace", body);
    await sdk.observations.accept("synthetic-workspace", body);
    expect(bodies).toEqual([body, body]);
    expect(first?.receipts?.[0]?.projectedAt).toBeNull();
    expect(
      (
        await sdk.observations.receipt("synthetic-workspace", fixture.source_event_id, {
          environment: "dev",
        })
      )?.status,
    ).toBe("stored");
    projected = true;
    expect(
      (
        await sdk.observations.receipt("synthetic-workspace", fixture.source_event_id, {
          environment: "dev",
        })
      )?.projectedAt,
    ).toBe("2026-10-03T00:00:02Z");
  });

  it("keeps pagination and exact scoped identity lookup on the server", async () => {
    server.use(
      http.get(`${BASE}/workspaces/synthetic-workspace/activity`, ({ request }) => {
        const query = new URL(request.url).searchParams;
        expect(query.get("agentId")).toBe("synthetic-candidate-1");
        expect(query.get("environment")).toBe("dev");
        expect(query.get("limit")).toBe("2");
        expect(query.get("cursor")).toBe("previous-agent");
        return HttpResponse.json({ entities: [], nextCursor: "next-agent" });
      }),
    );
    const result = await client().activity.entities("synthetic-workspace", {
      agentId: "synthetic-candidate-1",
      environment: "dev",
      limit: 2,
      cursor: "previous-agent",
    });
    expect(result?.nextCursor).toBe("next-agent");
  });

  it("surfaces authoring auth failures even when collection fails open", async () => {
    server.use(
      http.post(`${BASE}/workspaces/synthetic-workspace/activate`, () =>
        HttpResponse.json({ title: "Unauthorized", status: 401 }, { status: 401 }),
      ),
    );
    await expect(
      client().workspaces.activate("synthetic-workspace", { revision: "r1", generation: 1 }),
    ).rejects.toBeInstanceOf(AuthenticationError);
  });
});

it("uses the declared lifecycle alert body and scope", async () => {
  const payload = {
    name: "Synthetic open lifecycle incidents",
    metric: "lifecycle_open",
    operator: "gte",
    threshold: 1,
    destinationType: "email",
    destination: "synthetic@example.test",
    appId: "synthetic-app",
    environmentId: "synthetic-dev",
    service: "pipeline",
  } satisfies CreateAlertRuleInput;
  let sent: unknown;
  server.use(
    http.post(`${BASE}/v2/alerts`, async ({ request }) => {
      sent = await request.json();
      return HttpResponse.json({ title: "Not Found", status: 404 }, { status: 404 });
    }),
  );
  await expect(client().alerts.create(payload)).rejects.toBeInstanceOf(NotFoundError);
  expect(sent).toEqual(payload);
});
