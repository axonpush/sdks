using System.Globalization;
using System.Runtime.InteropServices;
using System.Text.Json;
using AxonPush;
using AxonPush.Cli;
using AxonPush.Internal.Api;

// CI is written against the number, so these match the other two CLIs exactly.
const int ExitSuccess = 0;
const int ExitGateFailed = 1;
const int ExitUsage = 2;
const int ExitRemoteFailure = 3;
const int ExitEvaluationFailure = 4;
const int ExitCancelled = 130;

string Usage() => """
Usage:
  axonpush-eval run --dataset <id> --revision <revision> --experiment <id> --command '<command>' [options]
  axonpush-eval run --dataset <id> --revision <revision> --target <id> --command '<command>' [options]

The evaluator command reads one JSON object from stdin and writes one JSON object to stdout:
  {"type":"axonpush.evaluation.input","experimentId":"…","item":{"id":"…","input":…}}
  {"output": <any JSON value>, "traceId"?: "…", "totalTokens"?: 12, "costUsd"?: 0.01, "error"?: "…"}

Options:
  --concurrency <n>           Local processes in flight (default: 4)
  --timeout <s>               Per-item evaluator timeout in seconds (default: 30)
  --startup-timeout <s>       Wait for the experiment to enter running (default: 30)
  --configuration <json>      Target configuration sent to the evaluator and a new experiment
  --target <id>               Create a new experiment and capture git lineage
  --name <name>               New experiment name
  --evaluator <id>@<version>  Repeatable evaluator version for a new experiment
  --baseline <id>             Baseline experiment for a new experiment
  --no-gate                   Do not invoke the release gate
  --minimum-score <n>         Fail below this absolute score
  --max-failure-rate <n>      Fail above this share of errored items (0-1)
  --maximum-latency-ms <n>    Fail above this mean latency
  --maximum-cost-usd <n>      Fail above this total run cost
  --max-score-regression <n>  Fail if the score drops more than this against the baseline
  --max-latency-increase-ratio <n> Fail above this latency increase vs baseline (0.1 = 10%)
  --max-cost-increase-ratio <n>    Fail above this cost increase vs baseline (0.1 = 10%)
  --json <path>               Write a JSON artifact
  --junit <path>              Write a JUnit XML artifact
  --github-summary <path>     Write GitHub Actions markdown (defaults to GITHUB_STEP_SUMMARY)

Exit codes: 0 passed, 1 gate failed, 2 invalid usage, 3 API failure, 4 evaluator failure, 130 cancelled.
Credentials use AXONPUSH_API_KEY, AXONPUSH_TENANT_ID/AXONPUSH_ORG_ID, AXONPUSH_BASE_URL, and AXONPUSH_ENVIRONMENT.
""";

try
{
    var parsed = Arguments.Parse(args);
    if (parsed.Command != "run")
    {
        Console.Error.WriteLine(Usage());
        return ExitUsage;
    }

    using var cancellation = new CancellationTokenSource();
    Console.CancelKeyPress += (_, eventArgs) =>
    {
        eventArgs.Cancel = true;
        cancellation.Cancel();
    };
    // Not ProcessExit: it fires after the token source is disposed.
    using var sigterm = PosixSignalRegistration.Create(PosixSignal.SIGTERM, context =>
    {
        context.Cancel = true;
        cancellation.Cancel();
    });

    var options = AxonPushOptions.FromEnvironment();
    options.FailOpen = false;
    using var client = new AxonPushClient(options);
    var api = new HttpEvaluationApi(client);

    var configuration = parsed.Json("configuration");
    var experimentId = parsed.Value("experiment")
        ?? await api.CreateExperimentAsync(
            NewExperiment(parsed, configuration), cancellation.Token).ConfigureAwait(false);

    var run = await Runner.RunAsync(
        api,
        new RunnerOptions
        {
            DatasetId = parsed.Require("dataset"),
            DatasetRevision = parsed.Require("revision"),
            ExperimentId = experimentId,
            Command = parsed.Require("command"),
            Concurrency = (int)parsed.Number("concurrency", 4),
            TimeoutSeconds = parsed.Number("timeout", 30),
            StartupTimeoutSeconds = parsed.Number("startup-timeout", 30),
            Configuration = configuration,
        },
        cancellation).ConfigureAwait(false);

    if (!parsed.Flag("no-gate") && !run.Cancelled)
    {
        run.Gate = await api.GateExperimentAsync(
            experimentId,
            Thresholds.ToWire(parsed.ThresholdValues()),
            new GateProvenance("cli", run.Lineage.GitCommit, run.Lineage.GitBranch),
            cancellation.Token).ConfigureAwait(false);
    }

    await Reports.WriteArtifactAsync(parsed.Value("json"), Reports.ToJsonReport(run)).ConfigureAwait(false);
    await Reports.WriteArtifactAsync(parsed.Value("junit"), Reports.ToJUnitXml(run)).ConfigureAwait(false);
    await Reports.WriteArtifactAsync(
        parsed.Value("github-summary") ?? Environment.GetEnvironmentVariable("GITHUB_STEP_SUMMARY"),
        Reports.ToGitHubSummary(run)).ConfigureAwait(false);
    Console.Out.Write(Reports.ToJsonReport(run));

    if (run.Cancelled) return ExitCancelled;
    if (run.Gate is { Passed: false }) return ExitGateFailed;
    return run.Results.Any(item => item.Status != "passed") ? ExitEvaluationFailure : ExitSuccess;
}
catch (OperationCanceledException)
{
    Console.Error.WriteLine("axonpush-eval: cancelled");
    return ExitCancelled;
}
catch (EvaluationApiException exception)
{
    Console.Error.WriteLine($"axonpush-eval: {exception.Message}");
    return ExitRemoteFailure;
}
catch (AxonPushApiException exception)
{
    Console.Error.WriteLine($"axonpush-eval: {exception.Message}");
    return ExitRemoteFailure;
}
catch (AxonPushException exception)
{
    Console.Error.WriteLine($"axonpush-eval: {exception.Message}");
    return ExitRemoteFailure;
}
catch (ArgumentException exception)
{
    Console.Error.WriteLine($"axonpush-eval: {exception.Message}");
    Console.Error.WriteLine(Usage());
    return ExitUsage;
}

