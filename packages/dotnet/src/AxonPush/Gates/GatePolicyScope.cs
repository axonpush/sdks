namespace AxonPush.Gates;

/// <summary>
/// The kinds of thing a release-gate policy can be scoped to. The wire accepts a
/// plain string; these constants spare callers a magic literal.
/// </summary>
public static class GatePolicyScope
{
    /// <summary>The policy applies to a dataset.</summary>
    public const string Dataset = "dataset";

    /// <summary>The policy applies to an evaluation target.</summary>
    public const string Target = "target";
}
