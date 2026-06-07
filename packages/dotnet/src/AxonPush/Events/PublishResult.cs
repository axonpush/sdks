using System.Net;

namespace AxonPush.Events;

/// <summary>
/// Outcome of an <see cref="EventsResource.PublishAsync"/> call.
/// </summary>
public sealed record PublishResult
{
    public required bool Success { get; init; }

    public HttpStatusCode? StatusCode { get; init; }

    public string? ErrorMessage { get; init; }

    public int Attempts { get; init; } = 1;

    public static PublishResult Ok(HttpStatusCode statusCode, int attempts) => new()
    {
        Success = true,
        StatusCode = statusCode,
        Attempts = attempts,
    };

    public static PublishResult Failed(string message, HttpStatusCode? statusCode, int attempts) => new()
    {
        Success = false,
        ErrorMessage = message,
        StatusCode = statusCode,
        Attempts = attempts,
    };
}
