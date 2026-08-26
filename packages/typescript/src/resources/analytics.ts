import {
  analyticsControllerBreakdown,
  analyticsControllerCompare,
  analyticsControllerTimeseries,
} from "../_internal/api/sdk.gen.js";
import type {
  AnalyticsBreakdownResponseDto,
  AnalyticsCompareResponseDto,
  AnalyticsTimeseriesResponseDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Aggregate timeseries, breakdowns and A/B comparisons. */
export class AnalyticsResource {
  constructor(private readonly client: ResourceClient) {}

  /** Breakdown. `GET /v2/analytics/breakdown` */
  async breakdown(query: {
    dimension: string;
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
    measure?: string;
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
  }): Promise<AnalyticsBreakdownResponseDto | null> {
    return this.client.invoke(analyticsControllerBreakdown, { query });
  }

  /** Compare. `GET /v2/analytics/compare` */
  async compare(query: {
    baseline: string;
    candidate: string;
    dimension: string;
    agent?: string;
    appId?: string;
    attr?: string;
    attrMax?: string;
    attrMin?: string;
    environment?: string;
    environmentId?: string;
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
    tool?: string;
    userId?: string;
  }): Promise<AnalyticsCompareResponseDto | null> {
    return this.client.invoke(analyticsControllerCompare, { query });
  }

  /** Timeseries. `GET /v2/analytics/timeseries` */
  async timeseries(query?: {
    agent?: string;
    appId?: string;
    attr?: string;
    attrMax?: string;
    attrMin?: string;
    environment?: string;
    environmentId?: string;
    from?: string;
    interval?: string;
    maxCostUsd?: string;
    maxDurationMs?: string;
    maxTokens?: string;
    measure?: string;
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
  }): Promise<AnalyticsTimeseriesResponseDto | null> {
    return this.client.invoke(analyticsControllerTimeseries, { query });
  }
}
