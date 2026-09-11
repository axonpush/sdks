"""Declarative integration manifest for the OTel-native telemetry module.

Each :class:`IntegrationManifest` entry describes a framework AxonPush can
observe through ``axonpush.telemetry``: the supported version range, the GenAI
capabilities it surfaces, the default content-capture policy, and a
copy-paste setup snippet. The structure is intentionally plain (dataclasses +
``Literal`` fields) so both the SDK and the docs site can read it without
importing any heavy dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Literal, Tuple

ContentCaptureMode = Literal["metadata_only", "redacted", "full"]

Capability = Literal[
    "chat",
    "tools",
    "streaming",
    "usage",
    "embeddings",
    "reasoning",
    "multimodal",
]


@dataclass(frozen=True)
class IntegrationManifest:
    """A single framework adapter the telemetry module knows how to wire up."""

    name: str
    package: str
    version_spec: str
    capabilities: Tuple[Capability, ...]
    content_capture_default: ContentCaptureMode
    setup_snippet: str
    notes: str = ""

    def supports(self, capability: Capability) -> bool:
        return capability in self.capabilities


_VERCEL_AI_SNIPPET = """\
from axonpush.telemetry import configure_telemetry, genai_span, record_genai_response

handle = configure_telemetry(
    base_url="https://ingest.axonpush.com",
    api_key="ak_...",
    channel_id="ch_...",
    service_name="my-agent",
    content_capture="metadata_only",
)

tracer = handle.tracer("vercel-ai")
with genai_span(
    tracer,
    operation="chat",
    request_model="gpt-4o",
    system="openai",
) as span:
    result = generate_text(model="gpt-4o", prompt="hello")
    record_genai_response(
        span,
        response_model=result.model,
        finish_reasons=[result.finish_reason],
        input_tokens=result.usage.prompt_tokens,
        output_tokens=result.usage.completion_tokens,
    )

handle.flush()
"""


MANIFESTS: Dict[str, IntegrationManifest] = {
    "vercel-ai": IntegrationManifest(
        name="Vercel AI SDK",
        package="ai",
        version_spec="ai>=0.5,<0.6",
        capabilities=("chat", "tools", "streaming", "usage"),
        content_capture_default="metadata_only",
        setup_snippet=_VERCEL_AI_SNIPPET,
        notes=(
            "Wraps generate_text / stream_text calls. Emits OTel GenAI "
            "semantic-convention attributes (gen_ai.*) to the AxonPush OTLP "
            "endpoint at {base_url}/v1/traces."
        ),
    ),
}


def get_manifest(key: str) -> IntegrationManifest:
    """Return the manifest for ``key`` or raise ``KeyError`` with the known keys."""
    try:
        return MANIFESTS[key]
    except KeyError:
        known = ", ".join(sorted(MANIFESTS)) or "(none)"
        raise KeyError(f"unknown integration {key!r}; known: {known}") from None


def list_manifests() -> List[IntegrationManifest]:
    return list(MANIFESTS.values())


__all__ = [
    "Capability",
    "ContentCaptureMode",
    "IntegrationManifest",
    "MANIFESTS",
    "get_manifest",
    "list_manifests",
]

# Silence "imported but unused" for the re-exported ``field`` helper kept for
# downstream manifest authors who add mutable capability sets.
_ = field
