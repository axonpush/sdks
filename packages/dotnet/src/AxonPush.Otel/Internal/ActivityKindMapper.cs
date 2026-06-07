using System.Diagnostics;

namespace AxonPush.Otel.Internal;

internal static class ActivityKindMapper
{
    /// <summary>
    /// Maps <see cref="ActivityKind"/> to the integer constant used by the OTel proto definition.
    /// AxonPush stores the int and the Python and TypeScript SDKs emit the same values.
    /// </summary>
    public static int ToProtoInt(ActivityKind kind) => kind switch
    {
        ActivityKind.Internal => 1,
        ActivityKind.Server => 2,
        ActivityKind.Client => 3,
        ActivityKind.Producer => 4,
        ActivityKind.Consumer => 5,
        _ => 0,
    };
}
