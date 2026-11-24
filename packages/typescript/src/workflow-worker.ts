import type { ActionReceipt, ActionRecord } from "./_internal/api/types.gen.js";

export interface WorkerHandlers {
  execute(action: ActionRecord): Promise<Record<string, unknown>>;
  lookup(
    action: ActionRecord,
  ): Promise<
    { result: "found"; observed: Record<string, unknown> } | { result: "absent" | "unavailable" }
  >;
}

export interface WorkflowRuntimeConfig {
  baseUrl: string;
  workspace: string;
  environment: string;
  apiKey: string;
  handler: string;
  requestTimeoutMs?: number;
  idleDelayMs?: number;
  errorDelayMs?: number;
  fetch?: typeof fetch;
  onEvent?: (event: WorkflowRuntimeEvent) => void;
}

export type WorkflowRuntimeEvent = {
  type: "claimed" | "completed" | "idle" | "retry" | "lease_lost";
  actionId?: string;
  caseKey?: string;
  mode?: string;
  delayMs?: number;
  status?: number;
};

class WorkflowHttpError extends Error {
  constructor(readonly status: number) {
    super(`Workflow runtime HTTP ${status}`);
  }
}

function endpoint(config: WorkflowRuntimeConfig, path: string): URL {
  const base = new URL(config.baseUrl);
  if (
    base.protocol !== "https:" &&
    !(base.protocol === "http:" && ["127.0.0.1", "localhost", "[::1]"].includes(base.hostname))
  )
    throw new Error("Workflow runtime requires HTTPS or loopback HTTP");
  const url = new URL(
    config.baseUrl.replace(/\/$/, "") +
      "/workspaces/" +
      encodeURIComponent(config.workspace) +
      "/workflows" +
      path,
  );
  url.searchParams.set("environment", config.environment);
  return url;
}

async function delay(ms: number, signal?: AbortSignal): Promise<void> {
  if (signal?.aborted) throw signal.reason;
  await new Promise<void>((resolve, reject) => {
    const timer = setTimeout(resolve, ms);
    signal?.addEventListener(
      "abort",
      () => {
        clearTimeout(timer);
        reject(signal.reason);
      },
      { once: true },
    );
  });
}

/** A long-running, lease-aware consumer for one workflow action handler. */
export class WorkflowRuntime {
  readonly config: WorkflowRuntimeConfig;
  readonly handlers: WorkerHandlers;

  constructor(config: WorkflowRuntimeConfig, handlers: WorkerHandlers) {
    endpoint(config, "/worker/claim");
    this.config = config;
    this.handlers = handlers;
  }

  private async post(path: string, body: unknown, signal?: AbortSignal): Promise<unknown> {
    const timeout = AbortSignal.timeout(this.config.requestTimeoutMs ?? 15_000);
    const combined = signal ? AbortSignal.any([signal, timeout]) : timeout;
    const response = await (this.config.fetch ?? fetch)(endpoint(this.config, path), {
      method: "POST",
      redirect: "error",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${this.config.apiKey}`,
      },
      body: JSON.stringify(body),
      signal: combined,
    });
    if (!response.ok) throw new WorkflowHttpError(response.status);
    return response.json();
  }

  /** Claim and settle at most one lease. Returns false when no work is available. */
  async tick(signal?: AbortSignal): Promise<boolean> {
    const { action } = (await this.post(
      "/worker/claim",
      { handler: this.config.handler },
      signal,
    )) as { action?: ActionRecord };
    if (!action) return false;
    const context = { actionId: action.id, caseKey: action.case_key, mode: action.mode };
    this.config.onEvent?.({ type: "claimed", ...context });
    let receipt: Omit<ActionReceipt, "revision">;
    if (action.mode === "execute") {
      try {
        receipt = { result: "executed", output: await this.handlers.execute(action) };
      } catch {
        // The side effect may have committed before the handler threw. Never
        // execute it again blindly; the next lease is a lookup.
        receipt = { result: "ambiguous" };
      }
    } else if (action.mode === "lookup") {
      try {
        receipt = await this.handlers.lookup(action);
      } catch {
        receipt = { result: "unavailable" };
      }
    } else throw new Error("Unrecognized workflow command");
    try {
      await this.post(
        `/cases/${encodeURIComponent(action.case_key)}/actions/${encodeURIComponent(action.id)}/receipt`,
        { ...receipt, revision: action.revision },
        signal,
      );
    } catch (error) {
      if (error instanceof WorkflowHttpError && error.status === 409) {
        this.config.onEvent?.({ type: "lease_lost", ...context, status: error.status });
        return true;
      }
      throw error;
    }
    this.config.onEvent?.({ type: "completed", ...context });
    return true;
  }

  /** Poll until the supplied signal is aborted. Transient failures back off safely. */
  async run(options: { signal?: AbortSignal } = {}): Promise<void> {
    const { signal } = options;
    while (!signal?.aborted) {
      try {
        const handled = await this.tick(signal);
        if (!handled) {
          const delayMs = this.config.idleDelayMs ?? 1_000;
          this.config.onEvent?.({ type: "idle", delayMs });
          await delay(delayMs, signal);
        }
      } catch (error) {
        if (signal?.aborted) break;
        if (error instanceof WorkflowHttpError && error.status < 500 && error.status !== 409) {
          throw error;
        }
        const delayMs = this.config.errorDelayMs ?? 2_000;
        this.config.onEvent?.({
          type: "retry",
          delayMs,
          status: error instanceof WorkflowHttpError ? error.status : undefined,
        });
        await delay(delayMs, signal);
      }
    }
  }
}

/** Process at most one lease. Kept for backwards compatibility. */
export async function runWorkflowWorkerOnce(
  config: WorkflowRuntimeConfig,
  handlers: WorkerHandlers,
): Promise<boolean> {
  return new WorkflowRuntime(config, handlers).tick();
}
