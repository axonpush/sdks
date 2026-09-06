import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it, vi } from "vitest";
import type { EvaluationApi } from "./api.js";
import { toGitHubSummary, toJUnitXml } from "./reports.js";
import { runLocalEvaluation } from "./runner.js";
import type { EvaluationItemResult, EvaluationRunResult } from "./types.js";

/**
 * A command that runs `source` as a script file rather than `node -e "..."`.
 * cmd.exe mangles the nested quotes of an inline script, so the inline form
 * silently produced an empty result on Windows and only ever ran on Linux.
 */
function evaluator(source: string): string {
  const file = join(mkdtempSync(join(tmpdir(), "axonpush-eval-")), "evaluator.mjs");
  writeFileSync(file, source, "utf-8");
  return `${JSON.stringify(process.execPath)} ${JSON.stringify(file)}`;
}

function api(
  items = [
    { id: "first", input: { name: "Ada" } },
    { id: "second", input: { name: "Lin" } },
  ],
) {
  const submitted: EvaluationItemResult[][] = [];
  const value: EvaluationApi = {
    fetchDatasetRevisionItems: vi.fn().mockResolvedValue(items),
    submitResults: vi.fn(async (_experimentId, results) => {
      submitted.push(results);
    }),
    startExperiment: vi.fn().mockResolvedValue(undefined),
    getExperimentStatus: vi.fn().mockResolvedValue("running"),
    cancelExperiment: vi.fn().mockResolvedValue(undefined),
    gateExperiment: vi.fn(),
  };
  return { value, submitted };
}

describe("runLocalEvaluation", () => {
  it("executes the local JSONL protocol and independently submits each item", async () => {
    const fixture = api();
    const command = evaluator(
      "let source='';process.stdin.on('data', c => source += c).on('end', () => { const input = JSON.parse(source); process.stdout.write(JSON.stringify({ output: input.item.input.name.toUpperCase(), totalTokens: 3 }) + '\\n'); });",
    );
    const result = await runLocalEvaluation(fixture.value, {
      datasetId: "dataset_1",
      datasetRevision: 3,
      experimentId: "experiment_1",
      command,
      concurrency: 2,
    });

    expect(result.cancelled).toBe(false);
    expect(result.results).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          itemId: "first",
          output: "ADA",
          totalTokens: 3,
          status: "passed",
        }),
        expect.objectContaining({
          itemId: "second",
          output: "LIN",
          totalTokens: 3,
          status: "passed",
        }),
      ]),
    );
    expect(fixture.submitted).toHaveLength(2);
    expect(fixture.value.startExperiment).toHaveBeenCalledWith(
      "experiment_1",
      expect.any(AbortSignal),
    );
  });

  it("records a timeout as a failed item without corrupting the complete run", async () => {
    const fixture = api([{ id: "slow", input: { name: "Slow" } }]);
    const command = evaluator(
      "setTimeout(() => process.stdout.write(JSON.stringify({ output: 'late' }) + '\\n'), 500)",
    );
    const result = await runLocalEvaluation(fixture.value, {
      datasetId: "dataset_1",
      datasetRevision: 1,
      experimentId: "experiment_1",
      command,
      timeoutMs: 20,
    });
    expect(result.results[0]).toMatchObject({
      itemId: "slow",
      status: "failed",
      error: expect.stringMatching(/timed out/),
    });
    expect(fixture.submitted[0]?.[0]?.error).toMatch(/timed out/);
  });

  it("cancels the remote experiment when the local signal is aborted", async () => {
    const fixture = api([{ id: "slow", input: { name: "Slow" } }]);
    const controller = new AbortController();
    const command = evaluator(
      "setTimeout(() => process.stdout.write(JSON.stringify({ output: 'late' }) + '\\n'), 500)",
    );
    const promise = runLocalEvaluation(fixture.value, {
      datasetId: "dataset_1",
      datasetRevision: 1,
      experimentId: "experiment_1",
      command,
      signal: controller.signal,
    });
    setTimeout(() => controller.abort(), 10);
    const result = await promise;
    expect(result.cancelled).toBe(true);
    expect(fixture.value.cancelExperiment).toHaveBeenCalledWith("experiment_1");
  });
});

describe("evaluation reports", () => {
  const result: EvaluationRunResult = {
    experimentId: "experiment_1",
    datasetId: "dataset_1",
    datasetRevision: 1,
    startedAt: "2026-01-01T00:00:00.000Z",
    completedAt: "2026-01-01T00:00:01.000Z",
    cancelled: false,
    lineage: { gitCommit: "a".repeat(40) },
    results: [
      { itemId: "good", output: "ok", latencyMs: 10, status: "passed" },
      { itemId: "bad", output: null, latencyMs: 20, status: "failed", error: "bad < xml" },
    ],
    gate: { passed: false, experimentId: "experiment_1", reasons: ["score dropped"] },
  };

  it("escapes JUnit and presents gate failures in GitHub summary", () => {
    expect(toJUnitXml(result)).toContain("bad &lt; xml");
    expect(toGitHubSummary(result)).toContain("Gate failed.");
    expect(toGitHubSummary(result)).toContain("score dropped");
  });
});
