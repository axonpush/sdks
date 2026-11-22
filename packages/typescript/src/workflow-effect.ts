/** Effect Schema authoring only; the shared Go verifier decides outcomes. */
import * as Schema from "effect/Schema";
import type * as AST from "effect/SchemaAST";
import type { Contract } from "./_internal/api/types.gen.js";
import { serializeWorkflow } from "./_internal/workflow-provider.js";

export type {
  WorkflowBinaryOptions,
  WorkflowDefinition as EffectWorkflowDefinition,
} from "./_internal/workflow-provider.js";
export {
  compileWorkflow as compileEffectWorkflow,
  verifyWorkflow as verifyEffectWorkflow,
} from "./_internal/workflow-provider.js";

import type { WorkflowDefinition } from "./_internal/workflow-provider.js";

/** String wire representation. Calendar validity is enforced by the native verifier. */
export const WorkflowTimestamp = Schema.String.check(
  Schema.isPattern(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2})$/),
);

export type EffectWorkflowOptions = Omit<Contract, "facts"> & {
  facts: Record<
    string,
    {
      schema: Schema.Top;
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
    `${path}: unsupported Effect schema or constraint; use Schema.Struct with String, Number/Finite, Boolean or WorkflowTimestamp fields`,
  );
}

function plain(ast: AST.AST, path: string, knownChecks = false) {
  if (
    ast.encoding ||
    ast.context ||
    (!knownChecks && ast.checks?.length) ||
    ("encodingChecks" in ast && ast.encodingChecks) ||
    (ast.annotations &&
      Reflect.ownKeys(ast.annotations).some(
        (k) => typeof k !== "string" || !["title", "description", "identifier"].includes(k),
      ))
  )
    unsupported(path);
}

function scalar(ast: AST.AST, path: string): string {
  const timestamp = ast === WorkflowTimestamp.ast;
  const finite = ast === Schema.Finite.ast;
  plain(ast, path, timestamp || finite);
  if (timestamp) return "timestamp";
  switch (ast._tag) {
    case "String":
      return "string";
    case "Number":
      return "number";
    case "Boolean":
      return "boolean";
    default:
      return unsupported(path);
  }
}

/** Lower original AST nodes; JSON Schema annotations cannot bypass unsupported checks. */
export function defineEffectWorkflow(options: EffectWorkflowOptions): WorkflowDefinition {
  const facts = Object.fromEntries(
    Object.entries(options.facts).map(([event, fact]) => {
      const path = `facts.${event}`;
      if (Object.keys(fact).some((k) => !["schema", "evidence_class"].includes(k)))
        unsupported(path);
      const ast = fact.schema.ast;
      plain(ast, path);
      if (ast._tag !== "Objects" || ast.indexSignatures.length) unsupported(path);
      const fields = Object.fromEntries(
        ast.propertySignatures.map((property) => {
          if (typeof property.name !== "string") unsupported(path);
          return [property.name, scalar(property.type, `${path}.${property.name}`)];
        }),
      );
      return [
        event,
        {
          fields,
          ...(fact.evidence_class === undefined ? {} : { evidence_class: fact.evidence_class }),
        },
      ];
    }),
  );
  return serializeWorkflow({ ...options, facts });
}
