import { setTimeout as delay } from "node:timers/promises";
import pRetry from "p-retry";
import { type ResolvedSettings, resolveSettings } from "../config.js";
import {
  APIConnectionError,
  AxonPushError,
  fromResponse,
  isRetryable,
  RateLimitError,
} from "../errors.js";
import { currentTrace } from "../tracing.js";
import type { Client, Config } from "./api/client/index.js";
import { createClient } from "./api/client/index.js";
import type { CreateClientConfig } from "./api/client.gen.js";

// Placeholder used by the module-global generated client until an AxonPush
// instance takes over. Derived from config so the two cannot drift; they
// previously disagreed on the base URL, the timeout unit and the fail-open
// default. Per-instance settings now live on {@link Transport}; this global
// only backs the shared generated `client` for callers that invoke
// operations without threading a transport (diagnostics / low-level tests).
let currentSettings: ResolvedSettings = resolveSettings({});

/**
 * `createClientConfig` is invoked by the generated `client.gen.ts` exactly
 * once at module load. We supply the default base URL up-front; per-request
 * behaviour (auth headers, tracing headers, error mapping) is wired via
 * {@link attachInterceptors}, which the module-global client wires lazily on
 * the first call to avoid the circular import that would otherwise block
 * top-level `import { client }` from this module.
 *
 * @param override Optional overrides supplied by the generated layer.
 * @returns A client config with our base URL merged into `override`.
 */
export const createClientConfig: CreateClientConfig = (override) => {
  const merged = {
    baseUrl: currentSettings.baseUrl,
    ...override,
  } as Config;
  return merged as ReturnType<CreateClientConfig>;
};

/**
 * Attach the AxonPush request/error interceptors to a generated client. The
 * request interceptor reads settings through `getSettings` so each client is
 * bound to its owning instance's configuration with no shared mutable slot.
 *
 * @param client The generated client to decorate.
 * @param getSettings Returns the settings that should drive this client.
 */
function attachInterceptors(client: Client, getSettings: () => ResolvedSettings): void {
  client.interceptors.request.use((request) => {
    const s = getSettings();
    if (s.apiKey) {
      // `pt_` public ingest tokens go on X-Public-Token; `ak_` API keys on x-axonpush-api-key.
      const header = s.apiKey.startsWith("pt_") ? "X-Public-Token" : "x-axonpush-api-key";
      request.headers.set(header, s.apiKey);
    }
    if (s.tenantId) request.headers.set("x-tenant-id", s.tenantId);
    if (s.environment) request.headers.set("X-Axonpush-Environment", s.environment);
    const trace = currentTrace();
    if (trace) {
      const spanId = trace.nextSpanId();
      request.headers.set("X-Axonpush-Trace-Id", trace.traceId);
      request.headers.set("X-Axonpush-Span-Id", spanId);
      request.headers.set("traceparent", trace.traceparent(spanId));
      const baggage = [
        s.orgId ? `axonpush.org_id=${encodeURIComponent(s.orgId)}` : undefined,
        s.environment
          ? `deployment.environment.name=${encodeURIComponent(s.environment)}`
          : undefined,
      ].filter(Boolean);
      if (baggage.length > 0) request.headers.set("baggage", baggage.join(","));
    }
    // Fetch strips standard Authorization on cross-origin redirects, but retains
    // our custom credential headers. Surface redirects as terminal responses.
    return new Request(request, { redirect: "manual" });
  });

  client.interceptors.error.use((error, response, _request, _options) => {
    if (error instanceof AxonPushError) return error;
    if (response) {
      let body: unknown;
      if (error && typeof error === "object") {
        body = error;
      } else if (typeof error === "string") {
        try {
          body = JSON.parse(error);
        } catch {
          body = { message: error };
        }
      }
      return fromResponse(response, body);
    }
    const message =
      error instanceof Error ? error.message : typeof error === "string" ? error : "Network error";
    return new APIConnectionError(message);
  });
}

// --- module-global generated client (legacy / low-level callers) ------------

