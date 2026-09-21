import {
  analyticsBreakdown,
  analyticsDimensions,
  analyticsDimensionValues,
  analyticsLatency,
  analyticsTimeseries,
} from "../_internal/api/sdk.gen.js";
import type {
  AnalyticsBreakdownData,
  AnalyticsDimensionsData,
  AnalyticsDimensionValuesData,
  AnalyticsLatencyData,
  AnalyticsTimeseriesData,
  BreakdownOutputBody,
  DimensionsOutputBody,
  DimensionValuesOutputBody,
  LatencyPercentilesDto,
  TimeseriesOutputBody,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type AnalyticsBreakdownParams = NonNullable<AnalyticsBreakdownData["query"]>;
export type AnalyticsTimeseriesParams = NonNullable<AnalyticsTimeseriesData["query"]>;
export type AnalyticsLatencyParams = NonNullable<AnalyticsLatencyData["query"]>;
export type AnalyticsDimensionsParams = NonNullable<AnalyticsDimensionsData["query"]>;
export type AnalyticsDimensionValuesParams = NonNullable<AnalyticsDimensionValuesData["query"]>;

/** Aggregate timeseries, latency percentiles, and dimension breakdowns. */
export class AnalyticsResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * Discover the custom dimensions (business attribute keys) this org emits.
   * Start here, then feed a key into {@link breakdown} (`dimension: "tag"`,
   * `tagKey`) or filter {@link timeseries}/{@link latency} with
   * `filterTagKey`+`filterTagValue`. `GET /analytics/dimensions`
   */
  async dimensions(query: AnalyticsDimensionsParams = {}): Promise<DimensionsOutputBody | null> {
    return this.client.invoke(analyticsDimensions, { query });
  }

  /** Observed values for one custom dimension. `GET /analytics/dimensions/values` */
  async dimensionValues(
    query: AnalyticsDimensionValuesParams,
  ): Promise<DimensionValuesOutputBody | null> {
    return this.client.invoke(analyticsDimensionValues, { query });
  }

  /** Breakdown by dimension (including custom tags). `GET /analytics/breakdown` */
  async breakdown(query: AnalyticsBreakdownParams = {}): Promise<BreakdownOutputBody | null> {
    return this.client.invoke(analyticsBreakdown, { query });
  }

  /** Bucketed timeseries. `GET /analytics/timeseries` */
  async timeseries(query: AnalyticsTimeseriesParams = {}): Promise<TimeseriesOutputBody | null> {
    return this.client.invoke(analyticsTimeseries, { query });
  }

  /** Latency + TTFT percentiles. `GET /analytics/latency` */
  async latency(query: AnalyticsLatencyParams = {}): Promise<LatencyPercentilesDto | null> {
    return this.client.invoke(analyticsLatency, { query });
  }
}
