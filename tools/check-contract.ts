/** Verify the mirrored producer contract and business resource reachability. */
import { createHash } from "node:crypto";
import { readdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path: string) => readFileSync(join(root, path), "utf8");
const bytes = read("contract/openapi.sdk.json");
const spec = JSON.parse(bytes);
const lock = JSON.parse(read("contract/spec.lock"));
const operationIds: string[] = [];
for (const item of Object.values(spec.paths) as Record<string, unknown>[]) {
  for (const operation of Object.values(item) as { operationId?: string }[]) {
    if (operation?.operationId) operationIds.push(operation.operationId);
  }
}
operationIds.sort();
if (createHash("sha256").update(bytes).digest("hex") !== lock.sha256)
  throw new Error("Contract digest does not match spec.lock");
if (`${operationIds.join("\n")}\n` !== read("contract/operations.txt"))
  throw new Error("Operation list does not match contract");
const snake = (name: string) =>
  name
    .replace(/([a-z0-9])([A-Z])/g, "$1_$2")
    .replaceAll(".", "_")
    .toLowerCase();
const camel = (name: string) =>
  snake(name).replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
const pascal = (name: string) => {
  const result = camel(name);
  return result[0].toUpperCase() + result.slice(1);
};
let count = 0;
for (const id of operationIds) {
  const [group, method] = id.split(".");
  if (!["workspaces", "templates", "observations", "activity"].includes(group)) continue;
  for (const [file, token] of [
    [`packages/typescript/src/resources/${group}.ts`, `${camel(id)},`],
    [`packages/python/src/axonpush/resources/${group}.py`, snake(id)],
    [
      `packages/dotnet/src/AxonPush/Operations/${pascal(group)}Resource.g.cs`,
      `${pascal(method)}Async(`,
    ],
  ])
    if (!read(file).includes(token)) throw new Error(`${id} is not reachable in ${file}`);
  count++;
}
const unwrapped = new Set(
  read("contract/unwrapped.txt")
    .split("\n")
    .filter((line) => line && !line.startsWith("#")),
);
const resourceFiles = readdirSync(join(root, "packages/typescript/src/resources")).filter(
  (file) => file.endsWith(".ts") && !file.startsWith("_"),
);
const wrappers = resourceFiles
  .map((file) => read(`packages/typescript/src/resources/${file}`))
  .join("\n");
for (const id of unwrapped)
  if (!operationIds.includes(id)) throw new Error(`Stale unwrapped operation ${id}`);
for (const id of operationIds) {
  if (!unwrapped.has(id) && !new RegExp(`\\b${camel(id)}\\b`).test(wrappers))
    throw new Error(`Operation ${id} needs a wrapper or an explicit unwrapped decision`);
}
const legacy = operationIds.filter((id) =>
  /^(dashboards|moderation|governPolicies|spendPolicies|gateway)\./.test(id),
);
if (legacy.length) throw new Error(`Retired controls are still public: ${legacy.join(", ")}`);
console.log(
  `Contract digest, ${operationIds.length} operations and ${count} cross-language business wrappers verified`,
);