let globalInterceptorsAttached = false;
let globalLastBaseUrl: string | undefined;

async function ensureGlobalInterceptors(): Promise<void> {
  if (globalInterceptorsAttached) return;
  globalInterceptorsAttached = true;
  const { client } = await import("./api/client.gen.js");
  if (!client) {
    globalInterceptorsAttached = false;
    return;
  }
  attachInterceptors(client, () => currentSettings);
}

async function applyGlobalBaseUrlIfChanged(): Promise<void> {
  if (globalLastBaseUrl === currentSettings.baseUrl) return;
  const { client } = await import("./api/client.gen.js");
  if (!client) return;
  client.setConfig({ baseUrl: currentSettings.baseUrl });
  globalLastBaseUrl = currentSettings.baseUrl;
}

/**
 * Update the module-scoped settings used by the shared generated client.
 *
 * Only affects {@link invokeSync} calls that do not thread a {@link Transport}
 * (diagnostics and low-level tests). The {@link AxonPush} facade owns a
 * per-instance {@link Transport} and never mutates this slot, so concurrent
 * clients no longer race over a single global.
 *
 * @param s Resolved settings produced by `resolveSettings`.
 */
export function setSettings(s: ResolvedSettings): void {
  currentSettings = s;
}

/**
 * Read the module-global settings backing the shared generated client.
 * Exposed for diagnostics and tests.
 *
 * @returns The {@link ResolvedSettings} backing the shared client.
 */
export function getSettings(): ResolvedSettings {
  return currentSettings;
}

// --- per-instance transport -------------------------------------------------

/**
 * Owns a generated client whose interceptors are bound to a single
 * {@link AxonPush} instance's settings. Created once per facade so multi-tenant
 * callers (different API keys / base URLs in the same process) never share a
 * mutable settings slot.
 */
export class Transport {
  private readonly settings: ResolvedSettings;
  private readonly client: Client;

  constructor(settings: ResolvedSettings) {
    this.settings = settings;
    this.client = createClient({ baseUrl: settings.baseUrl });
    attachInterceptors(this.client, () => this.settings);
  }

  /**
   * Run a generated operation against this instance's client with retries and
   * fail-open handling. See {@link invokeSync} for the retry semantics.
   */
  invoke<T>(
    op: GeneratedOp<T>,
    args?: unknown,
    opts: { failOpen?: boolean; maxRetries?: number } = {},
  ): Promise<T | null> {
    return runOp(op, args, {
      failOpen: opts.failOpen ?? this.settings.failOpen,
      maxRetries: opts.maxRetries ?? this.settings.maxRetries,
      client: this.client,
      timeout: this.settings.timeout,
    });
  }
}

/**
 * Generated operation function signature. `args` is the per-op options bag
 * baked into `sdk.gen.ts`; `T` is the success-response payload type. We
 * type `args` as `any` because the generator emits a distinct argument
 * type per op, and the chokepoint relies on shape-compatibility, not nominal
 * equality.
 */
export type GeneratedOp<T = unknown> = (args: any) => Promise<{ data?: T; [k: string]: unknown }>;

export const RETRY_BACKOFF_MS = [250, 500, 1000, 2000, 4000] as const;

