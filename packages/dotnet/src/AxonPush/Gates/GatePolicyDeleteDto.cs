namespace AxonPush.Gates;

/// <summary>The outcome of deleting a release-gate policy.</summary>
public sealed record GatePolicyDeleteDto
{
    /// <summary>Whether a policy was deleted.</summary>
    public required bool Deleted { get; init; }
}
