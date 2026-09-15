import { beforeEach, describe, expect, it, vi } from "vitest";
import * as ops from "../../_internal/api/sdk.gen.js";
import type { ResourceClient } from "../../resources/_client.js";
import { AppsResource } from "../../resources/apps.js";

vi.mock("../../_internal/api/sdk.gen.js", () => ({
  appsCreate: vi.fn(),
  appsDelete: vi.fn(),
  appsGet: vi.fn(),
  appsList: vi.fn(),
  appsUpdate: vi.fn(),
}));

interface InvokeCall {
  op: unknown;
  args: unknown;
}

function makeClient(listResult: unknown = null): {
  client: ResourceClient;
  calls: InvokeCall[];
} {
  const calls: InvokeCall[] = [];
  const client: ResourceClient = {
    environment: undefined,
    getOrCreateTrace: vi.fn(),
    invoke: vi.fn().mockImplementation(async (op, args) => {
      calls.push({ op, args });
      return op === ops.appsList ? listResult : null;
    }),
  };
  return { client, calls };
}

beforeEach(() => {
  vi.clearAllMocks();
});

describe("AppsResource", () => {
  it("list() invokes appsList and unwraps the envelope", async () => {
    const { client, calls } = makeClient({ apps: [{ appId: "a" }] });
    const res = await new AppsResource(client).list();
    expect(calls[0]?.op).toBe(ops.appsList);
    expect(calls[0]?.args).toEqual({});
    expect(res).toEqual([{ appId: "a" }]);
  });

  it("get(id) sends appId in the path", async () => {
    const { client, calls } = makeClient();
    await new AppsResource(client).get("app-1");
    expect(calls[0]?.op).toBe(ops.appsGet);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1" } });
  });

  it("create(name) packages a body", async () => {
    const { client, calls } = makeClient();
    await new AppsResource(client).create("checkout");
    expect(calls[0]?.op).toBe(ops.appsCreate);
    expect(calls[0]?.args).toEqual({ body: { name: "checkout" } });
  });

  it("update(id, name) sends a path + body", async () => {
    const { client, calls } = makeClient();
    await new AppsResource(client).update("app-1", "renamed");
    expect(calls[0]?.op).toBe(ops.appsUpdate);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1" }, body: { name: "renamed" } });
  });

  it("delete(id) sends only a path arg", async () => {
    const { client, calls } = makeClient();
    await new AppsResource(client).delete("app-1");
    expect(calls[0]?.op).toBe(ops.appsDelete);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1" } });
  });
});
