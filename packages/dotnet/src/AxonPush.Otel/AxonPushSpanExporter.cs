using System.Diagnostics;
using System.Reflection;
using AxonPush.Events;
using AxonPush.Otel.Internal;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;
using OpenTelemetry;

namespace AxonPush.Otel;

/// <summary>
/// OpenTelemetry span exporter that maps each <see cref="Activity"/> to an AxonPush
/// <c>app.span</c> event. Wrap in <c>BatchActivityExportProcessor</c> for production workloads.
/// </summary>
public sealed class AxonPushSpanExporter : BaseExporter<Activity>
{
    private readonly AxonPushClient _client;
    private readonly AxonPushSpanExporterOptions _options;
    private readonly Dictionary<string, object?> _resource;
    private readonly ILogger<AxonPushSpanExporter> _logger;

    public AxonPushSpanExporter(
        AxonPushClient client,
        AxonPushSpanExporterOptions options,
        ILoggerFactory? loggerFactory = null)
    {
        ArgumentNullException.ThrowIfNull(client);
        ArgumentNullException.ThrowIfNull(options);
        if (string.IsNullOrWhiteSpace(options.ChannelId))
        {
            throw new ArgumentException("ChannelId is required.", nameof(options));
        }

        _client = client;
        _options = options;
        _logger = (loggerFactory ?? NullLoggerFactory.Instance).CreateLogger<AxonPushSpanExporter>();
        _resource = BuildResource(options);
    }

    public override ExportResult Export(in Batch<Activity> batch)
    {
        var anyFailure = false;

        using (SuppressInstrumentationScope.Begin())
        {
            foreach (var activity in batch)
            {
                if (!TryExport(activity))
                {
                    anyFailure = true;
                }
            }
        }

        return anyFailure ? ExportResult.Failure : ExportResult.Success;
    }

    private bool TryExport(Activity activity)
    {
        try
        {
            var payload = SpanPayloadBuilder.Build(activity, _resource);
            var request = new PublishRequest
            {
                Identifier = activity.SpanId.ToHexString(),
                Payload = payload,
                ChannelId = _options.ChannelId,
                EventType = EventType.AppSpan,
                TraceId = activity.TraceId.ToHexString(),
                SpanId = activity.SpanId.ToHexString(),
                Environment = _options.Environment,
            };

            var result = _client.Events.PublishAsync(request).GetAwaiter().GetResult();
            if (!result.Success)
            {
                AxonPushOtelLogs.ExportFailed(_logger, activity.DisplayName, result.ErrorMessage ?? string.Empty);
                return false;
            }
            return true;
        }
        catch (Exception ex)
        {
            AxonPushOtelLogs.ExportThrew(_logger, activity.DisplayName, ex);
            return false;
        }
    }

    protected override bool OnForceFlush(int timeoutMilliseconds) => true;

    protected override bool OnShutdown(int timeoutMilliseconds) => true;

    private static Dictionary<string, object?> BuildResource(AxonPushSpanExporterOptions options)
    {
        var resource = new Dictionary<string, object?>(StringComparer.Ordinal)
        {
            ["service.name"] = options.ServiceName ?? Assembly.GetEntryAssembly()?.GetName().Name ?? "dotnet-app",
        };

        if (!string.IsNullOrWhiteSpace(options.ServiceVersion))
        {
            resource["service.version"] = options.ServiceVersion;
        }

        if (!string.IsNullOrWhiteSpace(options.Environment))
        {
            resource["deployment.environment"] = options.Environment;
        }

        return resource;
    }
}

internal static partial class AxonPushOtelLogs
{
    [LoggerMessage(EventId = 2000, Level = LogLevel.Warning,
        Message = "AxonPush span export failed for '{SpanName}': {Reason}")]
    public static partial void ExportFailed(ILogger logger, string spanName, string reason);

    [LoggerMessage(EventId = 2001, Level = LogLevel.Warning,
        Message = "AxonPush span exporter threw while exporting '{SpanName}'.")]
    public static partial void ExportThrew(ILogger logger, string spanName, Exception exception);
}
