/**
 * Every package states its version in two places. Keep them in step.
 *
 * ts-sdk shipped 0.0.7 with src/version.ts still saying 0.0.6, and the SDK
 * re-exports that constant publicly. Releases are tag-driven here, so nothing
 * else would notice.
 *
 *   bun run tools/check-versions.ts
 */
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (p: string) => readFileSync(join(root, p), "utf-8");

interface Check {
  package: string;
  sources: { file: string; version: string | undefined }[];
}

const extract = (file: string, re: RegExp): string | undefined => {
  const m = re.exec(read(file));
  return m?.[1];
};

const checks: Check[] = [
  {
    package: "@axonpush/sdk",
    sources: [
      {
        file: "packages/typescript/package.json",
        version: JSON.parse(read("packages/typescript/package.json")).version,
      },
      {
        file: "packages/typescript/src/version.ts",
        version: extract("packages/typescript/src/version.ts", /"([^"]+)"/),
      },
    ],
  },
  {
    package: "axonpush",
    sources: [
      {
        file: "packages/python/pyproject.toml",
        version: extract("packages/python/pyproject.toml", /^version\s*=\s*"([^"]+)"/m),
      },
      {
        file: "packages/python/src/axonpush/_version.py",
        version: extract("packages/python/src/axonpush/_version.py", /"([^"]+)"/),
      },
    ],
  },
  {
    package: "AxonPush",
    sources: [
      {
        file: "packages/dotnet/Directory.Build.props",
        version: extract("packages/dotnet/Directory.Build.props", /<VersionPrefix>([^<]+)</),
      },
    ],
  },
];

let failed = false;
for (const check of checks) {
  const versions = check.sources.map((s) => s.version);
  const unique = [...new Set(versions)];
  const label = `${check.package.padEnd(16)} ${unique.join(" / ")}`;
  if (unique.length === 1 && unique[0]) {
    console.log(`  ok    ${label}`);
    continue;
  }
  failed = true;
  console.log(`  FAIL  ${check.package}`);
  for (const s of check.sources) console.log(`          ${s.version ?? "(not found)"}  ${s.file}`);
}

if (failed) {
  console.log("\nversions disagree; make them match before tagging a release");
  process.exit(1);
}
console.log("\nall package versions consistent");
