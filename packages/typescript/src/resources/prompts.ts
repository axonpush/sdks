import {
  promptControllerCompare,
  promptControllerCreate,
  promptControllerCreateVersion,
  promptControllerDeployments,
  promptControllerGet,
  promptControllerList,
  promptControllerPromote,
  promptControllerRemove,
  promptControllerRollback,
  promptControllerUpdate,
  promptControllerVersion,
  promptControllerVersions,
} from "../_internal/api/sdk.gen.js";
import type {
  CreatePromptDto,
  CreatePromptVersionDto,
  PromotePromptDto,
  PromptComparisonDto,
  PromptDeleteDto,
  PromptDeploymentDto,
  PromptDeploymentListDto,
  PromptDto,
  PromptListDto,
  PromptVersionDto,
  PromptVersionListDto,
  RollbackPromptDto,
  UpdatePromptDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Prompt registry: versions, deployments, promotion and rollback. */
export class PromptsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/prompts` */
  async list(): Promise<PromptListDto | null> {
    return this.client.invoke(promptControllerList, {});
  }

  /** Create one. `POST /v2/prompts` */
  async create(body: CreatePromptDto): Promise<PromptDto | null> {
    return this.client.invoke(promptControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/prompts/{promptId}` */
  async delete(promptId: string): Promise<PromptDeleteDto | null> {
    return this.client.invoke(promptControllerRemove, { path: { promptId } });
  }

  /** Fetch one by id. `GET /v2/prompts/{promptId}` */
  async get(promptId: string): Promise<PromptDto | null> {
    return this.client.invoke(promptControllerGet, { path: { promptId } });
  }

  /** Update one. `PATCH /v2/prompts/{promptId}` */
  async update(promptId: string, body: UpdatePromptDto): Promise<PromptDto | null> {
    return this.client.invoke(promptControllerUpdate, { path: { promptId }, body });
  }

  /** Compare. `GET /v2/prompts/{promptId}/compare` */
  async compare(
    promptId: string,
    query: { baseline: string; candidate: string },
  ): Promise<PromptComparisonDto | null> {
    return this.client.invoke(promptControllerCompare, { path: { promptId }, query });
  }

  /** Deployments. `GET /v2/prompts/{promptId}/deployments` */
  async deployments(promptId: string): Promise<PromptDeploymentListDto | null> {
    return this.client.invoke(promptControllerDeployments, { path: { promptId } });
  }

  /** Promote. `POST /v2/prompts/{promptId}/promote` */
  async promote(promptId: string, body: PromotePromptDto): Promise<PromptDeploymentDto | null> {
    return this.client.invoke(promptControllerPromote, { path: { promptId }, body });
  }

  /** Rollback. `POST /v2/prompts/{promptId}/rollback` */
  async rollback(promptId: string, body: RollbackPromptDto): Promise<PromptDeploymentDto | null> {
    return this.client.invoke(promptControllerRollback, { path: { promptId }, body });
  }

  /** Versions. `GET /v2/prompts/{promptId}/versions` */
  async versions(promptId: string): Promise<PromptVersionListDto | null> {
    return this.client.invoke(promptControllerVersions, { path: { promptId } });
  }

  /** Create version. `POST /v2/prompts/{promptId}/versions` */
  async createVersion(
    promptId: string,
    body: CreatePromptVersionDto,
  ): Promise<PromptVersionDto | null> {
    return this.client.invoke(promptControllerCreateVersion, { path: { promptId }, body });
  }

  /** Version. `GET /v2/prompts/{promptId}/versions/{version}` */
  async version(promptId: string, version: string): Promise<PromptVersionDto | null> {
    return this.client.invoke(promptControllerVersion, { path: { promptId, version } });
  }
}
