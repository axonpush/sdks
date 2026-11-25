using System.Diagnostics;
using System.Text.Json;
using AxonPush.Events;
using AxonPush.Operations;

namespace AxonPush;

public sealed record RequestContext
{
    public required string WorkspaceId { get; init; }
    public required string Environment { get; init; }
    public IReadOnlyDictionary<string, string> Subjects { get; init; } = new Dictionary<string, string>();
    public string? RequestId { get; init; }
    public string? TraceId { get; init; }
    public string? SessionId { get; init; }
    public IReadOnlyDictionary<string, ObservationBindings> Bindings { get; init; } = new Dictionary<string, ObservationBindings>();
}
public sealed record ObservationBindings
{
    public IReadOnlyDictionary<string, string> Refs { get; init; } = new Dictionary<string, string>();
    public IReadOnlyDictionary<string, string> Attributes { get; init; } = new Dictionary<string, string>();
}

/// <summary>One client-owned request scope. Dispose in the async flow that opened it.</summary>
public sealed class RequestContextScope : IDisposable
{
    private static readonly AsyncLocal<IReadOnlyDictionary<object, RequestContext>?> Current = new();
    private readonly IReadOnlyDictionary<object, RequestContext>? _previous;
    private readonly AxonPushClient _client;
    private readonly RequestContext _context;
    private bool _disposed;
    internal static RequestContext? Read(object owner) => Current.Value?.GetValueOrDefault(owner);
    internal RequestContextScope(AxonPushClient client, RequestContext context)
    {
        if (string.IsNullOrWhiteSpace(context.WorkspaceId) || string.IsNullOrWhiteSpace(context.Environment)) throw new ArgumentException("Context requires workspace and environment");
        if (context.Subjects.Any(p => string.IsNullOrWhiteSpace(p.Key) || string.IsNullOrWhiteSpace(p.Value))) throw new ArgumentException("Invalid customer subjects");
        _client = client;
        _context = context with { TraceId = context.TraceId ?? Activity.Current?.TraceId.ToString(), Subjects = new Dictionary<string, string>(context.Subjects), Bindings = context.Bindings.ToDictionary(p => p.Key, p => p.Value with { Refs = new Dictionary<string, string>(p.Value.Refs), Attributes = new Dictionary<string, string>(p.Value.Attributes) }) };
        _previous = Current.Value;
        var next = _previous is null ? new Dictionary<object, RequestContext>() : new Dictionary<object, RequestContext>(_previous);
        next[client.ContextOwner] = _context; Current.Value = next;
    }
    public RequestContext Capture() => _context with { Subjects = new Dictionary<string, string>(_context.Subjects), Bindings = _context.Bindings.ToDictionary(p => p.Key, p => p.Value with { Refs = new Dictionary<string, string>(p.Value.Refs), Attributes = new Dictionary<string, string>(p.Value.Attributes) }) };
    public void Dispose() { if (_disposed) return; Current.Value = _previous; _disposed = true; }
    internal static Dictionary<string, object?> Attributes(RequestContext c)
    {
        var d = new Dictionary<string, object?> { ["axonpush.workspace_id"] = c.WorkspaceId, ["deployment.environment.name"] = c.Environment, ["telemetry.subjects"] = new Dictionary<string, string>(c.Subjects) };
        if (c.Subjects.TryGetValue("user", out var user)) d["user.id"] = user;
        if (c.RequestId is not null) d["axonpush.request_id"] = c.RequestId;
        if (c.SessionId is not null) d["session.id"] = c.SessionId;
        return d;
    }
    internal static PublishRequest Attach(object owner, PublishRequest request)
    {
        var c = Read(owner); if (c is null) return request;
        if (request.Environment is not null && request.Environment != c.Environment) throw new ArgumentException("Request environment mismatch");
        var metadata = Attributes(c);
        foreach (var pair in request.Metadata ?? new Dictionary<string, object?>())
        {
            if (pair.Key == "user.id" && c.Subjects.TryGetValue("user", out var id) && pair.Value?.ToString() != id) throw new ArgumentException("Conflicting user identity");
            if (pair.Key == "telemetry.subjects")
            {
                var subjects = JsonSerializer.Deserialize<Dictionary<string, string>>(JsonSerializer.Serialize(pair.Value)) ?? new();
                foreach (var subject in c.Subjects) { if (subjects.TryGetValue(subject.Key, out var existing) && existing != subject.Value) throw new ArgumentException("Conflicting subject"); subjects[subject.Key] = subject.Value; }
                metadata[pair.Key] = subjects;
            }
            else metadata[pair.Key] = pair.Value;
        }
        return request with { Environment = c.Environment, Metadata = metadata, TraceId = request.TraceId ?? c.TraceId };
    }
    public Task<StatusOutputBody?> PublishFactsAsync(string workflow, Input input, CancellationToken cancellationToken = default)
    {
        var subjects = new Dictionary<string, string>(_context.Subjects);
        foreach (var pair in input.Subjects ?? new Dictionary<string, string>()) { if (subjects.TryGetValue(pair.Key, out var id) && id != pair.Value) throw new ArgumentException("Conflicting case subject"); subjects[pair.Key] = pair.Value; }
        return _client.Workflows.FactsAsync(_context.WorkspaceId, new FactsInputBody { Workflow = workflow, Input = input with { Subjects = subjects, Facts = input.Facts?.Select(fact => fact with { TraceId = fact.TraceId ?? _context.TraceId }).ToArray() } }, _context.Environment, cancellationToken);
    }
    public Task<ActivityIngestReport?> ObserveAsync(ActivityObservation observation, CancellationToken cancellationToken = default)
    {
        if (observation.Environment is not null && observation.Environment != _context.Environment) throw new ArgumentException("Request environment mismatch");
        var refs = new Dictionary<string, string>(observation.Refs ?? new Dictionary<string, string>());
        var attrs = new Dictionary<string, JsonElement>(observation.Attributes ?? new Dictionary<string, JsonElement>());
        if (_context.Bindings.TryGetValue(observation.Event, out var bindings))
        {
            foreach (var p in bindings.Refs) if (_context.Subjects.TryGetValue(p.Value, out var id)) { if (refs.TryGetValue(p.Key, out var existing) && existing != id) throw new ArgumentException("Conflicting subject binding"); refs[p.Key] = id; }
            foreach (var p in bindings.Attributes) if (_context.Subjects.TryGetValue(p.Value, out var id)) { if (attrs.TryGetValue(p.Key, out var existing) && existing.ToString() != id) throw new ArgumentException("Conflicting subject binding"); attrs[p.Key] = JsonSerializer.SerializeToElement(id); }
        }
        return _client.Observations.AcceptAsync(_context.WorkspaceId, new WorkspaceIngestInputBody { Environment = _context.Environment, Observations = new[] { observation with { Environment = _context.Environment, Refs = refs, Attributes = attrs, SchemaVersion = 1, SourceEventId = string.IsNullOrEmpty(observation.SourceEventId) ? Guid.NewGuid().ToString() : observation.SourceEventId, OccurredAt = observation.OccurredAt == default ? DateTimeOffset.UtcNow : observation.OccurredAt, TraceId = observation.TraceId ?? Activity.Current?.TraceId.ToString() } }, }, cancellationToken);
    }
    public void AnnotateActivity(Activity activity) { foreach (var p in Attributes(_context)) activity.SetTag(p.Key, p.Value is IReadOnlyDictionary<string, string> ? JsonSerializer.Serialize(p.Value) : p.Value); }
}
