namespace AxonPush.Cli;

/// <summary>One command-line threshold and where it lands on the wire.</summary>
internal sealed record ThresholdOption(string Flag, string Wire, string Help);

/// <summary>
/// The CLI speaks in the terms a reviewer uses — "how far may the score fall",
/// "how much slower may it get" — while the gate endpoint takes a minimum delta
/// and percentages. Two of the conversions are more than a rename, so they live
/// here with the names rather than being scattered through argument parsing.
/// </summary>
internal static class Thresholds
{
    private const string RatioLatency = "max-latency-increase-ratio";
    private const string RatioCost = "max-cost-increase-ratio";
    private const string ScoreRegression = "max-score-regression";

    public static readonly IReadOnlyList<ThresholdOption> Options =
    [
        new("minimum-score", "minScore", "Fail below this absolute score"),
        new("max-failure-rate", "maxFailureRate", "Fail above this share of errored items (0-1)"),
        new("maximum-latency-ms", "maxLatencyMs", "Fail above this mean latency"),
        new("maximum-cost-usd", "maxCostUsd", "Fail above this total run cost"),
        new(ScoreRegression, "minScoreDelta",
            "Fail if the score drops more than this against the baseline"),
        new(RatioLatency, "maxLatencyIncreasePercent",
            "Fail above this latency increase vs baseline (0.1 = 10%)"),
        new(RatioCost, "maxCostIncreasePercent",
            "Fail above this cost increase vs baseline (0.1 = 10%)"),
    ];

    public static Dictionary<string, double> ToWire(IReadOnlyDictionary<string, double?> supplied)
    {
        var body = new Dictionary<string, double>(StringComparer.Ordinal);
        foreach (var option in Options)
        {
            if (!supplied.TryGetValue(option.Flag, out var value) || value is not { } number)
            {
                continue;
            }

            body[option.Wire] = option.Flag switch
            {
                ScoreRegression => -Math.Abs(number),
                RatioLatency or RatioCost => number * 100,
                _ => number,
            };
        }

        return body;
    }
}
