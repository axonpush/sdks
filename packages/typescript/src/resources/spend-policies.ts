import {
  spendPoliciesCreate,
  spendPoliciesDelete,
  spendPoliciesList,
  spendPoliciesUpdate,
} from "../_internal/api/sdk.gen.js";
import type { OkOutputBody, Policy, PolicyBodyWritable } from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Spend policy definition accepted by {@link SpendPoliciesResource.create}/`update`. */
export type SpendPolicyInput = PolicyBodyWritable;

/** Budget and rate-limit policies over spend. */
export class SpendPoliciesResource {
  constructor(private readonly client: ResourceClient) {}

  /** List spend policies. `GET /spend-policies` */
  async list(): Promise<Policy[] | null> {
    const res = await this.client.invoke(spendPoliciesList, {});
    return res?.policies ?? null;
  }

  /** Create a spend policy. `POST /spend-policies` */
  async create(body: SpendPolicyInput): Promise<Policy | null> {
    return this.client.invoke(spendPoliciesCreate, { body });
  }

  /** Update a spend policy. `PATCH /spend-policies/{policyId}` */
  async update(id: string, body: SpendPolicyInput): Promise<Policy | null> {
    return this.client.invoke(spendPoliciesUpdate, { path: { policyId: id }, body });
  }

  /** Delete a spend policy. `DELETE /spend-policies/{policyId}` */
  async delete(id: string): Promise<OkOutputBody | null> {
    return this.client.invoke(spendPoliciesDelete, { path: { policyId: id } });
  }
}
