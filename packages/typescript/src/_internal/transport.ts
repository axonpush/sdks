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
    if (s.apiKey) request.headers.set("X-API-Key", s.apiKey);
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
    return request;
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
// biome-ignore lint/suspicious/noExplicitAny: see doc comment above.
export type GeneratedOp<T = unknown> = (args: any) => Promise<{ data?: T; [k: string]: unknown }>;

export const RETRY_BACKOFF_MS = [250, 500, 1000, 2000, 4000] as const;

function delayFor(attempt: number, retryAfter?: number): number {
  if (retryAfter !== undefined) return Math.max(0, retryAfter * 1000);
  const idx = Math.min(attempt, RETRY_BACKOFF_MS.length - 1);
  return RETRY_BACKOFF_MS[idx] ?? RETRY_BACKOFF_MS[RETRY_BACKOFF_MS.length - 1] ?? 0;
}

const sleep = (ms: number): Promise<void> =>
  ms > 0 ? new Promise((resolve) => setTimeout(resolve, ms)) : Promise.resolve();

/**
 * Core retry loop shared by {@link Transport.invoke} and {@link invokeSync}.
 * When `client` is set, each op call is routed to that client (per-instance
 * interceptors); otherwise it falls back to the generated global client.
 */
async function runOp<T>(
  op: GeneratedOp<T>,
  args: unknown,
  opts: { failOpen: boolean; maxRetries: number; client?: Client },
): Promise<T | null> {
  const baseArgs = (args ?? {}) as Record<string, unknown>;
  if (opts.client) baseArgs.client = opts.client;
  let lastErr: unknown;

  for (let attempt = 0; attempt <= opts.maxRetries; attempt++) {
    try {
      const result = await op({ ...baseArgs, throwOnError: true });
      return result.data ?? null;
    } catch (err) {
      lastErr = err;
      if (!isRetryable(err) || attempt === opts.maxRetries) break;
      const retryAfter = err instanceof RateLimitError ? err.retryAfter : undefined;
      await sleep(delayFor(attempt, retryAfter));
    }
  }

  if (opts.failOpen && lastErr instanceof APIConnectionError) return null;
  throw lastErr;
}

/**
 * Single chokepoint against the shared generated client. Adds:
 *
 * - Retries on retryable errors with backoff `[250, 500, 1000, 2000, 4000]ms`,
 *   honouring {@link RateLimitError.retryAfter} when present.
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
  });
}
