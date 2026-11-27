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
if [ "${WOODPECKER_TOOLS_READY:-}" != 1 ]; then
  tools=()
  tools+=(bun@latest)
  tools+=(uv@latest)
  export WOODPECKER_TOOLS_READY=1
  exec mise exec "${tools[@]}" -- bash "$0"
fi

printf '%s\n' 'Step 4'
(
  cd .
bun install --frozen-lockfile
)

printf '%s\n' 'Regenerate TypeScript client'
(
  cd packages/typescript
bun run codegen
)

printf '%s\n' 'Regenerate Python client'
(
  cd packages/python
uv sync --extra dev
rm -rf _internal_api src/axonpush/_internal/api
uv run openapi-python-client generate --path ../../contract/openapi.sdk.json --config tools/openapi-config.yaml --overwrite --meta none
mkdir -p src/axonpush/_internal
mv _internal_api src/axonpush/_internal/api
)

printf '%s\n' 'Regenerate shared business resources and .NET DTOs'
(
  cd .
python3 tools/generate-operations.py
)

printf '%s\n' 'Verify contract and resource parity'
(
  cd .
bun run tools/check-contract.ts
bun run tools/surface-diff.ts
)

printf '%s\n' 'Fail if a checked-in client is stale'
(
  cd .
if ! git diff --exit-code -- packages/typescript/src/_internal/api packages/python/src/axonpush/_internal/api packages/dotnet/src/AxonPush/Operations packages/typescript/src/resources packages/python/src/axonpush/resources; then
  echo "::error::Generated SDKs are out of date. Run mise run codegen."
  exit 1
fi
)
