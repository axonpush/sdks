/**
 * Sentry SDK integration helper.
 *
 * Builds a Sentry DSN for the AxonPush Sentry ingest
 * (`/api/:projectId/envelope/` and `/api/:projectId/store/`) and forwards to
 * `Sentry.init(...)`. Usable with `@sentry/node`, `@sentry/browser`,
 * `@sentry/nextjs`, etc.
 *
 * The DSN key must be a channel-scoped public ingest token (`pt_...`); the
 * server resolves the org, channel and environment from it and refuses API
 * keys. Sentry SDKs require an integer project id, so the project segment is a
 * placeholder derived from the channel id (the same derivation the dashboard
 * uses) and is not used for routing.
 *
 * Usage (Node):
 *   import * as Sentry from "@sentry/node";
 *   import { installSentry } from "@axonpush/sdk/integrations/sentry";
 *   installSentry(Sentry, {
 *     publicToken: process.env.AXONPUSH_PUBLIC_TOKEN!,
 *     channelId: "ch-uuid",
 *     environment: "production",
 *     release: process.env.RELEASE,
 *   });
 */

import { logger } from "../logger.js";
import type { ChannelIdInput } from "./_base.js";

const ENV_PRECEDENCE = [
  "AXONPUSH_ENVIRONMENT",
  "SENTRY_ENVIRONMENT",
  "NODE_ENV",
  "APP_ENV",
  "ENV",
] as const;

function detectEnvironment(): string | undefined {
  if (typeof process === "undefined" || !process.env) return undefined;
  for (const name of ENV_PRECEDENCE) {
    const v = process.env[name];
    if (v && v.length > 0) return v;
  }
  return undefined;
}

function readEnv(name: string): string | undefined {
  if (typeof process === "undefined" || !process.env) return undefined;
  return process.env[name] || undefined;
}

export interface InstallSentryOptions {
  /** Channel-scoped public ingest token (`pt_...`). Falls back to `AXONPUSH_PUBLIC_TOKEN`. */
  publicToken?: string;
  /** Only used to derive the integer project id placeholder. Falls back to `AXONPUSH_CHANNEL_ID`. */
  channelId?: ChannelIdInput;
  host?: string;
  /** Fully-formed DSN (as shown in the dashboard). Overrides the other AxonPush options. */
  dsn?: string;
  environment?: string;
  release?: string;
  [key: string]: unknown;
}

export interface SentryLike {
  init: (options: Record<string, unknown>) => unknown;
}

export function sentryProjectId(channelId: ChannelIdInput | undefined): number {
  if (channelId === undefined) return 1;
  const hex = String(channelId).replace(/-/g, "").slice(0, 8);
  return Number.parseInt(hex, 16) || 1;
}

function requirePublicToken(token: string): void {
  if (!token.startsWith("pt_")) {
    throw new Error(
      "Sentry ingest needs a channel-scoped public ingest token (pt_...), not an API key. " +
        "Mint one in the dashboard or via /public-ingest-tokens.",
    );
  }
}

export function buildDsn(
  publicToken: string,
  channelId: ChannelIdInput | undefined,
  host: string,
): string {
  requirePublicToken(publicToken);
  const scheme = host.startsWith("localhost") || host.startsWith("127.") ? "http" : "https";
  return `${scheme}://${publicToken}@${host}/${sentryProjectId(channelId)}`;
}

export function installSentry(sentry: SentryLike, options: InstallSentryOptions = {}): void {
  if ("apiKey" in options) {
    throw new Error(
      "installSentry no longer accepts apiKey: Sentry ingest refuses API keys. " +
        "Pass publicToken: 'pt_...' or the dsn shown in the dashboard.",
    );
  }
  let dsn = options.dsn;
  if (!dsn) {
    const publicToken = options.publicToken ?? readEnv("AXONPUSH_PUBLIC_TOKEN");
    const channelId = options.channelId ?? readEnv("AXONPUSH_CHANNEL_ID");
    const host = options.host ?? readEnv("AXONPUSH_HOST") ?? "api.axonpush.xyz";
    if (!publicToken) {
      throw new Error(
        "installSentry needs a publicToken (pt_...) or a fully-formed dsn. " +
          "Pass one in options or set AXONPUSH_PUBLIC_TOKEN.",
      );
    }
    dsn = buildDsn(publicToken, channelId, host);
  }

  const resolvedEnv = options.environment ?? detectEnvironment();
  logger.debug(
    `installSentry: dsn host=${dsn.split("@")[1] ?? dsn} environment=${resolvedEnv ?? "<none>"} release=${options.release ?? "<none>"}`,
  );

  const {
    publicToken: _p,
    channelId: _c,
    host: _h,
    dsn: _d,
    environment: _e,
    release: _r,
    ...extraInitOptions
  } = options;
  void _p;
  void _c;
  void _h;
  void _d;
  void _e;
  void _r;

  const initOptions: Record<string, unknown> = {
    dsn,
    ...extraInitOptions,
  };
  if (resolvedEnv !== undefined && !("environment" in initOptions)) {
    initOptions.environment = resolvedEnv;
  }
  if (options.release !== undefined && !("release" in initOptions)) {
    initOptions.release = options.release;
  }

  sentry.init(initOptions);
}
