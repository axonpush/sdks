import { beforeEach, describe, expect, it, vi } from "vitest";

const invokeSync = vi.fn();

vi.mock("../_internal/transport.js", async () => {
  const actual = await vi.importActual<typeof import("../_internal/transport.js")>(
    "../_internal/transport.js",
  );
  return { ...actual, invokeSync };
});

const {
  datasetControllerItems,
  experimentControllerCancel,
  experimentControllerCreate,
  experimentControllerGate,
  experimentControllerGet,
  experimentControllerRun,
  experimentControllerSubmitResults,
} = await import("../_internal/api/sdk.gen.js");
const { EvaluationApiError, HttpEvaluationApi, toWireThresholds } = await import("./api.js");

/**
 * These calls used to bypass the transport entirely. The point of each
 * assertion is that they no longer do: every one goes through `invokeSync`,
 * which is what supplies retries, the shared error tree and a single auth path.
 */
describe("HttpEvaluationApi", () => {
  beforeEach(() => {
    invokeSync.mockReset();
  });

  const lastCall = () => invokeSync.mock.calls[0] as [unknown, unknown, unknown];

  it("reads a precise dataset revision through the generated operation", async () => {
    invokeSync.mockResolvedValue([{ id: "item_1", input: { name: "Ada" } }]);

    const items = await new HttpEvaluationApi().fetchDatasetRevisionItems("ds_1", 3);

    const [op, args] = lastCall();
    expect(op).toBe(datasetControllerItems);
    expect(args).toMatchObject({ path: { datasetId: "ds_1", revision: "3" } });
    expect(items).toEqual([
      { id: "item_1", input: { name: "Ada" }, expected: undefined, metadata: {} },
    ]);
  });

  it("accepts both a bare list and a data envelope", async () => {
    invokeSync.mockResolvedValue({ data: [{ itemId: "item_2" }] });

    const items = await new HttpEvaluationApi().fetchDatasetRevisionItems("ds_1", "latest");

    expect(items).toEqual([{ id: "item_2", input: undefined, expected: undefined, metadata: {} }]);
  });

  it("never fails open, so a dropped submission cannot read as a green run", async () => {
    invokeSync.mockResolvedValue(undefined);

    await new HttpEvaluationApi().submitResults("exp_1", [
      { itemId: "item_1", output: "ADA", latencyMs: 12, status: "passed" },
    ]);

    const [op, args, options] = lastCall();
    expect(op).toBe(experimentControllerSubmitResults);
    expect(args).toMatchObject({ path: { experimentId: "exp_1" } });
    expect(options).toMatchObject({ failOpen: false });
  });

  it("omits optional result fields rather than sending undefined", async () => {
    invokeSync.mockResolvedValue(undefined);

    await new HttpEvaluationApi().submitResults("exp_1", [
      { itemId: "item_1", output: "ADA", latencyMs: 12, status: "passed" },
    ]);

    const [, args] = lastCall();
    const { results } = (args as { body: { results: Record<string, unknown>[] } }).body;
    expect(Object.keys(results[0] ?? {}).sort()).toEqual(["itemId", "latencyMs", "output"]);
  });

  it("starts a run and reads the status back", async () => {
    invokeSync.mockResolvedValue(undefined);
    await new HttpEvaluationApi().startExperiment("exp_1");
    expect(lastCall()[0]).toBe(experimentControllerRun);

    invokeSync.mockReset();
    invokeSync.mockResolvedValue({ status: "running" });
    await expect(new HttpEvaluationApi().getExperimentStatus("exp_1")).resolves.toBe("running");
    expect(lastCall()[0]).toBe(experimentControllerGet);
  });

  it("cancels through the generated operation", async () => {
    invokeSync.mockResolvedValue(undefined);
    await new HttpEvaluationApi().cancelExperiment("exp_1");
    expect(lastCall()[0]).toBe(experimentControllerCancel);
  });

  it("returns the gate verdict", async () => {
    invokeSync.mockResolvedValue({ passed: true, failures: [] });

    const gate = await new HttpEvaluationApi().gateExperiment("exp_1", { minimumScore: 0.8 });

    const [op, args] = lastCall();
    expect(op).toBe(experimentControllerGate);
    expect(args).toMatchObject({ path: { experimentId: "exp_1" }, body: { minScore: 0.8 } });
    expect(gate.passed).toBe(true);
  });

  it("sends threshold names the gate endpoint actually accepts", () => {
    // The server validates with forbidNonWhitelisted, so an unknown key is a
    // 400 rather than an ignored field. These are the seven it accepts.
    const accepted = new Set([
      "minScore",
      "maxFailureRate",
      "maxLatencyMs",
      "maxCostUsd",
      "minScoreDelta",
      "maxLatencyIncreasePercent",
      "maxCostIncreasePercent",
    ]);
    const body = toWireThresholds({
      minimumScore: 0.8,
      maximumFailureRate: 0.05,
      maximumLatencyMs: 2000,
      maximumCostUsd: 5,
      maxScoreRegression: 0.02,
      maxLatencyIncreaseRatio: 0.1,
      maxCostIncreaseRatio: 0.25,
    });
    for (const key of Object.keys(body)) expect(accepted.has(key)).toBe(true);
    expect(Object.keys(body).length).toBe(7);
  });

  it("converts a tolerated regression into a minimum delta, and ratios into percentages", () => {
    expect(toWireThresholds({ maxScoreRegression: 0.02 })).toEqual({ minScoreDelta: -0.02 });
    expect(toWireThresholds({ maxScoreRegression: -0.02 })).toEqual({ minScoreDelta: -0.02 });
    expect(toWireThresholds({ maxCostIncreaseRatio: 0.1 })).toEqual({
      maxCostIncreasePercent: 10,
    });
    expect(toWireThresholds({ maxLatencyIncreaseRatio: 0.25 })).toEqual({
      maxLatencyIncreasePercent: 25,
    });
  });

  it("sends nothing when no threshold was configured", () => {
    expect(toWireThresholds(undefined)).toEqual({});
    expect(toWireThresholds({})).toEqual({});
  });

  it("creates an experiment and validates the returned id", async () => {
    invokeSync.mockResolvedValue({ id: "exp_9" });
    const api = new HttpEvaluationApi();
    await expect(
      api.createExperiment({ name: "n", datasetId: "d", datasetRevision: 1, targetId: "t" }),
    ).resolves.toEqual({ id: "exp_9" });
    expect(lastCall()[0]).toBe(experimentControllerCreate);

    invokeSync.mockReset();
    invokeSync.mockResolvedValue({});
    await expect(
      api.createExperiment({ name: "n", datasetId: "d", datasetRevision: 1, targetId: "t" }),
    ).rejects.toBeInstanceOf(EvaluationApiError);
  });

  it("rejects a malformed dataset item rather than yielding a broken one", async () => {
    invokeSync.mockResolvedValue([{ input: {} }]);
    await expect(
      new HttpEvaluationApi().fetchDatasetRevisionItems("ds_1", 1),
    ).rejects.toBeInstanceOf(EvaluationApiError);
  });
});
