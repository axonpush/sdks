import { errorsEvents, errorsGet, errorsList, errorsTriage } from "../_internal/api/sdk.gen.js";
import type {
  ErrorIssueDto,
  ErrorsEventsData,
  ErrorsGetData,
  ErrorsListData,
  EventDto,
  IssueDetailDto,
  IssueTriageDto,
  PatchErrorInputBodyWritable,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type ErrorsListParams = NonNullable<ErrorsListData["query"]>;
export type ErrorsGetParams = NonNullable<ErrorsGetData["query"]>;
export type ErrorsEventsParams = NonNullable<ErrorsEventsData["query"]>;

/** Triage action accepted by {@link ErrorsResource.triage}. */
export type ErrorTriageInput = PatchErrorInputBodyWritable;

/** Grouped error issues, their occurrences, and triage state. */
export class ErrorsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List error issues newest-first. `GET /errors` */
  async list(query: ErrorsListParams = {}): Promise<ErrorIssueDto[] | null> {
    const res = await this.client.invoke(errorsList, { query });
    return res?.issues ?? null;
  }

  /** Fetch one issue by fingerprint. `GET /errors/{fingerprint}` */
  async get(fingerprint: string, query: ErrorsGetParams = {}): Promise<IssueDetailDto | null> {
    return this.client.invoke(errorsGet, { path: { fingerprint }, query });
  }

  /** List occurrences of one issue. `GET /errors/{fingerprint}/events` */
  async events(fingerprint: string, query: ErrorsEventsParams = {}): Promise<EventDto[] | null> {
    const res = await this.client.invoke(errorsEvents, { path: { fingerprint }, query });
    return res?.events ?? null;
  }

  /** Apply a triage action to an issue. `PATCH /errors/{fingerprint}` */
  async triage(fingerprint: string, body: ErrorTriageInput): Promise<IssueTriageDto | null> {
    return this.client.invoke(errorsTriage, { path: { fingerprint }, body });
  }
}
