import {
  dashboardsCreate,
  dashboardsDelete,
  dashboardsGet,
  dashboardsList,
  dashboardsUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  DashboardBodyWritable,
  DashboardView,
  OkOutputBody,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Dashboard definition accepted by {@link DashboardsResource.create}/`update`. */
export type DashboardInput = DashboardBodyWritable;

/** Saved analytics dashboards — layout plus widget definitions. */
export class DashboardsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List saved dashboards. `GET /dashboards` */
  async list(): Promise<DashboardView[] | null> {
    const res = await this.client.invoke(dashboardsList, {});
    return res?.dashboards ?? null;
  }

  /** Fetch one dashboard. `GET /dashboards/{dashboardId}` */
  async get(id: string): Promise<DashboardView | null> {
    return this.client.invoke(dashboardsGet, { path: { dashboardId: id } });
  }

  /** Create a dashboard. `POST /dashboards` */
  async create(body: DashboardInput): Promise<DashboardView | null> {
    return this.client.invoke(dashboardsCreate, { body });
  }

  /** Replace a dashboard. `PUT /dashboards/{dashboardId}` */
  async update(id: string, body: DashboardInput): Promise<DashboardView | null> {
    return this.client.invoke(dashboardsUpdate, { path: { dashboardId: id }, body });
  }

  /** Delete a dashboard. `DELETE /dashboards/{dashboardId}` */
  async delete(id: string): Promise<OkOutputBody | null> {
    return this.client.invoke(dashboardsDelete, { path: { dashboardId: id } });
  }
}
