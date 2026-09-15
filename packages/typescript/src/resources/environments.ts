import {
  environmentsCreate,
  environmentsDelete,
  environmentsList,
  environmentsPromote,
  environmentsUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateEnvironmentInputBodyWritable,
  OkOutputBody,
  UpdateEnvironmentInputBodyWritable,
} from "../_internal/api/types.gen.js";
import type { Environment } from "../models.js";
import type { ResourceClient } from "./_client.js";

export type EnvironmentCreateInput = CreateEnvironmentInputBodyWritable;
export type EnvironmentUpdateInput = UpdateEnvironmentInputBodyWritable;

/** Manage org-level environments (e.g. `prod`, `staging`, `dev`). */
export class EnvironmentsResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * List all environments configured for the org. `GET /environments`
   *
   * @returns Array of environments, or `null` on fail-open error.
   */
  async list(): Promise<Environment[] | null> {
    const res = await this.client.invoke(environmentsList, {});
    return res?.environments ?? null;
  }

  /**
   * Create a new environment. `POST /environments`
   *
   * @param input - Environment fields; see {@link EnvironmentCreateInput}.
   * @returns The created environment, or `null` on fail-open error.
   */
  async create(input: EnvironmentCreateInput): Promise<Environment | null> {
    return this.client.invoke(environmentsCreate, { body: input });
  }

  /**
   * Update an existing environment. `PATCH /environments/{slug}`
   *
   * @param slug - Environment slug.
   * @param input - Patch object.
   * @returns The updated environment, or `null` on fail-open error.
   */
  async update(slug: string, input: EnvironmentUpdateInput): Promise<Environment | null> {
    return this.client.invoke(environmentsUpdate, { path: { slug }, body: input });
  }

  /**
   * Delete an environment. `DELETE /environments/{slug}`
   *
   * @param slug - Environment slug.
   * @returns Server ack, or `null` on fail-open error.
   */
  async delete(slug: string): Promise<OkOutputBody | null> {
    return this.client.invoke(environmentsDelete, { path: { slug } });
  }

  /**
   * Promote an environment to be the org default. `POST /environments/{slug}/promote`
   *
   * @param slug - Environment slug.
   * @returns The promoted environment, or `null` on fail-open error.
   */
  async promoteToDefault(slug: string): Promise<Environment | null> {
    return this.client.invoke(environmentsPromote, { path: { slug } });
  }
}
