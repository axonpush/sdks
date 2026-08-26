using System.Globalization;
using Microsoft.Extensions.Configuration;

namespace AxonPush;

/// <summary>
/// Configuration for an <see cref="AxonPushClient"/>.
/// </summary>
public sealed class AxonPushOptions
{
    /// <summary>API key. Maps to env var <c>AXONPUSH_API_KEY</c>.</summary>
    public string? ApiKey { get; set; }

    /// <summary>
    /// Default channel for published events. Maps to env var
    /// <c>AXONPUSH_CHANNEL_ID</c>, which every other SDK reads and this one did
    /// not, so a channel had to be supplied in code.
    /// </summary>
    public string? ChannelId { get; set; }

    /// <summary>Tenant identifier. Maps to env var <c>AXONPUSH_TENANT_ID</c>.</summary>
    public string? TenantId { get; set; }

    /// <summary>Base URL of the AxonPush API. Defaults to the public hosted endpoint.</summary>
    public Uri BaseUrl { get; set; } = new("https://api.axonpush.xyz");

    /// <summary>Environment tag emitted on every published event (e.g. "production").</summary>
    public string? Environment { get; set; }

    /// <summary>Per-request timeout. Defaults to 30 seconds.</summary>
    public TimeSpan Timeout { get; set; } = TimeSpan.FromSeconds(30);

    /// <summary>Maximum retry attempts on transient failure. Defaults to 3.</summary>
    public int MaxRetries { get; set; } = 3;

    /// <summary>
    /// When true (the default), the client swallows transient publish failures and logs them as
    /// warnings rather than throwing. Set to false to surface errors to callers.
    /// </summary>
    public bool FailOpen { get; set; } = true;

    /// <summary>
    /// Loads options from the supplied configuration (or environment variables when none is
    /// supplied). Recognises the standard <c>AXONPUSH_*</c> keys.
    /// </summary>
    public static AxonPushOptions FromEnvironment(IConfiguration? configuration = null)
    {
        configuration ??= new ConfigurationBuilder().AddEnvironmentVariables().Build();
        var options = new AxonPushOptions();
        options.ApplyFrom(configuration);
        return options;
    }

    internal void ApplyFrom(IConfiguration configuration)
    {
        ApiKey ??= configuration["AXONPUSH_API_KEY"];
        TenantId ??= configuration["AXONPUSH_TENANT_ID"];
        ChannelId ??= configuration["AXONPUSH_CHANNEL_ID"];

        var baseUrl = configuration["AXONPUSH_BASE_URL"];
        if (!string.IsNullOrWhiteSpace(baseUrl))
        {
            BaseUrl = new Uri(baseUrl);
        }

        Environment ??= configuration["AXONPUSH_ENVIRONMENT"];

        var timeout = configuration["AXONPUSH_TIMEOUT"];
        if (double.TryParse(timeout, NumberStyles.Float, CultureInfo.InvariantCulture, out var seconds) && seconds > 0)
        {
            Timeout = TimeSpan.FromSeconds(seconds);
        }

        var retries = configuration["AXONPUSH_MAX_RETRIES"];
        if (int.TryParse(retries, NumberStyles.Integer, CultureInfo.InvariantCulture, out var max) && max >= 0)
        {
            MaxRetries = max;
        }

        var failOpen = configuration["AXONPUSH_FAIL_OPEN"];
        if (!string.IsNullOrWhiteSpace(failOpen) && bool.TryParse(failOpen, out var parsed))
        {
            FailOpen = parsed;
        }
    }

    internal void Validate()
    {
        if (string.IsNullOrWhiteSpace(ApiKey))
        {
            throw new InvalidOperationException("AxonPushOptions.ApiKey is required (set AXONPUSH_API_KEY).");
        }

        if (string.IsNullOrWhiteSpace(TenantId))
        {
            throw new InvalidOperationException("AxonPushOptions.TenantId is required (set AXONPUSH_TENANT_ID).");
        }

        if (MaxRetries < 0)
        {
            throw new InvalidOperationException("AxonPushOptions.MaxRetries must be zero or greater.");
        }

        if (Timeout <= TimeSpan.Zero)
        {
            throw new InvalidOperationException("AxonPushOptions.Timeout must be positive.");
        }
    }
}
