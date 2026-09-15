import { analyticsBreakdown, analyticsTimeseries } from "../_internal/api/sdk.gen.js";
import type {
  AnalyticsBreakdownData,
  AnalyticsTimeseriesData,
  BreakdownOutputBody,
  TimeseriesOutputBody,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type AnalyticsBreakdownParams = NonNullable<AnalyticsBreakdownData["query"]>;
export type AnalyticsTimeseriesParams = NonNullable<AnalyticsTimeseriesData["query"]>;

/** Aggregate timeseries and dimension breakdowns. */
export class AnalyticsResource {
  constructor(private readonly client: ResourceClient) {}

  /** Breakdown by dimension. `GET /analytics/breakdown` */
  async breakdown(query: AnalyticsBreakdownParams = {}): Promise<BreakdownOutputBody | null> {
    return this.client.invoke(analyticsBreakdown, { query });
  }

  /** Bucketed timeseries. `GET /analytics/timeseries` */
  async timeseries(query: AnalyticsTimeseriesParams = {}): Promise<TimeseriesOutputBody | null> {
    return this.client.invoke(analyticsTimeseries, { query });
  }
}
