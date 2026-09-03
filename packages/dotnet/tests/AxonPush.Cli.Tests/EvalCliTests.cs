using System.Text.Json;
using Xunit;

namespace AxonPush.Cli.Tests;

/// <summary>The gate is the product claim; these hold it to the contract.</summary>
public class ThresholdTests
{
    // forbidNonWhitelisted: these are the seven names the gate accepts.
    private static readonly HashSet<string> AcceptedWireNames =
    [
        "minScore",
        "maxFailureRate",
        "maxLatencyMs",
        "maxCostUsd",
        "minScoreDelta",
        "maxLatencyIncreasePercent",
        "maxCostIncreasePercent",
    ];

    [Fact]
    public void EveryThresholdMapsOntoANameTheApiAccepts()
    {
        Assert.Equal(AcceptedWireNames, Thresholds.Options.Select(option => option.Wire).ToHashSet());
    }

    [Fact]
    public void UnsetThresholdsAreOmittedRatherThanSentAsZero()
    {
        var wire = Thresholds.ToWire(Thresholds.Options.ToDictionary(o => o.Flag, _ => (double?)null));

        Assert.Empty(wire);
    }

    [Fact]
    public void ADeliberateZeroSurvives()
    {
        var wire = Thresholds.ToWire(new Dictionary<string, double?> { ["minimum-score"] = 0 });

        Assert.Equal(0, wire["minScore"]);
    }

    [Fact]
    public void ToleratedRegressionBecomesAMinimumDelta()
    {
        var wire = Thresholds.ToWire(new Dictionary<string, double?> { ["max-score-regression"] = 0.02 });

        Assert.Equal(-0.02, wire["minScoreDelta"], 6);
    }

    [Fact]
    public void RatiosBecomePercentages()
    {
        var wire = Thresholds.ToWire(new Dictionary<string, double?>
        {
            ["max-latency-increase-ratio"] = 0.1,
            ["max-cost-increase-ratio"] = 0.25,
        });

        Assert.Equal(10, wire["maxLatencyIncreasePercent"], 6);
        Assert.Equal(25, wire["maxCostIncreasePercent"], 6);
    }
}

public class ReportTests
{
    private static RunResult Run(GateVerdict? gate = null, params ItemResult[] results) => new()
    {
        ExperimentId = "exp_1",
        DatasetId = "ds_1",
        DatasetRevision = "3",
        StartedAt = "2026-09-02T00:00:00.000Z",
        CompletedAt = "2026-09-02T00:00:01.000Z",
        Results = results,
        Gate = gate,
    };

    [Fact]
    public void JsonReportCarriesEveryKeyTheOtherCliisEmit()
    {
        var report = JsonDocument.Parse(Reports.ToJsonReport(Run())).RootElement;

        foreach (var key in new[]
        {
            "experimentId", "datasetId", "datasetRevision", "startedAt",
            "completedAt", "cancelled", "lineage", "results", "gate",
        })
        {
            Assert.True(report.TryGetProperty(key, out _), $"missing {key}");
        }
    }

    [Theory]
    [InlineData(true)]
    [InlineData(false)]
    public void JUnitReportsTheGateAsItsOwnCase(bool passed)
    {
        var gate = new GateVerdict
        {
            Passed = passed,
            Reasons = passed ? [] : ["score 0.9 is below 0.95"],
        };

        var xml = Reports.ToJUnitXml(Run(gate, new ItemResult { ItemId = "first", Status = "passed" }));

        Assert.Equal(!passed, xml.Contains("release gate", StringComparison.Ordinal));
        if (!passed)
        {
            Assert.Contains("score 0.9 is below 0.95", xml, StringComparison.Ordinal);
        }
    }

    [Fact]
    public void JUnitCarriesClassnameAndTiming()
    {
        var xml = Reports.ToJUnitXml(
            Run(null, new ItemResult { ItemId = "first", Status = "passed", LatencyMs = 218 }));

        Assert.Contains("classname=\"axonpush.evaluation\"", xml, StringComparison.Ordinal);
        Assert.Contains("time=\"0.218\"", xml, StringComparison.Ordinal);
        Assert.Contains("timestamp=\"2026-09-02T00:00:00.000Z\"", xml, StringComparison.Ordinal);
    }

    [Fact]
    public void SummaryNamesTheCommitWhenThereIsOne()
    {
        var run = Run(null, new ItemResult { ItemId = "first", Status = "passed" });
        var withCommit = new RunResult
        {
            ExperimentId = run.ExperimentId,
            DatasetId = run.DatasetId,
            DatasetRevision = run.DatasetRevision,
            StartedAt = run.StartedAt,
            Results = run.Results,
            Lineage = new GitLineage { GitCommit = "0123456789abcdef" },
        };

        Assert.Contains("`0123456789ab`", Reports.ToGitHubSummary(withCommit), StringComparison.Ordinal);
        Assert.Contains("| — |", Reports.ToGitHubSummary(run), StringComparison.Ordinal);
    }
}

public class ArgumentTests
{
    [Fact]
    public void RepeatedEvaluatorsAreAllKept()
    {
        var parsed = Arguments.Parse(["run", "--evaluator", "a@1", "--evaluator", "b@2"]);

        Assert.Equal(["a", "b"], parsed.Evaluators().Select(e => e.EvaluatorId));
    }

    [Fact]
    public void AnEvaluatorWithoutAVersionIsAUsageError()
    {
        var parsed = Arguments.Parse(["run", "--evaluator", "a"]);

        Assert.Throws<ArgumentException>(() => parsed.Evaluators().ToList());
    }

    [Fact]
    public void AFlagWithoutAValueIsAUsageError()
    {
        Assert.Throws<ArgumentException>(() => Arguments.Parse(["run", "--dataset"]));
    }

    [Fact]
    public void InlineValuesParse()
    {
        Assert.Equal("ds_1", Arguments.Parse(["run", "--dataset=ds_1"]).Value("dataset"));
    }
}
