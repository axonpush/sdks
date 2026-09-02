using System.Collections.Concurrent;
using System.Diagnostics;
using System.Globalization;
using System.Text.Json;
using AxonPush.Internal.Api;

namespace AxonPush.Cli;

internal sealed record RunnerOptions
{
    public required string DatasetId { get; init; }
    public required string DatasetRevision { get; init; }
    public required string ExperimentId { get; init; }
    public required string Command { get; init; }
    public int Concurrency { get; init; } = 4;
    public double TimeoutSeconds { get; init; } = 30;
    public double StartupTimeoutSeconds { get; init; } = 30;
    public JsonElement? Configuration { get; init; }
}

/// <summary>
/// Runs each dataset example through a local evaluator command, following the
/// same lifecycle as the TypeScript and Python runners: start the experiment,
/// wait for it to be running, submit each result as it lands, and cancel the
/// experiment on interrupt rather than leaving it running.
///
/// The evaluator executes on the caller's host. No customer code is uploaded.
/// </summary>
internal static class Runner
{
    private const string NoOutput =
        "Evaluator command did not emit a JSON object with an output field";

    private static readonly string[] TerminalStatuses = ["failed", "cancelled", "completed"];

    public static async Task<RunResult> RunAsync(
        IEvaluationApi api,
        RunnerOptions options,
        CancellationTokenSource cancellation)
    {
        var startedAt = Timestamp();
        var lineage = Git.Capture();
        var results = new ConcurrentBag<ItemResult>();
        IReadOnlyList<DatasetRevisionDataItemDto> items = [];

        try
        {
            await api.StartExperimentAsync(options.ExperimentId, cancellation.Token)
                .ConfigureAwait(false);
            await WaitForRunningAsync(api, options, cancellation.Token).ConfigureAwait(false);
            items = await api
                .FetchDatasetRevisionItemsAsync(
                    options.DatasetId, options.DatasetRevision, cancellation.Token)
                .ConfigureAwait(false);
        }
        catch (OperationCanceledException)
        {
            await cancellation.CancelAsync().ConfigureAwait(false);
        }

        Exception? submissionFailure = null;
        if (items.Count > 0 && !cancellation.IsCancellationRequested)
        {
            await Parallel.ForEachAsync(
                items,
                new ParallelOptions { MaxDegreeOfParallelism = Math.Max(1, options.Concurrency) },
                async (item, _) =>
                {
                    if (cancellation.IsCancellationRequested)
                    {
                        return;
                    }

                    var result = await EvaluateAsync(options, item, cancellation.Token)
                        .ConfigureAwait(false);
                    results.Add(result);
                    if (result.Status == "cancelled")
                    {
                        await cancellation.CancelAsync().ConfigureAwait(false);
                        return;
                    }

                    try
                    {
                        await api.SubmitResultsAsync(options.ExperimentId, [result], CancellationToken.None)
                            .ConfigureAwait(false);
                    }
                    catch (Exception exception) when (exception is not OperationCanceledException)
                    {
                        submissionFailure ??= exception;
                        await cancellation.CancelAsync().ConfigureAwait(false);
                    }
                }).ConfigureAwait(false);
        }

        var cancelled = cancellation.IsCancellationRequested && submissionFailure is null;
        if (cancelled)
        {
            try
            {
                await api.CancelExperimentAsync(options.ExperimentId).ConfigureAwait(false);
            }
            catch (Exception exception) when (exception is not OutOfMemoryException)
            {
                // The local cancellation is authoritative; the exit code stands.
            }
        }

        if (submissionFailure is not null)
        {
            throw submissionFailure;
        }

        return new RunResult
        {
            ExperimentId = options.ExperimentId,
            DatasetId = options.DatasetId,
            DatasetRevision = options.DatasetRevision,
            StartedAt = startedAt,
            CompletedAt = Timestamp(),
            Cancelled = cancelled,
            Lineage = lineage,
            Results = [.. results.OrderBy(item => item.ItemId, StringComparer.Ordinal)],
        };
    }

    private static string Timestamp() =>
        DateTimeOffset.UtcNow.ToString("yyyy-MM-ddTHH:mm:ss.fffZ", CultureInfo.InvariantCulture);

    private static async Task WaitForRunningAsync(
        IEvaluationApi api,
        RunnerOptions options,
        CancellationToken cancellationToken)
    {
        var deadline = DateTimeOffset.UtcNow.AddSeconds(options.StartupTimeoutSeconds);
        while (DateTimeOffset.UtcNow <= deadline)
        {
            cancellationToken.ThrowIfCancellationRequested();
            var status = await api.GetExperimentStatusAsync(options.ExperimentId, cancellationToken)
                .ConfigureAwait(false);
            if (status == "running")
            {
                return;
            }

            if (TerminalStatuses.Contains(status))
            {
                throw new EvaluationApiException(
                    $"Experiment {options.ExperimentId} entered {status} before local execution started");
            }

            await Task.Delay(250, cancellationToken).ConfigureAwait(false);
        }

        throw new EvaluationApiException(
            $"Experiment {options.ExperimentId} did not reach running within {options.StartupTimeoutSeconds:G}s");
    }

