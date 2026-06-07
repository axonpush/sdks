using AxonPush;
using AxonPush.SemanticKernel;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.SemanticKernel;
using OpenTelemetry.Trace;
using Xunit;

namespace AxonPush.SemanticKernel.Tests;

public class KernelBuilderExtensionsTests
{
    [Fact]
    public void AddAxonPushTelemetry_FlipsTheGenAISwitch()
    {
        var builder = Kernel.CreateBuilder();

        builder.AddAxonPushTelemetry(
            client =>
            {
                client.ApiKey = "ak";
                client.TenantId = "t";
            },
            exporter =>
            {
                exporter.ChannelId = "ch";
            });

        Assert.True(AppContext.TryGetSwitch(
            "Microsoft.SemanticKernel.Experimental.GenAI.EnableOTelDiagnostics",
            out var enabled) && enabled);
    }

    [Fact]
    public void AddAxonPushTelemetry_RegistersTracerProviderAndClient()
    {
        var builder = Kernel.CreateBuilder();

        builder.AddAxonPushTelemetry(
            client =>
            {
                client.ApiKey = "ak";
                client.TenantId = "t";
            },
            exporter =>
            {
                exporter.ChannelId = "ch";
                exporter.ServiceName = "test";
            });

        builder.Services.AddSingleton<AnyResolver>();
        var provider = builder.Services.BuildServiceProvider();

        Assert.NotNull(provider.GetService<AxonPushClient>());
        Assert.NotNull(provider.GetService<TracerProvider>());
    }

    private sealed class AnyResolver
    {
    }
}
