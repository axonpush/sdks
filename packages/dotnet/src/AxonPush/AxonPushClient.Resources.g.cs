using AxonPush.Internal;
using AxonPush.Resources;

namespace AxonPush;

/// <summary>Resource accessors. See tools/generate-dotnet-resources.py.</summary>
public sealed partial class AxonPushClient
{
    /// <summary>The Alerts resource.</summary>
    public AlertsResource Alerts { get; private set; } = null!;

    /// <summary>The Analytics resource.</summary>
    public AnalyticsResource Analytics { get; private set; } = null!;

    /// <summary>The ApiKeys resource.</summary>
    public ApiKeysResource ApiKeys { get; private set; } = null!;

    /// <summary>The Apps resource.</summary>
    public AppsResource Apps { get; private set; } = null!;

    /// <summary>The Assessments resource.</summary>
    public AssessmentsResource Assessments { get; private set; } = null!;

    /// <summary>The Channels resource.</summary>
    public ChannelsResource Channels { get; private set; } = null!;

    /// <summary>The Datasets resource.</summary>
    public DatasetsResource Datasets { get; private set; } = null!;

    /// <summary>The Environments resource.</summary>
    public EnvironmentsResource Environments { get; private set; } = null!;

    /// <summary>The EvaluationTargets resource.</summary>
    public EvaluationTargetsResource EvaluationTargets { get; private set; } = null!;

    /// <summary>The Evaluators resource.</summary>
    public EvaluatorsResource Evaluators { get; private set; } = null!;

    /// <summary>The Experiments resource.</summary>
    public ExperimentsResource Experiments { get; private set; } = null!;

    /// <summary>The Gates resource.</summary>
    public GatesResource Gates { get; private set; } = null!;

    /// <summary>The Issues resource.</summary>
    public IssuesResource Issues { get; private set; } = null!;

    /// <summary>The OnlineEvaluations resource.</summary>
    public OnlineEvaluationsResource OnlineEvaluations { get; private set; } = null!;

    /// <summary>The Organizations resource.</summary>
    public OrganizationsResource Organizations { get; private set; } = null!;

    /// <summary>The Prompts resource.</summary>
    public PromptsResource Prompts { get; private set; } = null!;

    /// <summary>The TraceIntelligence resource.</summary>
    public TraceIntelligenceResource TraceIntelligence { get; private set; } = null!;

    /// <summary>The Traces resource.</summary>
    public TracesResource Traces { get; private set; } = null!;

    /// <summary>The TracesV2 resource.</summary>
    public TracesV2Resource TracesV2 { get; private set; } = null!;

    /// <summary>The Webhooks resource.</summary>
    public WebhooksResource Webhooks { get; private set; } = null!;

    private void CreateResources(AxonPushTransport transport)
    {
        Alerts = new AlertsResource(transport);
        Analytics = new AnalyticsResource(transport);
        ApiKeys = new ApiKeysResource(transport);
        Apps = new AppsResource(transport);
        Assessments = new AssessmentsResource(transport);
        Channels = new ChannelsResource(transport);
        Datasets = new DatasetsResource(transport);
        Environments = new EnvironmentsResource(transport);
        EvaluationTargets = new EvaluationTargetsResource(transport);
        Evaluators = new EvaluatorsResource(transport);
        Experiments = new ExperimentsResource(transport);
        Gates = new GatesResource(transport);
        Issues = new IssuesResource(transport);
        OnlineEvaluations = new OnlineEvaluationsResource(transport);
        Organizations = new OrganizationsResource(transport);
        Prompts = new PromptsResource(transport);
        TraceIntelligence = new TraceIntelligenceResource(transport);
        Traces = new TracesResource(transport);
        TracesV2 = new TracesV2Resource(transport);
        Webhooks = new WebhooksResource(transport);
    }
}
