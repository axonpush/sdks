import { tracesGet, tracesList } from "../_internal/api/sdk.gen.js";
import type { GetTraceOutputBody, ListTracesOutputBody } from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Query parameters for {@link TracesResource.list}. `GET /traces` */
export interface TraceListParams {
  /** RFC3339 window start (defaults to 24h before `until`). */
  since?: string;
  /** RFC3339 window end (defaults to now). */
  until?: string;
  /** Max traces to return (default 50, max 500). */
  limit?: number;
  /** Rows to skip for paging. */
  offset?: number;
}

/**
 * List traces and fetch a single trace's spans.
 *
 * Replaces the old trace-v2 surface; `stats`, `facets`, `attribute-keys`,
 * `events` and `spans` search endpoints no longer exist in the Go contract.
 */
export class TracesResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * List traces newest-first. `GET /traces`
   *
   * @param params - Optional window & pagination.
   * @returns List envelope `{ traces }`, or `null` on fail-open error.
   */
  async list(params: TraceListParams = {}): Promise<ListTracesOutputBody | null> {
    const query = {
      ...(params.since !== undefined ? { since: params.since } : {}),
      ...(params.until !== undefined ? { until: params.until } : {}),
      ...(params.limit !== undefined ? { limit: params.limit } : {}),
      ...(params.offset !== undefined ? { offset: params.offset } : {}),
    };
    return this.client.invoke(tracesList, { query });
  }

  /**
   * Fetch a single trace with its spans. `GET /traces/{traceId}`
   *
   * @param traceId - Trace UUID.
   * @returns Trace envelope `{ traceId, spans }`, or `null` on fail-open error.
   */
  async get(traceId: string): Promise<GetTraceOutputBody | null> {
    return this.client.invoke(tracesGet, { path: { traceId } });
  }
}

/**
 * Back-compat alias for the pre-Go `client.tracesV2` accessor.
 * @deprecated Use {@link TracesResource} via `client.traces`.
 */
export const TracesV2Resource = TracesResource;
