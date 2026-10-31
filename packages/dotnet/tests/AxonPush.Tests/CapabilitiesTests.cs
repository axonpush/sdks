using System.Net;
using System.Text.Json;
using AxonPush.Internal;
using AxonPush.Operations;
using Xunit;

namespace AxonPush.Tests;

public sealed class CapabilitiesTests
{
    private const string Snapshot = """
        {"registryRevision":"test","operations":[
          {"operationId":"alerts.list","availability":"allowed"},
          {"operationId":"alerts.create","availability":"denied"},
          {"operationId":"events.get","availability":"conditional"}]}
        """;

    [Fact]
    public void Availability_MissingIsUnknownAndConditionalIsNotAllowed()
    {
        var snapshot = JsonSerializer.Deserialize<OperationCapabilities>(Snapshot, AxonPushJsonOptions.Default);
        Assert.Equal(OperationAvailability.Allowed, snapshot.GetAvailability("alerts.list"));
        Assert.Equal(OperationAvailability.Denied, snapshot.GetAvailability("alerts.create"));
        Assert.Equal(OperationAvailability.Conditional, snapshot.GetAvailability("events.get"));
        Assert.Equal(OperationAvailability.Unknown, snapshot.GetAvailability("missing"));
        Assert.Equal(OperationAvailability.Unknown, ((OperationCapabilities?)null).GetAvailability("alerts.list"));
    }

    [Fact]
    public async Task Discovery_DoesNotCachePermissionsAcrossFailedRequests()
    {
        using var handler = new Handler();
        using var http = new HttpClient(handler) { BaseAddress = new Uri("http://capabilities.example.test/") };
        using var sdk = new AxonPushClient(new AxonPushOptions { ApiKey = "ak_synthetic", TenantId = "tenant_synthetic", FailOpen = true, MaxRetries = 0 }, http);
        var first = await sdk.Capabilities.OperationsAsync();
        await Assert.ThrowsAsync<AxonPushException>(() => sdk.Capabilities.OperationsAsync());
        Assert.Equal(OperationAvailability.Allowed, first.GetAvailability("alerts.list"));
        Assert.Equal(2, handler.Count);
    }

    private sealed class Handler : HttpMessageHandler
    {
        public int Count { get; private set; }
        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            Assert.Equal("/capabilities/operations", request.RequestUri!.AbsolutePath);
            Count++;
            return Task.FromResult(new HttpResponseMessage(Count == 1 ? HttpStatusCode.OK : HttpStatusCode.ServiceUnavailable)
            { Content = new StringContent(Count == 1 ? Snapshot : "{}") });
        }
    }
}
