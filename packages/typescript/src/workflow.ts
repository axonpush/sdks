/** Offline wrapper around the same compiler/evaluator used by the server. */
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const execute = promisify(execFile);
export const workflowCompilerVersion = "0.1.0";
export type {
  FactsInputBody as PublishWorkflowFacts,
  Input as WorkflowInput,
} from "./_internal/api/types.gen.js";

export async function runWorkflow(
  args: string[],
  options: { binary?: string; timeout?: number } = {},
): Promise<unknown> {
  if (!args[0] || !["validate", "generate", "test", "action-test", "diff"].includes(args[0])) {
    throw new Error("Expected validate, generate, test, action-test or diff");
  }
  const binary = options.binary ?? process.env.AXONPUSH_WORKFLOW_BINARY;
  if (!binary) throw new Error("Set AXONPUSH_WORKFLOW_BINARY to the pinned compiler executable");
  const execution = { timeout: options.timeout ?? 30_000, maxBuffer: 8 * 1024 * 1024 };
  const version = await execute(binary, ["workflow", "version"], execution);
  if (JSON.parse(version.stdout).version !== workflowCompilerVersion) {
    throw new Error(`Workflow compiler ${workflowCompilerVersion} is required`);
  }
  const result = await execute(binary, ["workflow", ...args], execution);
  return result.stdout.trim() ? JSON.parse(result.stdout) : null;
}
export { runWorkflowWorkerOnce, type WorkerHandlers } from "./workflow-worker.js";