async function runOp<T>(
  op: GeneratedOp<T>,
  args: unknown,
  opts: { failOpen: boolean; maxRetries: number; client?: Client; timeout: number },
): Promise<T | null> {
  if (!Number.isInteger(opts.maxRetries) || opts.maxRetries < 0)
    throw new RangeError("maxRetries must be a nonnegative integer");
  const baseArgs: Record<string, unknown> = {
    ...((args ?? {}) as Record<string, unknown>),
    ...(opts.client ? { client: opts.client } : {}),
  };
  let retrySafe = false;
  const previousValidator = baseArgs.requestValidator as
    | ((request: Record<string, unknown>) => Promise<void>)
    | undefined;
  baseArgs.requestValidator = async (request: Record<string, unknown>) => {
    if (previousValidator) await previousValidator(request);
    const method = String(request.method).toUpperCase();
    const path = String(request.url).split("?")[0] ?? "";
    const body = request.body as
      | { dedupKey?: string; observations?: { source_event_id?: string }[] }
      | undefined;
    retrySafe =
      method === "GET" ||
      method === "HEAD" ||
      (method === "POST" &&
        ((path === "/event" && typeof body?.dedupKey === "string" && body.dedupKey.length > 0) ||
          (/^\/workspaces\/[^/]+\/observations$/.test(path) &&
            Array.isArray(body?.observations) &&
            body.observations.every(
              (item) => typeof item.source_event_id === "string" && item.source_event_id.length > 0,
            ))));
  };
  const callerSignal = baseArgs.signal as AbortSignal | undefined;
  const budget = AbortSignal.timeout(Math.ceil(opts.timeout));
  const signal = callerSignal ? AbortSignal.any([callerSignal, budget]) : budget;
  try {
    return await pRetry(
      async () => {
        signal.throwIfAborted();
        const attemptSignal = AbortSignal.any([
          signal,
          AbortSignal.timeout(Math.ceil(opts.timeout)),
        ]);
        try {
          const result = await op({ ...baseArgs, signal: attemptSignal, throwOnError: true });
          attemptSignal.throwIfAborted();
          return result.data ?? null;
        } catch (error) {
          signal.throwIfAborted();
          if (attemptSignal.aborted) throw new APIConnectionError("AxonPush request timed out");
          throw error;
        }
      },
      {
        retries: opts.maxRetries,
        minTimeout: 250,
        maxTimeout: 4000,
        factor: 2,
        randomize: true,
        signal,
        shouldRetry: ({ error }) => retrySafe && isRetryable(error),
        onFailedAttempt: async ({ error, retriesLeft }) => {
          if (
            retrySafe &&
            retriesLeft > 0 &&
            error instanceof RateLimitError &&
            error.retryAfter !== undefined
          ) {
            const extra = Math.max(0, error.retryAfter * 1000);
            if (extra > 0) await delay(Math.min(extra, 2147483647), undefined, { signal });
          }
        },
      },
    );
  } catch (error) {
    if (callerSignal?.aborted) throw callerSignal.reason;
    const failure = budget.aborted
      ? new APIConnectionError("AxonPush retry budget exhausted")
      : error;
    if (opts.failOpen && failure instanceof APIConnectionError) return null;
    throw failure;
  }
}

/**
 * Single chokepoint against the shared generated client. Adds:
 *
 * - Retries eligible reads and deduplicated writes with jittered backoff,
 *   honouring {@link RateLimitError.retryAfter} within the invocation deadline.
 * - Fail-open semantics: when `opts.failOpen` is true and the final attempt
 *   ends in {@link APIConnectionError}, return `null` instead of throwing.
 * - Exception passthrough for all other errors.
 *
 * Prefer {@link Transport.invoke} for per-instance settings; this entry point
 * uses the module-global settings and exists for diagnostics and tests.
 *
 * @typeParam T Success-response type returned by the generated op.
 * @param op A function from `src/_internal/api/sdk.gen.ts`.
 * @param args Options bag forwarded to `op` after `throwOnError: true` is set.
 * @param opts Per-call retry / fail-open overrides.
 * @returns The unwrapped `data` field of the response, or `null` when
 *   `failOpen` swallowed an {@link APIConnectionError}.
 * @throws {AxonPushError} On non-retryable failures or when retries are
 *   exhausted and `failOpen` is false.
 */
export async function invokeSync<T>(
  op: GeneratedOp<T>,
  args: unknown,
  opts: { failOpen?: boolean; maxRetries?: number } = {},
): Promise<T | null> {
  await ensureGlobalInterceptors();
  await applyGlobalBaseUrlIfChanged();
  return runOp(op, args, {
    failOpen: opts.failOpen ?? currentSettings.failOpen,
    maxRetries: opts.maxRetries ?? currentSettings.maxRetries,
    timeout: currentSettings.timeout,
  });
}
