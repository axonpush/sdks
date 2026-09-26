import { describe, expect, it, vi } from "vitest";
import type { ResourceClient } from "../../resources/_client.js";
import { AlertsResource } from "../../resources/alerts.js";
import { AnalyticsResource } from "../../resources/analytics.js";
import { AppsResource } from "../../resources/apps.js";
import { CapabilitiesResource } from "../../resources/capabilities.js";
import { ChannelsResource } from "../../resources/channels.js";
import { DashboardsResource } from "../../resources/dashboards.js";
import { EnvironmentsResource } from "../../resources/environments.js";
import { ErrorsResource } from "../../resources/errors.js";
import { EventsResource } from "../../resources/events.js";
import { GovernPoliciesResource } from "../../resources/govern-policies.js";
import { ModerationResource } from "../../resources/moderation.js";
import { OrganizationsResource } from "../../resources/organizations.js";
import { SpendPoliciesResource } from "../../resources/spend-policies.js";
import { TracesResource, TracesV2Resource } from "../../resources/traces.js";
import { WebhooksResource } from "../../resources/webhooks.js";

vi.mock("../../_internal/api/sdk.gen.js", async () => {
  const real = await vi.importActual<Record<string, unknown>>("../../_internal/api/sdk.gen.js");
  const stub: Record<string, unknown> = {};
  for (const k of Object.keys(real)) stub[k] = vi.fn();
  return stub;
});

const stubClient: ResourceClient = {
  environment: undefined,
  getOrCreateTrace: () => ({ traceId: "tr_x", nextSpanId: () => "sp_x" }),
  invoke: async () => null,
};

const expectations: Array<{ name: string; instance: object; methods: string[] }> = [
  {
    name: "EventsResource",
    instance: new EventsResource(stubClient),
    methods: ["publish", "search"],
  },
  {
    name: "ChannelsResource",
    instance: new ChannelsResource(stubClient),
    methods: ["list", "get", "create", "update", "delete"],
  },
  {
    name: "AppsResource",
    instance: new AppsResource(stubClient),
    methods: ["list", "get", "create", "update", "delete"],
  },
  {
    name: "EnvironmentsResource",
    instance: new EnvironmentsResource(stubClient),
    methods: ["list", "create", "update", "delete", "promoteToDefault"],
  },
  {
    name: "WebhooksResource",
    instance: new WebhooksResource(stubClient),
    methods: ["createEndpoint", "listEndpoints", "deleteEndpoint", "deliveries"],
  },
  {
    name: "TracesResource",
    instance: new TracesResource(stubClient),
    methods: ["list", "get"],
  },
  {
    name: "AlertsResource",
    instance: new AlertsResource(stubClient),
    methods: ["list", "create", "update", "delete", "occurrences"],
  },
  {
    name: "AnalyticsResource",
    instance: new AnalyticsResource(stubClient),
    methods: ["breakdown", "timeseries", "overview", "heatmap", "diff", "ingestionStatus"],
  },
  {
    name: "ModerationResource",
    instance: new ModerationResource(stubClient),
    methods: ["listRules", "createRule", "deleteRule", "listViolations", "efficacy"],
  },
  {
    name: "DashboardsResource",
    instance: new DashboardsResource(stubClient),
    methods: ["list", "get", "create", "update", "delete"],
  },
  {
    name: "ErrorsResource",
    instance: new ErrorsResource(stubClient),
    methods: ["list", "get", "events", "triage"],
  },
  {
    name: "GovernPoliciesResource",
    instance: new GovernPoliciesResource(stubClient),
    methods: ["list", "create", "update", "delete"],
  },
  {
    name: "SpendPoliciesResource",
    instance: new SpendPoliciesResource(stubClient),
    methods: ["list", "create", "update", "delete"],
  },
  {
    name: "CapabilitiesResource",
    instance: new CapabilitiesResource(stubClient),
    methods: ["get"],
  },
  {
    name: "OrganizationsResource",
    instance: new OrganizationsResource(stubClient),
    methods: [
      "get",
      "list",
      "update",
      "delete",
      "invite",
      "cancelInvitation",
      "removeMember",
      "transferOwnership",
      "leave",
      "acceptInvitation",
    ],
  },
];

describe("resource method parity (contract §3)", () => {
  for (const { name, instance, methods } of expectations) {
    for (const m of methods) {
      it(`${name} exposes ${m}()`, () => {
        expect(typeof (instance as Record<string, unknown>)[m]).toBe("function");
      });
    }
  }

  it("TracesV2Resource is a back-compat alias for TracesResource", () => {
    expect(TracesV2Resource).toBe(TracesResource);
  });
});
