"""Emit the v2 resource classes for both SDKs from contract/openapi.sdk.json.

The resource layer is formulaic -- a thin method per operation delegating to the
generated client through the one chokepoint -- so generating it keeps 12
resources identical across two languages rather than hand-copying 166 methods.
The output is checked in and editable like any other source.
"""
import io, json, os, re, sys

NL = chr(10)
DRY = '--apply' not in sys.argv
ROOT = 'contract/openapi.sdk.json'

# controller -> (module basename, TS class, python class, accessor, docstring)
RESOURCES = {
    'PromptController': ('prompts', 'PromptsResource', 'Prompts', 'prompts',
                         'Prompt registry: versions, deployments, promotion and rollback.'),
    'DatasetController': ('datasets', 'DatasetsResource', 'Datasets', 'datasets',
                          'Evaluation datasets and their immutable revisions.'),
    'EvaluatorController': ('evaluators', 'EvaluatorsResource', 'Evaluators', 'evaluators',
                            'Evaluators and their versions.'),
    'ExperimentController': ('experiments', 'ExperimentsResource', 'Experiments', 'experiments',
                             'Evaluation runs, their results and the release gate.'),
    'EvaluationTargetController': ('evaluation_targets', 'EvaluationTargetsResource',
                                   'EvaluationTargets', 'evaluation_targets',
                                   'The systems an experiment can run against.'),
    'AlertController': ('alerts', 'AlertsResource', 'Alerts', 'alerts',
                        'Alert rules over metric thresholds.'),
    'AssessmentController': ('assessments', 'AssessmentsResource', 'Assessments', 'assessments',
                             'Human and automated judgements attached to a trace.'),
    'AnalyticsController': ('analytics', 'AnalyticsResource', 'Analytics', 'analytics',
                            'Aggregate timeseries, breakdowns and A/B comparisons.'),
    'IssueController': ('issues', 'IssuesResource', 'Issues', 'issues',
                        'Clustered failures, their occurrences and triage actions.'),
    'OnlineEvaluationController': ('online_evaluations', 'OnlineEvaluationsResource',
                                   'OnlineEvaluations', 'online_evaluations',
                                   'Rules that evaluate live traffic as it arrives.'),
    'TraceIntelligenceController': ('trace_intelligence', 'TraceIntelligenceResource',
                                    'TraceIntelligence', 'trace_intelligence',
                                    'Semantic clustering over traces: clusters, flow and coverage.'),
    'TraceV2Controller': ('traces_v2', 'TracesV2Resource', 'TracesV2', 'traces_v2',
                          'Trace search with facets, spans and attribute keys.'),
    'GatePolicyController': ('gates', 'GatesResource', 'Gates', 'gates',
                             'Release-gate policies and the history of gate decisions.'),
    'GateRunController': ('gates', 'GatesResource', 'Gates', 'gates',
                          'Release-gate policies and the history of gate decisions.'),
}

# `remove` reads as the REST verb elsewhere in these SDKs
METHOD_RENAMES = {'remove': 'delete'}

# Two controllers back one resource, so their verbs need distinguishing.
CONTROLLER_RENAMES = {
    'GatePolicyController': {'list': 'listPolicies', 'get': 'getPolicy',
                             'save': 'savePolicy', 'remove': 'deletePolicy'},
    'GateRunController': {'list': 'listRuns'},
}


def method_name(ctrl, raw):
    return CONTROLLER_RENAMES.get(ctrl, {}).get(raw) or METHOD_RENAMES.get(raw, raw)


def controllers_for(mod):
    return [c for c in sorted(RESOURCES) if RESOURCES[c][0] == mod]

HTTP = ('get', 'post', 'put', 'patch', 'delete')

# `from` is a Python keyword, and a filter surface of 30+ parameters is
# unusable as keyword arguments, so those operations take one mapping instead.
PY_KEYWORDS = {'from', 'import', 'class', 'in', 'is', 'and', 'or', 'not', 'None',
               'lambda', 'global', 'pass', 'return', 'def', 'del', 'for', 'if'}
MAX_EXPLICIT_QUERY = 3


def query_style(o):
    names = [q for q, _ in o['query']]
    if not names:
        return 'none'
    if len(names) > MAX_EXPLICIT_QUERY or any(snake(n) in PY_KEYWORDS for n in names):
        return 'mapping'
    return 'explicit'


def snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).replace('__', '_').lower()


def camel(name):
    parts = name.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])


def ts_op(oid):
    """`AlertController_list` -> `alertControllerList`, as hey-api emits it."""
    head, tail = oid.split('_', 1)
    return head[0].lower() + head[1:] + tail[0].upper() + tail[1:]


def humanise(name):
    words = re.sub(r'(?<!^)(?=[A-Z])', ' ', name).lower().split()
    return (words[0].capitalize() + ' ' + ' '.join(words[1:])).strip()


