"""Emit the .NET resource layer from the TypeScript one and the generated client.

.NET was the only SDK without a generated client and the only one that did not
work. It now has both halves the others have: NSwag emits the API client from
contract/openapi.sdk.json, and this emits the resource layer over it.

TypeScript is the reference surface. Each resource's methods and their names
are read from packages/typescript/src/resources, so parity holds by
construction rather than by anyone remembering; surface-diff.ts then proves it.

    python tools/generate-dotnet-resources.py [--apply]
"""
import io, json, os, pathlib, re, sys

NL = chr(10)
DRY = '--apply' not in sys.argv

SPEC = 'contract/openapi.sdk.json'
TS_DIR = 'packages/typescript/src/resources'
GENERATED = 'packages/dotnet/src/AxonPush/Internal/Api/AxonPushApi.g.cs'
OUT_DIR = 'packages/dotnet/src/AxonPush/Resources'
CLIENT = 'packages/dotnet/src/AxonPush/AxonPushClient.cs'

# events keeps its hand-written resource: publishing is telemetry and stays
# fail-open, which a generated passthrough would silently drop.
SKIP = {'_client.ts', 'index.ts', 'events.ts'}


def ts_operation_name(operation_id):
    """`AlertController_list` -> `alertControllerList`, as hey-api emits it."""
    head, tail = operation_id.split('_', 1)
    return head[0].lower() + head[1:] + tail[0].upper() + tail[1:]


def pascal(name):
    return name[0].upper() + name[1:] if name else name


def read(path):
    return io.open(path, encoding='utf-8').read()


def operation_index():
    spec = json.loads(read(SPEC))
    index = {}
    for path, item in spec['paths'].items():
        for method, operation in item.items():
            oid = operation.get('operationId')
            if not oid:
                continue
            index[ts_operation_name(oid)] = {
                'id': oid,
                'path': path,
                'method': method.upper(),
                'summary': (operation.get('summary') or '').rstrip('.'),
            }
    return index


def ts_resources():
    """module -> (class name, [(method, ts operation name)]) in declaration order."""
    resources = {}
    for filename in sorted(os.listdir(TS_DIR)):
        if not filename.endswith('.ts') or filename in SKIP or filename.endswith('.test.ts'):
            continue
        text = read(os.path.join(TS_DIR, filename))
        class_match = re.search(r'export class ([A-Za-z0-9_]+)', text)
        if not class_match:
            continue
        methods = []
        for match in re.finditer(r'^  (?:async\s+)?([a-zA-Z][A-Za-z0-9]*)\(', text, re.M):
            if match.group(1) == 'constructor':
                continue
            tail = text[match.end():]
            invoke = re.search(r'invoke\(\s*([a-zA-Z][A-Za-z0-9]*)', tail)
            following = re.search(r'^  (?:async\s+)?[a-zA-Z][A-Za-z0-9]*\(', tail, re.M)
            if invoke and (not following or invoke.start() < following.start()):
                methods.append((match.group(1), invoke.group(1)))
        resources[filename[:-3]] = (class_match.group(1), methods)
    return resources


def split_params(text):
    """Top-level comma split, so generic arguments stay together."""
    parts, depth, current = [], 0, ''
    for char in text:
        if char in '<([':
            depth += 1
        elif char in '>)]':
            depth -= 1
        if char == ',' and depth == 0:
            parts.append(current.strip())
            current = ''
            continue
        current += char
    if current.strip():
        parts.append(current.strip())
    return parts


def param_name(param):
    return re.split(r'\s*=', param, 1)[0].strip().split(' ')[-1]


def generated_signatures():
    """(client class, method) -> (return type, parameter text)."""
    text = read(GENERATED)
    signatures = {}
    current = None
    pattern = re.compile(
        r'public partial class ([A-Za-z0-9_]+)|'
        r'public virtual async System\.Threading\.Tasks\.Task<(.+?)> ([A-Za-z0-9_]+)\('
    )
    for match in pattern.finditer(text):
        if match.group(1):
            current = match.group(1)
            continue
        depth, index = 1, match.end()
        while depth:
            if text[index] == '(':
                depth += 1
            elif text[index] == ')':
                depth -= 1
            index += 1
        params = text[match.end():index - 1]
        if 'cancellationToken' not in params:
            continue
        signatures[(current, match.group(3))] = (match.group(2), params)
    return signatures


