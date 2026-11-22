/** Zod authoring adapter. All contract validation and verdicts remain in Go. */
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import type { z } from "zod";
import type { Bundle, Contract, Input, Result } from "./_internal/api/types.gen.js";
import { runWorkflow } from "./workflow.js";

export type ZodWorkflowOptions = Omit<Contract, "facts"> & {
  facts: Record<
    string,
    {
      schema: z.ZodType;
      evidence_class?:
        | "claim"
        | "application_record"
        | "provider_record"
        | "human_attestation"
        | "inferred";
    }
  >;
};
export type ZodWorkflowDefinition = Readonly<{ source: string }>;
export type WorkflowBinaryOptions = { binary?: string; timeout?: number };

function unsupported(path: string): never {
  throw new Error(
    `${path}: unsupported Zod schema or constraint; use strict objects of plain string, number, boolean or z.iso.datetime({ offset: true }) fields`,
  );
}

// Inspect original definitions, not just JSON Schema: conversion can omit custom
// refinements. Fail closed on additional checks/options rather than weakening them.
function definition(schema: z.ZodType, path: string, allowed: string[]) {
  const def = schema?._zod?.def as unknown as Record<string, unknown>;
  if (
    !def ||
    Object.keys(def).some((key) => !allowed.includes(key)) ||
    (Array.isArray(def.checks) && def.checks.length > 0)
  )
    unsupported(path);
  return def;
}

function scalar(schema: z.ZodType, path: string): string {
  const def = definition(schema, path, [
    "type",
    "checks",
    "error",
    "format",
    "check",
    "offset",
    "local",
    "precision",
    "pattern",
  ]);
  if (def.type === "string" && def.format === "datetime") {
    if (
      def.offset !== true ||
      def.local !== false ||
      def.precision != null ||
      def.check !== "string_format"
    )
      unsupported(path);
    return "timestamp";
  }
  if (
    def.format ||
    def.check ||
    Object.keys(def).some((k) => !["type", "checks", "error"].includes(k))
  )
    unsupported(path);
  if (def.type === "string" || def.type === "number" || def.type === "boolean") return def.type;
  return unsupported(path);
}

function fields(schema: z.ZodType, path: string): Record<string, string> {
  const def = definition(schema, path, ["type", "checks", "error", "shape", "catchall"]);
  const catchall = def.catchall as z.ZodType | undefined;
  if (def.type !== "object" || catchall?._zod.def.type !== "never") unsupported(path);
  return Object.fromEntries(
    Object.entries(def.shape as Record<string, z.ZodType>).map(([key, value]) => [
      key,
      scalar(value, `${path}.${key}`),
    ]),
  );
}

function canonical(value: unknown): unknown {
  if (value === null || typeof value === "string" || typeof value === "boolean") return value;
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (Array.isArray(value)) return value.map(canonical);
  if (typeof value === "object" && Object.getPrototypeOf(value) === Object.prototype) {
    return Object.fromEntries(
      Object.entries(value as Record<string, unknown>)
        .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0))
        .map(([key, entry]) => [key, canonical(entry)]),
    );
  }
  throw new Error("Workflow configuration must contain only finite JSON values");
}

/** Pure, deterministic source generation; compile before publishing. JSON is YAML-compatible. */
export function defineZodWorkflow(options: ZodWorkflowOptions): ZodWorkflowDefinition {
  const facts = Object.fromEntries(
    Object.entries(options.facts).map(([event, fact]) => {
      if (Object.keys(fact).some((k) => !["schema", "evidence_class"].includes(k)))
        unsupported(`facts.${event}`);
      return [
        event,
        {
          fields: fields(fact.schema, `facts.${event}`),
          ...(fact.evidence_class === undefined ? {} : { evidence_class: fact.evidence_class }),
        },
      ];
    }),
  );
  return Object.freeze({
    source: `${JSON.stringify(canonical({ ...options, facts }), null, 2)}\n`,
  });
}

async function withSource<T>(
  workflow: ZodWorkflowDefinition,
  execute: (file: string, directory: string) => Promise<T>,
): Promise<T> {
  const directory = await mkdtemp(join(tmpdir(), "axonpush-zod-"));
  try {
    const file = join(directory, "workflow.json");
    await writeFile(file, workflow.source, { mode: 0o600 });
    return await execute(file, directory);
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
}

/** Invoke the version-pinned Go compiler, including its type checks and hashes. */
export async function compileZodWorkflow(
  workflow: ZodWorkflowDefinition,
  options: WorkflowBinaryOptions = {},
): Promise<Bundle> {
  return withSource(
    workflow,
    async (file) => (await runWorkflow(["validate", "--file", file], options)) as Bundle,
  );
}

/** Invoke the same Go evaluator used by the server, with an explicit fixture clock. */
export async function verifyZodWorkflow(
  workflow: ZodWorkflowDefinition,
  input: Input,
  options: WorkflowBinaryOptions = {},
): Promise<Result> {
  return withSource(workflow, async (file, directory) => {
    const fixture = join(directory, "case.json");
    await writeFile(fixture, JSON.stringify(input), { mode: 0o600 });
    return (await runWorkflow(["test", "--file", file, "--fixture", fixture], options)) as Result;
  });
}
