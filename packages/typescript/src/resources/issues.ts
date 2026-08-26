import {
  issueControllerAddToDataset,
  issueControllerGet,
  issueControllerList,
  issueControllerMerge,
  issueControllerOccurrences,
  issueControllerUpdate,
} from "../_internal/api/sdk.gen.js";
import type {
  AddIssueToDatasetDto,
  IssueOccurrenceResponseDto,
  IssueResponseDto,
  MergeIssueDto,
  UpdateIssueDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Clustered failures, their occurrences and triage actions. */
export class IssuesResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/issues` */
  async list(query?: { severity?: string; status?: string }): Promise<IssueResponseDto[] | null> {
    return this.client.invoke(issueControllerList, { query });
  }

  /** Fetch one by id. `GET /v2/issues/{issueId}` */
  async get(issueId: string): Promise<IssueResponseDto | null> {
    return this.client.invoke(issueControllerGet, { path: { issueId } });
  }

  /** Update one. `PATCH /v2/issues/{issueId}` */
  async update(issueId: string, body: UpdateIssueDto): Promise<IssueResponseDto | null> {
    return this.client.invoke(issueControllerUpdate, { path: { issueId }, body });
  }

  /** Add to dataset. `POST /v2/issues/{issueId}/actions/add-to-dataset` */
  async addToDataset(
    issueId: string,
    body: AddIssueToDatasetDto,
  ): Promise<IssueResponseDto | null> {
    return this.client.invoke(issueControllerAddToDataset, { path: { issueId }, body });
  }

  /** Merge. `POST /v2/issues/{issueId}/merge` */
  async merge(issueId: string, body: MergeIssueDto): Promise<IssueResponseDto | null> {
    return this.client.invoke(issueControllerMerge, { path: { issueId }, body });
  }

  /** Occurrences. `GET /v2/issues/{issueId}/occurrences` */
  async occurrences(issueId: string): Promise<IssueOccurrenceResponseDto[] | null> {
    return this.client.invoke(issueControllerOccurrences, { path: { issueId } });
  }
}
