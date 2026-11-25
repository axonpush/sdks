import { AsyncLocalStorage } from "node:async_hooks";
import type { FactsInputBody, Input } from "./_internal/api/types.gen.js";
import type { AxonPush } from "./client.js";
import type { ObserveParams } from "./observe.js";
import type { PublishParams } from "./resources/events.js";
import { currentTrace, withoutTrace, withTrace } from "./tracing.js";

export interface RequestContext {
  workspaceId: string;
  environment: string;
  subjects?: Readonly<Record<string, string>>;
  requestId?: string;
  traceId?: string;
  sessionId?: string;
  /** Event name -> declared refs/attribute field -> subject type. No fields are inferred. */
  bindings?: Readonly<
    Record<
      string,
      { refs?: Readonly<Record<string, string>>; attributes?: Readonly<Record<string, string>> }
    >
  >;
}
const contexts = new AsyncLocalStorage<ReadonlyMap<object, Readonly<RequestContext>>>();
export function currentRequestContext(owner: object): Readonly<RequestContext> | undefined {
  return contexts.getStore()?.get(owner);
}
export function runRequestContext<T>(owner: object, context: RequestContext, work: () => T): T {
  if (!context.workspaceId?.trim() || !context.environment?.trim())
    throw new Error("Request context requires workspaceId and environment");
  if (Object.keys(context.subjects ?? {}).length > 32)
    throw new Error("At most 32 subjects are supported");
  for (const [kind, id] of Object.entries(context.subjects ?? {}))
    if (!kind.trim() || kind.length > 80 || typeof id !== "string" || !id.trim() || id.length > 200)
      throw new Error("Subjects require nonempty entity types and opaque IDs");
  const snapshot = structuredClone(context);
  snapshot.traceId ??= currentTrace()?.traceId;
  const map = new Map(contexts.getStore());
  map.set(owner, snapshot);
  return withTrace(snapshot.traceId, () => {
    snapshot.traceId = currentTrace()?.traceId;
    return contexts.run(map, work);
  });
}
export function withoutRequestContext<T>(work: () => T): T {
  return withoutTrace(() => contexts.run(new Map(), work));
}
export function contextAttributes(context: RequestContext | undefined): Record<string, unknown> {
  return context
    ? {
        "axonpush.workspace_id": context.workspaceId,
        "deployment.environment.name": context.environment,
        ...(context.subjects && Object.keys(context.subjects).length
          ? { "telemetry.subjects": { ...context.subjects } }
          : {}),
        ...(context.subjects?.user ? { "user.id": context.subjects.user } : {}),
        ...(context.requestId ? { "axonpush.request_id": context.requestId } : {}),
        ...(context.sessionId ? { "session.id": context.sessionId } : {}),
      }
    : {};
}
function mergeSubjects(
  existing: Record<string, string> | undefined,
  supplied: Readonly<Record<string, string>> = {},
): Record<string, string> {
  if (
    existing !== undefined &&
    (typeof existing !== "object" || existing === null || Array.isArray(existing))
  )
    throw new Error("Invalid subject map");
  for (const [kind, id] of Object.entries(existing ?? {}))
    if (typeof id !== "string" || !kind.trim() || !id.trim())
      throw new Error("Invalid subject map");
  for (const [kind, id] of Object.entries(existing ?? {}))
    if (supplied[kind] !== undefined && supplied[kind] !== id)
      throw new Error(`Conflicting subject: ${kind}`);
  return { ...supplied, ...existing };
}
export function captureContextEvent<T extends PublishParams>(owner: object, params: T): T {
  const context = currentRequestContext(owner);
  if (!context) return params;
  if (params.environment && params.environment !== context.environment)
    throw new Error("Request environment mismatch");
  for (const source of [params.metadata, params.payload, params.payload?.attributes]) {
    if (!source || typeof source !== "object") continue;
    const bag = source as Record<string, unknown>;
    mergeSubjects(
      bag["telemetry.subjects"] as Record<string, string> | undefined,
      context.subjects,
    );
    for (const key of ["user.id", "enduser.id", "userId"])
      if (bag[key] !== undefined && context.subjects?.user && bag[key] !== context.subjects.user)
        throw new Error("Conflicting user identity");
    if (
      bag["axonpush.workspace_id"] !== undefined &&
      bag["axonpush.workspace_id"] !== context.workspaceId
    )
      throw new Error("Request workspace mismatch");
  }
  const metadata = { ...contextAttributes(context), ...params.metadata };
  const explicit = params.metadata?.["telemetry.subjects"] as Record<string, string> | undefined;
  metadata["telemetry.subjects"] = mergeSubjects(explicit, context.subjects);
  if (
    params.metadata?.["user.id"] !== undefined &&
    context.subjects?.user &&
    params.metadata["user.id"] !== context.subjects.user
  )
    throw new Error("Conflicting user identity");
  return {
    ...params,
    traceId: params.traceId ?? context.traceId,
    environment: context.environment,
    metadata: structuredClone(metadata),
  };
}
export function contextObservation(
  owner: object,
  workspaceId: string,
  params: ObserveParams,
): ObserveParams {
  const c = currentRequestContext(owner);
  if (!c) return params;
  if (workspaceId !== c.workspaceId || (params.environment && params.environment !== c.environment))
    throw new Error("Request workspace/environment mismatch");
  const mapping = c.bindings?.[params.event];
  const mapped = (
    bindings: Readonly<Record<string, string>> | undefined,
    explicit: Record<string, unknown> = {},
  ) => {
    const defaults: Record<string, string> = {};
    for (const [field, kind] of Object.entries(bindings ?? {})) {
      const id = c.subjects?.[kind];
      if (id === undefined) continue;
      if (explicit[field] !== undefined && explicit[field] !== id)
        throw new Error(`Conflicting subject binding: ${field}`);
      defaults[field] = id;
    }
    return { ...defaults, ...explicit };
  };
  return {
    ...params,
    environment: c.environment,
    refs: mapped(mapping?.refs, params.refs) as Record<string, string>,
    attributes: mapped(mapping?.attributes, params.attributes),
  };
}
/** Bound publisher: safe to pass to a generated hook or a queued job handler. */
export class ScopedAxonPush {
  readonly events: {
    publish: (params: PublishParams) => ReturnType<AxonPush["events"]["publish"]>;
  };
  readonly workflows: {
    facts: (workflow: string, input: Input) => ReturnType<AxonPush["workflows"]["facts"]>;
  };
  constructor(
    private readonly owner: AxonPush,
    readonly context: Readonly<RequestContext>,
  ) {
    this.events = { publish: (params) => this.run(() => owner.events.publish(params)) };
    this.workflows = { facts: (workflow, input) => this.facts(workflow, input) };
  }
  private run<T>(work: () => T): T {
    return runRequestContext(this.owner, this.context, work);
  }
  observe(params: ObserveParams | ObserveParams[]) {
    return this.run(() => this.owner.observe(this.context.workspaceId, params));
  }
  facts(workflow: string, input: Input) {
    const subjects = mergeSubjects(input.subjects, this.context.subjects);
    return this.run(() =>
      this.owner.workflows.facts(
        this.context.workspaceId,
        {
          workflow,
          input: {
            ...input,
            subjects,
            facts:
              input.facts?.map((fact) => ({
                ...fact,
                ...(!fact.trace_id && this.context.traceId
                  ? { trace_id: this.context.traceId }
                  : {}),
              })) ?? [],
          },
        } satisfies FactsInputBody,
        { environment: this.context.environment },
      ),
    );
  }
  /** Snapshot only allowlisted correlation fields; no credentials or profile traits. */
  capture(): RequestContext {
    return structuredClone(this.context);
  }
  /** Enrich an application-owned span without installing or replacing a provider. */
  annotateSpan(span: { setAttribute(key: string, value: unknown): unknown }) {
    for (const [key, value] of Object.entries(contextAttributes(this.context))) {
      span.setAttribute(key, typeof value === "object" ? JSON.stringify(value) : value);
    }
    for (const [kind, id] of Object.entries(this.context.subjects ?? {}))
      span.setAttribute(`axonpush.subject.${kind}`, id);
  }
}
