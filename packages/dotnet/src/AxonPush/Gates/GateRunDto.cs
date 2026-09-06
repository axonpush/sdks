namespace AxonPush.Gates;

/// <summary>A recorded release-gate decision for one experiment.</summary>
public sealed record GateRunDto
{
    /// <summary>Organisation the run belongs to.</summary>
    public required string OrgId { get; init; }

    /// <summary>Identifier for this gate decision.</summary>
    public required string GateRunId { get; init; }

    /// <summary>The experiment that was gated.</summary>
    public required string ExperimentId { get; init; }

    /// <summary>Whether the gate passed.</summary>
    public required bool Passed { get; init; }

    /// <summary>Human-readable reasons behind the decision.</summary>
    public required IReadOnlyList<string> Reasons { get; init; }

    /// <summary>The metrics the decision was made against, keyed by metric name.</summary>
    public required IReadOnlyDictionary<string, object?> Metrics { get; init; }

    /// <summary>The thresholds applied, keyed by name.</summary>
    public required IReadOnlyDictionary<string, double> Thresholds { get; init; }

    /// <summary>Where the decision came from, one of "cli", "api", "ui".</summary>
    public required string Source { get; init; }

    /// <summary>When the decision was recorded.</summary>
    public required DateTimeOffset CreatedAt { get; init; }

    /// <summary>The baseline experiment compared against, when any.</summary>
    public string? BaselineExperimentId { get; init; }

    /// <summary>The dataset the run covered.</summary>
    public string? DatasetId { get; init; }

    /// <summary>The evaluation target the run covered.</summary>
    public string? TargetId { get; init; }

    /// <summary>Git branch the run was attributed to.</summary>
    public string? GitBranch { get; init; }

    /// <summary>Git commit the run was attributed to.</summary>
    public string? GitCommit { get; init; }

    /// <summary>Release label the run was attributed to.</summary>
    public string? Release { get; init; }
}
