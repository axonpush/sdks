/**
 * Guards the three things about the contract that nothing else checks.
 *
 * 1. `contract/operations.txt` still lists exactly the spec's operations.
 * 2. `contract/spec.lock` says which server revision produced the spec.
 * 3. Every published operation is reachable from a hand-written resource in
 *    every language, or is listed in `contract/unwrapped.txt` with a reason.
 *
 * Point three is the one with teeth: a new server endpoint used to arrive as a
 * generated client with no way to call it, and nothing failed.
 *
 *   bun run tools/check-contract.ts [--update-unwrapped]
 */
import { existsSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { basename, dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path: string) => readFileSync(join(root, path), "utf-8");

const UPDATE = process.argv.includes("--update-unwrapped");

const SPEC = "contract/openapi.sdk.json";
const OPERATIONS = "contract/operations.txt";
const LOCK = "contract/spec.lock";
const UNWRAPPED = "contract/unwrapped.txt";

const camel = (operationId: string): string => {
  const joined = operationId.replace(/_(.)/g, (_, c: string) => c.toUpperCase());
  return joined.charAt(0).toLowerCase() + joined.slice(1);
};

const snake = (operationId: string): string =>
  operationId
    .split("_")
    .map((part) => part.replace(/([a-z0-9])([A-Z])/g, "$1_$2").toLowerCase())
    .join("_");

interface Binding {
  readonly language: string;
  symbol(operationId: string): string;
  /** Symbols the generated client actually exposes, so a bad derivation is loud. */
  generated(): Set<string>;
  /** Source the hand-written layer lives in. */
  callSites(): string;
}

function filesUnder(dir: string, ext: string): string[] {
  const absolute = join(root, dir);
  if (!existsSync(absolute)) return [];
  return readdirSync(absolute).flatMap((entry) => {
    const path = join(absolute, entry);
    if (statSync(path).isDirectory()) return filesUnder(join(dir, entry), ext);
    return entry.endsWith(ext) ? [join(dir, entry)] : [];
  });
}

const concat = (dirs: string[], ext: string): string =>
  dirs
    .flatMap((dir) => filesUnder(dir, ext))
    .map((file) => read(file))
    .join("\n");

const BINDINGS: Binding[] = [
  {
    language: "typescript",
    symbol: camel,
    generated: () =>
      new Set(
        [
          ...read("packages/typescript/src/_internal/api/sdk.gen.ts").matchAll(
            /^export const ([a-zA-Z0-9_]+)/gm,
          ),
        ].map((m) => m[1]),
      ),
    callSites: () =>
      concat(["packages/typescript/src/resources", "packages/typescript/src/evaluation"], ".ts"),
  },
  {
    language: "python",
    symbol: snake,
    generated: () =>
      new Set(
        filesUnder("packages/python/src/axonpush/_internal/api/api", ".py")
          .map((file) => basename(file, ".py"))
          .filter((name) => name && name !== "__init__"),
      ),
    callSites: () =>
      concat(
        ["packages/python/src/axonpush/resources", "packages/python/src/axonpush/eval"],
        ".py",
      ),
  },
];

const spec = JSON.parse(read(SPEC)) as {
  paths: Record<string, Record<string, { operationId?: string }>>;
};

const operationIds = Object.values(spec.paths)
  .flatMap((methods) => Object.values(methods).map((op) => op.operationId))
  .filter((id): id is string => Boolean(id))
  .sort();

const problems: string[] = [];

const snapshot = read(OPERATIONS).trim().split(/\r?\n/).filter(Boolean);
if (snapshot.join("\n") !== operationIds.join("\n")) {
  const missing = operationIds.filter((id) => !snapshot.includes(id));
  const stale = snapshot.filter((id) => !operationIds.includes(id));
  problems.push(
    `${OPERATIONS} is out of date (${missing.length} new, ${stale.length} stale). Re-run the server's spec:audit --update-operations.`,
  );
}

try {
  const lock = JSON.parse(read(LOCK)) as {
    source?: string;
    sha?: string | null;
    workflow?: string;
  };
  if (lock.source !== "axonpush/server") problems.push(`${LOCK}: source must be axonpush/server`);
  if (typeof lock.sha === "string" && !/^[0-9a-f]{7,40}$/.test(lock.sha)) {
    problems.push(`${LOCK}: sha "${lock.sha}" is not a git revision`);
  }
  if (lock.sha === null && lock.workflow !== "local") {
    problems.push(`${LOCK}: only a local sync may leave sha null`);
  }
} catch {
  problems.push(`${LOCK} is missing or is not JSON`);
}

const uncovered = new Map<string, string[]>();
for (const binding of BINDINGS) {
  const generated = binding.generated();
  const sources = binding.callSites();
  for (const operationId of operationIds) {
    const symbol = binding.symbol(operationId);
    if (!generated.has(symbol)) {
      problems.push(
        `${binding.language}: derived "${symbol}" for ${operationId}, which the generated client does not expose`,
      );
      continue;
    }
    if (!new RegExp(String.raw`\b${symbol}\b`).test(sources)) {
      const languages = uncovered.get(operationId) ?? [];
      languages.push(binding.language);
      uncovered.set(operationId, languages);
    }
  }
}

if (UPDATE) {
  const lines = [...uncovered.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([operationId, languages]) => `${operationId}  # unwrapped in ${languages.join(", ")}`);
  writeFileSync(join(root, UNWRAPPED), `${lines.join("\n")}\n`, "utf-8");
  console.log(`wrote ${UNWRAPPED} (${lines.length} operations)`);
  process.exit(0);
}

const allowed = new Set(
  (existsSync(join(root, UNWRAPPED)) ? read(UNWRAPPED) : "")
    .split(/\r?\n/)
    .map((line) => line.replace(/#.*$/, "").trim())
    .filter(Boolean),
);

for (const [operationId, languages] of [...uncovered].sort()) {
  if (!allowed.has(operationId)) {
    problems.push(`no resource method reaches ${operationId} (${languages.join(", ")})`);
  }
}
for (const operationId of [...allowed].sort()) {
  if (!operationIds.includes(operationId)) {
    problems.push(`${UNWRAPPED} lists ${operationId}, which the contract no longer publishes`);
  } else if (!uncovered.has(operationId)) {
    problems.push(`${UNWRAPPED} lists ${operationId}, which is now wrapped. Remove the line.`);
  }
}

console.log(
  `${operationIds.length} operations, ${operationIds.length - uncovered.size} wrapped, ${uncovered.size} deliberately unwrapped`,
);

if (problems.length > 0) {
  console.log("");
  for (const problem of problems) console.log(`  FAIL  ${problem}`);
  process.exit(1);
}
console.log("\ncontract, snapshot and resource coverage agree");