spec = json.load(io.open(ROOT, encoding='utf-8'))


def ref_name(schema):
    if not isinstance(schema, dict):
        return None, False
    if '$ref' in schema:
        return schema['$ref'].split('/')[-1], False
    if schema.get('type') == 'array' and isinstance(schema.get('items'), dict):
        inner = schema['items'].get('$ref')
        if inner:
            return inner.split('/')[-1], True
    return None, False


ops_by_ctrl = {}
for path, item in sorted(spec['paths'].items()):
    for method, op in item.items():
        if method not in HTTP:
            continue
        oid = op['operationId']
        ctrl, raw = oid.split('_', 1)
        if ctrl not in RESOURCES:
            continue
        params = op.get('parameters', [])
        path_params = sorted(
            (p['name'] for p in params if p.get('in') == 'path'),
            key=lambda n: path.index('{' + n + '}'),
        )
        query = [(p['name'], bool(p.get('required'))) for p in params if p.get('in') == 'query']
        body = None
        rb = op.get('requestBody')
        if rb:
            body, _ = ref_name((rb.get('content', {}).get('application/json', {}) or {}).get('schema', {}))
        result, is_list = None, False
        for code, resp in sorted(op.get('responses', {}).items()):
            if not code.startswith('2'):
                continue
            sch = (resp.get('content', {}).get('application/json', {}) or {}).get('schema', {})
            result, is_list = ref_name(sch)
            if result:
                break
        ops_by_ctrl.setdefault(ctrl, []).append({
            'op': oid, 'ctrl': ctrl, 'raw': raw, 'name': method_name(ctrl, raw),
            'method': method, 'path': path,
            'path_params': path_params, 'query': sorted(query), 'body': body,
            'result': result, 'is_list': is_list,
            'summary': op.get('summary') or '',
        })


def py_alias(o):
    """Unique per module: two controllers behind one resource both have `list`."""
    if len(controllers_for(RESOURCES[o['ctrl']][0])) > 1:
        return '_%s_%s_op' % (snake(o['ctrl'].replace('Controller', '')), snake(o['raw']))
    return '_%s_op' % snake(o['raw'])


def ops_for(mod):
    return [o for ctrl in controllers_for(mod) for o in ops_by_ctrl.get(ctrl, [])]


def ts_type(o):
    if not o['result']:
        return 'unknown'
    return f"{o['result']}[]" if o['is_list'] else o['result']


def py_type(o):
    if not o['result']:
        return 'Any'
    # `List`, not `list`: a method named `list` shadows the builtin in the
    # class body, so `-> list[X]` would resolve to the method
    return f"List[{o['result']}]" if o['is_list'] else o['result']


NAME_DOCS = {
    'list': 'List them all',
    'get': 'Fetch one by id',
    'create': 'Create one',
    'update': 'Update one',
    'delete': 'Delete one',
}


def describe(o):
    if o['summary']:
        head = o['summary'].rstrip('.')
    else:
        head = NAME_DOCS.get(o['name']) or humanise(o['name'])
    return f"{head}. `{o['method'].upper()} {o['path']}`"


def emit_ts(mod):
    _, cls, _, _, doc = RESOURCES[controllers_for(mod)[0]]
    ops = ops_for(mod)
    gen_ops = sorted({o['op'] for o in ops})
    types = sorted({o['result'] for o in ops if o['result']} | {o['body'] for o in ops if o['body']})
    L = []
    L.append('import {')
    for g in gen_ops:
        L.append(f'  {ts_op(g)},')
    L.append('} from "../_internal/api/sdk.gen.js";')
    if types:
        L.append('import type {')
        for t in types:
            L.append(f'  {t},')
        L.append('} from "../_internal/api/types.gen.js";')
    L.append('import type { ResourceClient } from "./_client.js";')
    L.append('')
    L.append('/** ' + doc + ' */')
    L.append(f'export class {cls} {{')
    L.append('  constructor(private readonly client: ResourceClient) {}')
    for o in ops:
        args, call = [], []
        for p in o['path_params']:
            args.append(f'{p}: string')
        if o['body']:
            args.append(f'body: {o["body"]}')
        req_q = [q for q, r in o['query'] if r]
        opt_q = [q for q, r in o['query'] if not r]
        if req_q or opt_q:
            fields = ''.join(f'{q}: string; ' for q in req_q) + ''.join(f'{q}?: string; ' for q in opt_q)
            args.append(('query: ' if req_q else 'query?: ') + '{ ' + fields.strip() + ' }')
        if o['path_params']:
            call.append('path: { ' + ', '.join(o['path_params']) + ' }')
        if o['body']:
            call.append('body')
        if o['query']:
            call.append('query')
        L.append('')
        L.append('  /** ' + describe(o) + ' */')
        sig = ', '.join(args)
        L.append(f'  async {o["name"]}({sig}): Promise<{ts_type(o)} | null> {{')
        payload = '{ ' + ', '.join(call) + ' }' if call else '{}'
        L.append(f'    return this.client.invoke({ts_op(o["op"])}, {payload});')
        L.append('  }')
    L.append('}')
    return NL.join(L) + NL


