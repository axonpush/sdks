import {
  datasetControllerCreate,
  datasetControllerCreateRevision,
  datasetControllerExportRevision,
  datasetControllerFromTraces,
  datasetControllerGet,
  datasetControllerImportRevision,
  datasetControllerItems,
  datasetControllerList,
  datasetControllerRemove,
  datasetControllerRevisions,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateDatasetDto,
  CreateDatasetRevisionDto,
  DatasetDeleteDto,
  DatasetDto,
  DatasetExportDto,
  DatasetListDto,
  DatasetRevisionDto,
  DatasetRevisionItemsDto,
  DatasetRevisionListDto,
  ImportDatasetRevisionDto,
  TraceDatasetSelectionDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

/** Evaluation datasets and their immutable revisions. */
export class DatasetsResource {
  constructor(private readonly client: ResourceClient) {}

  /** List them all. `GET /v2/datasets` */
  async list(): Promise<DatasetListDto | null> {
    return this.client.invoke(datasetControllerList, {});
  }

  /** Create one. `POST /v2/datasets` */
  async create(body: CreateDatasetDto): Promise<DatasetDto | null> {
    return this.client.invoke(datasetControllerCreate, { body });
  }

  /** Delete one. `DELETE /v2/datasets/{datasetId}` */
  async delete(datasetId: string): Promise<DatasetDeleteDto | null> {
    return this.client.invoke(datasetControllerRemove, { path: { datasetId } });
  }

  /** Fetch one by id. `GET /v2/datasets/{datasetId}` */
  async get(datasetId: string): Promise<DatasetDto | null> {
    return this.client.invoke(datasetControllerGet, { path: { datasetId } });
  }

  /** Revisions. `GET /v2/datasets/{datasetId}/revisions` */
  async revisions(datasetId: string): Promise<DatasetRevisionListDto | null> {
    return this.client.invoke(datasetControllerRevisions, { path: { datasetId } });
  }

  /** Create revision. `POST /v2/datasets/{datasetId}/revisions` */
  async createRevision(
    datasetId: string,
    body: CreateDatasetRevisionDto,
  ): Promise<DatasetRevisionDto | null> {
    return this.client.invoke(datasetControllerCreateRevision, { path: { datasetId }, body });
  }

  /** From traces. `POST /v2/datasets/{datasetId}/revisions/from-traces` */
  async fromTraces(
    datasetId: string,
    body: TraceDatasetSelectionDto,
  ): Promise<DatasetRevisionDto | null> {
    return this.client.invoke(datasetControllerFromTraces, { path: { datasetId }, body });
  }

  /** Import revision. `POST /v2/datasets/{datasetId}/revisions/import` */
  async importRevision(
    datasetId: string,
    body: ImportDatasetRevisionDto,
  ): Promise<DatasetRevisionDto | null> {
    return this.client.invoke(datasetControllerImportRevision, { path: { datasetId }, body });
  }

  /** Export revision. `GET /v2/datasets/{datasetId}/revisions/{revision}/export/{format}` */
  async exportRevision(
    datasetId: string,
    format: string,
    revision: string,
  ): Promise<DatasetExportDto | null> {
    return this.client.invoke(datasetControllerExportRevision, {
      path: { datasetId, format, revision },
    });
  }

  /** Items. `GET /v2/datasets/{datasetId}/revisions/{revision}/items` */
  async items(datasetId: string, revision: string): Promise<DatasetRevisionItemsDto | null> {
    return this.client.invoke(datasetControllerItems, { path: { datasetId, revision } });
  }
}
