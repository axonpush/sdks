namespace AxonPush.Gates;

/// <summary>A page of release-gate policies.</summary>
public sealed record GatePolicyListDto
{
    /// <summary>The policies.</summary>
    public required IReadOnlyList<GatePolicyDto> Data { get; init; }
}
