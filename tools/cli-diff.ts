/**
 * Cross-language parity for `axonpush-eval`.
 *
 * surface-diff.ts covers the resource layer, and nothing covered the CLIs — so
 * they drifted in about a dozen observable ways: flags one had and the other
 * did not, a revision one accepted and another rejected, and two different
 * JSON reports out of the same run. CI configuration is written against these,
 * so they are a contract, not an implementation detail.
 *
 *   bun run tools/cli-diff.ts
 */
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path: string) => readFileSync(join(root, path), "utf-8");

const TS_CLI = "packages/typescript/src/cli.ts";
const TS_TYPES = "packages/typescript/src/evaluation/types.ts";
const PY_CLI = "packages/python/src/axonpush/eval/cli.py";
const PY_THRESHOLDS = "packages/python/src/axonpush/eval/thresholds.py";
const PY_REPORTS = "packages/python/src/axonpush/eval/reports.py";
const CS_CLI = "packages/dotnet/src/AxonPush.Cli/Program.cs";
const CS_THRESHOLDS = "packages/dotnet/src/AxonPush.Cli/Thresholds.cs";
const CS_REPORTS = "packages/dotnet/src/AxonPush.Cli/Reports.cs";

const problems: string[] = [];

const normalise = (name: string) => name.replace(/[_-]/g, "").toLowerCase();

const matches = (text: string, pattern: RegExp, group = 1): string[] =>
  [...text.matchAll(pattern)].map((match) => match[group]);

/** The brace-balanced body that follows an opening anchor. */
function block(text: string, open: RegExp): string {
  const start = text.search(open);
  if (start === -1) return "";
  let depth = 0;
  for (let index = text.indexOf("{", start); index < text.length; index++) {
    if (text[index] === "{") depth++;
    if (text[index] === "}" && --depth === 0) return text.slice(start, index);
  }
  return "";
}

/** Name -> value. A set is modelled as name -> name, so one comparison covers both. */
type Surface = Map<string, string>;

const setOf = (names: string[]): Surface => new Map(names.map((name) => [normalise(name), name]));

const pairsOf = (entries: Array<[string, string]>): Surface =>
  new Map(entries.map(([name, value]) => [normalise(name), value]));

interface Comparison {
  readonly what: string;
  readonly surfaces: Record<string, Surface>;
}

function flags(): Comparison {
  return {
    what: "flags",
    surfaces: {
      typescript: setOf(matches(read(TS_CLI), /--([a-z][a-z0-9-]*)/g)),
      python: setOf([
        ...matches(read(PY_CLI), /add_argument\(\s*"--([a-z][a-z0-9-]*)"/g),
        ...matches(read(PY_THRESHOLDS), /ThresholdOption\(\s*"([a-z][a-z0-9-]*)"/g),
      ]),
      dotnet: setOf([
        ...matches(read(CS_CLI), /--([a-z][a-z0-9-]*)/g),
        ...matches(read(CS_THRESHOLDS), /new\("([a-z][a-z0-9-]*)"/g),
      ]),
    },
  };
}

function exitCodes(): Comparison {
  return {
    what: "exit codes",
    surfaces: {
      typescript: pairsOf(
        [...block(read(TS_TYPES), /export const EXIT_CODES = \{/).matchAll(/(\w+):\s*(\d+)/g)].map(
          (m) => [m[1], m[2]],
        ),
      ),
      python: pairsOf(
        [...read(PY_CLI).matchAll(/^EXIT_(\w+)\s*=\s*(\d+)/gm)].map((m) => [m[1], m[2]]),
      ),
      dotnet: pairsOf(
        [...read(CS_CLI).matchAll(/^const int Exit(\w+)\s*=\s*(\d+)/gm)].map((m) => [m[1], m[2]]),
      ),
    },
  };
}

function reportKeys(): Comparison {
  return {
    what: "json report keys",
    surfaces: {
      typescript: setOf(
        matches(
          block(read(TS_TYPES), /export interface EvaluationRunResult \{/),
          /^\s{2}(\w+)\??:/gm,
        ),
      ),
      python: setOf(matches(block(read(PY_REPORTS), /payload = \{/), /"(\w+)":/g)),
      dotnet: setOf(
        matches(
          block(read(CS_REPORTS), /internal sealed class RunResult/),
          /\[JsonPropertyName\("(\w+)"\)\]/g,
        ),
      ),
    },
  };
}

for (const { what, surfaces } of [flags(), exitCodes(), reportKeys()]) {
  const languages = Object.keys(surfaces);
  const empty = languages.filter((language) => surfaces[language].size === 0);
  if (empty.length > 0) {
    problems.push(
      `could not read ${what} for ${empty.join(", ")}; the shape cli-diff parses has changed`,
    );
    continue;
  }

  const union = new Set(languages.flatMap((language) => [...surfaces[language].keys()]));
  const gaps: string[] = [];
  for (const key of [...union].sort()) {
    const missing = languages.filter((language) => !surfaces[language].has(key));
    if (missing.length > 0) {
      const name = languages.map((l) => surfaces[l].get(key)).find(Boolean) ?? key;
      gaps.push(`${name}: missing from ${missing.join(", ")}`);
      continue;
    }
    const values = new Set(languages.map((language) => surfaces[language].get(key)));
    if (values.size > 1) {
      gaps.push(
        `${key}: ${languages.map((language) => `${language} ${surfaces[language].get(key)}`).join(", ")}`,
      );
    }
  }

  if (gaps.length === 0) {
    console.log(`  ok    ${what} (${union.size} across ${languages.join(", ")})`);
    continue;
  }
  problems.push(`${what} differ`);
  console.log(`  FAIL  ${what}`);
  for (const gap of gaps) console.log(`          ${gap}`);
}

if (problems.length > 0) {
  console.log("\nthe CLIs have drifted apart");
  process.exit(1);
}
console.log("\nCLIs match");
