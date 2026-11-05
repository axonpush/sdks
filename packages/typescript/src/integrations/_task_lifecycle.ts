import { randomUUID } from "node:crypto";
import { evidenceTasks } from "../evidence-context.js";

export interface DeclaredTaskContext {
  framework: string;
  runId: string;
  name?: string;
  input?: unknown;
  metadata?: Record<string, unknown>;
}
/** Explicitly opt in with the goal you intend the root run to perform.
 * Returning undefined leaves that run undeclared; names are never used as goals. */
export type DeclaredTaskGoal = string | ((context: DeclaredTaskContext) => string | undefined);
export interface TaskBoundary {
  identifier: "agent.task.start" | "agent.task.end";
  payload: Record<string, unknown>;
  metadata: Record<string, unknown>;
}
interface Entry {
  id: string;
  parentId?: string;
  root: string;
  runs: Set<string>;
}
const maximumRuns = 10_000;
const identity = (entry: Pick<Entry, "id" | "parentId">) => ({
  "axonpush.task_id": entry.id,
  ...(entry.parentId ? { "axonpush.parent_task_id": entry.parentId } : {}),
});
const boundary = (
  entry: Pick<Entry, "id" | "parentId">,
  identifier: TaskBoundary["identifier"],
  payload: Record<string, unknown>,
): TaskBoundary => ({
  identifier,
  payload,
  metadata: {
    ...identity(entry),
    "axonpush.evidence.version": 1,
    "axonpush.evidence.kind": identifier,
    "axonpush.evidence.origin": "sdk_reported",
  },
});

/** Callback identity is scoped by framework run IDs, not global mutable state.
 * Mappings are bounded and removed on root completion. No missing start is inferred. */
export class FrameworkTaskLifecycle {
  private readonly runs = new Map<string, Entry>();
  private readonly completed = new Set<string>();
  constructor(
    private readonly goal: DeclaredTaskGoal | undefined,
    private readonly framework: string,
  ) {}

  start(
    runId: string | undefined,
    parentRunId: string | undefined,
    context: Omit<DeclaredTaskContext, "framework" | "runId">,
  ): TaskBoundary | undefined {
    if (!this.goal || !runId) return;
    if (parentRunId) {
      this.metadata(runId, parentRunId);
      return;
    }
    if (this.runs.has(runId) || this.completed.has(runId) || this.runs.size >= maximumRuns) return;
    let goal: string | undefined;
    try {
      goal =
        typeof this.goal === "function"
          ? this.goal({ ...context, framework: this.framework, runId })
          : this.goal;
    } catch {
      return;
    }
    if (typeof goal !== "string" || !goal.trim() || goal.length > 32_000) return;
    const parent = evidenceTasks.getStore();
    const task: Entry = {
      id: randomUUID(),
      root: runId,
      runs: new Set([runId]),
      ...(parent ? { parentId: parent.id } : {}),
    };
    this.runs.set(runId, task);
    return boundary(task, "agent.task.start", { goal });
  }

  metadata(runId?: string, parentRunId?: string): Record<string, unknown> {
    let entry = runId ? this.runs.get(runId) : undefined;
    if (!entry && parentRunId) {
      entry = this.runs.get(parentRunId);
      if (entry && runId && this.runs.size < maximumRuns) {
        this.runs.set(runId, entry);
        entry.runs.add(runId);
      }
    }
    return entry ? identity(entry) : {};
  }

  finish(runId: string | undefined, outcome: "succeeded" | "failed"): TaskBoundary | undefined {
    if (!runId) return;
    const task = this.runs.get(runId);
    if (!task || task.root !== runId) return;
    for (const key of task.runs) this.runs.delete(key);
    task.runs.clear();
    this.completed.add(runId);
    if (this.completed.size > maximumRuns) {
      const oldest = this.completed.values().next().value;
      if (oldest !== undefined) this.completed.delete(oldest);
    }
    return boundary(task, "agent.task.end", { outcome });
  }
}

/** Root scope for runners whose hooks do not expose reliable failure boundaries.
 * Callers await the complete runner, including consuming a streaming result. */
export async function runDeclaredTask<T>(
  goal: string,
  emit: (event: TaskBoundary) => void,
  action: (taskId: string) => Promise<T>,
): Promise<T> {
  if (typeof goal !== "string" || !goal.trim() || goal.length > 32_000)
    throw new Error("A declared task requires a nonempty goal up to 32000 characters");
  const parent = evidenceTasks.getStore();
  const task = {
    id: randomUUID(),
    ...(parent ? { parentId: parent.id } : {}),
  };
  return evidenceTasks.run(task, async () => {
    emit(boundary(task, "agent.task.start", { goal }));
    let result: T;
    try {
      result = await action(task.id);
    } catch (error) {
      emit(boundary(task, "agent.task.end", { outcome: "failed" }));
      throw error;
    }
    emit(boundary(task, "agent.task.end", { outcome: "succeeded" }));
    return result;
  });
}
