import { beforeEach, describe, expect, it, vi } from "vitest";
import * as ops from "../../_internal/api/sdk.gen.js";
import type { ResourceClient } from "../../resources/_client.js";
import { AlertsResource } from "../../resources/alerts.js";
import { AnalyticsResource } from "../../resources/analytics.js";
import { DashboardsResource } from "../../resources/dashboards.js";
import { ErrorsResource } from "../../resources/errors.js";
import { GovernPoliciesResource } from "../../resources/govern-policies.js";
import { ModerationResource } from "../../resources/moderation.js";
import { OrganizationsResource } from "../../resources/organizations.js";
import { SpendPoliciesResource } from "../../resources/spend-policies.js";

vi.mock("../../_internal/api/sdk.gen.js", async () => {
  const real = await vi.importActual<Record<string, unknown>>("../../_internal/api/sdk.gen.js");
  const stub: Record<string, unknown> = {};
  for (const k of Object.keys(real)) stub[k] = vi.fn();
  return stub;
});

interface InvokeCall {
  op: unknown;
  args: unknown;
}

function makeClient(resultByOp: Map<unknown, unknown> = new Map()): {
  client: ResourceClient;
  calls: InvokeCall[];
} {
  const calls: InvokeCall[] = [];
  const client: ResourceClient = {
    environment: undefined,
    getOrCreateTrace: vi.fn(),
    invoke: vi.fn().mockImplementation(async (op, args) => {
      calls.push({ op, args });
      return resultByOp.has(op) ? resultByOp.get(op) : null;
    }),
  };
  return { client, calls };
}

beforeEach(() => {
  vi.clearAllMocks();
});

describe("DashboardsResource", () => {
  it("list() unwraps the dashboards envelope", async () => {
    const { client, calls } = makeClient(
      new Map([[ops.dashboardsList, { dashboards: [{ id: "d" }] }]]),
    );
    const res = await new DashboardsResource(client).list();
    expect(calls[0]?.op).toBe(ops.dashboardsList);
    expect(calls[0]?.args).toEqual({});
    expect(res).toEqual([{ id: "d" }]);
  });

  it("get(id) sends dashboardId in the path", async () => {
    const { client, calls } = makeClient();
    await new DashboardsResource(client).get("d-1");
    expect(calls[0]?.op).toBe(ops.dashboardsGet);
    expect(calls[0]?.args).toEqual({ path: { dashboardId: "d-1" } });
  });

  it("create(body) forwards the body", async () => {
    const { client, calls } = makeClient();
    await new DashboardsResource(client).create({ name: "ops" } as never);
    expect(calls[0]?.op).toBe(ops.dashboardsCreate);
    expect(calls[0]?.args).toEqual({ body: { name: "ops" } });
  });

  it("update(id, body) sends a path + body", async () => {
    const { client, calls } = makeClient();
    await new DashboardsResource(client).update("d-1", { name: "renamed" } as never);
    expect(calls[0]?.op).toBe(ops.dashboardsUpdate);
    expect(calls[0]?.args).toEqual({ path: { dashboardId: "d-1" }, body: { name: "renamed" } });
  });

  it("delete(id) sends only a path arg", async () => {
    const { client, calls } = makeClient();
    await new DashboardsResource(client).delete("d-1");
    expect(calls[0]?.op).toBe(ops.dashboardsDelete);
    expect(calls[0]?.args).toEqual({ path: { dashboardId: "d-1" } });
  });
});

describe("ErrorsResource", () => {
  it("list(query) unwraps the issues envelope", async () => {
    const { client, calls } = makeClient(
      new Map([[ops.errorsList, { issues: [{ fingerprint: "f" }] }]]),
    );
    const res = await new ErrorsResource(client).list({ status: "all" });
    expect(calls[0]?.op).toBe(ops.errorsList);
    expect(calls[0]?.args).toEqual({ query: { status: "all" } });
    expect(res).toEqual([{ fingerprint: "f" }]);
  });

  it("list() defaults to an empty query", async () => {
    const { client, calls } = makeClient();
    await new ErrorsResource(client).list();
    expect(calls[0]?.args).toEqual({ query: {} });
  });

  it("get(fingerprint) sends path + query", async () => {
    const { client, calls } = makeClient();
    await new ErrorsResource(client).get("fp-1");
    expect(calls[0]?.op).toBe(ops.errorsGet);
    expect(calls[0]?.args).toEqual({ path: { fingerprint: "fp-1" }, query: {} });
  });

  it("events(fingerprint) unwraps the events envelope", async () => {
    const { client, calls } = makeClient(new Map([[ops.errorsEvents, { events: [{ id: "e" }] }]]));
    const res = await new ErrorsResource(client).events("fp-1", { limit: 10 });
    expect(calls[0]?.op).toBe(ops.errorsEvents);
    expect(calls[0]?.args).toEqual({ path: { fingerprint: "fp-1" }, query: { limit: 10 } });
    expect(res).toEqual([{ id: "e" }]);
  });

  it("triage(fingerprint, body) sends path + body", async () => {
    const { client, calls } = makeClient();
    await new ErrorsResource(client).triage("fp-1", { action: "resolve" });
    expect(calls[0]?.op).toBe(ops.errorsTriage);
    expect(calls[0]?.args).toEqual({ path: { fingerprint: "fp-1" }, body: { action: "resolve" } });
  });
});

