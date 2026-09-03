using AxonPush.Internal;
using AxonPush.Internal.Api;

namespace AxonPush.Resources;

/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>
public sealed class ChannelsResource : ResourceBase
{
    private readonly ChannelControllerClient _channelControllerClient;

    internal ChannelsResource(AxonPushTransport transport)
        : base(transport)
    {
        _channelControllerClient = new ChannelControllerClient(Http);
    }

    /// <summary>List. <c>GET /channel</c></summary>
    public Task<System.Collections.Generic.ICollection<ChannelResponseDto>> ListAsync(string appId, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _channelControllerClient.ListChannelsAsync(appId, cancellationToken);

    /// <summary>Get. <c>GET /channel/{id}</c></summary>
    public Task<ChannelResponseDto> GetAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _channelControllerClient.GetChannelAsync(id, cancellationToken);

    /// <summary>Create. <c>POST /channel</c></summary>
    public Task<ChannelResponseDto> CreateAsync(CreateChannelDto body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _channelControllerClient.CreateChannelAsync(body, cancellationToken);

    /// <summary>Update. <c>PUT /channel/{id}</c></summary>
    public Task<OkResponseDto> UpdateAsync(string id, Function body, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _channelControllerClient.UpdateChannelAsync(id, body, cancellationToken);

    /// <summary>Delete. <c>DELETE /channel/{id}</c></summary>
    public Task<OkResponseDto> DeleteAsync(string id, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        => _channelControllerClient.DeleteChannelAsync(id, cancellationToken);
}
