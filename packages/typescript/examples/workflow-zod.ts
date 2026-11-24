import { writeFile } from "node:fs/promises";
import {
  compileZodWorkflow,
  defineZodWorkflow,
  verifyZodWorkflow,
} from "@axonpush/sdk/workflow/zod";
import { z } from "zod";

const bookingFields = {
  booking_request_id: z.string(),
  person_ref: z.string(),
  starts_at: z.iso.datetime({ offset: true }),
  service_ref: z.string(),
};

const workflow = defineZodWorkflow({
  schema_version: 1,
  workflow: "appointment_booking",
  case: { key: "booking_request_id" },
  facts: {
    "booking.accepted": { schema: z.strictObject(bookingFields) },
    "booking.record_observed": {
      schema: z.strictObject({ ...bookingFields, booking_ref: z.string() }),
      evidence_class: "provider_record",
    },
  },
  requirements: {
    booking_record: {
      trigger: { event: "booking.accepted" },
      evidence: {
        event: "booking.record_observed",
        match: {
          booking_request_id: "trigger.booking_request_id",
          person_ref: "trigger.person_ref",
          starts_at: "trigger.starts_at",
          service_ref: "trigger.service_ref",
        },
      },
      within: "2m",
      grace: "5m",
      fresh_for: "10m",
      source: "booking_adapter",
      max_matches: 1,
      evidence_key: "booking_ref",
    },
  },
  presentation: {
    title: "Appointment booking",
    stages: [{ id: "booking", label: "Booking record", requirements: ["booking_record"] }],
  },
});

// Both calls use compiler 0.1.0 bundled with the SDK.
const bundle = await compileZodWorkflow(workflow);
await writeFile("booking.contract.json", workflow.source);
const result = await verifyZodWorkflow(workflow, {
  case_id: "request-1",
  now: "2026-11-20T10:10:00Z",
  facts: [
    {
      id: "request-1:accepted",
      event: "booking.accepted",
      case_id: "request-1",
      source: "booking_adapter",
      occurred_at: "2026-11-20T10:00:00Z",
      received_at: "2026-11-20T10:00:01Z",
      fields: {
        booking_request_id: "request-1",
        person_ref: "synthetic-person",
        starts_at: "2026-11-21T10:00:00Z",
        service_ref: "synthetic-service",
      },
    },
  ],
  coverage: [
    {
      source: "booking_adapter",
      healthy: true,
      checked_at: "2026-11-20T10:10:00Z",
      complete_through: "2026-11-20T10:10:00Z",
    },
  ],
});
console.log(bundle.semantic_hash, result.obligations?.[0]?.state); // violated

// Publication uses the same HTTP operation as YAML:
// await author.workflows.publish(workspaceId, { source: workflow.source }, { environment: "dev" });
// Activate the returned definition ID explicitly. Keep external provider credentials in your app.
