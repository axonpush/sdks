/**
 * 04 — Multi-agent fan-out on one channel
 *
 * Three logical agents (`planner`, `coder`, `reviewer`) publish events on
 * one channel under a shared trace, then we list them back and pick out the
 * error events.
 *
 * Required env vars:
 *   AXONPUSH_API_KEY, AXONPUSH_TENANT_ID, AXONPUSH_CHANNEL_ID
 *
 * Run:
 *   bun run examples/04-multi-agent.ts
 */

import { AxonPush } from "../src/index";
import { CHANNEL_ID, requireEnv } from "./config";

const AGENTS = ["planner", "coder", "reviewer"] as const;
const TYPES = ["agent.start", "agent.message", "agent.error", "agent.end"] as const;

async function main() {
  requireEnv("AXONPUSH_API_KEY");
  requireEnv("AXONPUSH_TENANT_ID");
  if (!CHANNEL_ID) throw new Error("AXONPUSH_CHANNEL_ID required");

  const client = new AxonPush();
  const trace = client.getOrCreateTrace();

  for (let i = 0; i < 12; i++) {
    const agentId = AGENTS[i % AGENTS.length]!;
    const eventType = TYPES[i % TYPES.length]!;
    await client.events.publish({
      identifier: `${agentId}-${i}`,
      channelId: CHANNEL_ID,
      agentId,
      eventType,
      traceId: trace.traceId,
      payload: eventType === "agent.error" ? { reason: "synthetic failure" } : { step: i },
    });
  }

  const listing = await client.events.search({ channelId: CHANNEL_ID, limit: 20 });
  for (const event of listing?.events ?? []) {
    console.log(`[all] ${event.eventType} from ${event.agentId}`);
    if (event.eventType === "agent.error") {
      console.log(`[errors] ${event.eventId}: ${JSON.stringify(event.payload)}`);
    }
  }

  client.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
