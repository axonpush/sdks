import {
  datasetControllerItems,
  experimentControllerCancel,
  experimentControllerCreate,
  experimentControllerGate,
  experimentControllerGet,
  experimentControllerRun,
  experimentControllerSubmitResults,
} from "../_internal/api/sdk.gen.js";
import { type GeneratedOp, invokeSync } from "../_internal/transport.js";
import { AxonPushError } from "../errors.js";
import type {
  DatasetItem,
  EvaluationItemResult,
  GateProvenance,
  GateResult,
  GateThresholds,
  GitLineage,
} from "./types.js";

/**
 * The surface the runner depends on. Kept as an interface so tests can supply
 * a fake without a transport.
 */
export interface EvaluationApi {
  fetchDatasetRevisionItems(
    datasetId: string,
    revision: number | string,
    signal?: AbortSignal,
  ): Promise<DatasetItem[]>;
  submitResults(
    experimentId: string,
    results: EvaluationItemResult[],
    signal?: AbortSignal,
  ): Promise<void>;
  startExperiment(experimentId: string, signal?: AbortSignal): Promise<void>;
  getExperimentStatus(experimentId: string, signal?: AbortSignal): Promise<string>;
  cancelExperiment(experimentId: string): Promise<void>;
  gateExperiment(
    experimentId: string,
    thresholds?: GateThresholds,
    provenance?: GateProvenance,
    signal?: AbortSignal,
  ): Promise<GateResult>;
}

export interface CreateExperimentOptions extends GitLineage {
  name: string;
  datasetId: string;
  datasetRevision: number | string;
  targetId: string;
  evaluatorVersions?: Array<{ evaluatorId: string; version: number | string }>;
  baselineExperimentId?: string;
  configuration?: Record<string, unknown>;
}

/**
 * Raised when the evaluation API answers with a shape the runner cannot use.
 * Transport failures surface as the ordinary {@link AxonPushError} tree; this
 * class drives the CLI's exit-code mapping.
 */
export class EvaluationApiError extends AxonPushError {
  constructor(message: string) {
    super(message);
    this.name = "EvaluationApiError";
  }
}

const asRecord = (value: unknown): Record<string, unknown> =>
  value !== null && typeof value === "object" ? (value as Record<string, unknown>) : {};

/**
 * Accepts either a bare array or a `{ data: [...] }` envelope, since the v2
 * list endpoints are not yet consistent about which they return.
 */
function normalizeItems(payload: unknown): DatasetItem[] {
  const raw = Array.isArray(payload) ? payload : asRecord(payload).data;
  if (!Array.isArray(raw)) {
    throw new EvaluationApiError("Dataset revision items response was not a list");
  }
  return raw.map((entry) => {
    const item = asRecord(entry);
    const id = item.id ?? item.itemId;
    if (typeof id !== "string") {
      throw new EvaluationApiError("Dataset item was missing an id");
    }
    return {
      id,
      input: item.input,
      expected: item.expected,
      metadata: asRecord(item.metadata),
    } as DatasetItem;
  });
}

/**
 * Evaluation API backed by the generated client. Going through
 * {@link invokeSync} gives it retries, the shared error tree, one auth path and
 * the `X-Axonpush-Environment` header the rest of the SDK sends.
 */
export class HttpEvaluationApi implements EvaluationApi {
  /**
   * @param options Per-call overrides. Base URL, credentials and environment
   *   come from the active {@link AxonPush} instance, so nothing is passed here.
   */
  constructor(private readonly options: { maxRetries?: number } = {}) {}

  private async call<T>(op: GeneratedOp<T>, args: unknown): Promise<T> {
    // failOpen is off: a skipped submission would report an evaluation never run.
    const result = await invokeSync<T>(op, args, {
      failOpen: false,
      maxRetries: this.options.maxRetries,
    });
    return result as T;
  }

  async fetchDatasetRevisionItems(
    datasetId: string,
    revision: number | string,
    signal?: AbortSignal,
  ): Promise<DatasetItem[]> {
    const data = await this.call<unknown>(datasetControllerItems, {
      path: { datasetId, revision: String(revision) },
      signal,
    });
    return normalizeItems(data);
  }

  async submitResults(
    experimentId: string,
    results: EvaluationItemResult[],
    signal?: AbortSignal,
  ): Promise<void> {
    await this.call(experimentControllerSubmitResults, {
      path: { experimentId },
      body: {
        results: results.map(
          ({ itemId, output, traceId, latencyMs, totalTokens, costUsd, error }) => ({
            itemId,
            output,
            ...(traceId === undefined ? {} : { traceId }),
            latencyMs,
            ...(totalTokens === undefined ? {} : { totalTokens }),
            ...(costUsd === undefined ? {} : { costUsd }),
            ...(error === undefined ? {} : { error }),
          }),
        ),
      },
      signal,
    });
  }

