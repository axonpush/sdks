import { appsCreate, appsDelete, appsGet, appsList, appsUpdate } from "../_internal/api/sdk.gen.js";
import type { OkOutputBody } from "../_internal/api/types.gen.js";
import type { App } from "../models.js";
import type { ResourceClient } from "./_client.js";

/** Manage apps — the top-level container for channels. */
export class AppsResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * List all apps visible to the calling org. `GET /apps`
   *
   * @returns Array of apps, or `null` on fail-open error.
   */
  async list(): Promise<App[] | null> {
    const res = await this.client.invoke(appsList, {});
    return res?.apps ?? null;
  }

  /**
   * Fetch an app by id. `GET /apps/{appId}`
   *
   * @param id - App id.
   * @returns The app, or `null` on fail-open error.
   */
  async get(id: string): Promise<App | null> {
    return this.client.invoke(appsGet, { path: { appId: id } });
  }

  /**
   * Create a new app. `POST /apps`
   *
   * @param name - Human-readable app name.
   * @returns The created app, or `null` on fail-open error.
   */
  async create(name: string): Promise<App | null> {
    return this.client.invoke(appsCreate, { body: { name } });
  }

  /**
   * Rename an app. `PATCH /apps/{appId}`
   *
   * @param id - App id.
   * @param name - New app name.
   * @returns The updated app, or `null` on fail-open error.
   */
  async update(id: string, name: string): Promise<App | null> {
    return this.client.invoke(appsUpdate, { path: { appId: id }, body: { name } });
  }

  /**
   * Delete an app. `DELETE /apps/{appId}`
   *
   * @param id - App id.
   * @returns Server ack, or `null` on fail-open error.
   */
  async delete(id: string): Promise<OkOutputBody | null> {
    return this.client.invoke(appsDelete, { path: { appId: id } });
  }
}
