"""Client-side telemetry capture and redaction policy."""

from __future__ import annotations

import re
from typing import Any

from axonpush._config import Settings

_SECRET_KEY = re.compile(
    r"^(authorization|proxy-authorization|cookie|set-cookie|password|passwd|secret|"
    r"client_secret|api[-_.]?key|access[-_.]?token|refresh[-_.]?token|private[-_.]?key)$",
    re.IGNORECASE,
)
_CONTENT_KEY = re.compile(
    r"^(prompt|prompts|messages?|completion|completions|input|output|response|"
    r"tool[-_.]?(arguments?|result|output)|retrieval[-_.]?(documents?|content))$",
    re.IGNORECASE,
)

#: How much of a content value ``redacted`` keeps.
#:
#: The three capture modes are a ladder over the content-key heuristic:
#: ``metadata_only`` drops content outright, ``full`` keeps it, and
#: ``redacted`` sits between — enough of a prompt or completion to recognise
#: a run, not enough to reconstruct it. Explicit controls (``redact_keys``,
#: ``max_content_length``, secret-shaped keys) are always-on and unaffected
#: by the mode. Matches CONTENT_PREVIEW_LENGTH server-side.
CONTENT_PREVIEW_LENGTH = 256


def redact_telemetry(value: Any, settings: Settings) -> Any:
    """Return a recursively copied value safe for telemetry transport."""

    configured_keys = {key.casefold() for key in settings.redact_keys}
    previewing = settings.content_capture_mode == "redacted"

    def visit(current: Any, in_content: bool = False) -> Any:
        if isinstance(current, str):
            limit = (
                min(CONTENT_PREVIEW_LENGTH, settings.max_content_length)
                if in_content
                else settings.max_content_length
            )
            if len(current) > limit:
                # Name whichever limit actually bound. Saying "preview" when
                # max_content_length did the cutting would misreport why the
                # value is short.
                preview_bound = in_content and CONTENT_PREVIEW_LENGTH < settings.max_content_length
                marker = "[REDACTED_PREVIEW]" if preview_bound else "[TRUNCATED]"
                return f"{current[:limit]}…{marker}"
            return current
        if isinstance(current, list):
            return [visit(item, in_content) for item in current]
        if isinstance(current, tuple):
            return [visit(item, in_content) for item in current]
        if isinstance(current, dict):
            output: dict[Any, Any] = {}
            for key, child in current.items():
                key_text = str(key)
                is_content = bool(_CONTENT_KEY.match(key_text))
                should_redact = (
                    bool(_SECRET_KEY.match(key_text))
                    or key_text.casefold() in configured_keys
                    or (settings.content_capture_mode == "metadata_only" and is_content)
                )
                if should_redact:
                    output[key] = "[REDACTED]"
                else:
                    # ``redacted`` marks the subtree; nested content keys
                    # inherit it so messages[].content is previewed the same
                    # as a bare prompt.
                    output[key] = visit(child, in_content or (previewing and is_content))
            return output
        return current

    return visit(value)


__all__ = ["CONTENT_PREVIEW_LENGTH", "redact_telemetry"]
