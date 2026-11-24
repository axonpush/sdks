/** Offline wrapper around the same compiler/evaluator used by the server. */
import { execFile } from "node:child_process";
import { existsSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import { promisify } from "node:util";

const execute = promisify(execFile);
export const workflowCompilerVersion = "0.1.0";
export type {
  FactsInputBody as PublishWorkflowFacts,
  Input as WorkflowInput,
} from "./_internal/api/types.gen.js";

/** Resolve the pinned optional platform package, with an explicit env override. */
export function resolveWorkflowBinary(): string {
  if (process.env.AXONPUSH_WORKFLOW_BINARY) return process.env.AXONPUSH_WORKFLOW_BINARY;
  const platform = process.platform === "win32" ? "windows" : process.platform;
  const architecture = process.arch === "x64" ? "amd64" : process.arch;
  const packageName = `@axonpush/workflow-${platform}-${architecture}`;
  try {
    const require = createRequire(import.meta.url);
    const root = dirname(require.resolve(`${packageName}/package.json`));
    const binary = join(root, "bin", process.platform === "win32" ? "axonpush.exe" : "axonpush");
    if (existsSync(binary)) return binary;
  } catch {
    // The actionable error below lists the exact optional package.
  }
  throw new Error(
    `Install ${packageName} or set AXONPUSH_WORKFLOW_BINARY to the pinned compiler executable`,
  );
}

export async function runWorkflow(
  args: string[],
  options: { binary?: string; timeout?: number } = {},
): Promise<unknown> {
  if (!args[0] || !["validate", "generate", "test", "action-test", "diff"].includes(args[0])) {
    throw new Error("Expected validate, generate, test, action-test or diff");
  }
  const binary = options.binary ?? resolveWorkflowBinary();
  const execution = { timeout: options.timeout ?? 30_000, maxBuffer: 8 * 1024 * 1024 };
  const version = await execute(binary, ["workflow", "version"], execution);
  if (JSON.parse(version.stdout).version !== workflowCompilerVersion) {
    throw new Error(`Workflow compiler ${workflowCompilerVersion} is required`);
  }
  const result = await execute(binary, ["workflow", ...args], execution);
  return result.stdout.trim() ? JSON.parse(result.stdout) : null;
}
export {
  runWorkflowWorkerOnce,
  type WorkerHandlers,
  WorkflowRuntime,
  type WorkflowRuntimeConfig,
  type WorkflowRuntimeEvent,
} from "./workflow-worker.js";
