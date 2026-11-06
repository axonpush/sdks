export const MAX_EXCEPTION_STACK_LENGTH = 32 * 1024;
export const MAX_EXCEPTION_MESSAGE_LENGTH = 4096;
const MAX_EXCEPTION_TYPE_LENGTH = 256;
const TRUNCATED = "\n[axonpush diagnostic truncated]";

function bounded(value: string, limit: number): string {
  return value.length <= limit ? value : value.slice(0, limit - TRUNCATED.length) + TRUNCATED;
}

function stringProperty(value: object, key: string): string | undefined {
  try {
    const field = (value as Record<string, unknown>)[key];
    return typeof field === "string" ? field : undefined;
  } catch {
    // Error.stack can run a caller-supplied prepareStackTrace or accessor.
    return undefined;
  }
}

/** Recognize native errors across browser realms without trusting a plain stack field. */
export function isNativeError(value: unknown): value is Error {
  if (!value || typeof value !== "object") return false;
  try {
    return (
      value instanceof Error ||
      ["[object Error]", "[object DOMException]"].includes(Object.prototype.toString.call(value))
    );
  } catch {
    return false;
  }
}

/** A readable native error body, without evaluating its stack formatter. */
export function exceptionSummary(value: Error): string {
  const name = stringProperty(value, "name") || stringProperty(value, "type");
  const message = stringProperty(value, "message");
  return (
    [
      name ? bounded(name, MAX_EXCEPTION_TYPE_LENGTH) : "",
      message ? bounded(message, MAX_EXCEPTION_MESSAGE_LENGTH) : "",
    ]
      .filter(Boolean)
      .join(": ") || "Error"
  );
}

/** Preserve bounded captured metadata without serializing arbitrary Error properties. */
export function exceptionAttributes(value: unknown): Record<string, string> {
  if (!value || typeof value !== "object") return {};
  const native = isNativeError(value);
  const name = native
    ? stringProperty(value, "name") || stringProperty(value, "type")
    : stringProperty(value, "type") || stringProperty(value, "name");
  const message = stringProperty(value, "message");
  const stack = stringProperty(value, "stack");
  // Pino/Winston serialize errors into records. A business field named stack
  // alone is not evidence of an exception.
  const serialized =
    typeof stack === "string" &&
    typeof message === "string" &&
    ((!!name && /(?:Error|Exception)$/.test(name)) ||
      /(?:^|\n)\s*at\s|^[\w.$]+(?:Error|Exception):/.test(stack));
  if (!native && !serialized) return {};
  return {
    ...(name ? { "exception.type": bounded(name, MAX_EXCEPTION_TYPE_LENGTH) } : {}),
    ...(message !== undefined
      ? { "exception.message": bounded(message, MAX_EXCEPTION_MESSAGE_LENGTH) }
      : {}),
    ...(stack ? { "exception.stacktrace": bounded(stack, MAX_EXCEPTION_STACK_LENGTH) } : {}),
  };
}

/** Keep legacy framework error fields bounded alongside standard attributes. */
export function exceptionPayload(value: unknown): Record<string, unknown> {
  const attributes = exceptionAttributes(value);
  return {
    error: attributes["exception.message"] ?? "",
    error_type: attributes["exception.type"] ?? "",
    attributes,
  };
}

/** Bound duplicate diagnostic fields before they enter a publisher queue. */
export function boundedExceptionContext(context: Record<string, unknown>): Record<string, unknown> {
  const out = { ...context };
  for (const [key, limit] of [
    ["stack", MAX_EXCEPTION_STACK_LENGTH],
    ["exception.stacktrace", MAX_EXCEPTION_STACK_LENGTH],
    ["exception.message", MAX_EXCEPTION_MESSAGE_LENGTH],
    ["exception.type", MAX_EXCEPTION_TYPE_LENGTH],
  ] as const) {
    if (typeof out[key] === "string") out[key] = bounded(out[key], limit);
  }
  for (const key of ["err", "error"]) {
    if (Object.hasOwn(out, key)) out[key] = boundedErrorRecord(out[key], 0);
  }
  return out;
}

function boundedErrorRecord(value: unknown, depth: number): unknown {
  if (typeof value === "string") return bounded(value, MAX_EXCEPTION_MESSAGE_LENGTH);
  const attributes = exceptionAttributes(value);
  if (!Object.keys(attributes).length || !value || typeof value !== "object") return value;
  if (depth >= 8) return "[axonpush exception cause truncated]";
  if (isNativeError(value)) {
    return {
      name: attributes["exception.type"],
      message: attributes["exception.message"],
      stack: attributes["exception.stacktrace"],
    };
  }
  const record: Record<string, unknown> = {};
  try {
    for (const [field, descriptor] of Object.entries(Object.getOwnPropertyDescriptors(value))) {
      if (descriptor.enumerable && "value" in descriptor) {
        Object.defineProperty(record, field, {
          value: descriptor.value,
          writable: true,
          enumerable: true,
          configurable: true,
        });
      }
    }
  } catch {
    // A proxy may refuse inspection; keep whichever diagnostics were readable.
  }
  if (attributes["exception.type"]) record.type ??= attributes["exception.type"];
  if (attributes["exception.message"] !== undefined)
    record.message = attributes["exception.message"];
  if (attributes["exception.stacktrace"]) record.stack = attributes["exception.stacktrace"];
  for (const [field, limit] of [
    ["stack", MAX_EXCEPTION_STACK_LENGTH],
    ["message", MAX_EXCEPTION_MESSAGE_LENGTH],
    ["name", MAX_EXCEPTION_TYPE_LENGTH],
    ["type", MAX_EXCEPTION_TYPE_LENGTH],
  ] as const) {
    if (typeof record[field] === "string") record[field] = bounded(record[field], limit);
  }
  if (Object.prototype.hasOwnProperty.call(record, "cause")) {
    record.cause = boundedErrorRecord(record.cause, depth + 1);
  }
  return record;
}
