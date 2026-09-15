"""Emit resource classes for both SDKs from contract/openapi.sdk.json.

The resource layer is formulaic -- a thin method per operation delegating to the
generated client through the one chokepoint -- so generating it keeps resources
identical across two languages rather than hand-copying methods. The output is
checked in and editable like any other source.

NOTE (Go rewrite): the contract now uses dotted operationIds
(``alerts.list``, ``analytics.timeseries``, ``traces.list`` ...) instead of the
old NestJS ``AlertController_list`` scheme. This tool parses the dotted form.

Several resources are now HAND-MAINTAINED and deliberately excluded from the
``RESOURCES`` map below, because they carry logic the scaffolder cannot express:
list endpoints unwrap Huma envelope bodies (``{environments: [...]}`` etc.) into
plain lists, ``traces`` was renamed from ``traces_v2`` (with a back-compat
alias), and ``analytics`` dropped the removed ``compare`` op. Regenerating those
would clobber that logic. Add a tag here only for genuinely formulaic resources.
"""
import io, json, os, re, sys

NL = chr(10)
DRY = '--apply' not in sys.argv
ROOT = 'contract/openapi.sdk.json'

# tag -> (module basename, TS class, python class, accessor, docstring)
# Keyed by the OpenAPI tag, which is also the generated python api sub-package.
# Intentionally empty by default: the alerts / analytics / traces resources are
# hand-maintained (see module docstring). Populate for new formulaic resources.
RESOURCES: dict[str, tuple[str, str, str, str, str]] = {}

# `remove` reads as the REST verb elsewhere in these SDKs
METHOD_RENAMES = {'remove': 'delete'}

HTTP = ('get', 'post', 'put', 'patch', 'delete')

# `from` is a Python keyword, and a large filter surface is unusable as keyword
# arguments, so those operations take one mapping instead.
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
    name = name.replace('.', '_').replace('-', '_')
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).replace('__', '_').lower()


def camel(name):
    parts = snake(name).split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])


def op_tail(oid):
    """Last dotted segment of an operationId: ``alerts.list`` -> ``list``.

    Falls back to the whole id for un-dotted ids like ``createEvent``.
    """
    return oid.split('.')[-1] if '.' in oid else oid


def ts_op(oid):
    """`alerts.list` -> `alertsList`, matching hey-api's generated export."""
    return camel(oid)


def humanise(name):
    words = re.sub(r'(?<!^)(?=[A-Z])', ' ', snake(name).replace('_', ' ')).lower().split()
    return (words[0].capitalize() + ' ' + ' '.join(words[1:])).strip() if words else ''


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


ops_by_tag = {}
for path, item in sorted(spec['paths'].items()):
    for method, op in item.items():
        if method not in HTTP:
            continue
        oid = op.get('operationId')
        if not oid:
            continue
        tags = op.get('tags') or []
        tag = tags[0] if tags else None
        if tag not in RESOURCES:
            continue
        raw = op_tail(oid)
        params = op.get('parameters', [])
        path_params = [p['name'] for p in params if p.get('in') == 'path']
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
        ops_by_tag.setdefault(tag, []).append({
            'op': oid, 'name': METHOD_RENAMES.get(raw, raw), 'method': method, 'path': path,
            'path_params': path_params, 'query': sorted(query), 'body': body,
            'result': result, 'is_list': is_list,
            'summary': op.get('summary') or '',
        })


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


def emit_ts(tag):
    mod, cls, _, _, doc = RESOURCES[tag]
    ops = ops_by_tag[tag]
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


def emit_py(tag):
    mod, _, cls, _, doc = RESOURCES[tag]
    ops = ops_by_tag[tag]
    gen = sorted({(o['op'], snake(op_tail(o['op']))) for o in ops})
    types = sorted({o['result'] for o in ops if o['result']} | {o['body'] for o in ops if o['body']})
    L = ['"""' + doc + '"""', '', 'from __future__ import annotations', '',
         'from collections.abc import Mapping', 'from typing import TYPE_CHECKING, Any, List', '']
    L.append('from axonpush._internal.api.api.' + PY_TAG[tag] + ' import (')
    for oid, tail in gen:
        L.append(f'    {snake(oid)} as _{tail}_op,')
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
            call = f'_{snake(op_tail(o["op"]))}_op'
            joined = (', ' + ', '.join(kwargs)) if kwargs else ''
            if style == 'mapping':
                joined += ', **dict(params or {})'
            L.append(f'        return {aw}self._client._invoke({call}{joined})')
        L.append('')
        L.append('')
    return NL.join(L).rstrip(NL) + NL


PY_TAG = {}
# resolve tag dirs from the generated tree
API_DIR = 'packages/python/src/axonpush/_internal/api/api'
for tag in RESOURCES:
    PY_TAG[tag] = None
    if not ops_by_tag.get(tag):
        print('  ! no operations for tag', tag)
        continue
    target = snake(ops_by_tag[tag][0]['op'])
    for d in os.listdir(API_DIR):
        if os.path.isfile(os.path.join(API_DIR, d, target + '.py')):
            PY_TAG[tag] = d
            break
    if PY_TAG[tag] is None:
        print('  ! no tag dir for', tag, target)

written = 0
for tag in sorted(RESOURCES):
    if not ops_by_tag.get(tag):
        continue
    mod = RESOURCES[tag][0]
    ts_path = f'packages/typescript/src/resources/{mod.replace("_", "-")}.ts'
    py_path = f'packages/python/src/axonpush/resources/{mod}.py'
    if not DRY:
        io.open(ts_path, 'w', encoding='utf-8', newline=NL).write(emit_ts(tag))
        io.open(py_path, 'w', encoding='utf-8', newline=NL).write(emit_py(tag))
    written += 1
    print('  %-24s %2d ops -> %s + %s' % (tag, len(ops_by_tag[tag]), ts_path.split('/')[-1], py_path.split('/')[-1]))

if not RESOURCES:
    print('  (no tags configured; all resources are hand-maintained)')
print(NL + '%d resources, %d operations' % (written, sum(len(v) for v in ops_by_tag.values())))
print('(dry run; pass --apply to write)' if DRY else 'written')