static CreateExperimentDto NewExperiment(Arguments parsed, JsonElement? configuration)
{
    var target = parsed.Value("target")
        ?? throw new ArgumentException("--target is required when --experiment is not given");
    var lineage = Git.Capture();
    return new CreateExperimentDto
    {
        Name = parsed.Value("name")
            ?? $"local-{parsed.Require("dataset")}-r{parsed.Require("revision")}",
        DatasetId = parsed.Require("dataset"),
        DatasetRevision = HttpEvaluationApi.ParseRevision(parsed.Require("revision")),
        TargetId = target,
        EvaluatorVersions = [.. parsed.Evaluators()],
        BaselineExperimentId = parsed.Value("baseline"),
        Configuration = configuration,
        GitCommit = lineage.GitCommit,
        GitBranch = lineage.GitBranch,
        GitDirty = lineage.GitDirty,
    };
}

/// <summary>The same hand-rolled option parsing the TypeScript CLI uses.</summary>
internal sealed class Arguments
{
    private readonly Dictionary<string, List<string>> _values = new(StringComparer.Ordinal);
    private readonly HashSet<string> _flags = new(StringComparer.Ordinal);

    public string? Command { get; private init; }

    public static Arguments Parse(string[] argv)
    {
        var parsed = new Arguments { Command = argv.FirstOrDefault() };
        for (var index = 1; index < argv.Length; index++)
        {
            var token = argv[index];
            if (!token.StartsWith("--", StringComparison.Ordinal))
            {
                throw new ArgumentException($"Unexpected argument: {token}");
            }

            var separator = token.IndexOf('=', StringComparison.Ordinal);
            var key = separator > 0 ? token[2..separator] : token[2..];
            if (key.Length == 0)
            {
                throw new ArgumentException("Option name cannot be empty");
            }

            if (key == "no-gate")
            {
                parsed._flags.Add(key);
                continue;
            }

            var value = separator > 0
                ? token[(separator + 1)..]
                : index + 1 < argv.Length ? argv[++index] : null;
            if (string.IsNullOrEmpty(value) || value.StartsWith("--", StringComparison.Ordinal))
            {
                throw new ArgumentException($"Option --{key} requires a value");
            }

            if (!parsed._values.TryGetValue(key, out var list))
            {
                parsed._values[key] = list = [];
            }

            list.Add(value);
        }

        return parsed;
    }

    public string? Value(string key) => _values.TryGetValue(key, out var list) ? list[^1] : null;

    public bool Flag(string key) => _flags.Contains(key);

    public string Require(string key) =>
        Value(key) ?? throw new ArgumentException($"--{key} is required");

    public double Number(string key, double fallback) =>
        Value(key) is { } raw
            ? double.TryParse(raw, NumberStyles.Float, CultureInfo.InvariantCulture, out var value)
                ? value
                : throw new ArgumentException($"--{key} must be a number")
            : fallback;

    public JsonElement? Json(string key)
    {
        if (Value(key) is not { } raw)
        {
            return null;
        }

        try
        {
            return JsonDocument.Parse(raw).RootElement.Clone();
        }
        catch (JsonException exception)
        {
            throw new ArgumentException($"--{key} must be JSON: {exception.Message}", exception);
        }
    }

    public Dictionary<string, double?> ThresholdValues()
    {
        var supplied = new Dictionary<string, double?>(StringComparer.Ordinal);
        foreach (var option in Thresholds.Options)
        {
            supplied[option.Flag] = Value(option.Flag) is { } raw
                ? double.TryParse(raw, NumberStyles.Float, CultureInfo.InvariantCulture, out var value)
                    ? value
                    : throw new ArgumentException($"--{option.Flag} must be a number")
                : null;
        }

        return supplied;
    }

    public IEnumerable<EvaluatorVersionRefDto> Evaluators()
    {
        if (!_values.TryGetValue("evaluator", out var entries))
        {
            yield break;
        }

        foreach (var entry in entries)
        {
            var separator = entry.LastIndexOf('@');
            if (separator <= 0 || separator == entry.Length - 1)
            {
                throw new ArgumentException("--evaluator must have the form <id>@<version>");
            }

            yield return new EvaluatorVersionRefDto
            {
                EvaluatorId = entry[..separator],
                Version = double.Parse(entry[(separator + 1)..], CultureInfo.InvariantCulture),
            };
        }
    }
}
