using System.Globalization;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace AxonPush.Cli;

internal sealed class ItemResult
{
    [JsonPropertyName("itemId")] public string ItemId { get; init; } = string.Empty;
    [JsonPropertyName("status")] public string Status { get; init; } = "failed";
    [JsonPropertyName("output")] public object? Output { get; init; }
    [JsonPropertyName("error")] public string? Error { get; init; }
    [JsonPropertyName("latencyMs")] public double LatencyMs { get; init; }
    [JsonPropertyName("totalTokens")] public double? TotalTokens { get; init; }
    [JsonPropertyName("costUsd")] public double? CostUsd { get; init; }
    [JsonPropertyName("traceId")] public string? TraceId { get; init; }
}

internal sealed class GateVerdict
{
    [JsonPropertyName("passed")] public bool Passed { get; init; }
    [JsonPropertyName("reasons")] public IReadOnlyList<string> Reasons { get; init; } = [];
    [JsonPropertyName("metrics")]
    public IReadOnlyDictionary<string, object?> Metrics { get; init; }
        = new Dictionary<string, object?>();
    [JsonPropertyName("gateRunId")] public string? GateRunId { get; init; }
}

internal sealed class GitLineage
{
    [JsonPropertyName("gitCommit")] public string? GitCommit { get; init; }
    [JsonPropertyName("gitBranch")] public string? GitBranch { get; init; }
    [JsonPropertyName("gitDirty")] public bool? GitDirty { get; init; }
}

internal sealed class RunResult
{
    [JsonPropertyName("experimentId")] public string ExperimentId { get; init; } = string.Empty;
    [JsonPropertyName("datasetId")] public string DatasetId { get; init; } = string.Empty;
    [JsonPropertyName("datasetRevision")] public string DatasetRevision { get; init; } = string.Empty;
    [JsonPropertyName("startedAt")] public string StartedAt { get; init; } = string.Empty;
    [JsonPropertyName("completedAt")] public string CompletedAt { get; set; } = string.Empty;
    [JsonPropertyName("cancelled")] public bool Cancelled { get; set; }
    [JsonPropertyName("lineage")] public GitLineage Lineage { get; init; } = new();
    [JsonPropertyName("results")] public IReadOnlyList<ItemResult> Results { get; set; } = [];
    [JsonPropertyName("gate")] public GateVerdict? Gate { get; set; }
}

/// <summary>
/// Artifacts a CI run leaves behind. Byte-comparable with the TypeScript and
/// Python CLIs, because a pipeline is written against the report, not the
/// language that produced it.
/// </summary>
internal static class Reports
{
    private const string SuiteName = "axonpush.evaluation";

    private static readonly JsonSerializerOptions Json = new()
    {
        WriteIndented = true,
        DefaultIgnoreCondition = JsonIgnoreCondition.Never,
    };

    public static string ToJsonReport(RunResult run) =>
        JsonSerializer.Serialize(run, Json) + "\n";

    private static string Xml(string value) => value
        .Replace("&", "&amp;", StringComparison.Ordinal)
        .Replace("<", "&lt;", StringComparison.Ordinal)
        .Replace(">", "&gt;", StringComparison.Ordinal)
        .Replace("\"", "&quot;", StringComparison.Ordinal)
        .Replace("'", "&apos;", StringComparison.Ordinal);

    public static string ToJUnitXml(RunResult run)
    {
        var blocked = run.Gate is { Passed: false };
        var failures = run.Results.Count(item => item.Status != "passed") + (blocked ? 1 : 0);
        var skipped = run.Results.Count(item => item.Status == "cancelled");
        var builder = new StringBuilder();
        builder.Append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
        builder.Append(CultureInfo.InvariantCulture, $"<testsuite name=\"{SuiteName}\" tests=\"{run.Results.Count + (blocked ? 1 : 0)}\" failures=\"{failures}\" skipped=\"{skipped}\" timestamp=\"{Xml(run.StartedAt)}\">\n");

        foreach (var item in run.Results)
        {
            var attrs = string.Create(
                CultureInfo.InvariantCulture,
                $"classname=\"{SuiteName}\" name=\"{Xml(item.ItemId)}\" time=\"{item.LatencyMs / 1000:F3}\"");
            if (item.Status == "passed")
            {
                builder.Append(CultureInfo.InvariantCulture, $"  <testcase {attrs}/>\n");
                continue;
            }

            var kind = item.Status == "cancelled" ? "skipped" : "failure";
            builder.Append(CultureInfo.InvariantCulture,
                $"  <testcase {attrs}><{kind} message=\"{Xml(item.Error ?? item.Status)}\"/></testcase>\n");
        }

        if (run.Gate is { Passed: false } gate)
        {
            // The gate is the point of the run, so CI should show it as a failing
            // test rather than only as a non-zero exit code.
            builder.Append(CultureInfo.InvariantCulture,
                $"  <testcase classname=\"{SuiteName}\" name=\"release gate\" time=\"0.000\"><failure message=\"gate failed\">{Xml(string.Join("; ", gate.Reasons))}</failure></testcase>\n");
        }

        builder.Append("</testsuite>\n");
        return builder.ToString();
    }

    public static string ToGitHubSummary(RunResult run)
    {
        var passed = run.Results.Count(item => item.Status == "passed");
        var failed = run.Results.Count(item => item.Status == "failed");
        var status = run.Cancelled
            ? "Cancelled"
            : run.Gate is { } verdict
                ? verdict.Passed ? "Passed" : "Failed"
                : failed > 0 ? "Completed with failures" : "Passed";
        var commit = run.Lineage.GitCommit;
        var lines = new List<string>
        {
            "## AxonPush evaluation",
            "",
            $"**{status}** · {passed}/{run.Results.Count} item(s) passed"
                + (failed > 0 ? $" · {failed} failed" : string.Empty),
            "",
            "| Experiment | Dataset revision | Commit |",
            "| --- | --- | --- |",
            $"| `{run.ExperimentId}` | `{run.DatasetId}@{run.DatasetRevision}` | "
                + (string.IsNullOrEmpty(commit) ? "—" : $"`{commit[..Math.Min(12, commit.Length)]}`")
                + " |",
        };

        if (run.Gate is { } gate)
        {
            lines.AddRange(["", "### Release gate", "", gate.Passed ? "Gate passed." : "Gate failed."]);
            if (gate.Reasons.Count > 0)
            {
                lines.Add("");
                lines.AddRange(gate.Reasons.Select(reason => $"- {reason}"));
            }
        }

        var unsuccessful = run.Results.Where(item => item.Status != "passed").ToList();
        if (unsuccessful.Count > 0)
        {
            lines.AddRange(["", "### Failed items", ""]);
            lines.AddRange(unsuccessful.Select(item => $"- `{item.ItemId}`: {item.Error ?? item.Status}"));
        }

        return string.Join("\n", lines) + "\n";
    }

    /// <summary>Write an artifact, creating the directory. A missing path is a no-op.</summary>
    public static async Task WriteArtifactAsync(string? path, string contents)
    {
        if (string.IsNullOrWhiteSpace(path))
        {
            return;
        }

        var directory = Path.GetDirectoryName(Path.GetFullPath(path));
        if (!string.IsNullOrEmpty(directory))
        {
            Directory.CreateDirectory(directory);
        }

        await File.WriteAllTextAsync(path, contents).ConfigureAwait(false);
    }
}
