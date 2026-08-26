using System.Reflection;
using AxonPush.Otel;
using AxonPush.SemanticKernel.Internal;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;
using Microsoft.SemanticKernel;
using OpenTelemetry;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

namespace AxonPush.SemanticKernel;

/// <summary>
/// Extensions that wire AxonPush telemetry into a Semantic Kernel application with one call.
/// </summary>
public static class AxonPushKernelBuilderExtensions
{
    /// <summary>
    /// Enables Semantic Kernel's GenAI OpenTelemetry diagnostics and registers a
    /// <see cref="TracerProvider"/> that exports SK spans to AxonPush.
    /// </summary>
    /// <param name="builder">The kernel builder.</param>
    /// <param name="configureClient">Configures the <see cref="AxonPushOptions"/> used to talk to AxonPush.</param>
    /// <param name="configureExporter">Configures the <see cref="AxonPushSpanExporterOptions"/>.</param>
    /// <param name="enableSensitiveData">
    /// When <c>true</c>, also flips Semantic Kernel's "sensitive" diagnostic switch so prompts and
    /// completions appear in span events. Off by default to keep PII out of observability backends.
    /// </param>
    public static IKernelBuilder AddAxonPushTelemetry(
        this IKernelBuilder builder,
        Action<AxonPushOptions> configureClient,
        Action<AxonPushSpanExporterOptions> configureExporter,
        bool enableSensitiveData = false)
    {
        ArgumentNullException.ThrowIfNull(builder);
        builder.Services.AddAxonPushTelemetryForSemanticKernel(configureClient, configureExporter, enableSensitiveData);
        return builder;
    }
}

/// <summary>
/// Extensions for wiring AxonPush telemetry into a Semantic Kernel application via
/// <see cref="IServiceCollection"/> (e.g. when using <c>Host.CreateApplicationBuilder</c>).
/// </summary>
public static class AxonPushServiceCollectionExtensions
{
    public static IServiceCollection AddAxonPushTelemetryForSemanticKernel(
        this IServiceCollection services,
        Action<AxonPushOptions> configureClient,
        Action<AxonPushSpanExporterOptions> configureExporter,
        bool enableSensitiveData = false)
    {
        ArgumentNullException.ThrowIfNull(services);
        ArgumentNullException.ThrowIfNull(configureClient);
        ArgumentNullException.ThrowIfNull(configureExporter);

        SkTelemetrySwitch.Enable(enableSensitiveData);

        services.TryAddSingleton(_ =>
        {
            var options = AxonPushOptions.FromEnvironment();
            configureClient(options);
            return new AxonPushClient(options);
        });

        services.AddSingleton(provider =>
        {
            var client = provider.GetRequiredService<AxonPushClient>();
            var entryAssembly = Assembly.GetEntryAssembly();
            var serviceName = entryAssembly?.GetName().Name ?? "semantic-kernel-app";
            var serviceVersion = entryAssembly?.GetName().Version?.ToString();

            return Sdk.CreateTracerProviderBuilder()
                .AddSource("Microsoft.SemanticKernel*")
                .ConfigureResource(r => r.AddService(serviceName, serviceVersion: serviceVersion))
                .AddAxonPushExporter(client, opts =>
                {
                    var configured = new AxonPushSpanExporterOptions { ChannelId = string.Empty };
                    configureExporter(configured);
                    opts.ChannelId = configured.ChannelId;
                    opts.ServiceName = configured.ServiceName ?? serviceName;
                    opts.ServiceVersion = configured.ServiceVersion ?? serviceVersion;
                    opts.Environment = configured.Environment;
                })
                .Build()!;
        });

        return services;
    }
}
