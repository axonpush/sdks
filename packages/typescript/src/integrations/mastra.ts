import type {
  FeedbackEvent,
  LogEvent,
  MetricEvent,
  ObservabilityExporter,
  ScoreEvent,
  TracingEvent,
} from "@mastra/core/observability";
import type { AxonPush } from "../client.js";
import type { EventType } from "../index.js";
import type { PublishParams } from "../resources/events.js";
import type { TraceContext } from "../tracing.js";
import {
  coerceChannelId,
  type IntegrationConfig,
  initTrace,
  safePublish,
  safePublishParams,
  truncate,
} from "./_base.js";
import {
  type DeclaredTaskGoal,
  FrameworkTaskLifecycle,
  runDeclaredTask,
  type TaskBoundary,
} from "./_task_lifecycle.js";

export interface MastraExporterConfig extends IntegrationConfig {
  serviceName?: string;
  serviceVersion?: string;
  release?: string;
  taskGoal?: DeclaredTaskGoal;
}

const dateToNano = (value: Date | undefined): string | undefined =>
  value ? (BigInt(value.getTime()) * 1_000_000n).toString() : undefined;

const semanticKind = (type: string): string => {
  if (type.includes("agent")) return "agent";
  if (type.includes("workflow")) return "workflow";
  if (type.includes("model")) return "llm";
  if (type.includes("tool")) return "tool";
  if (type.includes("rag") || type.includes("memory")) return "retriever";
  return "custom";
};

/**
 * Mastra 1.x observability exporter.
 *
 * Pass this object to `new Observability({ configs: { default: {
 * exporters: [new AxonPushMastraExporter(...)] }}})`. It consumes Mastra's
 * native span, log, metric, score, and feedback events without requiring
 * lifecycle hooks or coupling AxonPush to Mastra's agent runtime.
 */
export class AxonPushMastraExporter implements ObservabilityExporter {
  readonly name = "axonpush";
  private readonly client: AxonPush;
  private readonly channelId: string;
  private readonly agentId: string;
  private readonly serviceName: string;
  private readonly serviceVersion?: string;
  private readonly release?: string;
  private readonly tasks: FrameworkTaskLifecycle;

  constructor(config: MastraExporterConfig) {
    this.client = config.client;
    this.channelId = coerceChannelId(config.channelId);
    this.agentId = config.agentId ?? "mastra";
    this.serviceName = config.serviceName ?? "mastra";
    this.serviceVersion = config.serviceVersion;
    this.release = config.release;
    this.tasks = new FrameworkTaskLifecycle(config.taskGoal, "mastra");
  }

  onTracingEvent(event: TracingEvent): Promise<void> {
    return this.exportTracingEvent(event);
  }

  async exportTracingEvent(event: TracingEvent): Promise<void> {
    const span = event.exportedSpan;
    const key = `${span.traceId}:${span.id}`;
    const parent = span.parentSpanId ? `${span.traceId}:${span.parentSpanId}` : undefined;
    const kind = semanticKind(String(span.type));
    if (event.type === "span_started") {
      const root =
        !parent &&
        !span.isInternal &&
        !span.nestedUnderParent &&
        ["agent", "workflow"].includes(kind);
      const task = root
        ? this.tasks.start(key, undefined, {
            name: span.name,
            input: span.input,
            metadata: span.metadata,
          })
        : undefined;
      this.tasks.metadata(key, parent);
      if (task) await this.publishTask(task, span.traceId, span.id);
      return;
    }
    if (event.type !== "span_ended") return;
    const attributes = {
      ...(span.attributes ?? {}),
      "gen_ai.operation.name": String(span.type),
      "openinference.span.kind": kind.toUpperCase(),
    };
    const payload: Record<string, unknown> = {
      name: span.name,
      startTimeUnixNano: dateToNano(span.startTime),
      endTimeUnixNano: dateToNano(span.endTime),
      parentSpanId: span.parentSpanId,
      attributes,
      input: span.input,
      output: span.output,
      error: span.errorInfo,
      resource: {
        "service.name": this.serviceName,
        ...(this.serviceVersion ? { "service.version": this.serviceVersion } : {}),
        ...(this.release ? { "deployment.release": this.release } : {}),
      },
    };
    await this.publish({
      identifier: span.name,
      payload,
      traceId: span.traceId,
      spanId: span.id,
      parentSpanId: span.parentSpanId,
      eventType: "app.span",
      metadata: {
        framework: "mastra",
        mastraSpanType: String(span.type),
        entityType: span.entityType,
        entityId: span.entityId,
        ...(span.metadata ?? {}),
        ...this.tasks.metadata(key, parent),
      },
    });
    const task = this.tasks.finish(key, span.errorInfo ? "failed" : "succeeded");
    if (task) await this.publishTask(task, span.traceId, span.id);
  }

