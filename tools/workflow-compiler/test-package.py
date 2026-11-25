"""Exercise a packed wheel or npm tarball in a fresh consumer project."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

artifact = Path(sys.argv[1]).resolve(strict=True)
examples = Path(__file__).resolve().parents[2] / "packages/typescript/examples"
env = os.environ.copy()
env.pop("AXONPUSH_WORKFLOW_BINARY", None)
env.pop("PYTHONPATH", None)

with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)

    def run(*args: str) -> str:
        cmd = shutil.which(args[0]) or args[0]
        return subprocess.check_output(
            [cmd, *args[1:]], cwd=root, env=env, text=True, timeout=180
        ).strip()

    if artifact.suffix == ".whl":
        run("uv", "venv", "--python", "3.12", "venv")
        scripts = root / "venv" / ("Scripts" if os.name == "nt" else "bin")
        python = str(scripts / ("python.exe" if os.name == "nt" else "python"))
        run("uv", "pip", "install", "--python", python, str(artifact))
        cli = [str(scripts / ("axonpush.exe" if os.name == "nt" else "axonpush"))]
        run(python, "-I", "-c", "from axonpush import AxonPush, AsyncAxonPush; "
            "from axonpush.workflow_worker import WorkflowWorker; from axonpush.workflow import run; "
            "run('init'); assert run('validate')['semantic_hash']; "
            "run('generate', '--language', 'python', '--out', 'generated')")
    else:
        (root / "package.json").write_text('{"private":true,"type":"module"}')
        run("npm", "install", "--no-audit", "--no-fund", str(artifact), "zod@4", "effect@^4.1.5")
        cli = ["npm", "exec", "--offline", "--", "axonpush"]
        run("node", "--input-type=module", "-e",
            'import { runWorkflow, WorkflowRuntime } from "@axonpush/sdk/workflow"; '
            'await runWorkflow(["init"]); if (!(await runWorkflow(["validate"])).semantic_hash) throw Error(); '
            'await runWorkflow(["generate","--language","typescript","--out","generated"]);')
        verdicts = []
        for provider in ("zod", "effect"):
            filename = f"workflow-{provider}.ts"
            shutil.copyfile(examples / filename, root / filename)
            verdicts.append(run("bun", "run", filename).split())
        assert verdicts[0] == verdicts[1] and verdicts[0][-1] == "violated", verdicts
    assert json.loads(run(*cli, "workflow", "version"))["version"] == "0.1.1"
    run(*cli, "workflow", "init", "--template", "booking-reschedule", "--out", "booking")
    result = run(*cli, "workflow", "action-test", "--file", "booking/workflow.yaml",
                 "--fixture", "booking/review.json")
    assert "review" in result, result
    print(f"{artifact.name}: bundled CLI, generation and booking scenario passed")
