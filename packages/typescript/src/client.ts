import { type GeneratedOp, Transport } from "./_internal/transport.js";
import { type AxonPushOptions, type ResolvedSettings, resolveSettings } from "./config.js";
import {
  buildObservation,
  type IdentifyParams,
  type IdentifyReport,
  MAX_OBSERVATION_BATCH,
  mergeReports,
  type ObserveParams,
  type ObserveReport,
} from "./observe.js";
import { redactTelemetry as applyTelemetryRedaction } from "./redaction.js";
import { ActivityResource } from "./resources/activity.js";
import { AlertsResource } from "./resources/alerts.js";
import { AnalyticsResource } from "./resources/analytics.js";
import { AppsResource } from "./resources/apps.js";
import { CapabilitiesResource } from "./resources/capabilities.js";
import { ChannelsResource } from "./resources/channels.js";
import { EnvironmentsResource } from "./resources/environments.js";
import { ErrorsResource } from "./resources/errors.js";
import { EventsResource } from "./resources/events.js";
import { ObservationsResource } from "./resources/observations.js";
import { OrganizationsResource } from "./resources/organizations.js";
import { TemplatesResource } from "./resources/templates.js";
import { TracesResource } from "./resources/traces.js";
import { WebhooksResource } from "./resources/webhooks.js";
import { WorkspacesResource } from "./resources/workspaces.js";
import { getOrCreateTrace, type TraceContext } from "./tracing.js";

/**
 * High-level facade over the AxonPush REST API.
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

  readonly workspaces: WorkspacesResource;
  readonly templates: TemplatesResource;
  readonly observations: ObservationsResource;
  readonly activity: ActivityResource;
  /** Events resource — `publish`, `search`. */
  readonly events: EventsResource;
  /** Channels resource — `list`, `get`, `create`, `update`, `delete`. */
  readonly channels: ChannelsResource;
  /** Apps resource — `list`, `get`, `create`, `update`, `delete`. */
  readonly apps: AppsResource;
  /** Environments resource — `list`, `create`, `update`, `delete`, `promoteToDefault`. */
  readonly environments: EnvironmentsResource;
  /** Webhooks resource — `createEndpoint`, `listEndpoints`, `deleteEndpoint`, `deliveries`. */
  readonly webhooks: WebhooksResource;
  /** Organizations resource — `get`, `list`, `update`, `delete`, `invite`, `cancelInvitation`, `removeMember`, `transferOwnership`. */
  readonly organizations: OrganizationsResource;
  /** Alert rules over metric thresholds. */
  readonly alerts: AlertsResource;
  /** Timeseries and dimension breakdowns. */
  readonly analytics: AnalyticsResource;
  /** Traces — `list`, `get`. */
  readonly traces: TracesResource;
  /**
   * Back-compat alias for {@link AxonPush.traces}.
   * @deprecated Use `client.traces`.
   */
  readonly tracesV2: TracesResource;
  /** Error issues — `list`, `get`, `events`, `triage`. */
  readonly errors: ErrorsResource;
  /** Server capabilities — version, feature flags, license, scopes. */
  readonly capabilities: CapabilitiesResource;

  /**
   * @param options Optional caller overrides; falsy fields fall through to
   *   `AXONPUSH_*` env vars and then documented defaults.
   */
  constructor(options?: AxonPushOptions) {
    this.settings = resolveSettings(options);
    this.transport = new Transport(this.settings);
    this.workspaces = new WorkspacesResource(this);
    this.templates = new TemplatesResource(this);
    this.observations = new ObservationsResource(this);
    this.activity = new ActivityResource(this);
    this.events = new EventsResource(this);
    this.channels = new ChannelsResource(this);
    this.apps = new AppsResource(this);
    this.environments = new EnvironmentsResource(this);
    this.webhooks = new WebhooksResource(this);
    this.organizations = new OrganizationsResource(this);
    this.alerts = new AlertsResource(this);
    this.analytics = new AnalyticsResource(this);
    this.traces = new TracesResource(this);
    this.tracesV2 = this.traces;
    this.errors = new ErrorsResource(this);
    this.capabilities = new CapabilitiesResource(this);
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
   * Send one or more observations to a workspace. Builds the core envelope
   * (schema version, a UUID `source_event_id` and an ISO `occurred_at` when
   * absent, the bound trace id when there is one). Arrays are sent in batches
   * of {@link MAX_OBSERVATION_BATCH}. Nothing is sent unless this is called.
   *
   * @returns Receipts plus any undeclared attribute keys the server dropped,
   *   or `null` when fail-open swallowed a connection error.
   */
  async observe(
    workspaceId: string,
    observations: ObserveParams | ObserveParams[],
  ): Promise<ObserveReport | null> {
    const list = (Array.isArray(observations) ? observations : [observations]).map((params) =>
      buildObservation(params, {
        environment: this.settings.environment,
        redact: (value) => this.redactTelemetry(value),
      }),
    );
    const reports: ObserveReport[] = [];
    for (let i = 0; i < list.length; i += MAX_OBSERVATION_BATCH) {
      const report = await this.observations.accept(workspaceId, {
        observations: list.slice(i, i + MAX_OBSERVATION_BATCH),
      });
      if (report) reports.push(report);
    }
    if (reports.length === 0) return null;
    return reports.length === 1 ? (reports[0] ?? null) : mergeReports(reports);
  }

  /**
   * Attach profile traits (names, plans, anything declared in the entity's
   * `profile`) to an entity. Traits merge; a `null` value deletes a trait.
   * Undeclared keys come back in `dropped`.
   */
  async identify(workspaceId: string, params: IdentifyParams): Promise<IdentifyReport | null> {
    return this.activity.identify(workspaceId, {
      entity: params.entity,
      id: params.id,
      traits: this.redactTelemetry(params.traits),
    });
  }

  /**
   * Same as {@link AxonPush.identify}; reads better for organisation-like
   * entities such as `company` or `team`.
   */
  async group(workspaceId: string, params: IdentifyParams): Promise<IdentifyReport | null> {
    return this.identify(workspaceId, params);
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
   * Idempotent teardown hook. Currently a no-op; reserved for flushing
   * publishers, etc. once those are owned by the facade.
   */
  close(): void {
    /* noop */
  }
}

export type { AxonPushOptions } from "./config.js";
