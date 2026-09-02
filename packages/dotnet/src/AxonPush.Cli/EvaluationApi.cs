using System.Globalization;
using AxonPush.Internal.Api;

namespace AxonPush.Cli;

/// <summary>The API answered with a shape the runner cannot use.</summary>
internal sealed class EvaluationApiException : Exception
{
    public EvaluationApiException(string message) : base(message) { }

    public EvaluationApiException(string message, Exception inner) : base(message, inner) { }
}

internal sealed record GateProvenance(string? Source, string? GitCommit, string? GitBranch);

/// <summary>
/// The surface the runner depends on, mirroring the TypeScript and Python
/// EvaluationApi so all three describe the same lifecycle.
/// </summary>
internal interface IEvaluationApi
{
    Task<string> CreateExperimentAsync(CreateExperimentDto options, CancellationToken cancellationToken);

    Task<IReadOnlyList<DatasetRevisionDataItemDto>> FetchDatasetRevisionItemsAsync(
        string datasetId, string revision, CancellationToken cancellationToken);

    Task SubmitResultsAsync(string experimentId, IReadOnlyList<ItemResult> results, CancellationToken cancellationToken);

    Task StartExperimentAsync(string experimentId, CancellationToken cancellationToken);

    Task<string> GetExperimentStatusAsync(string experimentId, CancellationToken cancellationToken);

    Task CancelExperimentAsync(string experimentId);

    Task<GateVerdict> GateExperimentAsync(
        string experimentId,
        IReadOnlyDictionary<string, double> thresholds,
        GateProvenance provenance,
        CancellationToken cancellationToken);
}

internal sealed class HttpEvaluationApi : IEvaluationApi
{
    private readonly AxonPushClient _client;

    public HttpEvaluationApi(AxonPushClient client)
    {
        _client = client;
    }

    public static double ParseRevision(string revision) =>
        double.TryParse(revision, NumberStyles.Integer, CultureInfo.InvariantCulture, out var value)
            ? value
            : throw new EvaluationApiException($"--revision must be a number, got \"{revision}\"");

    public async Task<string> CreateExperimentAsync(
        CreateExperimentDto options,
        CancellationToken cancellationToken)
    {
        var created = await _client.Experiments.CreateAsync(options, cancellationToken)
            .ConfigureAwait(false);
        return string.IsNullOrEmpty(created?.ExperimentId)
            ? throw new EvaluationApiException("The API did not return an experiment id")
            : created.ExperimentId;
    }

    public async Task<IReadOnlyList<DatasetRevisionDataItemDto>> FetchDatasetRevisionItemsAsync(
        string datasetId,
        string revision,
        CancellationToken cancellationToken)
    {
        var response = await _client.Datasets
            .ItemsAsync(datasetId, ParseRevision(revision), cancellationToken)
            .ConfigureAwait(false);
        return response?.Data is null
            ? throw new EvaluationApiException("Dataset revision items response was invalid")
            : [.. response.Data];
    }

    public Task SubmitResultsAsync(
        string experimentId,
        IReadOnlyList<ItemResult> results,
        CancellationToken cancellationToken) =>
        _client.Experiments.SubmitResultsAsync(
            experimentId,
            new SubmitLocalExperimentResultsDto
            {
                Results = [.. results.Select(item => new LocalExperimentResultDto
                {
                    ItemId = item.ItemId,
                    Output = item.Output!,
                    Error = item.Error,
                    LatencyMs = item.LatencyMs,
                    TotalTokens = item.TotalTokens,
                    CostUsd = item.CostUsd,
                    TraceId = item.TraceId,
                })],
            },
            cancellationToken);

    public Task StartExperimentAsync(string experimentId, CancellationToken cancellationToken) =>
        _client.Experiments.RunAsync(experimentId, cancellationToken);

    public async Task<string> GetExperimentStatusAsync(
        string experimentId,
        CancellationToken cancellationToken)
    {
        var experiment = await _client.Experiments.GetAsync(experimentId, cancellationToken)
            .ConfigureAwait(false);
        return experiment is null
            ? throw new EvaluationApiException("Experiment status response was invalid")
            : experiment.Status.ToString().ToLowerInvariant();
    }

    public Task CancelExperimentAsync(string experimentId) =>
        _client.Experiments.CancelAsync(experimentId);

    public async Task<GateVerdict> GateExperimentAsync(
        string experimentId,
        IReadOnlyDictionary<string, double> thresholds,
        GateProvenance provenance,
        CancellationToken cancellationToken)
    {
        var body = new ExperimentGateDto
        {
            MinScore = Read(thresholds, "minScore"),
            MaxFailureRate = Read(thresholds, "maxFailureRate"),
            MaxLatencyMs = Read(thresholds, "maxLatencyMs"),
            MaxCostUsd = Read(thresholds, "maxCostUsd"),
            MinScoreDelta = Read(thresholds, "minScoreDelta"),
            MaxLatencyIncreasePercent = Read(thresholds, "maxLatencyIncreasePercent"),
            MaxCostIncreasePercent = Read(thresholds, "maxCostIncreasePercent"),
            Source = Source(provenance.Source),
            GitCommit = provenance.GitCommit,
            GitBranch = provenance.GitBranch,
        };

        ExperimentGateResultDto? verdict;
        try
        {
            verdict = await _client.Experiments.GateAsync(experimentId, body, cancellationToken)
                .ConfigureAwait(false);
        }
        catch (AxonPushApiException exception) when (exception.StatusCode == 400 && Attributed(body))
        {
            // The API validates with forbidNonWhitelisted, so a server older
            // than the provenance fields rejects the whole call. Losing the
            // commit attribution beats failing every run in a pipeline we
            // cannot upgrade.
            WarnOnce(
                "This axonpush server does not accept source, gitCommit, gitBranch on the gate. "
                + "The decision will be recorded without them; upgrade the server to attribute "
                + "it to a commit.");
            body.Source = null;
            body.GitCommit = null;
            body.GitBranch = null;
            body.Release = null;
            verdict = await _client.Experiments.GateAsync(experimentId, body, cancellationToken)
                .ConfigureAwait(false);
        }

        return verdict is null
            ? throw new EvaluationApiException("Gate response was invalid")
            : new GateVerdict
            {
                Passed = verdict.Passed,
                Reasons = [.. verdict.Reasons],
                Metrics = Metrics(verdict.Metrics),
                GateRunId = verdict.GateRunId,
            };
    }

    private static GateRunSource? Source(string? source) =>
        Enum.TryParse<GateRunSource>(source, ignoreCase: true, out var parsed) ? parsed : null;

    private static bool Attributed(ExperimentGateDto body) =>
        body.Source is not null || body.GitCommit is not null || body.GitBranch is not null
        || body.Release is not null;

    private static bool _warned;

    private static void WarnOnce(string message)
    {
        if (_warned)
        {
            return;
        }

        _warned = true;
        Console.Error.WriteLine($"axonpush: {message}");
    }

    private static double? Read(IReadOnlyDictionary<string, double> thresholds, string key) =>
        thresholds.TryGetValue(key, out var value) ? value : null;

    private static Dictionary<string, object?> Metrics(object? metrics) =>
        metrics is IDictionary<string, object?> typed
            ? new Dictionary<string, object?>(typed)
            : [];
}
