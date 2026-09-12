import { type GeneratedOp, Transport } from "./_internal/transport.js";
import { type AxonPushOptions, type ResolvedSettings, resolveSettings } from "./config.js";
import type { RealtimeClient, RealtimeOptions } from "./realtime/index.js";
import { redactTelemetry as applyTelemetryRedaction } from "./redaction.js";
import { AlertsResource } from "./resources/alerts.js";
import { AnalyticsResource } from "./resources/analytics.js";
import { ApiKeysResource } from "./resources/api-keys.js";
import { AppsResource } from "./resources/apps.js";
import { ChannelsResource } from "./resources/channels.js";
import { EnvironmentsResource } from "./resources/environments.js";
import { EventsResource } from "./resources/events.js";
import { OrganizationsResource } from "./resources/organizations.js";
import { TracesV2Resource } from "./resources/traces-v2.js";
import { WebhooksResource } from "./resources/webhooks.js";
import { getOrCreateTrace, type TraceContext } from "./tracing.js";

/**
 * High-level facade over the AxonPush REST + realtime APIs.
 *
 * Resource accessors (`events`, `channels`, ...) are constructed once
 * per `AxonPush` instance and exposed as plain properties so callers can
 * write `client.events.publish(...)` without awaiting.
 */
export class AxonPush {
  /** Fully-resolved configuration, materialised in the constructor. */
  readonly settings: ResolvedSettings;

  /** Per-instance transport; carries this facade's settings, no shared slot. */
  private readonly transport: Transport;

  /** Events resource — `publish`, `list`, `search`. */
  readonly events: EventsResource;
  /** Channels resource — `create`, `get`, `update`, `delete`. */
  readonly channels: ChannelsResource;
  /** Apps resource — `list`, `get`, `create`, `update`, `delete`. */
  readonly apps: AppsResource;
  /** Environments resource — `list`, `create`, `update`, `delete`, `promoteToDefault`. */
  readonly environments: EnvironmentsResource;
  /** Webhooks resource — `createEndpoint`, `listEndpoints`, `deleteEndpoint`, `deliveries`. */
  readonly webhooks: WebhooksResource;
  /** API keys resource — `create`, `list`, `delete`. */
  readonly apiKeys: ApiKeysResource;
  /** Organizations resource — `create`, `get`, `list`, `update`, `delete`, `invite`, `removeMember`, `transferOwnership`. */
  readonly organizations: OrganizationsResource;
  /** Alert rules over metric thresholds. */
  readonly alerts: AlertsResource;
  /** Timeseries, breakdowns and comparisons. */
  readonly analytics: AnalyticsResource;
  /** Trace search with facets and spans. */
  readonly tracesV2: TracesV2Resource;

  /**
   * @param options Optional caller overrides; falsy fields fall through to
   *   `AXONPUSH_*` env vars and then documented defaults.
   */
  constructor(options?: AxonPushOptions) {
    this.settings = resolveSettings(options);
    this.transport = new Transport(this.settings);
    this.events = new EventsResource(this);
    this.channels = new ChannelsResource(this);
    this.apps = new AppsResource(this);
    this.environments = new EnvironmentsResource(this);
    this.webhooks = new WebhooksResource(this);
    this.apiKeys = new ApiKeysResource(this);
    this.organizations = new OrganizationsResource(this);
    this.alerts = new AlertsResource(this);
    this.analytics = new AnalyticsResource(this);
    this.tracesV2 = new TracesV2Resource(this);
  }

  /** The configured environment label (or `undefined` if none). */
  get environment(): string | undefined {
    return this.settings.environment;
  }

  /** Apply client-side secret/content policy before telemetry leaves the process. */
  redactTelemetry<T>(value: T): T {
    return applyTelemetryRedaction(value, this.settings);
  }

  /**
   * Open a realtime (MQTT-over-WSS) connection. The realtime module is
   * imported lazily so callers that never use realtime do not pay for the
   * `mqtt` peer dependency at module-load time.
   *
   * @param opts Realtime client options (forwarded as the second arg).
   * @returns A `RealtimeClient` instance ready to subscribe / publish.
   */
  async connectRealtime(opts?: RealtimeOptions): Promise<RealtimeClient> {
    const { RealtimeClient: Ctor } = await import("./realtime/index.js");
    return new Ctor(this, opts);
  }

  /**
   * Run a generated SDK operation through the transport chokepoint.
   *
   * @typeParam T Success-response type returned by `op`.
   * @param op A function from `src/_internal/api/sdk.gen.ts`.
   * @param args Options bag forwarded to `op`.
   * @returns The unwrapped response data, or `null` if `failOpen` swallowed
   *   an `APIConnectionError`.
   * @throws {AxonPushError} On non-retryable failures.
   */
  invoke<T>(op: GeneratedOp<T>, args?: unknown): Promise<T | null> {
    return this.transport.invoke<T>(op, args);
  }

  /**
   * Return the active {@link TraceContext} or create a fresh one.
   *
   * @param seedTraceId Optional pre-existing trace id to adopt.
   * @returns The trace context for the current async flow.
   */
  getOrCreateTrace(seedTraceId?: string): TraceContext {
    return getOrCreateTrace(seedTraceId);
  }

  /**
   * Idempotent teardown hook. Currently a no-op; reserved for releasing
   * realtime connections, flushing publishers, etc. once those are owned by
   * the facade.
   */
  close(): void {
    /* noop */
  }
}

export type { AxonPushOptions } from "./config.js";
