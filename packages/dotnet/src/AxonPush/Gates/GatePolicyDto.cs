namespace AxonPush.Gates;

/// <summary>
/// A release-gate policy: the thresholds a candidate experiment must clear for a
/// given scope (a dataset or an evaluation target).
/// </summary>
public sealed record GatePolicyDto
{
    /// <summary>Organisation the policy belongs to.</summary>
    public required string OrgId { get; init; }

    /// <summary>Scope kind, one of <see cref="GatePolicyScope"/>.</summary>
    public required string ScopeType { get; init; }

    /// <summary>The dataset or evaluation-target id the policy applies to.</summary>
    public required string ScopeId { get; init; }

    /// <summary>Whether the policy is currently resolved when a gate runs.</summary>
    public required bool Enabled { get; init; }

    /// <summary>When the policy was created.</summary>
    public required DateTimeOffset CreatedAt { get; init; }

    /// <summary>When the policy was last updated.</summary>
    public required DateTimeOffset UpdatedAt { get; init; }

    /// <summary>Who created the policy.</summary>
    public string? CreatedBy { get; init; }

    /// <summary>Human-readable name.</summary>
    public string? Name { get; init; }

    /// <summary>Free-form description.</summary>
    public string? Description { get; init; }

    /// <summary>Minimum absolute score the candidate must reach.</summary>
    public double? MinScore { get; init; }

    /// <summary>Smallest score change against the baseline that still passes. Usually negative.</summary>
    public double? MinScoreDelta { get; init; }

    /// <summary>Maximum share of dataset items allowed to error, 0-1.</summary>
    public double? MaxFailureRate { get; init; }

    /// <summary>Maximum mean latency in milliseconds.</summary>
    public double? MaxLatencyMs { get; init; }

    /// <summary>Maximum total run cost in USD.</summary>
    public double? MaxCostUsd { get; init; }

    /// <summary>Maximum latency increase against the baseline, in percent.</summary>
    public double? MaxLatencyIncreasePercent { get; init; }

    /// <summary>Maximum cost increase against the baseline, in percent.</summary>
    public double? MaxCostIncreasePercent { get; init; }
}
