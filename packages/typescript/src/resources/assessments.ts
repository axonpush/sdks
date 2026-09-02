import {
  assessmentControllerCreate,
  assessmentControllerList,
  assessmentControllerRemove,
  assessmentControllerRemoveByQuery,
} from "../_internal/api/sdk.gen.js";
import type {
  AssessmentDeleteResponseDto,
  AssessmentDto,
  AssessmentListResponseDto,
  CreateAssessmentDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Human and automated judgements attached to a trace. */
export class AssessmentsResource {
  constructor(private readonly client: ResourceClient) {}

  /** Remove by query. `DELETE /v2/traces/{traceId}/assessments` */
  async removeByQuery(
    traceId: string,
    query: { assessmentId: string },
  ): Promise<AssessmentDeleteResponseDto | null> {
    return this.client.invoke(assessmentControllerRemoveByQuery, { path: { traceId }, query });
  }

  /** List them all. `GET /v2/traces/{traceId}/assessments` */
  async list(traceId: string): Promise<AssessmentListResponseDto | null> {
    return this.client.invoke(assessmentControllerList, { path: { traceId } });
  }

  /** Create one. `POST /v2/traces/{traceId}/assessments` */
  async create(traceId: string, body: CreateAssessmentDto): Promise<AssessmentDto | null> {
    return this.client.invoke(assessmentControllerCreate, { path: { traceId }, body });
  }

  /** Delete one. `DELETE /v2/traces/{traceId}/assessments/{assessmentId}` */
  async delete(traceId: string, assessmentId: string): Promise<AssessmentDeleteResponseDto | null> {
    return this.client.invoke(assessmentControllerRemove, { path: { traceId, assessmentId } });
  }
}
