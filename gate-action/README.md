# axonpush release gate

Replays the production failures you have already captured against the change in
a pull request, and fails the build if it regresses.

```yaml
name: agent regressions
on: pull_request

permissions:
  contents: read
  pull-requests: write   # only needed for the PR comment

jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-node@v5
        with:
          node-version: 22

      - uses: axonpush/sdks/gate-action@gate-action-v1
        with:
          dataset: ${{ vars.AXONPUSH_DATASET }}
          revision: 4
          target: ${{ vars.AXONPUSH_TARGET }}
          evaluator: |
            exact-match@1
          command: python scripts/evaluate.py
          minimum-score: 0.85
          max-failure-rate: 0.05
          api-key: ${{ secrets.AXONPUSH_API_KEY }}
          tenant-id: ${{ secrets.AXONPUSH_TENANT_ID }}
```

## The evaluator command

Your command is run once per dataset example. It reads one JSON object on stdin
and writes one JSON object on stdout — no framework, no import from us:

```
in   {"type":"axonpush.evaluation.input","experimentId":"…","item":{"id":"…","input":…}}
out  {"output": <any JSON value>, "traceId"?: "…", "totalTokens"?: 12, "costUsd"?: 0.01, "error"?: "…"}
```

The same protocol is understood by `axonpush-eval` in the TypeScript, Python
and .NET SDKs, so the script you write here also runs on your laptop, and a
pipeline written against one runs against any of them.

## Thresholds

Leave them all unset and the gate resolves the stored policy for the
experiment's evaluation target, then its dataset. With no enabled policy either,
the gate passes: a team that has not configured a gate is not blocked by one.
Set thresholds here to override the policy for one run, or manage the policy
once with `client.gates.savePolicy(...)` and let every pipeline inherit it.

| Input | Blocks when |
|---|---|
| `minimum-score` | the run scores below this |
| `max-failure-rate` | more than this share of examples error (0-1) |
| `maximum-latency-ms` | mean latency exceeds this |
| `maximum-cost-usd` | the run costs more than this |
| `max-score-regression` | the score falls further than this against the baseline |
| `max-latency-increase-ratio` | the run is more than this fraction slower than the baseline |
| `max-cost-increase-ratio` | the run costs more than this fraction above the baseline |

The last three need `baseline` set to a completed experiment.

## Trialling it without blocking

Set `fail-on-gate: false`. The gate still runs, still comments, still writes the
job summary — it just does not fail the build. Turn it on once the signal is
worth trusting.

## Outputs

| Output | |
|---|---|
| `passed` | `true` when the gate passed |
| `experiment-id` | the experiment the gate ran against |
| `report` | path to the JSON report on the runner |
| `junit` | path to the JUnit XML, so test reporters pick the run up |
| `summary` | path to the markdown written to the job summary |
| `exit-code` | the CLI's exit code, when the distinction matters |

Exit codes: `0` passed, `1` the gate blocked, `2` invalid usage, `3` the API
failed, `4` an example failed to evaluate, `130` cancelled. The action treats
`1` and `4` as a failed gate, passes `130` through as a cancellation, and stops
the job on anything else.
