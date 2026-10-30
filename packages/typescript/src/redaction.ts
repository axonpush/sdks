import type { ResolvedSettings } from "./config.js";

const SECRET_KEY =
  /^(authorization|proxy-authorization|cookie|set-cookie|password|passwd|secret|client_secret|api[-_.]?key|access[-_.]?token|refresh[-_.]?token|private[-_.]?key)$/i;
const CONTENT_KEY =
  /^(?:(?:(?:gen_ai|llm|ai)\.(?:(?:input|output|content)\.)?)?(?:prompts?|messages?|completions?|input|output|response|tool[-_.]?(?:arguments?|results?|output)|retrieval[-_.]?(?:documents?|content))|(?:gen_ai|llm|ai)\.tool(?:\.call)?\.(?:arguments?|results?|output))$/i;

export function redactTelemetry<T>(value: T, settings: ResolvedSettings): T {
  const visit = (current: unknown, inContent = false): unknown => {
    if (typeof current === "string") {
      const limit = inContent
        ? Math.min(256, settings.maxContentLength)
        : settings.maxContentLength;
      const chars = Array.from(current);
      return chars.length > limit
        ? `${chars.slice(0, limit).join("")}…${inContent && limit < settings.maxContentLength ? "[REDACTED_PREVIEW]" : "[TRUNCATED]"}`
        : current;
    }
    if (Array.isArray(current)) return current.map((item) => visit(item, inContent));
    if (!current || typeof current !== "object") return current;
    const output: Record<string, unknown> = {};
    for (const [key, child] of Object.entries(current as Record<string, unknown>)) {
      if (
        SECRET_KEY.test(key) ||
        settings.redactKeys.some((candidate) => candidate.toLowerCase() === key.toLowerCase()) ||
        (settings.contentCaptureMode === "metadata_only" && CONTENT_KEY.test(key))
      ) {
        output[key] = "[REDACTED]";
      } else {
        output[key] = visit(
          child,
          inContent || (settings.contentCaptureMode === "redacted" && CONTENT_KEY.test(key)),
        );
      }
    }
    return output;
  };
  return visit(value) as T;
}
