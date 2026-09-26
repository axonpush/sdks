import {
  governPoliciesCreate,
  governPoliciesDelete,
  governPoliciesList,
  governPoliciesUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  GovernPolicyBodyWritable,
  GovernPolicyView,
  OkOutputBody,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Govern policy definition accepted by {@link GovernPoliciesResource.create}/`update`. */
export type GovernPolicyInput = GovernPolicyBodyWritable;

/** Request-mutation policies applied to gateway traffic. */
export class GovernPoliciesResource {
  constructor(private readonly client: ResourceClient) {}

  /** List govern policies. `GET /govern-policies` */
  async list(): Promise<GovernPolicyView[] | null> {
    const res = await this.client.invoke(governPoliciesList, {});
    return res?.policies ?? null;
  }

  /** Create a govern policy. `POST /govern-policies` */
  async create(body: GovernPolicyInput): Promise<GovernPolicyView | null> {
    return this.client.invoke(governPoliciesCreate, { body });
  }

  /** Update a govern policy. `PATCH /govern-policies/{policyId}` */
  async update(id: string, body: GovernPolicyInput): Promise<GovernPolicyView | null> {
    return this.client.invoke(governPoliciesUpdate, { path: { policyId: id }, body });
  }

  /** Delete a govern policy. `DELETE /govern-policies/{policyId}` */
  async delete(id: string): Promise<OkOutputBody | null> {
    return this.client.invoke(governPoliciesDelete, { path: { policyId: id } });
  }
}