    private static async Task<ItemResult> EvaluateAsync(
        RunnerOptions options,
        DatasetRevisionDataItemDto item,
        CancellationToken cancellationToken)
    {
        var itemId = item.ItemId ?? string.Empty;
        var payload = JsonSerializer.Serialize(new Dictionary<string, object?>
        {
            ["type"] = "axonpush.evaluation.input",
            ["experimentId"] = options.ExperimentId,
            ["item"] = new Dictionary<string, object?> { ["id"] = itemId, ["input"] = item.Input },
            ["configuration"] = options.Configuration,
        });

        var clock = Stopwatch.StartNew();
        using var timeout = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        timeout.CancelAfter(TimeSpan.FromSeconds(options.TimeoutSeconds));

        try
        {
            var (exitCode, stdout, stderr) = await ExecuteAsync(options.Command, payload, timeout.Token)
                .ConfigureAwait(false);
            if (exitCode != 0)
            {
                return Failed(itemId, clock, stderr.Trim().Length > 0
                    ? stderr.Trim()
                    : $"Evaluator exited with code {exitCode}");
            }

            var output = ReadOutput(stdout);
            var error = Text(output, "error");
            return new ItemResult
            {
                ItemId = itemId,
                Status = error is null ? "passed" : "failed",
                Output = Value(output, "output"),
                Error = error,
                LatencyMs = clock.Elapsed.TotalMilliseconds,
                TotalTokens = Number(output, "totalTokens"),
                CostUsd = Number(output, "costUsd"),
                TraceId = Text(output, "traceId"),
            };
        }
        catch (OperationCanceledException) when (cancellationToken.IsCancellationRequested)
        {
            return new ItemResult
            {
                ItemId = itemId,
                Status = "cancelled",
                Error = "Evaluation was cancelled",
                LatencyMs = clock.Elapsed.TotalMilliseconds,
            };
        }
        catch (OperationCanceledException)
        {
            return Failed(itemId, clock,
                $"Evaluator timed out after {options.TimeoutSeconds:G}s");
        }
        catch (Exception exception) when (exception is not OutOfMemoryException)
        {
            return Failed(itemId, clock, exception.Message);
        }
    }

    private static ItemResult Failed(string itemId, Stopwatch clock, string error) => new()
    {
        ItemId = itemId,
        Status = "failed",
        Error = error,
        LatencyMs = clock.Elapsed.TotalMilliseconds,
    };

    private static async Task<(int ExitCode, string StdOut, string StdErr)> ExecuteAsync(
        string command,
        string payload,
        CancellationToken cancellationToken)
    {
        // The command is a shell string by design: it runs only on the caller's
        // machine and makes ordinary CI commands ergonomic.
        var startInfo = new ProcessStartInfo(OperatingSystem.IsWindows() ? "cmd.exe" : "/bin/sh")
        {
            RedirectStandardInput = true,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true,
        };
        if (OperatingSystem.IsWindows())
        {
            // `/d /s /c "..."` is cmd's "strip the outer quotes, take the rest
            // verbatim" form. Passing the command through ArgumentList instead
            // re-quotes it and cmd then treats the quotes as part of the path.
            startInfo.Arguments = $"/d /s /c \"{command}\"";
        }
        else
        {
            startInfo.ArgumentList.Add("-c");
            startInfo.ArgumentList.Add(command);
        }

        using var process = new Process { StartInfo = startInfo };
        process.Start();

        await process.StandardInput.WriteLineAsync(payload).ConfigureAwait(false);
        process.StandardInput.Close();

        var stdout = process.StandardOutput.ReadToEndAsync(cancellationToken);
        var stderr = process.StandardError.ReadToEndAsync(cancellationToken);
        try
        {
            await process.WaitForExitAsync(cancellationToken).ConfigureAwait(false);
        }
        catch (OperationCanceledException)
        {
            process.Kill(entireProcessTree: true);
            throw;
        }

        return (process.ExitCode,
            await stdout.ConfigureAwait(false),
            await stderr.ConfigureAwait(false));
    }

    /// <summary>The last JSON line carrying an `output` field wins; diagnostics may precede it.</summary>
    private static JsonElement ReadOutput(string stdout)
    {
        var lines = stdout
            .Split('\n', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Reverse();
        foreach (var line in lines)
        {
            try
            {
                var parsed = JsonDocument.Parse(line).RootElement;
                if (parsed.ValueKind == JsonValueKind.Object && parsed.TryGetProperty("output", out _))
                {
                    return parsed;
                }
            }
            catch (JsonException)
            {
                // Keep looking for the single protocol result line.
            }
        }

        throw new EvaluationApiException(NoOutput);
    }

    private static JsonElement? Value(JsonElement element, string name) =>
        element.TryGetProperty(name, out var property) ? property.Clone() : null;

    private static string? Text(JsonElement element, string name) =>
        element.TryGetProperty(name, out var property) && property.ValueKind == JsonValueKind.String
            ? property.GetString()
            : null;

    private static double? Number(JsonElement element, string name) =>
        element.TryGetProperty(name, out var property) && property.ValueKind == JsonValueKind.Number
            ? property.GetDouble()
            : null;
}
