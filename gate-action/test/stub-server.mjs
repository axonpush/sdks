/**
 * The smallest server the release gate can run against: the six routes the CLI
 * touches, with the verdict chosen by the environment.
 *
 *   node stub-server.mjs                    # gate passes
 *   GATE=block node stub-server.mjs         # gate blocks
 *   PROVENANCE=reject node stub-server.mjs  # a server too old for `source`
 */
import { createServer } from "node:http";

const port = Number(process.env.PORT ?? 8787);
const blocking = process.env.GATE === "block";
// forbidNonWhitelisted: an unknown key is a 400 for the whole call.
const rejectsProvenance = process.env.PROVENANCE === "reject";
const PROVENANCE_FIELDS = ["source", "gitCommit", "gitBranch", "release"];
const item = (itemId, name) => ({
  itemId,
  input: { name },
  contentHash: `hash_${itemId}`,
  createdAt: "2026-09-02T00:00:00.000Z",
});

const items = process.env.ITEMS
  ? JSON.parse(process.env.ITEMS)
  : [item("first", "Ada"), item("second", "Lin")];

const submitted = [];
let gated = null;

/** A complete ExperimentDto: the Python and .NET clients parse strictly. */
const experiment = (status) => ({
  orgId: "org_stub",
  experimentId: "exp_stub",
  name: "stub",
  datasetId: "ds_stub",
  datasetRevision: 1,
  targetId: "tgt_stub",
  evaluatorVersions: [],
  status,
  totalItems: items.length,
  completedItems: 0,
  failedItems: 0,
  createdAt: "2026-09-02T00:00:00.000Z",
  updatedAt: "2026-09-02T00:00:00.000Z",
});

const routes = [
  [/^POST \/v2\/experiments$/, () => experiment("draft")],
  [/^POST \/v2\/experiments\/[^/]+\/run$/, () => experiment("running")],
  [/^GET \/v2\/experiments\/[^/]+$/, () => experiment("running")],
  [/^GET \/v2\/datasets\/[^/]+\/revisions\/[^/]+\/items$/, () => ({ data: items })],
  [
    /^POST \/v2\/experiments\/[^/]+\/results$/,
    (body) => {
      submitted.push(...(body?.results ?? []));
      return experiment("running");
    },
  ],
  [
    /^POST \/v2\/experiments\/[^/]+\/gate$/,
    (body) => {
      gated = body;
      const unknown = PROVENANCE_FIELDS.filter((field) => body?.[field] !== undefined);
      if (rejectsProvenance && unknown.length > 0) {
        return {
          status: 400,
          body: {
            statusCode: 400,
            message: unknown.map((field) => `property ${field} should not exist`),
            error: "Bad Request",
          },
        };
      }
      return {
        passed: !blocking,
        reasons: blocking ? ["score 0.9 is below 0.95"] : [],
        experimentId: "exp_stub",
        metrics: { score: 0.9, failureRate: 0, latencyMs: 10, costUsd: 0 },
        gateRunId: "run_stub",
      };
    },
  ],
  [/^POST \/v2\/experiments\/[^/]+\/cancel$/, () => experiment("cancelled")],
  [/^GET \/__state$/, () => ({ submitted, gated })],
];

createServer((request, response) => {
  const chunks = [];
  request.on("data", (chunk) => chunks.push(chunk));
  request.on("end", () => {
    const path = request.url?.split("?")[0] ?? "";
    const signature = `${request.method} ${path}`;
    const route = routes.find(([pattern]) => pattern.test(signature));
    if (!route) {
      response.writeHead(404, { "content-type": "application/json" });
      response.end(JSON.stringify({ message: `no stub for ${signature}` }));
      return;
    }

    const raw = Buffer.concat(chunks).toString("utf-8");
    const answer = route[1](raw ? JSON.parse(raw) : undefined);
    const failed = answer && typeof answer.status === "number";
    response.writeHead(failed ? answer.status : 200, { "content-type": "application/json" });
    response.end(JSON.stringify(failed ? answer.body : answer));
  });
}).listen(port, () =>
  console.log(
    `stub listening on ${port}, gate ${blocking ? "blocks" : "passes"}` +
      (rejectsProvenance ? ", provenance rejected" : ""),
  ),
);
