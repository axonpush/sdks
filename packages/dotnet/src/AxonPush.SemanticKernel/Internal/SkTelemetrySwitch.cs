namespace AxonPush.SemanticKernel.Internal;

/// <summary>
/// Flips the Microsoft Semantic Kernel diagnostic switches that gate OpenTelemetry emission.
/// </summary>
/// <remarks>
/// Semantic Kernel caches these flags into <c>static readonly bool</c> fields, so they must be
/// flipped before any SK type is JITted. Calling <c>AddAxonPushTelemetry</c> during DI
/// registration is early enough for normal hosts.
/// </remarks>
internal static class SkTelemetrySwitch
{
    private const string EnableDiagnosticsSwitch =
        "Microsoft.SemanticKernel.Experimental.GenAI.EnableOTelDiagnostics";

    private const string EnableSensitiveSwitch =
        "Microsoft.SemanticKernel.Experimental.GenAI.EnableOTelDiagnosticsSensitive";

    public static void Enable(bool enableSensitiveData)
    {
        AppContext.SetSwitch(EnableDiagnosticsSwitch, true);
        if (enableSensitiveData)
        {
            AppContext.SetSwitch(EnableSensitiveSwitch, true);
        }
    }
}
