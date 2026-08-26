import {
  evaluatorControllerCreate,
  evaluatorControllerCreateVersion,
  evaluatorControllerGet,
  evaluatorControllerList,
  evaluatorControllerRemove,
  evaluatorControllerVersion,
  evaluatorControllerVersions,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateEvaluatorDto,
  CreateEvaluatorVersionDto,
  EvaluatorDeleteDto,
  EvaluatorDto,
  EvaluatorListDto,
  EvaluatorVersionDto,
  EvaluatorVersionListDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Evaluators and their versions. */
export class EvaluatorsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/evaluators` */
  async list(): Promise<EvaluatorListDto | null> {
    return this.client.invoke(evaluatorControllerList, {});
  }

  /** Create one. `POST /v2/evaluators` */
  async create(body: CreateEvaluatorDto): Promise<EvaluatorDto | null> {
    return this.client.invoke(evaluatorControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/evaluators/{evaluatorId}` */
  async delete(evaluatorId: string): Promise<EvaluatorDeleteDto | null> {
    return this.client.invoke(evaluatorControllerRemove, { path: { evaluatorId } });
  }

  /** Fetch one by id. `GET /v2/evaluators/{evaluatorId}` */
  async get(evaluatorId: string): Promise<EvaluatorDto | null> {
    return this.client.invoke(evaluatorControllerGet, { path: { evaluatorId } });
  }

  /** Versions. `GET /v2/evaluators/{evaluatorId}/versions` */
  async versions(evaluatorId: string): Promise<EvaluatorVersionListDto | null> {
    return this.client.invoke(evaluatorControllerVersions, { path: { evaluatorId } });
  }

  /** Create version. `POST /v2/evaluators/{evaluatorId}/versions` */
  async createVersion(
    evaluatorId: string,
    body: CreateEvaluatorVersionDto,
  ): Promise<EvaluatorVersionDto | null> {
    return this.client.invoke(evaluatorControllerCreateVersion, { path: { evaluatorId }, body });
  }

  /** Version. `GET /v2/evaluators/{evaluatorId}/versions/{version}` */
  async version(evaluatorId: string, version: string): Promise<EvaluatorVersionDto | null> {
    return this.client.invoke(evaluatorControllerVersion, { path: { evaluatorId, version } });
  }
}
