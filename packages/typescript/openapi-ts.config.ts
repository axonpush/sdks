import { defineConfig } from "@hey-api/openapi-ts";

/**
 * Codegen config for the AxonPush TypeScript SDK.
 *
 * Input is contract/openapi.sdk.json, mirrored in from the server and
 * committed, so codegen needs no running backend. The two NestJS-swagger
 * quirks the old tools/patch-spec.ts fixed are now fixed at the producer.
 */
export default defineConfig({
  input: "../../contract/openapi.sdk.json",
  output: {
    path: "./src/_internal/api",
  },
  plugins: [
    "@hey-api/typescript",
    "@hey-api/sdk",
    {
      name: "@hey-api/client-fetch",
      runtimeConfigPath: "./src/_internal/transport.ts",
    },
  ],
});
