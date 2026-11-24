/** Shared source serialization and native compiler bridge for authoring providers. */
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { runWorkflow } from "../workflow.js";
import type { Bundle, Input, Result } from "./api/types.gen.js";
export type WorkflowDefinition = Readonly<{ source: string }>;
export type WorkflowBinaryOptions = { binary?: string; timeout?: number };
function canonical(value: unknown): unknown {
  if (value === null || typeof value === "string" || typeof value === "boolean") return value;
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (Array.isArray(value)) return value.map(canonical);
  if (typeof value === "object" && Object.getPrototypeOf(value) === Object.prototype) {
    return Object.fromEntries(
      Object.entries(value as Record<string, unknown>)
        .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0))
        .map(([key, entry]) => [key, canonical(entry)]),
    );
  }
  throw new Error("Workflow configuration must contain only finite JSON values");
}

export function serializeWorkflow(contract: unknown): WorkflowDefinition {
  return Object.freeze({ source: `${JSON.stringify(canonical(contract), null, 2)}\n` });
}
async function withSource<T>(
  workflow: WorkflowDefinition,
  execute: (file: string, directory: string) => Promise<T>,
): Promise<T> {
  const directory = await mkdtemp(join(tmpdir(), "axonpush-workflow-"));
  try {
    const file = join(directory, "workflow.json");
    await writeFile(file, workflow.source, { mode: 0o600 });
    return await execute(file, directory);
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
}

/** Invoke the version-pinned Go compiler, including its type checks and hashes. */
export async function compileWorkflow(
  workflow: WorkflowDefinition,
  options: WorkflowBinaryOptions = {},
): Promise<Bundle> {
  return withSource(
    workflow,
    async (file) => (await runWorkflow(["validate", "--file", file], options)) as Bundle,
  );
}

/** Invoke the same Go evaluator used by the server, with an explicit fixture clock. */
export async function verifyWorkflow(
  workflow: WorkflowDefinition,
  input: Input,
  options: WorkflowBinaryOptions = {},
): Promise<Result> {
  return withSource(workflow, async (file, directory) => {
    const fixture = join(directory, "case.json");
    await writeFile(fixture, JSON.stringify(input), { mode: 0o600 });
    return (await runWorkflow(["test", "--file", file, "--fixture", fixture], options)) as Result;
  });
}
