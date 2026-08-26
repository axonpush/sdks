import { fileURLToPath } from "node:url";
/**
 * Make the generated client valid Node ESM.
 *
 * openapi-ts emits extensionless relative imports, which Node refuses to
 * resolve at runtime. That went unnoticed while the package was bundled; the
 * build now emits real modules with tsc, so the specifiers have to be real too.
 *
 * Also rewrites the runtime-config import from `.ts` to `.js`, which the
 * generator writes from `runtimeConfigPath`. This replaces a `perl -pi -e` in
 * the codegen script that did not run on Windows.
 *
 *   bun run tools/postprocess-generated.ts
 */
import { existsSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";

const GENERATED = resolve(dirname(fileURLToPath(import.meta.url)), "..", "src", "_internal", "api");

function walk(dir: string): string[] {
  const out: string[] = [];
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    if (statSync(path).isDirectory()) out.push(...walk(path));
    else if (path.endsWith(".ts")) out.push(path);
  }
  return out;
}

const RELATIVE = /(from\s+["']|import\(\s*["'])(\.\.?\/[^"']*)(["'])/g;

let touched = 0;
let specifiers = 0;

for (const file of walk(GENERATED)) {
  const original = readFileSync(file, "utf-8");
  const here = dirname(file);
  const next = original
    .replace("from '../transport.ts'", "from '../transport.js'")
    .replace(RELATIVE, (match, head: string, spec: string, tail: string) => {
      if (/\.(js|json|mjs|cjs)$/.test(spec)) return match;
      const target = resolve(here, spec);
      // `./client` is a directory in the generated tree, `./sdk.gen` is a file
      const suffix = existsSync(`${target}.ts`)
        ? ".js"
        : existsSync(join(target, "index.ts"))
          ? "/index.js"
          : null;
      if (suffix === null) {
        console.log(`  unresolved: ${spec} (from ${file})`);
        return match;
      }
      specifiers += 1;
      return `${head}${spec}${suffix}${tail}`;
    });
  if (next !== original) {
    writeFileSync(file, next);
    touched += 1;
  }
}

console.log(`postprocessed ${touched} generated files (${specifiers} specifiers)`);
