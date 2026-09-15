import { capabilitiesGet } from "../_internal/api/sdk.gen.js";
import type { CapabilitiesOutputBody } from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type { CapabilitiesOutputBody };

/** Server-advertised capabilities: version, feature flags, license, scopes. */
export class CapabilitiesResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * Fetch the capabilities the server exposes to the current key. `GET /capabilities`
   *
   * @returns The capabilities document, or `null` on fail-open error.
   */
  async get(): Promise<CapabilitiesOutputBody | null> {
    return this.client.invoke(capabilitiesGet, {});
  }
}
