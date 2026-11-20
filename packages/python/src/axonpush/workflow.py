"""Local workflow tooling. Evaluation is delegated to the pinned Go executable."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any

from axonpush._internal.api.models import FactsInputBody as PublishWorkflowFacts
from axonpush._internal.api.models import Input as WorkflowInput

__all__ = ["run", "PublishWorkflowFacts", "WorkflowInput", "COMPILER_VERSION"]

COMPILER_VERSION = "0.1.0"


def run(*arguments: str, binary: str | None = None, timeout: float = 30) -> Any:
    """Run a local command without a shell; no model or server calls are made.

    Supply AXONPUSH_WORKFLOW_BINARY or an explicit path to a verified release
    binary. Publishing is deliberately excluded from this offline helper.
    """
    if not arguments or arguments[0] not in {"validate", "generate", "test", "diff"}:
        raise ValueError("Expected validate, generate, test or diff")
    executable = binary or os.environ.get("AXONPUSH_WORKFLOW_BINARY")
    if not executable or not Path(executable).is_file():
        raise ValueError("Set AXONPUSH_WORKFLOW_BINARY to the pinned compiler executable")
    executable = str(Path(executable).resolve())
    version = subprocess.run(
        [executable, "workflow", "version"], capture_output=True, text=True,
        check=True, timeout=timeout,
    )
    if json.loads(version.stdout).get("version") != COMPILER_VERSION:
        raise ValueError(f"Workflow compiler {COMPILER_VERSION} is required")
    result = subprocess.run(
        [executable, "workflow", *arguments], capture_output=True, text=True,
        check=True, timeout=timeout,
    )
    return json.loads(result.stdout) if result.stdout.strip() else None
