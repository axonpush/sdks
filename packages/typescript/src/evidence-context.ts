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
