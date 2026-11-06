/** Preserve standard exception metadata without serializing arbitrary Error properties. */
export function exceptionAttributes(value: unknown): Record<string, string> {
  if (!value || typeof value !== "object") return {};
  const error = value as Record<string, unknown>;
  const name = typeof error.type === "string" ? error.type : error.name;
  const message = error.message;
  const stack = error.stack;
  if (!(value instanceof Error) && typeof stack !== "string") return {};
  return {
    ...(typeof name === "string" && name ? { "exception.type": name } : {}),
    ...(typeof message === "string" ? { "exception.message": message } : {}),
    ...(typeof stack === "string" && stack ? { "exception.stacktrace": stack } : {}),
  };
}
