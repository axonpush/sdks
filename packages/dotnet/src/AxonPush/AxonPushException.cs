using System.Net;

namespace AxonPush;

/// <summary>
/// Thrown when an AxonPush API call fails and the client is configured with
/// <see cref="AxonPushOptions.FailOpen"/> set to <c>false</c>.
/// </summary>
public class AxonPushException : Exception
{
    public AxonPushException(string message) : base(message) { }

    public AxonPushException(string message, Exception innerException) : base(message, innerException) { }

    public HttpStatusCode? StatusCode { get; init; }

    public string? ResponseBody { get; init; }
}
