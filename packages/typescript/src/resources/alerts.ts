import {
  alertsCreate,
  alertsDelete,
  alertsList,
  alertsOccurrences,
  alertsUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  AlertOccurrenceDto,
  AlertRuleDto,
  AlertsListResponse,
  AlertsOccurrencesData,
  CreateInputBodyWritable,
  DeleteOutputBody,
  UpdateInputBodyWritable,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type CreateAlertRuleInput = CreateInputBodyWritable;
export type UpdateAlertRuleInput = UpdateInputBodyWritable;
export type AlertOccurrencesParams = NonNullable<AlertsOccurrencesData["query"]>;

/** Alert rules over metric thresholds. */
export class AlertsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/alerts` */
  async list(): Promise<AlertsListResponse | null> {
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

  /** Recent firings of one rule. `GET /v2/alerts/{alertRuleId}/occurrences` */
  async occurrences(
    alertRuleId: string,
    query: AlertOccurrencesParams = {},
  ): Promise<AlertOccurrenceDto[] | null> {
    const res = await this.client.invoke(alertsOccurrences, { path: { alertRuleId }, query });
    return res?.data ?? null;
  }
}