def postprocess_generated():
    """Two corrections NSwag cannot be configured into making.

    It records each enum's wire value as `EnumMember` but asks for
    `JsonStringEnumConverter`, which uses the .NET member name, so `cli` went
    out as `Cli`. And every client builds bare serializer options, so unset
    optional fields are sent as explicit nulls.
    """
    path = pathlib.Path(GENERATED)
    text = path.read_text(encoding='utf-8')
    before = text
    text = text.replace(
        'System.Text.Json.Serialization.JsonStringEnumConverter<',
        'AxonPush.Internal.EnumMemberJsonConverter<',
    )
    text = text.replace(
        'var settings = new System.Text.Json.JsonSerializerOptions();',
        'var settings = AxonPush.Internal.AxonPushApiJson.CreateOptions();',
    )
    if text != before:
        path.write_text(text, encoding='utf-8', newline=NL)
    converters = text.count('AxonPush.Internal.EnumMemberJsonConverter<')
    options = text.count('AxonPush.Internal.AxonPushApiJson.CreateOptions()')
    print('  postprocessed %d enum converters, %d serializer factories' % (converters, options))


postprocess_generated()
OPERATIONS = operation_index()
SIGNATURES = generated_signatures()


def target(ts_op):
    operation = OPERATIONS[ts_op]
    controller, raw = operation['id'].split('_', 1)
    return f'{controller}Client', pascal(raw) + 'Async', operation


def emit(class_name, methods):
    clients, body = {}, []
    for method_name, ts_op in methods:
        client_class, generated, operation = target(ts_op)
        signature = SIGNATURES.get((client_class, generated))
        if signature is None:
            raise SystemExit(
                f'{class_name}.{method_name}: {client_class}.{generated} is not in the '
                f'generated client. Regenerate with `nswag run nswag.json`.'
            )
        field = '_' + client_class[0].lower() + client_class[1:]
        clients[field] = client_class
        return_type, params = signature
        args = ', '.join(param_name(part) for part in split_params(params))
        summary = operation['summary'] or re.sub(r'(?<!^)(?=[A-Z])', ' ', method_name).capitalize()
        body.append('')
        body.append(f'    /// <summary>{summary}. <c>{operation["method"]} {operation["path"]}</c></summary>')
        body.append(f'    public Task<{return_type}> {pascal(method_name)}Async({params.strip()})')
        body.append(f'        => {field}.{generated}({args});')

    lines = [
        'using AxonPush.Internal;',
        'using AxonPush.Internal.Api;',
        '',
        'namespace AxonPush.Resources;',
        '',
        f'/// <summary>Generated from the TypeScript surface. See tools/generate-dotnet-resources.py.</summary>',
        f'public sealed class {class_name} : ResourceBase',
    ]
    lines.append('{')
    for field, client_class in clients.items():
        lines.append(f'    private readonly {client_class} {field};')
    lines.append('')
    lines.append(f'    internal {class_name}(AxonPushTransport transport)')
    lines.append('        : base(transport)')
    lines.append('    {')
    for field, client_class in clients.items():
        lines.append(f'        {field} = new {client_class}(Http);')
    lines.append('    }')
    lines.extend(body)
    lines.append('}')
    return NL.join(lines) + NL


resources = ts_resources()
written = []
for module, (class_name, methods) in sorted(resources.items()):
    if not methods:
        print('  ! no methods parsed for', module)
        continue
    path = os.path.join(OUT_DIR, class_name + '.cs')
    source = emit(class_name, methods)
    if not DRY:
        os.makedirs(OUT_DIR, exist_ok=True)
        io.open(path, 'w', encoding='utf-8', newline=NL).write(source)
    written.append((class_name, len(methods)))
    print('  %-32s %2d methods -> %s.cs' % (module, len(methods), class_name))

accessors = [(name[:-8] if name.endswith('Resource') else name, name) for name, _ in written]

partial = [
    'using AxonPush.Internal;',
    'using AxonPush.Resources;',
    '',
    'namespace AxonPush;',
    '',
    '/// <summary>Resource accessors. See tools/generate-dotnet-resources.py.</summary>',
    'public sealed partial class AxonPushClient',
    '{',
]
for prop, cls in accessors:
    partial.append(f'    /// <summary>The {prop} resource.</summary>')
    partial.append(f'    public {cls} {prop} {{ get; private set; }} = null!;')
    partial.append('')
partial.append('    private void CreateResources(AxonPushTransport transport)')
partial.append('    {')
for prop, cls in accessors:
    partial.append(f'        {prop} = new {cls}(transport);')
partial.append('    }')
partial.append('}')
if not DRY:
    io.open(CLIENT.replace('.cs', '.Resources.g.cs'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(partial) + NL
    )
print(NL + '%d resources, %d methods' % (len(written), sum(count for _, count in written)))
print('accessors: ' + ', '.join(f'{prop} => {cls}' for prop, cls in accessors))
print('(dry run; pass --apply to write)' if DRY else 'written')
