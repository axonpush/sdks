namespace AxonPush;

/// <summary>
/// Known event-type discriminators recognised by the AxonPush events API.
/// </summary>
public static class EventType
{
    public const string AppSpan = "app.span";
    public const string AppLog = "app.log";
    public const string AgentStart = "agent.start";
    public const string AgentEnd = "agent.end";
    public const string AgentError = "agent.error";
    public const string AgentMessage = "agent.message";
    public const string AgentHandoff = "agent.handoff";
    public const string AgentLlmToken = "agent.llm.token";
    public const string AgentLog = "agent.log";
    public const string AgentToolCallStart = "agent.tool_call.start";
    public const string AgentToolCallEnd = "agent.tool_call.end";
}
