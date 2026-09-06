namespace AxonPush.Gates;

/// <summary>A page of recorded release-gate decisions.</summary>
public sealed record GateRunListDto
{
    /// <summary>The gate runs.</summary>
    public required IReadOnlyList<GateRunDto> Data { get; init; }

    /// <summary>Cursor for the next page, or null when there are no more.</summary>
    public string? Cursor { get; init; }
}
