/**
 * Public model aliases over the auto-generated `_internal/api/types.gen.ts`.
 *
 * Importers should use these names rather than reaching into the
 * private `_internal` package directly. Names are stable across the
 * public API; field changes still flow through codegen.
 *
 * The Go/Huma contract exposes DTO models (`AppDto`, `ChannelDto`, ...)
 * and envelope bodies (`ListEnvironmentsOutputBody`, ...). We re-export the
 * DTOs under ergonomic names and keep the envelope types available for
 * callers that want the raw wrapper.
 */

export type {
  AppDto as App,
  ChannelDto as Channel,
  // Webhook shapes.
  DeliveryDto as WebhookDelivery,
  EndpointDto as WebhookEndpoint,
  EnvironmentDto as Environment,
  EventBody,
  // Event resource shapes.
  EventDto as EventDetails,
  EventOutputBody as Event,
  ListEnvironmentsOutputBody,
  OrganizationDto as Organization,
  SearchEventsOutputBody,
  TraceSummaryDto as TraceSummary,
  UserOrgDto as UserOrg,
  UserOrgsOutputBody,
} from "./_internal/api/types.gen.js";

/**
 * Canonical event-type discriminators accepted by
 * {@link EventsResource.publish}. The Go backend no longer publishes a
 * closed enum for this field (it is a free-form string, defaulting to
 * `"custom"`), so we surface a small set of well-known members for editor
 * autocomplete while widening to `string` via the `string & {}` no-op
 * intersection.
 */
export type CanonicalEventType =
  | "custom"
  | "app.log"
  | "agent.handoff"
  | "agent.tool_call.start"
  | "agent.tool_call.end"
  | "llm.call.start"
  | "llm.call.end";

/** Event type accepted by publish — canonical members plus any string. */
export type EventType = CanonicalEventType | (string & {});