  async createExperiment(
    input: CreateExperimentOptions,
    signal?: AbortSignal,
  ): Promise<{ id: string }> {
    const data = await this.call<unknown>(experimentControllerCreate, { body: input, signal });
    const record = asRecord(data);
    const id = record.experimentId ?? record.id;
    if (typeof id !== "string") {
      throw new EvaluationApiError("Create experiment response was invalid");
    }
    return { id };
  }

  async startExperiment(experimentId: string, signal?: AbortSignal): Promise<void> {
    await this.call(experimentControllerRun, { path: { experimentId }, signal });
  }

  async getExperimentStatus(experimentId: string, signal?: AbortSignal): Promise<string> {
    const data = await this.call<unknown>(experimentControllerGet, {
      path: { experimentId },
      signal,
    });
    const status = asRecord(data).status;
    if (typeof status !== "string") {
      throw new EvaluationApiError("Experiment status response was invalid");
    }
    return status;
  }

  async cancelExperiment(experimentId: string): Promise<void> {
    await this.call(experimentControllerCancel, { path: { experimentId } });
  }

  async gateExperiment(
    experimentId: string,
    thresholds?: GateThresholds,
    provenance?: GateProvenance,
    signal?: AbortSignal,
  ): Promise<GateResult> {
    const wireThresholds = toWireThresholds(thresholds);
    const wireProvenance = toWireProvenance(provenance);
    const send = (body: Record<string, unknown>) =>
      this.call<unknown>(experimentControllerGate, { path: { experimentId }, body, signal });

    let data: unknown;
    try {
      data = await send({ ...wireThresholds, ...wireProvenance });
    } catch (error) {
      // forbidNonWhitelisted: a server older than these fields rejects the whole call.
      if (!isUnknownFieldRejection(error, wireProvenance)) throw error;
      warnOnce(
        `This axonpush server does not accept ${Object.keys(wireProvenance).join(", ")} on the gate. ` +
          "The decision will be recorded without them; upgrade the server to attribute it to a commit.",
      );
      data = await send(wireThresholds);
    }

    const record = asRecord(data);
    if (typeof record.passed !== "boolean") {
      throw new EvaluationApiError("Gate response was invalid");
    }
    return record as unknown as GateResult;
  }
}

const isUnknownFieldRejection = (
  error: unknown,
  provenance: Record<string, string>,
): error is AxonPushError =>
  Object.keys(provenance).length > 0 && error instanceof AxonPushError && error.statusCode === 400;

let warned = false;

function warnOnce(message: string): void {
  if (warned) return;
  warned = true;
  process.stderr.write(`axonpush: ${message}\n`);
}

/**
 * Translate the SDK's threshold names into the ones the gate endpoint accepts.
 *
 * Two conversions are more than a rename:
 * - `maxScoreRegression` is how far the score may fall (positive), while
 *   `minScoreDelta` is the lowest acceptable delta (negative).
 * - the ratio options are fractions; the API takes percentages.
 */
export function toWireThresholds(thresholds?: GateThresholds): Record<string, number> {
  if (!thresholds) return {};
  const body: Record<string, number> = {};
  const set = (key: string, value: number | undefined) => {
    if (value !== undefined && Number.isFinite(value)) body[key] = value;
  };
  set("minScore", thresholds.minimumScore);
  set("maxFailureRate", thresholds.maximumFailureRate);
  set("maxLatencyMs", thresholds.maximumLatencyMs);
  set("maxCostUsd", thresholds.maximumCostUsd);
  set(
    "minScoreDelta",
    thresholds.maxScoreRegression === undefined
      ? undefined
      : -Math.abs(thresholds.maxScoreRegression),
  );
  set(
    "maxLatencyIncreasePercent",
    thresholds.maxLatencyIncreaseRatio === undefined
      ? undefined
      : thresholds.maxLatencyIncreaseRatio * 100,
  );
  set(
    "maxCostIncreasePercent",
    thresholds.maxCostIncreaseRatio === undefined
      ? undefined
      : thresholds.maxCostIncreaseRatio * 100,
  );
  return body;
}

/**
 * `forbidNonWhitelisted`: only the four fields the gate declares may be sent.
 * `gitDirty` belongs to the experiment, not the decision, and is rejected here.
 */
export function toWireProvenance(provenance?: GateProvenance): Record<string, string> {
  if (!provenance) return {};
  const body: Record<string, string> = {};
  for (const key of ["source", "gitCommit", "gitBranch", "release"] as const) {
    const value = provenance[key];
    if (value) body[key] = value;
  }
  return body;
}
