import {
  evaluationTargetControllerCreate,
  evaluationTargetControllerGet,
  evaluationTargetControllerList,
  evaluationTargetControllerRemove,
  evaluationTargetControllerUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateEvaluationTargetDto,
  EvaluationTargetDeleteDto,
  EvaluationTargetDto,
  EvaluationTargetListDto,
  UpdateEvaluationTargetDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** The systems an experiment can run against. */
export class EvaluationTargetsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/evaluation-targets` */
  async list(): Promise<EvaluationTargetListDto | null> {
    return this.client.invoke(evaluationTargetControllerList, {});
  }

  /** Create one. `POST /v2/evaluation-targets` */
  async create(body: CreateEvaluationTargetDto): Promise<EvaluationTargetDto | null> {
    return this.client.invoke(evaluationTargetControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/evaluation-targets/{targetId}` */
  async delete(targetId: string): Promise<EvaluationTargetDeleteDto | null> {
    return this.client.invoke(evaluationTargetControllerRemove, { path: { targetId } });
  }

  /** Fetch one by id. `GET /v2/evaluation-targets/{targetId}` */
  async get(targetId: string): Promise<EvaluationTargetDto | null> {
    return this.client.invoke(evaluationTargetControllerGet, { path: { targetId } });
  }

  /** Update one. `PATCH /v2/evaluation-targets/{targetId}` */
  async update(
    targetId: string,
    body: UpdateEvaluationTargetDto,
  ): Promise<EvaluationTargetDto | null> {
    return this.client.invoke(evaluationTargetControllerUpdate, { path: { targetId }, body });
  }
}
