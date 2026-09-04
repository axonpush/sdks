/**
 * AxonPush — real-time event infrastructure for AI agent systems.
 *
 * Top-level package. Public API is re-exported here; internal helpers
 * live under `./_internal` and are not part of the supported surface.
 */

// Core (Stream A)
export { AxonPush } from "./client.js";
export type { AxonPushOptions } from "./config.js";
export {
  APIConnectionError,
  AuthenticationError,
  AxonPushError,
  ForbiddenError,
  NotFoundError,
  RateLimitError,
  RetryableError,
  ServerError,
  ValidationError,
} from "./errors.js";
export type {
  CreateExperimentOptions,
  DatasetItem,
  EvaluationApi,
  EvaluationItemResult,
  EvaluationRunResult,
  GateResult,
  GateThresholds,
  GitLineage,
  LocalEvaluationInput,
  LocalEvaluationOutput,
  LocalRunnerOptions,
} from "./evaluation/index.js";
// Evaluation runner — customer code remains local and communicates through JSONL.
export {
  captureGitLineage,
  EvaluationApiError,
  EXIT_CODES,
  HttpEvaluationApi,
  runLocalEvaluation,
  toGitHubSummary,
  toJsonReport,
  toJUnitXml,
} from "./evaluation/index.js";
// Integrations — primitives + helpers (Stream D).
// Framework-specific installers are reachable via
// `@axonpush/sdk/integrations/<name>` per package.json `exports`.
export {
  type ChannelIdInput,
  coerceChannelId,
  type IntegrationConfig,
  safePublish,
  truncate,
} from "./integrations/_base.js";
export {
  BullMQPublisher,
  type BullMQPublisherOptions,
  type BullMQWorkerOptions,
  createBullMQWorker,
} from "./integrations/_bullmq_publisher.js";
export {
  BackgroundPublisher,
  type BackgroundPublisherOptions,
  DEFAULT_QUEUE_SIZE,
  DEFAULT_SHUTDOWN_TIMEOUT_MS,
  detectServerless,
  type Flushable,
  flushAfterInvocation,
  type OverflowPolicy,
  type PublisherMode,
} from "./integrations/_publisher.js";
export { AxonPushAnthropicTracer } from "./integrations/anthropic.js";
export {
  type ConsoleCaptureConfig,
  type ConsoleCaptureHandle,
  setupConsoleCapture,
} from "./integrations/console.js";
export { axonPushADKCallbacks } from "./integrations/google-adk.js";
export { AxonPushCallbackHandler } from "./integrations/langchain.js";
export { AxonPushLangGraphHandler } from "./integrations/langgraph.js";
export { AxonPushLlamaIndexHandler } from "./integrations/llamaindex.js";
export { AxonPushMastraExporter, AxonPushMastraHooks } from "./integrations/mastra.js";
export { AxonPushRunHooks } from "./integrations/openai-agents.js";
export { AxonPushSpanExporter, type OtelExporterConfig } from "./integrations/otel.js";
export {
  type AxonPushPinoStream,
  createAxonPushPinoStream,
  type PinoStreamConfig,
} from "./integrations/pino.js";
export {
  buildDsn as buildSentryDsn,
  type InstallSentryOptions,
  installSentry,
  type SentryLike,
} from "./integrations/sentry.js";
export { axonPushMiddleware } from "./integrations/vercel-ai.js";
export {
  createAxonPushWinstonTransport,
  type WinstonTransportConfig,
} from "./integrations/winston.js";
// Models + Resources (Stream B)
export type {
  ApiKey,
  App,
  CanonicalEventType,
  Channel,
  CreateEventDto,
  Environment,
  Event,
  EventDetails,
  EventListResponseDto,
  EventType,
  Organization,
  WebhookDelivery,
  WebhookDeliveryStatus,
  WebhookEndpoint,
  WebhookEndpointCreateResponseDto,
} from "./models.js";
export type {
  IotCredentials,
  PublishData,
  RealtimeOptions,
  SubscribeFilters,
  TopicParts,
} from "./realtime/index.js";
// Realtime (Stream C)
export { RealtimeClient } from "./realtime/index.js";
export { ApiKeysResource } from "./resources/api-keys.js";
export { AppsResource } from "./resources/apps.js";
export { ChannelsResource } from "./resources/channels.js";
export { EnvironmentsResource } from "./resources/environments.js";
export { EventsResource } from "./resources/events.js";
export { OrganizationsResource } from "./resources/organizations.js";
export { TracesV2Resource } from "./resources/traces-v2.js";
export { WebhooksResource } from "./resources/webhooks.js";
export { currentTrace, getOrCreateTrace, TraceContext } from "./tracing.js";
export { __version__ } from "./version.js";
