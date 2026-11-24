import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Schema, SchemaGetter } from "effect";
import { describe, expect, it } from "vitest";
import { z } from "zod";
import type { Bundle, Input } from "../_internal/api/types.gen.js";
import { runWorkflow } from "../workflow.js";
import {
  compileEffectWorkflow,
  defineEffectWorkflow,
  type EffectWorkflowOptions,
  verifyEffectWorkflow,
  WorkflowTimestamp,
} from "../workflow-effect.js";
import { defineZodWorkflow } from "../workflow-zod.js";

const options = (): EffectWorkflowOptions => ({
  schema_version: 1,
  workflow: "booking",
  case: { key: "request_id" },
  facts: {
    "booking.accepted": {
      schema: Schema.Struct({ request_id: Schema.String, starts_at: WorkflowTimestamp }),
    },
    "booking.observed": {
      schema: Schema.Struct({ request_id: Schema.String, starts_at: WorkflowTimestamp }),
      evidence_class: "provider_record",
    },
  },
  requirements: {
    record: {
      trigger: { event: "booking.accepted" },
      evidence: {
        event: "booking.observed",
        match: { request_id: "trigger.request_id", starts_at: "trigger.starts_at" },
      },
      source: "adapter",
      within: "2m",
      grace: "5m",
      fresh_for: "10m",
    },
  },
  presentation: { title: "Booking" },
});

describe("Effect workflow authoring", () => {
  it("produces the same source as Zod, independent of key ordering", () => {
    const input = options();
    const policy = {
      from: "booked",
      to: "rescheduled",
      actors: ["agent"],
      handler: "adapter",
      requirement: "record",
      expected: { request_id: "case_id", starts_at: "input.starts_at" },
    };
    input.initial_state = "booked";
    const effect = defineEffectWorkflow({
      ...input,
      actions: {
        move: {
          ...policy,
          inputs: Schema.Struct({ starts_at: WorkflowTimestamp }),
          outputs: Schema.Struct({ revision: Schema.Number }),
        },
      },
    });
    const zod = defineZodWorkflow({
      ...input,
      actions: {
        move: {
          ...policy,
          inputs: z.strictObject({ starts_at: z.iso.datetime({ offset: true }) }),
          outputs: z.strictObject({ revision: z.number() }),
        },
      },
      facts: {
        "booking.observed": {
          schema: z.strictObject({
            starts_at: z.iso.datetime({ offset: true }),
            request_id: z.string(),
          }),
          evidence_class: "provider_record",
        },
        "booking.accepted": {
          schema: z.strictObject({
            request_id: z.string(),
            starts_at: z.iso.datetime({ offset: true }),
          }),
        },
      },
    });
    expect(effect.source).toBe(zod.source);
  });

  it("supports scalar numbers, finite numbers and booleans", () => {
    const input = options();
    input.facts["booking.accepted"] = {
      schema: Schema.Struct({
        request_id: Schema.String,
        count: Schema.Number,
        total: Schema.Finite,
        enabled: Schema.Boolean,
      }),
    };
    expect(JSON.parse(defineEffectWorkflow(input).source).facts["booking.accepted"].fields).toEqual(
      { request_id: "string", count: "number", total: "number", enabled: "boolean" },
    );
  });

  it.each([
    Schema.String.check(Schema.isMinLength(1)),
    Schema.Number.check(Schema.isGreaterThan(0)),
    Schema.optional(Schema.String),
    Schema.NullOr(Schema.String),
    Schema.Literal("x"),
    Schema.Array(Schema.String),
    Schema.Struct({ nested: Schema.String }),
    Schema.NumberFromString,
    Schema.DateTimeUtcFromString,
    Schema.String.pipe(
      Schema.decodeTo(Schema.String, {
        decode: SchemaGetter.transform((v) => v),
        encode: SchemaGetter.transform((v) => v),
      }),
    ),
    WorkflowTimestamp.check(Schema.isMinLength(1)),
    Schema.String.annotate({ jsonSchema: { type: "string" } }),
  ])("rejects unsupported field schema %#", (schema) => {
    const input = options();
    input.facts["booking.accepted"] = { schema: Schema.Struct({ request_id: schema }) };
    expect(() => defineEffectWorkflow(input)).toThrow("facts.booking.accepted.request_id");
  });

  it("rejects root checks and records", () => {
    const input = options();
    input.facts["booking.accepted"] = {
      schema: Schema.Struct({ request_id: Schema.String }).check(Schema.makeFilter(() => true)),
    };
    expect(() => defineEffectWorkflow(input)).toThrow("unsupported Effect");
    input.facts["booking.accepted"] = { schema: Schema.Record(Schema.String, Schema.String) };
    expect(() => defineEffectWorkflow(input)).toThrow("unsupported Effect");
  });

  it("never runs user-defined filters", () => {
    let calls = 0;
    const input = options();
    input.facts["booking.accepted"] = {
      schema: Schema.Struct({
        request_id: Schema.String.check(
          Schema.makeFilter(() => {
            calls++;
            return true;
          }),
        ),
      }),
    };
    expect(() => defineEffectWorkflow(input)).toThrow();
    expect(calls).toBe(0);
  });
});

