import {
  onlineEvaluationControllerBackfill,
  onlineEvaluationControllerCreate,
  onlineEvaluationControllerGet,
  onlineEvaluationControllerList,
  onlineEvaluationControllerRemove,
  onlineEvaluationControllerRuns,
  onlineEvaluationControllerUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  BackfillOnlineRuleDto,
  CreateOnlineRuleDto,
  DeleteResultDto,
  OnlineRuleResponseDto,
  OnlineRuleRunResponseDto,
  UpdateOnlineRuleDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Rules that evaluate live traffic as it arrives. */
export class OnlineEvaluationsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/online-evaluation-rules` */
  async list(): Promise<OnlineRuleResponseDto[] | null> {
    return this.client.invoke(onlineEvaluationControllerList, {});
  }

  /** Create one. `POST /v2/online-evaluation-rules` */
  async create(body: CreateOnlineRuleDto): Promise<OnlineRuleResponseDto | null> {
    return this.client.invoke(onlineEvaluationControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/online-evaluation-rules/{ruleId}` */
  async delete(ruleId: string): Promise<DeleteResultDto | null> {
    return this.client.invoke(onlineEvaluationControllerRemove, { path: { ruleId } });
  }

  /** Fetch one by id. `GET /v2/online-evaluation-rules/{ruleId}` */
  async get(ruleId: string): Promise<OnlineRuleResponseDto | null> {
    return this.client.invoke(onlineEvaluationControllerGet, { path: { ruleId } });
  }

  /** Update one. `PATCH /v2/online-evaluation-rules/{ruleId}` */
  async update(ruleId: string, body: UpdateOnlineRuleDto): Promise<OnlineRuleResponseDto | null> {
    return this.client.invoke(onlineEvaluationControllerUpdate, { path: { ruleId }, body });
  }

  /** Backfill. `POST /v2/online-evaluation-rules/{ruleId}/backfill` */
  async backfill(
    ruleId: string,
    body: BackfillOnlineRuleDto,
  ): Promise<OnlineRuleRunResponseDto[] | null> {
    return this.client.invoke(onlineEvaluationControllerBackfill, { path: { ruleId }, body });
  }

  /** Runs. `GET /v2/online-evaluation-rules/{ruleId}/runs` */
  async runs(ruleId: string): Promise<OnlineRuleRunResponseDto[] | null> {
    return this.client.invoke(onlineEvaluationControllerRuns, { path: { ruleId } });
  }
}
