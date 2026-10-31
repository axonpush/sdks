import { describe, expect, it, vi } from "vitest";
import { capabilitiesGet, capabilitiesOperations } from "../../_internal/api/sdk.gen.js";
import type { ResourceClient } from "../../resources/_client.js";
import {
  CapabilitiesResource,
  type OperationCapabilities,
  operationAvailability,
} from "../../resources/capabilities.js";

const snapshot: OperationCapabilities = {
  registryRevision: "test",
  operations: [
    { operationId: "alerts.list", availability: "allowed" },
    { operationId: "alerts.create", availability: "denied" },
    { operationId: "events.get", availability: "conditional" },
  ],
};
describe("operation discovery", () => {
  it("preserves explicit decisions and treats missing or failed discovery as unknown", () => {
    expect(operationAvailability(snapshot, "alerts.list")).toBe("allowed");
    expect(operationAvailability(snapshot, "alerts.create")).toBe("denied");
    expect(operationAvailability(snapshot, "events.get")).toBe("conditional");
    expect(operationAvailability(snapshot, "missing")).toBe("unknown");
    expect(operationAvailability(null, "alerts.list")).toBe("unknown");
  });
  it("keeps deployment get() and refreshes caller operations on every call", async () => {
    const invoke = vi
      .fn()
      .mockResolvedValueOnce({ version: "test" })
      .mockResolvedValueOnce(snapshot)
      .mockResolvedValueOnce(null);
    const client: ResourceClient = { environment: undefined, getOrCreateTrace: vi.fn(), invoke };
    const resource = new CapabilitiesResource(client);
    expect(await resource.get()).toEqual({ version: "test" });
    expect(operationAvailability(await resource.operations(), "alerts.list")).toBe("allowed");
    expect(operationAvailability(await resource.operations(), "alerts.list")).toBe("unknown");
    expect(invoke).toHaveBeenNthCalledWith(1, capabilitiesGet, {});
    expect(invoke).toHaveBeenNthCalledWith(2, capabilitiesOperations, { cache: "no-store" });
    expect(invoke).toHaveBeenCalledTimes(3);
  });
});