describe.skipIf(!process.env.AXONPUSH_WORKFLOW_BINARY)("Effect native parity", () => {
  it("uses the same Go semantics as YAML for all four verdicts and rejects invalid facts", async () => {
    const workflow = defineEffectWorkflow(options());
    const bundle = await compileEffectWorkflow(workflow);
    const directory = await mkdtemp(join(tmpdir(), "axonpush-effect-test-"));
    try {
      const yamlFile = join(directory, "contract.yaml");
      await writeFile(
        yamlFile,
        `schema_version: 1
workflow: booking
case: {key: request_id}
facts:
  booking.accepted:
    fields: {request_id: string, starts_at: timestamp}
  booking.observed:
    fields: {request_id: string, starts_at: timestamp}
    evidence_class: provider_record
requirements:
  record:
    trigger: {event: booking.accepted}
    evidence:
      event: booking.observed
      match: {request_id: trigger.request_id, starts_at: trigger.starts_at}
    source: adapter
    within: 2m
    grace: 5m
    fresh_for: 10m
presentation: {title: Booking}
`,
      );
      expect(bundle.semantic_hash).toBe(
        ((await runWorkflow(["validate", "--file", yamlFile])) as Bundle).semantic_hash,
      );
      const input: Input = {
        case_id: "req1",
        now: "2026-11-20T10:10:00Z",
        facts: [
          {
            id: "start",
            event: "booking.accepted",
            case_id: "req1",
            source: "adapter",
            occurred_at: "2026-11-20T10:00:00Z",
            received_at: "2026-11-20T10:00:01Z",
            fields: { request_id: "req1", starts_at: "2026-11-21T10:00:00Z" },
          },
        ],
        coverage: [
          {
            source: "adapter",
            healthy: true,
            checked_at: "2026-11-20T10:10:00Z",
            complete_through: "2026-11-20T10:10:00Z",
          },
        ],
      };
      for (const state of ["violated", "unverifiable", "pending", "satisfied"]) {
        const current = structuredClone(input);
        if (state === "unverifiable") current.coverage![0]!.healthy = false;
        if (state === "pending") {
          current.now = "2026-11-20T10:01:00Z";
          current.coverage = [];
        }
        if (state === "satisfied")
          current.facts!.push({
            ...current.facts![0]!,
            id: "done",
            event: "booking.observed",
            occurred_at: "2026-11-20T10:01:00Z",
            received_at: "2026-11-20T10:01:01Z",
            fields: { request_id: "req1", starts_at: "2026-11-21T15:30:00+05:30" },
          });
        const result = await verifyEffectWorkflow(workflow, current);
        expect(result.obligations![0]!.state).toBe(state);
        const fixture = join(directory, "case.json");
        await writeFile(fixture, JSON.stringify(current));
        expect(result).toEqual(
          await runWorkflow(["test", "--file", yamlFile, "--fixture", fixture]),
        );
      }
      const bad = structuredClone(input);
      bad.facts![0]!.fields.extra = "unmodeled";
      await expect(verifyEffectWorkflow(workflow, bad)).rejects.toThrow();
      bad.facts![0]!.fields = { request_id: "req1", starts_at: "invalid-time" };
      await expect(verifyEffectWorkflow(workflow, bad)).rejects.toThrow();
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  }, 60_000);
});
