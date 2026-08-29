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

      - uses: axonpush/sdks/gate-action@v1
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

The same protocol is understood by `axonpush-eval` in both the TypeScript and
Python SDKs, so the script you write here also runs on your laptop.

## Thresholds

Leave them all unset and the gate passes: a team that has not configured a gate
is not blocked by one. Set what you care about, or store the thresholds once as
a gate policy on the dataset and let CI inherit them.

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

A JUnit XML file is written alongside the report, so test reporters pick the
run up without extra configuration.
