import {
  experimentControllerCancel,
  experimentControllerCompare,
  experimentControllerCreate,
  experimentControllerGate,
  experimentControllerGet,
  experimentControllerList,
  experimentControllerRemove,
  experimentControllerResults,
  experimentControllerRun,
  experimentControllerSubmitResults,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateExperimentDto,
  ExperimentComparisonDto,
  ExperimentDeleteDto,
  ExperimentDto,
  ExperimentGateDto,
  ExperimentGateResultDto,
  ExperimentListDto,
  ExperimentResultListDto,
  SubmitLocalExperimentResultsDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Evaluation runs, their results and the release gate. */
export class ExperimentsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/experiments` */
  async list(): Promise<ExperimentListDto | null> {
    return this.client.invoke(experimentControllerList, {});
  }

  /** Create one. `POST /v2/experiments` */
  async create(body: CreateExperimentDto): Promise<ExperimentDto | null> {
    return this.client.invoke(experimentControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/experiments/{experimentId}` */
  async delete(experimentId: string): Promise<ExperimentDeleteDto | null> {
    return this.client.invoke(experimentControllerRemove, { path: { experimentId } });
  }

  /** Fetch one by id. `GET /v2/experiments/{experimentId}` */
  async get(experimentId: string): Promise<ExperimentDto | null> {
    return this.client.invoke(experimentControllerGet, { path: { experimentId } });
  }

  /** Cancel. `POST /v2/experiments/{experimentId}/cancel` */
  async cancel(experimentId: string): Promise<ExperimentDto | null> {
    return this.client.invoke(experimentControllerCancel, { path: { experimentId } });
  }

  /** Compare. `GET /v2/experiments/{experimentId}/compare` */
  async compare(
    experimentId: string,
    query?: { baselineExperimentId?: string },
  ): Promise<ExperimentComparisonDto | null> {
    return this.client.invoke(experimentControllerCompare, { path: { experimentId }, query });
  }

  /** Gate. `POST /v2/experiments/{experimentId}/gate` */
  async gate(
    experimentId: string,
    body: ExperimentGateDto,
  ): Promise<ExperimentGateResultDto | null> {
    return this.client.invoke(experimentControllerGate, { path: { experimentId }, body });
  }

  /** Results. `GET /v2/experiments/{experimentId}/results` */
  async results(experimentId: string): Promise<ExperimentResultListDto | null> {
    return this.client.invoke(experimentControllerResults, { path: { experimentId } });
  }

  /** Submit results. `POST /v2/experiments/{experimentId}/results` */
  async submitResults(
    experimentId: string,
    body: SubmitLocalExperimentResultsDto,
  ): Promise<ExperimentDto | null> {
    return this.client.invoke(experimentControllerSubmitResults, { path: { experimentId }, body });
  }

  /** Run. `POST /v2/experiments/{experimentId}/run` */
  async run(experimentId: string): Promise<ExperimentDto | null> {
    return this.client.invoke(experimentControllerRun, { path: { experimentId } });
  }
}
