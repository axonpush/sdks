using System.Diagnostics;
using System.Reflection;

namespace AxonPush.Internal;

/// <summary>
/// Stamps the axonpush headers on every request. It lives in the pipeline
/// rather than in one publish method so the generated API clients are
/// authenticated the same way the events path is.
/// </summary>
internal sealed class AxonPushHeaderHandler : DelegatingHandler
{
    private static readonly string UserAgent =
        $"axonpush-dotnet/{typeof(AxonPushHeaderHandler).Assembly.GetName().Version?.ToString(3) ?? "0.0.0"}";

    private readonly AxonPushOptions _options;

    public AxonPushHeaderHandler(AxonPushOptions options)
    {
        _options = options;
    }

    protected override Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
    {
        Stamp(request, "X-API-Key", _options.ApiKey);
        Stamp(request, "x-tenant-id", _options.TenantId);
        Stamp(request, "X-Axonpush-Environment", _options.Environment);

        var current = Activity.Current;
        if (current is not null && current.TraceId != default)
        {
            Stamp(request, "X-Axonpush-Trace-Id", current.TraceId.ToHexString());
        }

        if (request.Headers.UserAgent.Count == 0)
        {
            request.Headers.TryAddWithoutValidation("User-Agent", UserAgent);
        }

        return base.SendAsync(request, cancellationToken);
    }

    private static void Stamp(HttpRequestMessage request, string name, string? value)
    {
        if (!string.IsNullOrWhiteSpace(value) && !request.Headers.Contains(name))
        {
            request.Headers.Add(name, value);
        }
    }
}
