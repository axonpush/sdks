using AxonPush.Events;
using AxonPush.Operations;
using AxonPush.Internal;
using Microsoft.Extensions.Logging;

namespace AxonPush;

/// <summary>
/// Entry point for the AxonPush HTTP API. Construct one client per application, treat it as a
/// singleton, and dispose at shutdown.
/// </summary>
public sealed class AxonPushClient : IDisposable, IAsyncDisposable
{
    private readonly AxonPushTransport _transport;
    internal object ContextOwner => _transport;
    public RequestContextScope BeginContext(RequestContext context) => new(this, context);
    public void AnnotateActivity(System.Diagnostics.Activity activity) { var context = RequestContextScope.Read(_transport); if (context is null) return; foreach (var p in RequestContextScope.Attributes(context)) activity.SetTag(p.Key, p.Value is IReadOnlyDictionary<string, string> ? System.Text.Json.JsonSerializer.Serialize(p.Value) : p.Value); }

    public AxonPushClient(AxonPushOptions options, ILoggerFactory? loggerFactory = null)
        : this(options, null, loggerFactory)
    {
    }

    /// <summary>Use a caller-owned HTTP client. Its handler must disable automatic redirects
    /// (<c>AllowAutoRedirect = false</c>) to keep custom API-key headers at the configured endpoint.
    /// The SDK cannot inspect or change an injected client's handler.</summary>
    public AxonPushClient(AxonPushOptions options, HttpClient? httpClient, ILoggerFactory? loggerFactory = null)
    {
        ArgumentNullException.ThrowIfNull(options);
        _transport = new AxonPushTransport(options, httpClient, loggerFactory);
        Events = new EventsResource(_transport);
        Audit = new AuditResource(_transport);
        AuditProduct = new AuditProductResource(_transport);
        Workspaces = new WorkspacesResource(_transport);
        Workflows = new WorkflowsResource(_transport);
        Templates = new TemplatesResource(_transport);
        Observations = new ObservationsResource(_transport);
        Activity = new ActivityResource(_transport);
        Telemetry = new TelemetryResource(_transport);
        Capabilities = new CapabilitiesResource(_transport);

    }

    /// <summary>The events resource (POST /event).</summary>
    public EventsResource Events { get; }
    public AuditResource Audit { get; }
    public AuditProductResource AuditProduct { get; }
    public WorkspacesResource Workspaces { get; }
    public WorkflowsResource Workflows { get; }
    public TemplatesResource Templates { get; }
    public ObservationsResource Observations { get; }
    public ActivityResource Activity { get; }
    public TelemetryResource Telemetry { get; }
    public CapabilitiesResource Capabilities { get; }


    public void Dispose()
    {
        _transport.Dispose();
    }

    public ValueTask DisposeAsync()
    {
        _transport.Dispose();
        return ValueTask.CompletedTask;
    }
}
