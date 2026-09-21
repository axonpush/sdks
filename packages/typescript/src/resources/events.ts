import { createEvent, eventsSearch } from "../_internal/api/sdk.gen.js";
import type { EventBody, EventsSearchData } from "../_internal/api/types.gen.js";
import type { Event, EventDetails, EventType, SearchEventsOutputBody } from "../models.js";
import type { ResourceClient } from "./_client.js";

/** Parameters accepted by {@link EventsResource.publish}. */
export interface PublishParams {
  /** Stable, caller-supplied identifier — used for dedupe. */
  identifier: string;
  /** Free-form JSON body. */
  payload: Record<string, unknown>;
  /** Channel UUID this event belongs to. */
  channelId: string;
  /** Logical agent that produced this event. */
  agentId?: string;
  /** Trace UUID to attach this event to. Auto-generated when omitted. */
  traceId?: string;
  /** Span ID. Auto-generated from the trace context when omitted. */
  spanId?: string;
  /** Parent W3C span ID for hierarchy reconstruction. */
  parentSpanId?: string;
  /**
   * Parent event ID — used to model hand-offs. Emitted into `metadata` as
   * `axonpush.parent_event_id` since the ingest body no longer has a
   * dedicated field for it.
   */
  parentEventId?: string;
  /** Discriminator. Defaults to `"custom"` when omitted. */
  eventType?: EventType;
  /** Free-form metadata. */
  metadata?: Record<string, unknown>;
  /** Immutable prompt identifier, emitted as `gen_ai.prompt.id`. */
  promptId?: string;
  /** Immutable prompt version, emitted as `gen_ai.prompt.version`. */
  promptVersionId?: string;
  /**
   * Environment slug override. Only honoured when the API key has
   * `allowEnvironmentOverride=true`. Falls through to the client's
   * default environment when omitted. Sent via the `X-Axonpush-Environment`
   * request header by the transport, not the body.
   */
  environment?: string;
  /**
   * Idempotency key. Duplicate events sharing a `dedupKey` are collapsed.
   */
  dedupKey?: string;
  /**
   * Ignored by the backend — ingest is always asynchronous. Kept for
   * back-compat with callers that still pass it.
   */
  sync?: boolean;
}

/** Search filters (cross-channel). `GET /events` */
export interface EventSearchParams {
  /** Max events to return (default 50, max 500). */
  limit?: number;
  /** ISO 8601 / RFC3339 window end (defaults to now). */
  until?: string;
  /** ISO 8601 / RFC3339 window start (defaults to 24h before `until`). */
  since?: string;
  traceId?: string;
  /** Filter by a single event type. */
  eventType?: string;
  appId?: string;
  channelId?: string;
  environmentId?: string;
  source?: string;
  status?: string;
  /** Filter by agent id (tool-call / handoff spans carry one). */
  agentId?: string;
  /** Filter by agent name. */
  agentName?: string;
  /** Filter by tool name (`gen_ai.tool.name`). */
  toolName?: string;
  /** Filter by semantic kind (`agent`, `tool`, `llm`, `retriever`, `db`, `http`, `log`). */
  semanticKind?: string;
  /** Case-insensitive contains match on search text. */
  q?: string;
  /** JSONB attribute key for equality filter (paired with `attrValue`). */
  attrKey?: string;
  /** JSONB attribute value for equality filter (paired with `attrKey`). */
  attrValue?: string;
}

/**
 * Publish and search events.
 *
 * Resources never throw on transport errors when the client was
 * constructed with `failOpen=true` (the default). Callers receive
 * `null` instead.
 */
export class EventsResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * Publish a single event to a channel. `POST /event`
   *
   * @param params - Event parameters; see {@link PublishParams}.
   * @returns The event ingest ack, or `null` when fail_open swallowed a transport error.
   * @throws {AxonPushError} when fail_open is false and the call fails.
   */
  async publish(params: PublishParams): Promise<Event | null> {
    const trace = this.client.getOrCreateTrace(params.traceId);

    const hasMeta =
      params.metadata !== undefined ||
      params.promptId !== undefined ||
      params.promptVersionId !== undefined ||
      params.parentEventId !== undefined;
    const rawMeta = hasMeta
      ? {
          ...(params.metadata ?? {}),
          ...(params.promptId === undefined ? {} : { "gen_ai.prompt.id": params.promptId }),
          ...(params.promptVersionId === undefined
            ? {}
            : { "gen_ai.prompt.version": params.promptVersionId }),
          ...(params.parentEventId === undefined
            ? {}
            : { "axonpush.parent_event_id": params.parentEventId }),
        }
      : undefined;

    const body: EventBody = {
      identifier: params.identifier,
      payload: this.client.redactTelemetry?.(params.payload) ?? params.payload,
      channel_id: params.channelId,
      traceId: trace.traceId,
      spanId: params.spanId ?? trace.nextSpanId(),
      eventType: params.eventType ?? "custom",
      sync: params.sync ?? false,
      ...(params.agentId !== undefined ? { agentId: params.agentId } : {}),
      ...(params.parentSpanId !== undefined ? { parentSpanId: params.parentSpanId } : {}),
      ...(params.dedupKey !== undefined ? { dedupKey: params.dedupKey } : {}),
      ...(rawMeta !== undefined
        ? { metadata: this.client.redactTelemetry?.(rawMeta) ?? rawMeta }
        : {}),
    };
    return this.client.invoke(createEvent, { body });
  }

  /**
   * Search events across channels using server-side filters. `GET /events`
   *
   * @param params - Optional pagination & filter parameters.
   * @returns Search response envelope, or `null` on fail-open error.
   */
  async search(params: EventSearchParams = {}): Promise<SearchEventsOutputBody | null> {
    return this.client.invoke(eventsSearch, { query: this.buildSearchQuery(params) });
  }

  private buildSearchQuery(p: EventSearchParams): EventsSearchData["query"] {
    return {
      ...(p.since !== undefined ? { since: p.since } : {}),
      ...(p.until !== undefined ? { until: p.until } : {}),
      ...(p.limit !== undefined ? { limit: p.limit } : {}),
      ...(p.appId !== undefined ? { appId: p.appId } : {}),
      ...(p.channelId !== undefined ? { channelId: p.channelId } : {}),
      ...(p.environmentId !== undefined ? { environmentId: p.environmentId } : {}),
      ...(p.eventType !== undefined ? { eventType: p.eventType } : {}),
      ...(p.source !== undefined ? { source: p.source } : {}),
      ...(p.status !== undefined ? { status: p.status } : {}),
      ...(p.traceId !== undefined ? { traceId: p.traceId } : {}),
      ...(p.agentId !== undefined ? { agentId: p.agentId } : {}),
      ...(p.agentName !== undefined ? { agentName: p.agentName } : {}),
      ...(p.toolName !== undefined ? { toolName: p.toolName } : {}),
      ...(p.semanticKind !== undefined ? { semanticKind: p.semanticKind } : {}),
      ...(p.q !== undefined ? { q: p.q } : {}),
      ...(p.attrKey !== undefined ? { attrKey: p.attrKey } : {}),
      ...(p.attrValue !== undefined ? { attrValue: p.attrValue } : {}),
    };
  }
}

export type { EventDetails };
