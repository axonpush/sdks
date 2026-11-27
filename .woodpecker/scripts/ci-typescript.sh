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
  tools+=(go@stable)
  tools+=(bun@latest)
  export WOODPECKER_TOOLS_READY=1
  exec mise exec "${tools[@]}" -- bash "$0"
fi

printf '%s\n' 'Step 3'
(
  cd .
bun install --frozen-lockfile
)

printf '%s\n' Lint
(
  cd .
bunx biome check .
)

printf '%s\n' 'Resource aliases match operation contracts'
(
  cd .
bun run packages/typescript/tools/check-resource-contract.ts
)

printf '%s\n' Typecheck
(
  cd packages/typescript
bunx tsc --noEmit
)

printf '%s\n' Test
(
  cd packages/typescript
python3 ../../tools/workflow-compiler/bundle.py --host-only typescript
AXONPUSH_WORKFLOW_BINARY="$PWD/bin/linux-amd64/axonpush" bunx vitest run
)

printf '%s\n' Build
(
  cd packages/typescript
bun run build
)

printf '%s\n' 'Validate the published package'
(
  cd packages/typescript
bunx publint
bunx @arethetypeswrong/cli --pack --profile esm-only
artifact=$(npm pack --silent --pack-destination "$RUNNER_TEMP")
python3 ../../tools/workflow-compiler/test-package.py "$RUNNER_TEMP/$artifact"
)
