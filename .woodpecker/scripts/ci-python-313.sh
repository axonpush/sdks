#!/usr/bin/env bash
set -eo pipefail
export GITHUB_WORKSPACE="$CI_WORKSPACE"
export GITHUB_SHA="$CI_COMMIT_SHA"
export GITHUB_REF="$CI_COMMIT_REF"
export GITHUB_REF_NAME="${CI_COMMIT_REF##refs/heads/}"
GITHUB_REF_NAME="${GITHUB_REF_NAME##refs/tags/}"
export GITHUB_REPOSITORY="$CI_REPO"
export GITHUB_REPOSITORY_OWNER="$CI_REPO_OWNER"
export GITHUB_EVENT_NAME="$CI_PIPELINE_EVENT"
if [ "$GITHUB_EVENT_NAME" = manual ]; then GITHUB_EVENT_NAME=workflow_dispatch; fi
export RUNNER_TEMP="$(mktemp -d /tmp/woodpecker.XXXXXX)"
export GITHUB_ENV="$RUNNER_TEMP/environment" GITHUB_OUTPUT="$RUNNER_TEMP/output"
touch "$GITHUB_ENV" "$GITHUB_OUTPUT"
export MISE_TRUSTED_CONFIG_PATHS="$CI_WORKSPACE"
export UV_PYTHON=''3.13''
if [ "${WOODPECKER_TOOLS_READY:-}" != 1 ]; then
  tools=()
  tools+=(uv@latest)
  export WOODPECKER_TOOLS_READY=1
  exec mise exec "${tools[@]}" -- bash "$0"
fi

printf '%s\n' 'Step 3'
(
  cd packages/python
uv python install 3.13
)

printf '%s\n' 'Step 4'
(
  cd packages/python
uv sync --extra dev --extra all
)

# Shared Ruff and resource-contract checks run once in python-310.
# Mypy runs with all optional integrations in python-312; runtime tests run on every version.
printf '%s\n' Test
(
  cd packages/python
uv run pytest
)
