import { randomUUID } from "node:crypto";
import type {
  ActivityIngestReport,
  ActivityObservation,
  IdentifyOutputBody,
} from "./_internal/api/types.gen.js";
import { currentTrace } from "./tracing.js";

/** Largest batch the observations endpoint accepts in one request. */
export const MAX_OBSERVATION_BATCH = 100;

/**
 * One observation for {@link AxonPush.observe}. Only `event` is required;
 * attribute keys must be declared in the workspace's data dictionary or the
 * server drops and counts them.
 */
export interface ObserveParams {
  event: string;
  /** Entity type to opaque identifier, e.g. `{ ticket: "t_42", agent: "a_7" }`. */
  refs?: Record<string, string>;
  attributes?: Record<string, unknown>;
  /** Defaults to now. */
  occurredAt?: string | Date;
  /** Idempotency key; defaults to a random UUID. Reuse it when retrying the same fact. */
  sourceEventId?: string;
  /** Defaults to the bound trace context, when there is one. */
  traceId?: string;
  spanId?: string;
  /** Defaults to the client's configured environment. */
  environment?: string;
  /** Marks reconstructed state rather than live activity. */
  snapshot?: boolean;
  source?: { ref?: string; revision?: number };
}

/**
 * Profile traits for one entity. Keys must be listed in the entity's
 * `profile`; a `null` value deletes that trait.
 */
export interface IdentifyParams {
  entity: string;
  id: string;
  traits: Record<string, unknown>;
}

export type ObserveReport = ActivityIngestReport;
export type IdentifyReport = IdentifyOutputBody;

export function buildObservation(
  params: ObserveParams,
  defaults: { environment?: string; redact?: <T>(value: T) => T } = {},
): ActivityObservation {
  const trace = currentTrace();
  const occurredAt =
    params.occurredAt instanceof Date
      ? params.occurredAt.toISOString()
      : (params.occurredAt ?? new Date().toISOString());
  const traceId = params.traceId ?? trace?.w3cTraceId();
  const environment = params.environment ?? defaults.environment;
  const attributes = params.attributes ?? {};
  return {
    schema_version: 1,
    source_event_id: params.sourceEventId ?? randomUUID(),
    event: params.event,
    occurred_at: occurredAt,
    refs: params.refs ?? {},
    attributes: defaults.redact ? defaults.redact(attributes) : attributes,
    ...(environment !== undefined ? { environment } : {}),
    ...(traceId !== undefined ? { trace_id: traceId } : {}),
    ...(params.spanId !== undefined ? { span_id: params.spanId } : {}),
    ...(params.snapshot !== undefined ? { snapshot: params.snapshot } : {}),
    ...(params.source !== undefined ? { source: params.source } : {}),
  };
}

export function mergeReports(reports: ActivityIngestReport[]): ActivityIngestReport {
  const dropped = new Set<string>();
  let dropCount = 0;
  const receipts: NonNullable<ActivityIngestReport["receipts"]> = [];
  for (const report of reports) {
    receipts.push(...(report.receipts ?? []));
    for (const key of report.dropped ?? []) dropped.add(key);
    dropCount += report.dropCount ?? 0;
  }
  return { receipts, dropped: [...dropped], dropCount };
}
