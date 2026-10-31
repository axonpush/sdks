import { createServer, type Server } from "node:http";
import { afterAll, beforeAll, expect, it } from "vitest";
import { getHealthz } from "../_internal/api/index.js";
import { Transport } from "../_internal/transport.js";
import { resolveSettings } from "../config.js";

let origin: Server;
let destination: Server;
let baseUrl: string;
let destinationUrl: string;
let status = 302;
let destinationRequests = 0;

async function listen(server: Server): Promise<string> {
  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  const address = server.address();
  if (!address || typeof address === "string") throw new Error("missing listener address");
  return `http://127.0.0.1:${address.port}`;
}

beforeAll(async () => {
  destination = createServer((_request, response) => {
    destinationRequests++;
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end('{"status":"ok"}');
  });
  destinationUrl = await listen(destination);
  origin = createServer((_request, response) => {
    response.writeHead(status, { Location: `${destinationUrl}/stolen` });
    response.end();
  });
  baseUrl = await listen(origin);
});

afterAll(async () => {
  await Promise.all(
    [origin, destination].map(
      (server) =>
        new Promise<void>((resolve, reject) => {
          server.close((error) => (error ? reject(error) : resolve()));
          server.closeAllConnections();
        }),
    ),
  );
});

it.each([301, 302, 303, 307, 308])(
  "never forwards SDK credentials across HTTP %i redirects",
  async (redirect) => {
    status = redirect;
    destinationRequests = 0;
    for (const apiKey of ["ak_synthetic", "pt_synthetic"]) {
      const transport = new Transport(
        resolveSettings({ apiKey, baseUrl, failOpen: false, maxRetries: 2 }),
      );
      await expect(transport.invoke(getHealthz, { redirect: "follow" })).rejects.toBeDefined();
    }
    expect(destinationRequests).toBe(0);
  },
);
