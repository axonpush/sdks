/**
 * Cross-language parity over the hand-written resource layer.
 *
 * ts-sdk already had a parity test, but it lived inside the TypeScript package
 * and hard-coded the method list, so it compared TypeScript against a copy of
 * itself and could not tell when Python fell behind. This reads the actual
 * source of each package and compares them to each other.
 *
 * Python ships a sync and an async class per resource in one file. They are
 * read as two separate surfaces, because collapsing them into one set hid an
 * AsyncFoo that had fallen behind its own Foo.
 *
 * Naming convention differs by language, so names are normalised before
 * comparison: listAll / list_all / ListAll all reduce to `listall`.
 *
 *   bun run tools/surface-diff.ts
 */
import { readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

const normalise = (name: string): string => name.replace(/[_-]/g, "").toLowerCase();

const strip = (name: string, affix: string): string => {
  if (name.startsWith(affix)) return name.slice(affix.length);
  if (name.endsWith(affix)) return name.slice(0, -affix.length);
  return name;
};

interface Language {
  readonly name: string;
  readonly dirs: readonly string[];
  readonly ext: string;
  /** Narrows which files in `dirs` hold a resource, when the directory holds more. */
  accepts?(file: string): boolean;
  read(text: string, resource: string): Array<[string, Set<string>]>;
}

function methodsIn(text: string, pattern: RegExp, exclude: (name: string) => boolean): Set<string> {
  const methods = new Set<string>();
  for (const match of text.matchAll(pattern)) {
    const name = match[1];
    if (!exclude(name)) methods.add(normalise(name));
  }
  return methods;
}

/** Split a Python module into its top-level classes so sync and async stay apart. */
function pythonClasses(text: string): Array<[string, string]> {
  const bounds = [...text.matchAll(/^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[(:]/gm)];
  return bounds.map((match, index) => {
    const start = match.index ?? 0;
    const end = index + 1 < bounds.length ? (bounds[index + 1].index ?? text.length) : text.length;
    return [match[1], text.slice(start, end)] as [string, string];
  });
}

function pythonLanguage(name: string, wanted: (className: string) => boolean): Language {
  return {
    name,
    dirs: ["packages/python/src/axonpush/resources"],
    ext: ".py",
    read: (text) =>
      pythonClasses(text)
        .filter(([className]) => wanted(className))
        .map(([className, body]) => [
          strip(normalise(className), "async"),
          methodsIn(body, /^ {4}(?:async\s+)?def\s+([a-zA-Z][a-zA-Z0-9_]*)\s*\(/gm, (n) =>
            n.startsWith("_"),
          ),
        ]),
  };
}

const LANGUAGES: Language[] = [
  {
    name: "typescript",
    dirs: ["packages/typescript/src/resources"],
    ext: ".ts",
    read: (text, resource) => [
      [
        resource,
        methodsIn(
          text,
          /^ {2}(?:async\s+)?([a-zA-Z][a-zA-Z0-9_]*)\s*\(/gm,
          (name) => name === "constructor",
        ),
      ],
    ],
  },
  pythonLanguage("python", (className) => !className.startsWith("Async")),
  pythonLanguage("python-async", (className) => className.startsWith("Async")),
  {
    name: "dotnet",
    // EventsResource stays hand-written under Events/, so both roots are read.
    dirs: ["packages/dotnet/src/AxonPush/Resources", "packages/dotnet/src/AxonPush/Events"],
    ext: ".cs",
    accepts: (file) => file.endsWith("Resource.cs") && file !== "ResourceBase.cs",
    read: (text, resource) => [
      [
        resource,
        new Set(
          [
            ...methodsIn(
              text,
              /^\s{4}public\s+(?:async\s+)?[\w<>,?[\].\s]+?\s([A-Z][A-Za-z0-9_]*)\s*\(/gm,
              (name) => name === "Dispose" || name === "DisposeAsync",
            ),
          ].map((name) => strip(name, "async")),
        ),
      ],
    ],
  },
];

/**
 * Python's async classes live in the same file as their sync twin, so one file
 * yields two entries. Every other language is one class per file.
 */
function surfaceOf(language: Language): Map<string, Set<string>> | null {
  const files: Array<[string, string]> = [];
  for (const dir of language.dirs) {
    let entries: string[];
    try {
      entries = readdirSync(join(root, dir));
    } catch {
      continue;
    }
    for (const file of entries) {
      if (
        !file.endsWith(language.ext) ||
        file.startsWith("_") ||
        file.endsWith(`.test${language.ext}`) ||
        file === `index${language.ext}` ||
        file.endsWith(`.g${language.ext}`) ||
        language.accepts?.(file) === false
      ) {
        continue;
      }
      files.push([dir, file]);
    }
  }
  if (files.length === 0) return null;

  const out = new Map<string, Set<string>>();
  for (const [dir, file] of files.sort(([, a], [, b]) => a.localeCompare(b))) {
    const text = readFileSync(join(root, dir, file), "utf-8");
    const resource = strip(normalise(file.slice(0, -language.ext.length)), "resource");
    for (const [key, methods] of language.read(text, resource)) out.set(key, methods);
  }
  return out;
}

const surfaces = new Map<string, Map<string, Set<string>>>();
for (const language of LANGUAGES) {
  const surface = surfaceOf(language);
  if (surface) {
    surfaces.set(language.name, surface);
    continue;
  }
  console.log(`could not read the ${language.name} surface at ${language.dirs.join(", ")}`);
  process.exit(1);
}

if (surfaces.size < 2) {
  console.log("need at least two surfaces to compare");
  process.exit(1);
}

const languages = [...surfaces.keys()];
const resources = [
  ...new Set(languages.flatMap((l) => [...(surfaces.get(l) as Map<string, Set<string>>).keys()])),
].sort();
const pad = Math.max(...languages.map((l) => l.length));

let failed = false;
console.log(`comparing ${resources.length} resources across ${languages.join(", ")}\n`);

for (const resource of resources) {
  const present = languages.filter((l) => surfaces.get(l)?.has(resource));
  const missing = languages.filter((l) => !surfaces.get(l)?.has(resource));
  if (missing.length > 0) {
    failed = true;
    console.log(`  FAIL  ${resource}: missing from ${missing.join(", ")}`);
    continue;
  }

  const union = new Set(present.flatMap((l) => [...(surfaces.get(l)?.get(resource) ?? [])]));
  const gaps = present
    .map(
      (l) => [l, [...union].filter((m) => !surfaces.get(l)?.get(resource)?.has(m)).sort()] as const,
    )
    .filter(([, missingMethods]) => missingMethods.length > 0);

  if (gaps.length === 0) {
    console.log(`  ok    ${resource} (${union.size} methods)`);
    continue;
  }
  failed = true;
  console.log(`  FAIL  ${resource}`);
  for (const [language, missingMethods] of gaps) {
    console.log(`          ${language.padEnd(pad)} missing: ${missingMethods.join(", ")}`);
  }
}

if (failed) {
  console.log("\nthe SDKs have drifted apart");
  process.exit(1);
}
console.log("\nsurfaces match");
