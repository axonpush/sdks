import { AsyncLocalStorage } from "node:async_hooks";

export interface EvidenceTask {
  id: string;
  parentId?: string;
}
export const evidenceTasks = new AsyncLocalStorage<EvidenceTask>();

export function taskMetadata(): Record<string, unknown> {
  const task = evidenceTasks.getStore();
  return task
    ? {
        "axonpush.task_id": task.id,
        ...(task.parentId ? { "axonpush.parent_task_id": task.parentId } : {}),
      }
    : {};
}

/** Copy task identity at admission, before a background/durable queue handoff. */
export function captureTask<T extends { metadata?: Record<string, unknown> }>(params: T): T {
  const metadata = taskMetadata();
  return Object.keys(metadata).length
    ? { ...params, metadata: { ...metadata, ...params.metadata } }
    : params;
}

/** A long-lived worker must not inherit its creator's application task. */
export function withoutEvidenceTask<T>(work: () => T): T {
  return evidenceTasks.exit(work);
}