  private publishTask(task: TaskBoundary, traceId: string, spanId: string): Promise<void> {
    return this.publish({
      identifier: task.identifier,
      eventType: "custom",
      payload: task.payload,
      traceId,
      spanId,
      metadata: { framework: "mastra", ...task.metadata },
    });
  }

  async onLogEvent(event: LogEvent): Promise<void> {
    const log = event.log;
    await this.publish({
      identifier: log.message,
      payload: {
        timeUnixNano: dateToNano(log.timestamp),
        severityText: log.level.toUpperCase(),
        body: log.message,
        attributes: log.data ?? {},
        resource: { "service.name": this.serviceName },
      },
      traceId: log.traceId,
      spanId: log.spanId,
      eventType: "app.log",
      metadata: { framework: "mastra", ...(log.metadata ?? {}) },
    });
  }

  async onMetricEvent(event: MetricEvent): Promise<void> {
    const metric = event.metric;
    await this.publish({
      identifier: `metric.${metric.name}`,
      payload: {
        name: metric.name,
        value: metric.value,
        labels: metric.labels,
        costContext: metric.costContext,
        occurredAt: metric.timestamp.toISOString(),
      },
      traceId: metric.traceId,
      spanId: metric.spanId,
      eventType: "custom",
      metadata: { framework: "mastra", signal: "metric", ...(metric.metadata ?? {}) },
    });
  }

  async onScoreEvent(event: ScoreEvent): Promise<void> {
    const score = event.score;
    await this.publish({
      identifier: `score.${score.scorerId}`,
      payload: { ...score, timestamp: score.timestamp.toISOString() },
      traceId: score.traceId,
      spanId: score.spanId,
      eventType: "custom",
      metadata: { framework: "mastra", signal: "score" },
    });
  }

  async onFeedbackEvent(event: FeedbackEvent): Promise<void> {
    const feedback = event.feedback;
    await this.publish({
      identifier: `feedback.${feedback.feedbackType}`,
      payload: { ...feedback, timestamp: feedback.timestamp.toISOString() },
      traceId: feedback.traceId,
      spanId: feedback.spanId,
      eventType: "custom",
      metadata: { framework: "mastra", signal: "feedback" },
    });
  }

  async flush(): Promise<void> {}

  async shutdown(): Promise<void> {}

  private async publish(params: Omit<PublishParams, "channelId" | "agentId">): Promise<void> {
    await safePublishParams(this.client, {
      ...params,
      channelId: this.channelId,
      agentId: this.agentId,
    });
  }
}

/**
 * Legacy Mastra 0.10 lifecycle hooks.
 *
 * Plug `beforeToolUse` / `afterToolUse` into a Mastra `Agent`'s tool
 * lifecycle, and `onWorkflowStart` / `onWorkflowEnd` / `onWorkflowError`
 * into a workflow run.
 *
 * @deprecated Mastra 1.x users should use {@link AxonPushMastraExporter}.
 */
export class AxonPushMastraHooks {
  private client: AxonPush;
  private channelId: string;
  private agentId: string;
  private trace: TraceContext;

  constructor(config: IntegrationConfig) {
    this.client = config.client;
    this.channelId = coerceChannelId(config.channelId);
    this.agentId = config.agentId ?? "mastra";
    this.trace = initTrace(config.traceId);
  }

  private emit(identifier: string, eventType: EventType, payload: Record<string, unknown>): void {
    void safePublish(this.client, this.channelId, identifier, eventType, payload, {
      agentId: this.agentId,
      trace: this.trace,
      metadata: { framework: "mastra" },
    });
  }

  task<T>(goal: string, run: (taskId: string) => Promise<T>): Promise<T> {
    return runDeclaredTask(
      goal,
      (event) => {
        void safePublish(this.client, this.channelId, event.identifier, "custom", event.payload, {
          agentId: this.agentId,
          trace: this.trace,
          metadata: { framework: "mastra", ...event.metadata },
        });
      },
      run,
    );
  }

  beforeToolUse(toolName: string, input?: unknown): void {
    this.emit(`tool.${toolName}.start`, "agent.tool_call.start", {
      tool_name: toolName,
      input: truncate(input, 500),
    });
  }

  afterToolUse(toolName: string, output?: unknown): void {
    this.emit(`tool.${toolName}.end`, "agent.tool_call.end", {
      tool_name: toolName,
      output: truncate(output, 500),
    });
  }

  onWorkflowStart(workflowName: string, input?: unknown): void {
    this.emit("workflow.start", "agent.start", {
      workflow_name: workflowName,
      input: truncate(input, 500),
    });
  }

  onWorkflowEnd(workflowName: string, output?: unknown): void {
    this.emit("workflow.end", "agent.end", {
      workflow_name: workflowName,
      output: truncate(output, 500),
    });
  }

  onWorkflowError(workflowName: string, error: Error): void {
    this.emit("workflow.error", "agent.error", {
      workflow_name: workflowName,
      error: error.message,
      error_type: error.name,
    });
  }
}
