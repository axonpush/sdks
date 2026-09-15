import { alertsCreate, alertsDelete, alertsList, alertsUpdate } from "../_internal/api/sdk.gen.js";
import type {
  AlertRuleDto,
  CreateInputBodyWritable,
  DeleteOutputBody,
  ListOutputBody,
  UpdateInputBodyWritable,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type CreateAlertRuleInput = CreateInputBodyWritable;
export type UpdateAlertRuleInput = UpdateInputBodyWritable;

/** Alert rules over metric thresholds. */
export class AlertsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/alerts` */
  async list(): Promise<ListOutputBody | null> {
    return this.client.invoke(alertsList, {});
  }

  /** Create one. `POST /v2/alerts` */
  async create(body: CreateAlertRuleInput): Promise<AlertRuleDto | null> {
    return this.client.invoke(alertsCreate, { body });
  }

  /** Delete one. `DELETE /v2/alerts/{alertRuleId}` */
  async delete(alertRuleId: string): Promise<DeleteOutputBody | null> {
    return this.client.invoke(alertsDelete, { path: { alertRuleId } });
  }

  /** Update one. `PATCH /v2/alerts/{alertRuleId}` */
  async update(alertRuleId: string, body: UpdateAlertRuleInput): Promise<AlertRuleDto | null> {
    return this.client.invoke(alertsUpdate, { path: { alertRuleId }, body });
  }
}
