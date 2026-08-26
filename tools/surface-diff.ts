/**
 * Cross-language parity over the hand-written resource layer.
 *
 * ts-sdk already had a parity test, but it lived inside the TypeScript package
 * and hard-coded the method list, so it compared TypeScript against a copy of
 * itself and could not tell when Python fell behind. This reads the actual
 * source of each package and compares them to each other.
 *
 * Naming convention differs by language, so names are normalised before
 * comparison: listAll / list_all / ListAll all reduce to `listall`.
 *
 *   bun run tools/surface-diff.ts
 */
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const root = join(import.meta.dir, "..");

const normalise = (name: string): string => name.replace(/[_-]/g, "").toLowerCase();

/** Resources are one file per resource in both packages, `_`-prefixed files excluded. */
function readDir(dir: string, ext: string): string[] {
  try {
    return readdirSync(join(root, dir))
      .filter((f) => f.endsWith(ext) && !f.startsWith("_") && f !== `index${ext}`)
      .sort();
  } catch {
    return [];
  }
}

function typescriptSurface(): Map<string, Set<string>> {
  const out = new Map<string, Set<string>>();
  for (const file of readDir("packages/typescript/src/resources", ".ts")) {
    if (file.endsWith(".test.ts")) continue;
    const text = readFileSync(join(root, "packages/typescript/src/resources", file), "utf-8");
    const methods = new Set<string>();
    // `async name(` / `name(` at class-member indentation, skipping the ctor
    for (const m of text.matchAll(/^ {2}(?:async\s+)?([a-zA-Z][a-zA-Z0-9_]*)\s*\(/gm)) {
      if (m[1] !== "constructor") methods.add(normalise(m[1]));
    }
    out.set(normalise(file.replace(/\.ts$/, "")), methods);
  }
  return out;
}

function pythonSurface(): Map<string, Set<string>> {
  const out = new Map<string, Set<string>>();
  for (const file of readDir("packages/python/src/axonpush/resources", ".py")) {
    const text = readFileSync(join(root, "packages/python/src/axonpush/resources", file), "utf-8");
    const methods = new Set<string>();
    for (const m of text.matchAll(/^ {4}(?:async\s+)?def\s+([a-zA-Z][a-zA-Z0-9_]*)\s*\(/gm)) {
      if (!m[1].startsWith("_")) methods.add(normalise(m[1]));
    }
    out.set(normalise(file.replace(/\.py$/, "")), methods);
  }
  return out;
}

const ts = typescriptSurface();
const py = pythonSurface();

if (ts.size === 0 || py.size === 0) {
  console.log(`could not read a surface (ts=${ts.size} resources, py=${py.size} resources)`);
  process.exit(1);
}

let failed = false;
const resources = [...new Set([...ts.keys(), ...py.keys()])].sort();

console.log(`comparing ${resources.length} resources\n`);
for (const resource of resources) {
  const a = ts.get(resource);
  const b = py.get(resource);
  if (!a) {
    console.log(`  FAIL  ${resource}: missing from typescript`);
    failed = true;
    continue;
  }
  if (!b) {
    console.log(`  FAIL  ${resource}: missing from python`);
    failed = true;
    continue;
  }
  const onlyTs = [...a].filter((m) => !b.has(m)).sort();
  const onlyPy = [...b].filter((m) => !a.has(m)).sort();
  if (onlyTs.length === 0 && onlyPy.length === 0) {
    console.log(`  ok    ${resource} (${a.size} methods)`);
    continue;
  }
  failed = true;
  console.log(`  FAIL  ${resource}`);
  if (onlyTs.length > 0) console.log(`          typescript only: ${onlyTs.join(", ")}`);
  if (onlyPy.length > 0) console.log(`          python only:     ${onlyPy.join(", ")}`);
}

if (failed) {
  console.log("\nthe SDKs have drifted apart");
  process.exit(1);
}
console.log("\nsurfaces match");
