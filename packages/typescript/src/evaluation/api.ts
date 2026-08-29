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
 *
 * Transport failures now surface as the ordinary {@link AxonPushError} tree,
 * because these calls go through the same chokepoint as every other request.
 * The class stays for the CLI's exit-code mapping and for callers catching it.
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
 * Evaluation API backed by the generated client.
 *
 * This used to be a hand-written `fetch` layer with its own timeout, error
 * class and header assembly, written before the v2 routes reached the
 * contract. It sent `x-api-key` and `authorization: Bearer` together, and an
 * `?environment=` query no v2 evaluation route reads. Going through
 * {@link invokeSync} means retries, the shared error tree, one auth path and
 * the `X-Axonpush-Environment` header the rest of the SDK sends.
 */
export class HttpEvaluationApi implements EvaluationApi {
  /**
   * @param options Per-call overrides. Base URL, credentials and environment
   *   come from the active {@link AxonPush} instance, so nothing is passed here.
   */
  constructor(private readonly options: { maxRetries?: number } = {}) {}

  private async call<T>(op: GeneratedOp<T>, args: unknown): Promise<T> {
    // failOpen is off: a runner that silently skips a submission would report a
    // green evaluation it never actually ran
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
    const id = asRecord(data).id;
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
    signal?: AbortSignal,
  ): Promise<GateResult> {
    const data = await this.call<unknown>(experimentControllerGate, {
      path: { experimentId },
      body: toWireThresholds(thresholds),
      signal,
    });
    const record = asRecord(data);
    if (typeof record.passed !== "boolean") {
      throw new EvaluationApiError("Gate response was invalid");
    }
    return record as unknown as GateResult;
  }
}

/**
 * Translate the SDK's threshold names into the ones the gate endpoint accepts.
 *
 * These two vocabularies had drifted apart completely: the SDK sent
 * `minimumScore`/`maxCostIncreaseRatio`, the API accepts
 * `minScore`/`maxCostIncreasePercent`, and the server validates with
 * `forbidNonWhitelisted`, so every threshold the CLI was asked to enforce came
 * back as a 400 instead of a gate decision.
 *
 * Two of the conversions are more than a rename:
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
