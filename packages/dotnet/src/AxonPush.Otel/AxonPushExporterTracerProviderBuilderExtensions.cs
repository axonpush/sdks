using Microsoft.Extensions.Logging;
using OpenTelemetry;
using OpenTelemetry.Trace;

namespace AxonPush.Otel;

/// <summary>
/// Convenience extensions for wiring an <see cref="AxonPushSpanExporter"/> into a
/// <see cref="TracerProviderBuilder"/>.
/// </summary>
public static class AxonPushExporterTracerProviderBuilderExtensions
{
    /// <summary>
    /// Adds the AxonPush span exporter using an existing <see cref="AxonPushClient"/>. The caller
    /// owns the client lifetime.
    /// </summary>
    public static TracerProviderBuilder AddAxonPushExporter(
        this TracerProviderBuilder builder,
        AxonPushClient client,
        Action<AxonPushSpanExporterOptions> configureExporter,
        ILoggerFactory? loggerFactory = null)
    {
        ArgumentNullException.ThrowIfNull(builder);
        ArgumentNullException.ThrowIfNull(client);
        ArgumentNullException.ThrowIfNull(configureExporter);

        var exporterOptions = CreateExporterOptions(configureExporter);
        var exporter = new AxonPushSpanExporter(client, exporterOptions, loggerFactory);
        return builder.AddProcessor(new BatchActivityExportProcessor(exporter));
    }

    /// <summary>
    /// Adds the AxonPush span exporter, constructing an <see cref="AxonPushClient"/> from the
    /// supplied options. The exporter owns the client.
    /// </summary>
    public static TracerProviderBuilder AddAxonPushExporter(
        this TracerProviderBuilder builder,
        Action<AxonPushOptions> configureClient,
        Action<AxonPushSpanExporterOptions> configureExporter,
        ILoggerFactory? loggerFactory = null)
    {
        ArgumentNullException.ThrowIfNull(builder);
        ArgumentNullException.ThrowIfNull(configureClient);
        ArgumentNullException.ThrowIfNull(configureExporter);

        var clientOptions = AxonPushOptions.FromEnvironment();
        configureClient(clientOptions);
        var client = new AxonPushClient(clientOptions, loggerFactory);

        return builder.AddAxonPushExporter(client, configureExporter, loggerFactory);
    }

    private static AxonPushSpanExporterOptions CreateExporterOptions(Action<AxonPushSpanExporterOptions> configure)
    {
        var options = new AxonPushSpanExporterOptions { ChannelId = string.Empty };
        configure(options);
        if (string.IsNullOrWhiteSpace(options.ChannelId))
        {
            throw new InvalidOperationException("AxonPushSpanExporterOptions.ChannelId must be set.");
        }
        return options;
    }
}
