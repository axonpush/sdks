import { capabilitiesGet, capabilitiesOperations } from "../_internal/api/sdk.gen.js";
import type { CapabilitiesOutputBody, OperationCapabilities } from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type { CapabilitiesOutputBody, OperationCapabilities };
export type OperationAvailability = "allowed" | "denied" | "conditional" | "unknown";

/** Missing or failed discovery never grants access. Execution always reauthorizes. */
export function operationAvailability(
  snapshot: OperationCapabilities | null | undefined,
  operationId: string,
): OperationAvailability {
  const value = snapshot?.operations?.find(
    (operation) => operation.operationId === operationId,
  )?.availability;
  return value === "allowed" || value === "denied" || value === "conditional" ? value : "unknown";
}

/** Deployment metadata and caller-specific operation discovery. */
export class CapabilitiesResource {
  constructor(private readonly client: ResourceClient) {}

  /** Deployment capabilities (version, flags, license, scope catalogue). */
  async get(): Promise<CapabilitiesOutputBody | null> {
    return this.client.invoke(capabilitiesGet, {});
  }

  /** Fetch current caller permissions without caching. Null means unknown, never allowed. */
  async operations(): Promise<OperationCapabilities | null> {
    return this.client.invoke(capabilitiesOperations, { cache: "no-store" });
  }
}
