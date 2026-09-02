using AxonPush.Internal;

namespace AxonPush.Resources;

/// <summary>
/// What every resource has: the shared HTTP pipeline. Each resource then owns
/// the generated client (or clients) for the controllers behind it.
/// </summary>
public abstract class ResourceBase
{
    private protected ResourceBase(AxonPushTransport transport)
    {
        ArgumentNullException.ThrowIfNull(transport);
        Http = transport.HttpClient;
    }

    private protected HttpClient Http { get; }
}