describe("GovernPoliciesResource", () => {
  it("list() unwraps the policies envelope", async () => {
    const { client, calls } = makeClient(
      new Map([[ops.governPoliciesList, { policies: [{ id: "g" }] }]]),
    );
    const res = await new GovernPoliciesResource(client).list();
    expect(calls[0]?.op).toBe(ops.governPoliciesList);
    expect(res).toEqual([{ id: "g" }]);
  });

  it("create(body) forwards the body", async () => {
    const { client, calls } = makeClient();
    await new GovernPoliciesResource(client).create({ name: "redact" } as never);
    expect(calls[0]?.op).toBe(ops.governPoliciesCreate);
    expect(calls[0]?.args).toEqual({ body: { name: "redact" } });
  });

  it("update(id, body) sends policyId + body", async () => {
    const { client, calls } = makeClient();
    await new GovernPoliciesResource(client).update("g-1", { name: "x" } as never);
    expect(calls[0]?.op).toBe(ops.governPoliciesUpdate);
    expect(calls[0]?.args).toEqual({ path: { policyId: "g-1" }, body: { name: "x" } });
  });

  it("delete(id) sends policyId", async () => {
    const { client, calls } = makeClient();
    await new GovernPoliciesResource(client).delete("g-1");
    expect(calls[0]?.op).toBe(ops.governPoliciesDelete);
    expect(calls[0]?.args).toEqual({ path: { policyId: "g-1" } });
  });
});

describe("SpendPoliciesResource", () => {
  it("list() unwraps the policies envelope", async () => {
    const { client, calls } = makeClient(
      new Map([[ops.spendPoliciesList, { policies: [{ id: "s" }] }]]),
    );
    const res = await new SpendPoliciesResource(client).list();
    expect(calls[0]?.op).toBe(ops.spendPoliciesList);
    expect(res).toEqual([{ id: "s" }]);
  });

  it("create(body) forwards the body", async () => {
    const { client, calls } = makeClient();
    await new SpendPoliciesResource(client).create({ name: "budget" } as never);
    expect(calls[0]?.op).toBe(ops.spendPoliciesCreate);
    expect(calls[0]?.args).toEqual({ body: { name: "budget" } });
  });

  it("update(id, body) sends policyId + body", async () => {
    const { client, calls } = makeClient();
    await new SpendPoliciesResource(client).update("s-1", { name: "x" } as never);
    expect(calls[0]?.op).toBe(ops.spendPoliciesUpdate);
    expect(calls[0]?.args).toEqual({ path: { policyId: "s-1" }, body: { name: "x" } });
  });

  it("delete(id) sends policyId", async () => {
    const { client, calls } = makeClient();
    await new SpendPoliciesResource(client).delete("s-1");
    expect(calls[0]?.op).toBe(ops.spendPoliciesDelete);
    expect(calls[0]?.args).toEqual({ path: { policyId: "s-1" } });
  });
});

describe("AnalyticsResource additions", () => {
  it("overview(query) invokes analyticsOverview", async () => {
    const { client, calls } = makeClient();
    await new AnalyticsResource(client).overview({ bucket: "day" });
    expect(calls[0]?.op).toBe(ops.analyticsOverview);
    expect(calls[0]?.args).toEqual({ query: { bucket: "day" } });
  });

  it("heatmap() defaults to an empty query", async () => {
    const { client, calls } = makeClient();
    await new AnalyticsResource(client).heatmap();
    expect(calls[0]?.op).toBe(ops.analyticsHeatmap);
    expect(calls[0]?.args).toEqual({ query: {} });
  });

  it("diff(body) posts the body", async () => {
    const { client, calls } = makeClient();
    await new AnalyticsResource(client).diff({ baseline: {}, selection: {} } as never);
    expect(calls[0]?.op).toBe(ops.analyticsDiff);
    expect(calls[0]?.args).toEqual({ body: { baseline: {}, selection: {} } });
  });

  it("ingestionStatus(query) invokes analyticsIngestionStatus", async () => {
    const { client, calls } = makeClient();
    await new AnalyticsResource(client).ingestionStatus({ environment: "prod" });
    expect(calls[0]?.op).toBe(ops.analyticsIngestionStatus);
    expect(calls[0]?.args).toEqual({ query: { environment: "prod" } });
  });
});

describe("AlertsResource.occurrences", () => {
  it("unwraps the data envelope", async () => {
    const { client, calls } = makeClient(
      new Map([[ops.alertsOccurrences, { data: [{ id: "o" }] }]]),
    );
    const res = await new AlertsResource(client).occurrences("ar-1", { limit: 5 });
    expect(calls[0]?.op).toBe(ops.alertsOccurrences);
    expect(calls[0]?.args).toEqual({ path: { alertRuleId: "ar-1" }, query: { limit: 5 } });
    expect(res).toEqual([{ id: "o" }]);
  });
});

describe("ModerationResource.efficacy", () => {
  it("invokes moderationEfficacy", async () => {
    const { client, calls } = makeClient();
    await new ModerationResource(client).efficacy({ since: "t0" });
    expect(calls[0]?.op).toBe(ops.moderationEfficacy);
    expect(calls[0]?.args).toEqual({ query: { since: "t0" } });
  });
});

describe("OrganizationsResource additions", () => {
  it("leave(orgId) sends only a path arg", async () => {
    const { client, calls } = makeClient();
    await new OrganizationsResource(client).leave("org-1");
    expect(calls[0]?.op).toBe(ops.organizationLeave);
    expect(calls[0]?.args).toEqual({ path: { orgId: "org-1" } });
  });

  it("acceptInvitation(body) posts the code", async () => {
    const { client, calls } = makeClient();
    await new OrganizationsResource(client).acceptInvitation({ code: "abc" });
    expect(calls[0]?.op).toBe(ops.organizationInvitationsAccept);
    expect(calls[0]?.args).toEqual({ body: { code: "abc" } });
  });
});
