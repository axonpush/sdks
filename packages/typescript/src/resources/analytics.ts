import {
  analyticsBreakdown,
  analyticsDiff,
  analyticsDimensions,
  analyticsDimensionValues,
  analyticsHeatmap,
  analyticsIngestionStatus,
  analyticsLatency,
  analyticsOverview,
  analyticsTimeseries,
} from "../_internal/api/sdk.gen.js";
import type {
  AnalyticsBreakdownData,
  AnalyticsDimensionsData,
  AnalyticsDimensionValuesData,
  AnalyticsHeatmapData,
  AnalyticsIngestionStatusData,
  AnalyticsLatencyData,
  AnalyticsOverviewData,
  AnalyticsOverviewOutputBody,
  AnalyticsTimeseriesData,
  BreakdownOutputBody,
  DiffInputBodyWritable,
  DiffOutputBody,
  DimensionsOutputBody,
  DimensionValuesOutputBody,
  HeatmapOutputBody,
  IngestionStatusOutputBody,
  LatencyPercentilesDto,
  TimeseriesOutputBody,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type AnalyticsBreakdownParams = NonNullable<AnalyticsBreakdownData["query"]>;
export type AnalyticsTimeseriesParams = NonNullable<AnalyticsTimeseriesData["query"]>;
export type AnalyticsLatencyParams = NonNullable<AnalyticsLatencyData["query"]>;
export type AnalyticsDimensionsParams = NonNullable<AnalyticsDimensionsData["query"]>;
export type AnalyticsDimensionValuesParams = NonNullable<AnalyticsDimensionValuesData["query"]>;
export type AnalyticsOverviewParams = NonNullable<AnalyticsOverviewData["query"]>;
export type AnalyticsHeatmapParams = NonNullable<AnalyticsHeatmapData["query"]>;
export type AnalyticsIngestionStatusParams = NonNullable<AnalyticsIngestionStatusData["query"]>;

/** Cohort-diff request accepted by {@link AnalyticsResource.diff}. */
export type AnalyticsDiffInput = DiffInputBodyWritable;

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

  /** Headline totals, timeseries, and breakdowns in one call. `GET /analytics/overview` */
  async overview(query: AnalyticsOverviewParams = {}): Promise<AnalyticsOverviewOutputBody | null> {
    return this.client.invoke(analyticsOverview, { query });
  }

  /** Latency-band-by-time heatmap. `GET /analytics/heatmap` */
  async heatmap(query: AnalyticsHeatmapParams = {}): Promise<HeatmapOutputBody | null> {
    return this.client.invoke(analyticsHeatmap, { query });
  }

  /** Rank the attributes that most explain a cohort difference. `POST /analytics/diff` */
  async diff(body: AnalyticsDiffInput): Promise<DiffOutputBody | null> {
    return this.client.invoke(analyticsDiff, { body });
  }

  /** Ingestion freshness and recent event counts. `GET /analytics/ingestion-status` */
  async ingestionStatus(
    query: AnalyticsIngestionStatusParams = {},
  ): Promise<IngestionStatusOutputBody | null> {
    return this.client.invoke(analyticsIngestionStatus, { query });
  }
}
