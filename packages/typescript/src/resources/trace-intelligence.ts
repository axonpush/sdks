import {
  traceIntelligenceControllerAddToDataset,
  traceIntelligenceControllerCoverage,
  traceIntelligenceControllerCreateBackfill,
  traceIntelligenceControllerFlow,
  traceIntelligenceControllerGetBackfill,
  traceIntelligenceControllerGetCluster,
  traceIntelligenceControllerGetSettings,
  traceIntelligenceControllerGetSignals,
  traceIntelligenceControllerListBackfills,
  traceIntelligenceControllerListClusters,
  traceIntelligenceControllerTestProvider,
  traceIntelligenceControllerUpdateSettings,
} from "../_internal/api/sdk.gen.js";
import type {
  AddTraceClusterToDatasetDto,
  CreateTraceIntelligenceBackfillDto,
  TestTraceIntelligenceProviderDto,
  TraceClusterDatasetActionResponseDto,
  TraceIntelligenceBackfillResponseDto,
  TraceIntelligenceClusterListResponseDto,
  TraceIntelligenceClusterResponseDto,
  TraceIntelligenceCoverageResponseDto,
  TraceIntelligenceFlowResponseDto,
  TraceIntelligenceProviderTestResponseDto,
  TraceIntelligenceSettingsResponseDto,
  TraceIntelligenceSignalsResponseDto,
  UpdateTraceIntelligenceSettingsDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Semantic clustering over traces: clusters, flow and coverage. */
export class TraceIntelligenceResource {
  constructor(private readonly client: ResourceClient) {}

  /** List backfills. `GET /v2/trace-intelligence/backfills` */
  async listBackfills(): Promise<TraceIntelligenceBackfillResponseDto[] | null> {
    return this.client.invoke(traceIntelligenceControllerListBackfills, {});
  }

  /** Create backfill. `POST /v2/trace-intelligence/backfills` */
  async createBackfill(
    body: CreateTraceIntelligenceBackfillDto,
  ): Promise<TraceIntelligenceBackfillResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerCreateBackfill, { body });
  }

  /** Get backfill. `GET /v2/trace-intelligence/backfills/{jobId}` */
  async getBackfill(jobId: string): Promise<TraceIntelligenceBackfillResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerGetBackfill, { path: { jobId } });
  }

  /** List clusters. `GET /v2/trace-intelligence/clusters` */
  async listClusters(query: {
    appId: string;
    environmentId: string;
    cursor?: string;
    from?: string;
    limit?: string;
    search?: string;
    signalKind?: string;
    to?: string;
  }): Promise<TraceIntelligenceClusterListResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerListClusters, { query });
  }

  /** Get cluster. `GET /v2/trace-intelligence/clusters/{clusterId}` */
  async getCluster(clusterId: string): Promise<TraceIntelligenceClusterResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerGetCluster, { path: { clusterId } });
  }

  /** Add to dataset. `POST /v2/trace-intelligence/clusters/{clusterId}/actions/add-to-dataset` */
  async addToDataset(
    clusterId: string,
    body: AddTraceClusterToDatasetDto,
  ): Promise<TraceClusterDatasetActionResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerAddToDataset, {
      path: { clusterId },
      body,
    });
  }

  /** Coverage. `GET /v2/trace-intelligence/coverage` */
  async coverage(query: {
    appId: string;
    environmentId: string;
    from?: string;
    to?: string;
  }): Promise<TraceIntelligenceCoverageResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerCoverage, { query });
  }

  /** Flow. `GET /v2/trace-intelligence/flow` */
  async flow(query: {
    appId: string;
    environmentId: string;
    from: string;
    to: string;
    includeUnclustered?: string;
    minimumVolume?: string;
  }): Promise<TraceIntelligenceFlowResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerFlow, { query });
  }

  /** Get settings. `GET /v2/trace-intelligence/settings` */
  async getSettings(): Promise<TraceIntelligenceSettingsResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerGetSettings, {});
  }

  /** Update settings. `PUT /v2/trace-intelligence/settings` */
  async updateSettings(
    body: UpdateTraceIntelligenceSettingsDto,
  ): Promise<TraceIntelligenceSettingsResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerUpdateSettings, { body });
  }

  /** Test provider. `POST /v2/trace-intelligence/settings/provider/test` */
  async testProvider(
    body: TestTraceIntelligenceProviderDto,
  ): Promise<TraceIntelligenceProviderTestResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerTestProvider, { body });
  }

  /** Get signals. `GET /v2/trace-intelligence/traces/{traceId}/signals` */
  async getSignals(traceId: string): Promise<TraceIntelligenceSignalsResponseDto | null> {
    return this.client.invoke(traceIntelligenceControllerGetSignals, { path: { traceId } });
  }
}
