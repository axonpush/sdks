"""Generate sync/async compatibility facades from one sync source and OpenAPI types.

Keep business conveniences (body builders and envelope unwrapping) in
resource-facades/. Query parameters and enum conversions come from the existing
openapi-python-client output; never edit generated resource files directly.
"""

from __future__ import annotations

import argparse
import ast
import copy
import subprocess
import tempfile
from contextlib import nullcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = ROOT / "packages/python/src/axonpush/_internal/api"
DEST = ROOT / "packages/python/src/axonpush/resources"


class AwaitInvocations(ast.NodeTransformer):
    def __init__(self, methods: set[str]) -> None:
        self.methods = methods

    def visit_Call(self, node: ast.Call) -> ast.AST:
        self.generic_visit(node)
        if isinstance(node.func, ast.Attribute) and (
            node.func.attr == "_invoke"
            or (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == "self"
                and node.func.attr in self.methods
            )
        ):
            return ast.Await(value=node)
        return node


def generate(source: Path, destination: Path) -> None:
    tree = ast.parse(source.read_text())
    operations = {
        alias.asname or alias.name: API
        / "api"
        / node.module.rsplit(".", 1)[-1]
        / (alias.name + ".py")
        for node in tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module
        and node.module.startswith("axonpush._internal.api.api.")
        for alias in node.names
    }
    added_enums: set[str] = set()
    for cls in [node for node in tree.body if isinstance(node, ast.ClassDef)]:
        for method in cls.body:
            if not isinstance(method, ast.FunctionDef) or method.name == "__init__":
                continue
            calls = [
                n
                for n in ast.walk(method)
                if isinstance(n, ast.Call)
                and isinstance(n.func, ast.Attribute)
                and n.func.attr == "_invoke"
            ]
            for call in calls:
                if not call.args or not isinstance(call.args[0], ast.Name):
                    continue
                operation = ast.parse(operations[call.args[0].id].read_text())
                kwargs = next(
                    n
                    for n in operation.body
                    if isinstance(n, ast.FunctionDef) and n.name == "_get_kwargs"
                )
                forwarded = {k.arg: k for k in call.keywords}
                spread = any(k.arg is None for k in call.keywords)
                spread_values: dict[str, str] = {}
                arguments = {
                    a.arg: a for a in [*method.args.args, *method.args.kwonlyargs]
                }
                for arg, default in zip(
                    kwargs.args.kwonlyargs, kwargs.args.kw_defaults
                ):
                    if arg.arg in ("client", "body") or arg.arg.startswith("_"):
                        continue
                    names = {
                        n.id
                        for n in ast.walk(arg.annotation)
                        if isinstance(n, ast.Name)
                    }
                    enums = names - {
                        "str",
                        "int",
                        "float",
                        "bool",
                        "Unset",
                        "Any",
                        "list",
                        "dict",
                    }
                    # Generated query models are string enums. Refuse unexpected types
                    # rather than quietly inventing a conversion when the contract evolves.
                    for enum in enums:
                        candidates = [
                            n
                            for n in operation.body
                            if isinstance(n, ast.ImportFrom)
                            and any(a.name == enum for a in n.names)
                        ]
                        if (
                            not candidates
                            or not candidates[0].module
                            or not candidates[0].module.startswith("models.")
                        ):
                            raise ValueError(
                                f"Unsupported query type {enum} in {source.name}"
                            )
                        model = ast.parse(
                            (
                                API / (candidates[0].module.replace(".", "/") + ".py")
                            ).read_text()
                        )
                        if not any(
                            isinstance(n, ast.ClassDef)
                            and any(
                                isinstance(b, ast.Name) and b.id == "Enum"
                                for b in n.bases
                            )
                            for n in model.body
                        ):
                            raise ValueError(f"Query type {enum} is not an enum")
                    added_enums.update(enums)
                    if arg.arg not in arguments:
                        annotation = ast.unparse(arg.annotation).replace(
                            "Unset", "None"
                        )
                        if enums:
                            annotation += " | str"
                        newarg = ast.arg(
                            arg=arg.arg,
                            annotation=ast.parse(annotation, mode="eval").body,
                        )
                        method.args.kwonlyargs.append(newarg)
                        method.args.kw_defaults.append(
                            ast.Constant(None) if default is not None else None
                        )
                        arguments[arg.arg] = newarg
                    expr = f"{next(iter(enums))}({arg.arg})" if enums else arg.arg
                    if spread and arg.arg not in forwarded:
                        spread_values[arg.arg] = (
                            f"{expr} if {arg.arg} is not None else None"
                        )
                        continue
                    if arg.arg not in forwarded:
                        keyword = ast.keyword(
                            arg=arg.arg, value=ast.Name(id=arg.arg, ctx=ast.Load())
                        )
                        call.keywords.append(keyword)
                        forwarded[arg.arg] = keyword
                    # Preserve customized aliases/body builders; normalize direct query
                    # forwarding consistently for both existing and newly exposed fields.
                    forwarded[arg.arg].value = ast.parse(
                        f"{expr} if {arg.arg} is not None else UNSET", mode="eval"
                    ).body
                if spread_values:
                    original = [
                        ast.unparse(k.value) for k in call.keywords if k.arg is None
                    ]
                    entries = ["**" + value for value in original] + [
                        repr(key) + ": " + value for key, value in spread_values.items()
                    ]
                    merged = (
                        "{k: v for k, v in {"
                        + ", ".join(entries)
                        + "}.items() if v is not None}"
                    )
                    call.keywords = [k for k in call.keywords if k.arg is not None] + [
                        ast.keyword(arg=None, value=ast.parse(merged, mode="eval").body)
                    ]
        sibling = copy.deepcopy(cls)
        sibling.name = "Async" + cls.name
        for i, method in enumerate(sibling.body):
            if not isinstance(method, ast.FunctionDef):
                continue
            if method.name == "__init__":
                for arg in method.args.args:
                    if arg.arg == "client":
                        arg.annotation = ast.Name(
                            id="AsyncClientProtocol", ctx=ast.Load()
                        )
                continue
            method = AwaitInvocations(
                {
                    n.name
                    for n in cls.body
                    if isinstance(n, ast.FunctionDef) and n.name != "__init__"
                }
            ).visit(method)
            sibling.body[i] = ast.AsyncFunctionDef(
                **{
                    key: value
                    for key, value in vars(method).items()
                    if key in ast.AsyncFunctionDef._fields
                }
            )
        tree.body.append(sibling)
    imports = ast.parse(
        "from axonpush._internal.api.types import UNSET\n"
        + (
            "from axonpush._internal.api.models import "
            + ", ".join(sorted(added_enums))
            if added_enums
            else ""
        )
    )
    # Future imports must stay before ordinary imports.
    insertion = next(
        (
            i
            for i, n in enumerate(tree.body)
            if isinstance(n, (ast.Import, ast.ImportFrom))
            and not (isinstance(n, ast.ImportFrom) and n.module == "__future__")
        ),
        1,
    )
    tree.body[insertion:insertion] = imports.body
    ast.fix_missing_locations(tree)
    (destination / source.name).write_text(
        "# Generated by tools/generate-resource-facades.py; edit tools/resource-facades/.\n"
        + ast.unparse(tree)
        + "\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail on drift without writing resource files",
    )
    args = parser.parse_args()
    sources = sorted((ROOT / "tools/resource-facades").glob("*.py"))
    with (
        tempfile.TemporaryDirectory()
        if args.check
        else nullcontext(str(DEST)) as directory
    ):
        destination = Path(directory)
        for source in sources:
            generate(source, destination)
        paths = [str(destination / source.name) for source in sources]
        config = str(ROOT / "packages/python/pyproject.toml")
        for command in (["check", "--fix"], ["format"]):
            subprocess.run(
                ["uv", "run", "ruff", *command, "--config", config, *paths],
                cwd=ROOT / "packages/python",
                check=True,
            )
        if args.check:
            changed = [
                source.name
                for source in sources
                if (destination / source.name).read_bytes()
                != (DEST / source.name).read_bytes()
            ]
            if changed:
                parser.error("Generated facades out of date: " + ", ".join(changed))
            print("Generated resource facades are current.")
