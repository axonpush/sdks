import {
  tracesGet,
  tracesGroupMembers,
  tracesGroups,
  tracesList,
} from "../_internal/api/sdk.gen.js";
import type {
  GetTraceOutputBody,
  ListTracesOutputBody,
  TraceGroupMembersOutputBody,
  TraceGroupsBody,
  TracesGetData,
  TracesGroupMembersData,
  TracesGroupsData,
  TracesListData,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/**
 * Query parameters for {@link TracesResource.list}. `GET /traces`
 *
 * Every filter the endpoint accepts: window and paging (`since`, `until`,
 * `limit`, `offset`), free text (`q`), facet filters (`service`,
 * `operation`, `model`, `agent`, `tool`, ...), `errorsOnly`,
 * `minDurationMs` and `sort`.
 */
export type TraceListParams = NonNullable<TracesListData["query"]>;

/**
 * List traces and fetch a single trace's spans.
 *
 * Replaces the old trace-v2 surface; `stats`, `facets`, `attribute-keys`,
 * `events` and `spans` search endpoints no longer exist in the Go contract.
 */
export class TracesResource {
  constructor(private readonly client: ResourceClient) {}

  async groups(query: TracesGroupsData["query"] = {}): Promise<TraceGroupsBody | null> {
    return this.client.invoke(tracesGroups, { query });
  }

  async groupMembers(
    groupKey: string,
    query: TracesGroupMembersData["query"] = {},
  ): Promise<TraceGroupMembersOutputBody | null> {
    return this.client.invoke(tracesGroupMembers, { path: { groupKey }, query });
  }

  /**
   * List traces newest-first. `GET /traces`
   *
   * @param params - Optional window, pagination and filters.
   * @returns List envelope `{ traces }`, or `null` on fail-open error.
   */
  async list(params: TraceListParams = {}): Promise<ListTracesOutputBody | null> {
    const query = Object.fromEntries(
      Object.entries(params).filter(([, value]) => value !== undefined),
    ) as TraceListParams;
    return this.client.invoke(tracesList, { query });
  }

  /**
   * Fetch one bounded page of a trace's spans. `GET /traces/{traceId}`
   *
   * @param traceId - Trace UUID.
   * @returns Trace envelope `{ traceId, spans }`, or `null` on fail-open error.
   */
  async get(
    traceId: string,
    query: TracesGetData["query"] = {},
  ): Promise<GetTraceOutputBody | null> {
    return this.client.invoke(tracesGet, { path: { traceId }, query });
  }
}

/**
 * Back-compat alias for the pre-Go `client.tracesV2` accessor.
 * @deprecated Use {@link TracesResource} via `client.traces`.
 */
export const TracesV2Resource = TracesResource;
