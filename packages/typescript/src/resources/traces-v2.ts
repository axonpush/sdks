import {
  traceV2ControllerAttributeKeys,
  traceV2ControllerDetail,
  traceV2ControllerEvents,
  traceV2ControllerFacets,
  traceV2ControllerList,
  traceV2ControllerSpans,
  traceV2ControllerStats,
} from "../_internal/api/sdk.gen.js";
import type {
  TraceAttributeKeysV2ResponseDto,
  TraceDetailV2ResponseDto,
  TraceEventsV2ResponseDto,
  TraceFacetsV2ResponseDto,
  TraceListV2ResponseDto,
  TraceSpanSearchV2ResponseDto,
  TraceV2ControllerStatsResponse,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Aggregated dashboard stats returned by {@link TracesV2Resource.stats}. */
export type DashboardStatsV2 = NonNullable<TraceV2ControllerStatsResponse>;

/** Trace search with facets, spans and attribute keys. */
export class TracesV2Resource {
  constructor(private readonly client: ResourceClient) {}

  /** Aggregated dashboard stats. `GET /v2/traces/stats` */
  async stats(query?: { appId?: string; environment?: string }): Promise<DashboardStatsV2 | null> {
    return this.client.invoke(traceV2ControllerStats, { query });
  }

  /** List them all. `GET /v2/traces` */
  async list(query?: {
    agent?: string;
    appId?: string;
    attr?: string;
    attrMax?: string;
    attrMin?: string;
    cursor?: string;
    environment?: string;
    environmentId?: string;
    fields?: string;
    from?: string;
    limit?: string;
    maxCostUsd?: string;
    maxDurationMs?: string;
    maxTokens?: string;
    minCostUsd?: string;
    minDurationMs?: string;
    minTokens?: string;
    model?: string;
    promptId?: string;
    promptVersionId?: string;
    provider?: string;
    query?: string;
    release?: string;
    res?: string;
    semanticKind?: string;
    service?: string;
    sessionId?: string;
    sort?: string;
    spanKind?: string;
    spanMinDurationMs?: string;
    spanModel?: string;
    spanStatus?: string;
    spanTool?: string;
    status?: string;
    to?: string;
    tool?: string;
    userId?: string;
  }): Promise<TraceListV2ResponseDto | null> {
    return this.client.invoke(traceV2ControllerList, { query });
  }

  /** Attribute keys. `GET /v2/traces/attribute-keys` */
  async attributeKeys(query?: {
    agent?: string;
    appId?: string;
    attr?: string;
    attrMax?: string;
    attrMin?: string;
    environment?: string;
    environmentId?: string;
    from?: string;
    maxCostUsd?: string;
    maxDurationMs?: string;
    maxTokens?: string;
    minCostUsd?: string;
    minDurationMs?: string;
    minTokens?: string;
    model?: string;
    prefix?: string;
    promptId?: string;
    promptVersionId?: string;
    provider?: string;
    query?: string;
    release?: string;
    res?: string;
    scope?: string;
    semanticKind?: string;
    service?: string;
    sessionId?: string;
    spanKind?: string;
    spanMinDurationMs?: string;
    spanModel?: string;
    spanStatus?: string;
    spanTool?: string;
    status?: string;
    to?: string;
    tool?: string;
    userId?: string;
  }): Promise<TraceAttributeKeysV2ResponseDto | null> {
    return this.client.invoke(traceV2ControllerAttributeKeys, { query });
  }

  /** Facets. `GET /v2/traces/facets` */
  async facets(query?: {
    agent?: string;
    appId?: string;
    attr?: string;
    attrMax?: string;
    attrMin?: string;
    environment?: string;
    environmentId?: string;
    fields?: string;
    from?: string;
    maxCostUsd?: string;
    maxDurationMs?: string;
    maxTokens?: string;
    minCostUsd?: string;
    minDurationMs?: string;
    minTokens?: string;
    model?: string;
    promptId?: string;
    promptVersionId?: string;
    provider?: string;
    query?: string;
    release?: string;
    res?: string;
    semanticKind?: string;
    service?: string;
    sessionId?: string;
    spanKind?: string;
    spanMinDurationMs?: string;
    spanModel?: string;
    spanStatus?: string;
    spanTool?: string;
    status?: string;
    to?: string;
    tool?: string;
    userId?: string;
  }): Promise<TraceFacetsV2ResponseDto | null> {
    return this.client.invoke(traceV2ControllerFacets, { query });
  }

  /** Detail. `GET /v2/traces/{traceId}` */
  async detail(traceId: string): Promise<TraceDetailV2ResponseDto | null> {
    return this.client.invoke(traceV2ControllerDetail, { path: { traceId } });
  }

  /** Events. `GET /v2/traces/{traceId}/events` */
  async events(traceId: string): Promise<TraceEventsV2ResponseDto | null> {
    return this.client.invoke(traceV2ControllerEvents, { path: { traceId } });
  }

  /** Spans. `GET /v2/traces/{traceId}/spans` */
  async spans(
    traceId: string,
    query?: { limit?: string; q?: string },
  ): Promise<TraceSpanSearchV2ResponseDto | null> {
    return this.client.invoke(traceV2ControllerSpans, { path: { traceId }, query });
  }
}