def emit_py(mod):
    _, _, cls, _, doc = RESOURCES[controllers_for(mod)[0]]
    ops = ops_for(mod)
    types = sorted({o['result'] for o in ops if o['result']} | {o['body'] for o in ops if o['body']})
    L = ['"""' + doc + '"""', '', 'from __future__ import annotations', '',
         'from collections.abc import Mapping', 'from typing import TYPE_CHECKING, Any, List', '']
    by_tag = {}
    for o in ops:
        by_tag.setdefault(PY_TAG[o['ctrl']], []).append(o)
    for tag in sorted(by_tag):
        L.append('from axonpush._internal.api.api.' + tag + ' import (')
        for o in sorted(by_tag[tag], key=lambda x: x['op']):
            L.append(f'    {snake(o["op"])} as {py_alias(o)},')
        L.append(')')
    if types:
        L.append('from axonpush._internal.api.models import (')
        for t in types:
            L.append(f'    {t},')
        L.append(')')
    L.append('')
    L.append('if TYPE_CHECKING:')
    L.append('    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol')
    L.append('')
    L.append('')
    for is_async in (False, True):
        name = ('Async' + cls) if is_async else cls
        proto = 'AsyncClientProtocol' if is_async else 'SyncClientProtocol'
        L.append(f'class {name}:')
        L.append(f'    """{"Async sibling of :class:`" + cls + "`." if is_async else doc}"""')
        L.append('')
        L.append(f'    def __init__(self, client: {proto}) -> None:')
        L.append('        self._client = client')
        for o in ops:
            args, kwargs = ['self'], []
            for p in o['path_params']:
                args.append(f'{snake(p)}: str')
                kwargs.append(f'{snake(p)}={snake(p)}')
            if o['body']:
                args.append(f'body: {o["body"]}')
                kwargs.append('body=body')
            style = query_style(o)
            if style == 'explicit':
                for q, req in sorted(o['query'], key=lambda t: not t[1]):
                    args.append(f'{snake(q)}: str' if req else f'{snake(q)}: str | None = None')
                    kwargs.append(f'{snake(q)}={snake(q)}')
            elif style == 'mapping':
                args.append('params: Mapping[str, Any] | None = None')
            L.append('')
            aw, ad = ('await ', 'async ') if is_async else ('', '')
            L.append(f'    {ad}def {snake(o["name"])}({", ".join(args)}) -> {py_type(o)} | None:')
            body_doc = describe(o) if not is_async else f'See :meth:`{cls}.{snake(o["name"])}`.'
            L.append(f'        """{body_doc}"""')
            call = py_alias(o)
            joined = (', ' + ', '.join(kwargs)) if kwargs else ''
            if query_style(o) == 'mapping':
                joined += ', **dict(params or {})'
            L.append(f'        return {aw}self._client._invoke({call}{joined})')
        L.append('')
        L.append('')
    return NL.join(L).rstrip(NL) + NL


# resolve each controller's generated python tag directory from the tree
API_DIR = 'packages/python/src/axonpush/_internal/api/api'
PY_TAG = {}
for ctrl in RESOURCES:
    target = snake(ops_by_ctrl[ctrl][0]['op'])
    PY_TAG[ctrl] = next(
        (tag for tag in os.listdir(API_DIR)
         if os.path.isfile(os.path.join(API_DIR, tag, target + '.py'))),
        None,
    )
    if PY_TAG[ctrl] is None:
        print('  ! no tag dir for', ctrl, target)

modules = sorted({spec_[0] for spec_ in RESOURCES.values()})
for mod in modules:
    ts_path = f'packages/typescript/src/resources/{mod.replace("_", "-")}.ts'
    py_path = f'packages/python/src/axonpush/resources/{mod}.py'
    if not DRY:
        io.open(ts_path, 'w', encoding='utf-8', newline=NL).write(emit_ts(mod))
        io.open(py_path, 'w', encoding='utf-8', newline=NL).write(emit_py(mod))
    print('  %-28s %2d ops -> %s + %s' % (
        '+'.join(controllers_for(mod)), len(ops_for(mod)),
        ts_path.split('/')[-1], py_path.split('/')[-1]))

print(NL + '%d resources, %d operations' % (len(modules), sum(len(v) for v in ops_by_ctrl.values())))
print('(dry run; pass --apply to write)' if DRY else 'written')
