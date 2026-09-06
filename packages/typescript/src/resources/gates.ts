import {
  gatePolicyControllerGet,
  gatePolicyControllerList,
  gatePolicyControllerRemove,
  gatePolicyControllerSave,
  gateRunControllerList,
} from "../_internal/api/sdk.gen.js";
import type {
  GatePolicyDeleteDto,
  GatePolicyDto,
  GatePolicyListDto,
  GateRunListDto,
  SaveGatePolicyDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Release-gate policies and the history of gate decisions. */
export class GatesResource {
  constructor(private readonly client: ResourceClient) {}

  /** List policies. `GET /v2/gate-policies` */
  async listPolicies(): Promise<GatePolicyListDto | null> {
    return this.client.invoke(gatePolicyControllerList, {});
  }

  /** Save policy. `POST /v2/gate-policies` */
  async savePolicy(body: SaveGatePolicyDto): Promise<GatePolicyDto | null> {
    return this.client.invoke(gatePolicyControllerSave, { body });
  }

  /** Delete policy. `DELETE /v2/gate-policies/{scopeType}/{scopeId}` */
  async deletePolicy(scopeType: string, scopeId: string): Promise<GatePolicyDeleteDto | null> {
    return this.client.invoke(gatePolicyControllerRemove, { path: { scopeType, scopeId } });
  }

  /** Get policy. `GET /v2/gate-policies/{scopeType}/{scopeId}` */
  async getPolicy(scopeType: string, scopeId: string): Promise<GatePolicyDto | null> {
    return this.client.invoke(gatePolicyControllerGet, { path: { scopeType, scopeId } });
  }

  /** List runs. `GET /v2/gate-runs` */
  async listRuns(query?: {
    cursor?: string;
    experimentId?: string;
    limit?: string;
  }): Promise<GateRunListDto | null> {
    return this.client.invoke(gateRunControllerList, { query });
  }
}
