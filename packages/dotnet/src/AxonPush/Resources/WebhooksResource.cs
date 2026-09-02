using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class WebhooksResource : ResourceBase
{
    private readonly WebhookControllerClient _webhookControllerClient;

    internal WebhooksResource(AxonPushTransport transport)
        : base(transport)
    {
        _webhookControllerClient = new WebhookControllerClient(Http);
    }

    /// <summary>Create endpoint. <c>POST /webhooks/endpoints</c></summary>
    public Task<WebhookEndpointCreateResponseDto> CreateEndpointAsync(CreateWebhookEndpointDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _webhookControllerClient.CreateEndpointAsync(body, cancellationToken);

    /// <summary>List endpoints. <c>GET /webhooks/endpoints/channel/{channelId}</c></summary>
    public Task<System.Collections.Generic.ICollection<WebhookEndpointResponseDto>> ListEndpointsAsync(string channelId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _webhookControllerClient.ListEndpointsAsync(channelId, cancellationToken);

    /// <summary>Delete endpoint. <c>DELETE /webhooks/endpoints/{id}</c></summary>
    public Task<MessageResponseDto> DeleteEndpointAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _webhookControllerClient.DeleteEndpointAsync(id, cancellationToken);

    /// <summary>Deliveries. <c>GET /webhooks/deliveries/{endpointId}</c></summary>
    public Task<System.Collections.Generic.ICollection<WebhookDeliveryResponseDto>> DeliveriesAsync(string endpointId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _webhookControllerClient.GetDeliveriesAsync(endpointId, cancellationToken);
}
