namespace AxonPush.Operations;

public enum OperationAvailability
{
    Unknown,
    Allowed,
    Denied,
    Conditional,
}

/// <summary>Discovery is advisory. Every invocation is authorized again by the server.</summary>
public static class CapabilityDiscovery
{
    public static OperationAvailability GetAvailability(this OperationCapabilities? snapshot, string operationId)
    {
        var availability = snapshot?.Operations?.FirstOrDefault(operation => operation.OperationId == operationId)?.Availability;
        return availability switch
        {
            "allowed" => OperationAvailability.Allowed,
            "denied" => OperationAvailability.Denied,
            "conditional" => OperationAvailability.Conditional,
            _ => OperationAvailability.Unknown,
        };
    }
}
