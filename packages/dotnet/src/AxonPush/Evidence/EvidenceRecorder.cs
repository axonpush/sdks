using AxonPush.Events;

namespace AxonPush.Evidence;

internal sealed record EvidenceTask(string Id, string? ParentId);

internal static class EvidenceContext
{
    internal static readonly AsyncLocal<EvidenceTask?> Current = new();
    internal static PublishRequest Attach(PublishRequest request)
    {
        var task = Current.Value;
        if (task is null) return request;
        var metadata = request.Metadata is null ? new Dictionary<string, object?>() : new(request.Metadata);
        metadata.TryAdd("axonpush.task_id", task.Id);
        if (task.ParentId is not null) metadata.TryAdd("axonpush.parent_task_id", task.ParentId);
        return request with { Metadata = metadata };
    }
}

/// <summary>Customer-reported evidence using the existing passive publisher.
/// Recording a decision does not authenticate its actor or enforce a policy.</summary>
public sealed class EvidenceRecorder(EventsResource events, string channelId, string agentId)
{
    public async Task<T> TaskAsync<T>(string goal, Func<string, CancellationToken, Task<T>> action, CancellationToken cancellationToken = default)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(goal);
        ArgumentNullException.ThrowIfNull(action);
        var parent = EvidenceContext.Current.Value;
        var task = new EvidenceTask(Guid.NewGuid().ToString(), parent?.Id);
        EvidenceContext.Current.Value = task;
        try
        {
            await EmitAsync("agent.task.start", new() { ["goal"] = goal }, cancellationToken).ConfigureAwait(false);
            T value;
            try { value = await action(task.Id, cancellationToken).ConfigureAwait(false); }
            catch
            {
                try { await EmitAsync("agent.task.end", new() { ["outcome"] = "failed" }, cancellationToken).ConfigureAwait(false); }
                catch { /* Preserve the application exception. */ }
                throw;
            }
            await EmitAsync("agent.task.end", new() { ["outcome"] = "succeeded" }, cancellationToken).ConfigureAwait(false);
            return value;
        }
        finally { EvidenceContext.Current.Value = parent; }
    }

    public Task<PublishResult> DecisionAsync(string decision, string targetSpanId, string actor, string? reason = null, CancellationToken cancellationToken = default)
    {
        if (decision is not ("approved" or "overrode" or "stopped" or "escalated")) throw new ArgumentException("Unknown oversight decision", nameof(decision));
        return EmitAsync("oversight.decision", new() { ["decision"] = decision, ["target_span_id"] = targetSpanId, ["actor"] = actor, ["reason"] = reason }, cancellationToken);
    }

    public Task<PublishResult> DeniedAsync(string rule, string tool, string mode, string? reason = null, CancellationToken cancellationToken = default)
    {
        if (mode is not ("shadow" or "enforce")) throw new ArgumentException("Unknown policy mode", nameof(mode));
        return EmitAsync("policy.denied", new() { ["rule"] = rule, ["tool"] = tool, ["mode"] = mode, ["reason"] = reason }, cancellationToken);
    }

    public Task<PublishResult> NoticeShownAsync(string noticeId, string audience, string channel, CancellationToken cancellationToken = default) =>
        EmitAsync("notice.shown", new() { ["notice_id"] = noticeId, ["audience"] = audience, ["channel"] = channel }, cancellationToken);

    private Task<PublishResult> EmitAsync(string kind, Dictionary<string, object?> payload, CancellationToken cancellationToken) =>
        events.PublishAsync(new PublishRequest
        {
            Identifier = kind,
            ChannelId = channelId,
            AgentId = agentId,
            EventType = "custom",
            Payload = payload,
            Metadata = new Dictionary<string, object?>
            {
                ["axonpush.evidence.version"] = 1,
                ["axonpush.evidence.kind"] = kind,
                ["axonpush.evidence.origin"] = "sdk_reported"
            }
        }, cancellationToken);
}
