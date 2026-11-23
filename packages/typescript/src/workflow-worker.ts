import type { ActionRecord, ActionReceipt } from "./_internal/api/types.gen.js";

export interface WorkerHandlers {
  execute(action: ActionRecord): Promise<Record<string, unknown>>;
  lookup(
    action: ActionRecord,
  ): Promise<
    { result: "found"; observed: Record<string, unknown> } | { result: "absent" | "unavailable" }
  >;
}

/** Process at most one lease. A failed receipt is recovered by a read after lease expiry. */
export async function runWorkflowWorkerOnce(
  config: {
    baseUrl: string;
    workspace: string;
    environment: string;
    apiKey: string;
    handler: string;
  },
  handlers: WorkerHandlers,
): Promise<boolean> {
  const base = new URL(config.baseUrl);
  if (
    base.protocol !== "https:" &&
    !(base.protocol === "http:" && ["127.0.0.1", "localhost", "[::1]"].includes(base.hostname))
  )
    throw new Error("Worker requires HTTPS or loopback HTTP");
  async function post(path: string, body: unknown) {
    const url = new URL(
      config.baseUrl.replace(/\/$/, "") +
        "/workspaces/" +
        encodeURIComponent(config.workspace) +
        "/workflows" +
        path,
    );
    url.searchParams.set("environment", config.environment);
    const response = await fetch(url, {
      method: "POST",
      redirect: "error",
      headers: { "Content-Type": "application/json", Authorization: "Bearer " + config.apiKey },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(15000),
    });
    if (!response.ok) throw new Error("Workflow worker HTTP " + response.status);
    return response.json();
  }
  const { action } = (await post("/worker/claim", { handler: config.handler })) as {
    action?: ActionRecord;
  };
  if (!action) return false;
  let receipt: Omit<ActionReceipt, "revision">;
  if (action.mode === "execute") {
    try {
      receipt = { result: "executed", output: await handlers.execute(action) };
    } catch {
      receipt = { result: "ambiguous" };
    }
  } else if (action.mode === "lookup") {
    try {
      receipt = await handlers.lookup(action);
    } catch {
      receipt = { result: "unavailable" };
    }
  } else throw new Error("Unrecognized workflow command");
  await post(
    "/cases/" +
      encodeURIComponent(action.case_key) +
      "/actions/" +
      encodeURIComponent(action.id) +
      "/receipt",
    { ...receipt, revision: action.revision },
  );
  return true;
}
