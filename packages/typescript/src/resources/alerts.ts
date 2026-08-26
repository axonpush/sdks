import {
  alertControllerCreate,
  alertControllerList,
  alertControllerRemove,
  alertControllerUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  AlertDeleteDto,
  AlertRuleDto,
  AlertRuleListDto,
  CreateAlertRuleDto,
  UpdateAlertRuleDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Alert rules over metric thresholds. */
export class AlertsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/alerts` */
  async list(): Promise<AlertRuleListDto | null> {
    return this.client.invoke(alertControllerList, {});
  }

  /** Create one. `POST /v2/alerts` */
  async create(body: CreateAlertRuleDto): Promise<AlertRuleDto | null> {
    return this.client.invoke(alertControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/alerts/{alertRuleId}` */
  async delete(alertRuleId: string): Promise<AlertDeleteDto | null> {
    return this.client.invoke(alertControllerRemove, { path: { alertRuleId } });
  }

  /** Update one. `PATCH /v2/alerts/{alertRuleId}` */
  async update(alertRuleId: string, body: UpdateAlertRuleDto): Promise<AlertRuleDto | null> {
    return this.client.invoke(alertControllerUpdate, { path: { alertRuleId }, body });
  }
}
