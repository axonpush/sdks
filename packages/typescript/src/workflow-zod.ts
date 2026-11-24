/** Zod authoring adapter. All contract validation and verdicts remain in Go. */
import type { z } from "zod";
import type { ActionSpec, Contract } from "./_internal/api/types.gen.js";
import { serializeWorkflow } from "./_internal/workflow-provider.js";

export type {
  WorkflowBinaryOptions,
  WorkflowDefinition as ZodWorkflowDefinition,
} from "./_internal/workflow-provider.js";
export {
  compileWorkflow as compileZodWorkflow,
  verifyWorkflow as verifyZodWorkflow,
} from "./_internal/workflow-provider.js";

import type { WorkflowDefinition as ZodWorkflowDefinition } from "./_internal/workflow-provider.js";

export type ZodWorkflowOptions = Omit<Contract, "facts" | "actions"> & {
  actions?: Record<
    string,
    Omit<ActionSpec, "inputs" | "outputs"> & { inputs: z.ZodType; outputs: z.ZodType }
  >;
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
  const actions =
    options.actions &&
    Object.fromEntries(
      Object.entries(options.actions).map(([name, action]) => [
        name,
        {
          ...action,
          inputs: fields(action.inputs, `actions.${name}.inputs`),
          outputs: fields(action.outputs, `actions.${name}.outputs`),
        },
      ]),
    );
  return serializeWorkflow({ ...options, facts, ...(actions ? { actions } : {}) });
}
