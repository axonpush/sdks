"""Stage the pinned Go verifier for SDK packages. Run with Python 3.12+ and Go."""

import argparse
import hashlib
import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKAGES = HERE.parents[1] / "packages"
DESTINATIONS = {
    "typescript": PACKAGES / "typescript/bin",
    "python": PACKAGES / "python/src/axonpush/bin",
}
# Public compiler and booking fixtures from axonpush/server's workflow module,
# commit afaf0d45d20c45d5619a052f69a0e8af2da012f5. Refresh from upstream only.
SOURCE_SHA256 = "8af0e6a7717cb38134e53cc341a735859de98e03e906335348c97c20b3d29487"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packages", choices=DESTINATIONS, nargs="+")
    parser.add_argument("--host-only", action="store_true", help="for local smoke tests")
    args = parser.parse_args()
    archive = HERE / "source.tar.gz"
    if hashlib.sha256(archive.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise SystemExit("Workflow compiler source checksum mismatch")

    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp)
        with tarfile.open(archive) as tar:
            tar.extractall(src, filter="data")
        env = dict(os.environ, GOWORK="off", CGO_ENABLED="0")

        def go_output(*command: str) -> str:
            return subprocess.check_output(["go", *command], cwd=src, env=env, text=True).strip()

        targets = [(s, a) for s in ("linux", "darwin", "windows") for a in ("amd64", "arm64")]
        if args.host_only:
            targets = [(go_output("env", "GOHOSTOS"), go_output("env", "GOHOSTARCH"))]
        yaml_dir = Path(go_output("list", "-mod=readonly", "-f", "{{.Dir}}", "gopkg.in/yaml.v3"))
        notices = {
            "LICENSE-workflow": src / "LICENSE",
            "LICENSE-go": Path(go_output("env", "GOROOT")) / "LICENSE",
            "LICENSE-yaml": yaml_dir / "LICENSE",
            "NOTICE-yaml": yaml_dir / "NOTICE",
        }
        for name in args.packages:
            dest = DESTINATIONS[name]
            dest.mkdir(parents=True, exist_ok=True)
            for filename, source in notices.items():
                shutil.copyfile(source, dest / filename)
        for system, arch in targets:
            filename = "axonpush.exe" if system == "windows" else "axonpush"
            binary = src / filename
            subprocess.run(
                ["go", "build", "-mod=readonly", "-trimpath", "-buildvcs=false",
                 "-ldflags=-s -w -buildid=", "-o", str(binary), "./cmd/axonpush"],
                cwd=src, env=dict(env, GOOS=system, GOARCH=arch), check=True, timeout=300,
            )
            for name in args.packages:
                dest = DESTINATIONS[name] / f"{system}-{arch}"
                dest.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(binary, dest / filename)
                (dest / filename).chmod(0o755)
            print(f"Staged {system}-{arch}", flush=True)


if __name__ == "__main__":
    main()
