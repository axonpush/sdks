import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { z } from "zod";
import type { Bundle, Input } from "../_internal/api/types.gen.js";
import { runWorkflow } from "../workflow.js";
import {
  compileZodWorkflow,
  defineZodWorkflow,
  verifyZodWorkflow,
  type ZodWorkflowOptions,
} from "../workflow-zod.js";

const options = (): ZodWorkflowOptions => ({
  schema_version: 1,
  workflow: "booking",
  case: { key: "request_id" },
  facts: {
    "booking.accepted": {
      schema: z.strictObject({
        request_id: z.string(),
        starts_at: z.iso.datetime({ offset: true }),
      }),
    },
    "booking.observed": {
      schema: z.strictObject({
        request_id: z.string(),
        starts_at: z.iso.datetime({ offset: true }),
      }),
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

describe("Zod workflow provider", () => {
  it("emits identical source independent of object key insertion order", () => {
    const a = options();
    const b = { ...a, facts: Object.fromEntries(Object.entries(a.facts).reverse()) };
    b.facts["booking.accepted"] = {
      schema: z.strictObject({
        starts_at: z.iso.datetime({ offset: true }),
        request_id: z.string(),
      }),
    };
    expect(defineZodWorkflow(a).source).toBe(defineZodWorkflow(b).source);
    expect(JSON.parse(defineZodWorkflow(a).source).facts["booking.accepted"].fields.starts_at).toBe(
      "timestamp",
    );
  });

  it.each([
    z.string().min(1),
    z.string().refine(() => true),
    z.string().transform((v) => v),
    z.string().optional(),
    z.string().nullable(),
    z.string().default("x"),
    z.coerce.string(),
    z.number().int(),
    z.number().min(0),
    z.enum(["a", "b"]),
    z.array(z.string()),
    z.object({ nested: z.string() }),
    z.date(),
    z.literal("x"),
    z.iso.datetime(),
    z.iso.datetime({ offset: true, precision: 3 }),
    z.iso.datetime({ offset: true, local: true }),
  ])("rejects unsupported field schema %#", (schema) => {
    const input = options();
    input.facts["booking.accepted"] = { schema: z.strictObject({ request_id: schema }) };
    expect(() => defineZodWorkflow(input)).toThrow("facts.booking.accepted.request_id");
  });

  it.each([
    z.object({ request_id: z.string() }),
    z.looseObject({ request_id: z.string() }),
    z.strictObject({ request_id: z.string() }).refine(() => true),
  ])("requires strict, unrefined fact objects %#", (schema) => {
    const input = options();
    input.facts["booking.accepted"] = { schema };
    expect(() => defineZodWorkflow(input)).toThrow("unsupported Zod");
  });

  it("supports finite numbers and booleans without inventing contract constraints", () => {
    const input = options();
    input.facts["booking.accepted"] = {
      schema: z.strictObject({ request_id: z.string(), count: z.number(), enabled: z.boolean() }),
    };
    expect(JSON.parse(defineZodWorkflow(input).source).facts["booking.accepted"].fields).toEqual({
      request_id: "string",
      count: "number",
      enabled: "boolean",
    });
  });
});

// Set to the real native compiler in CI/local parity runs; no JS verifier mock.
describe.skipIf(!process.env.AXONPUSH_WORKFLOW_BINARY)("Go verifier parity", () => {
  it("compiles YAML and Zod to the same semantics and evaluates all four outcomes", async () => {
    const workflow = defineZodWorkflow(options());
    const bundle = await compileZodWorkflow(workflow);
    const directory = await mkdtemp(join(tmpdir(), "axonpush-parity-"));
    try {
      const file = join(directory, "workflow.yaml");
      await writeFile(
        file,
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
      const yaml = (await runWorkflow(["validate", "--file", file])) as Bundle;
      expect(bundle.semantic_hash).toBe(yaml.semantic_hash);
      const input: Input = {
        case_id: "req1",
        now: "2026-11-20T10:10:00Z",
        facts: [
          {
            id: "start",
            case_id: "req1",
            event: "booking.accepted",
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
        const result = await verifyZodWorkflow(workflow, current);
        expect(result.obligations![0]!.state).toBe(state);
        const fixture = join(directory, "case.json");
        await writeFile(fixture, JSON.stringify(current));
        expect(result).toEqual(await runWorkflow(["test", "--file", file, "--fixture", fixture]));
      }
      const invalid = options();
      invalid.requirements.record!.evidence.match = { starts_at: "trigger.missing" };
      await expect(compileZodWorkflow(defineZodWorkflow(invalid))).rejects.toThrow();
    } finally {
      await rm(directory, { recursive: true, force: true });
    }
  }, 60_000);
});
