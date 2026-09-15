import { beforeEach, describe, expect, it, vi } from "vitest";
import * as ops from "../../_internal/api/sdk.gen.js";
import type { ResourceClient } from "../../resources/_client.js";
import { ChannelsResource } from "../../resources/channels.js";

vi.mock("../../_internal/api/sdk.gen.js", () => ({
  channelsCreate: vi.fn(),
  channelsDelete: vi.fn(),
  channelsGet: vi.fn(),
  channelsList: vi.fn(),
  channelsUpdate: vi.fn(),
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
      return op === ops.channelsList ? listResult : null;
    }),
  };
  return { client, calls };
}

beforeEach(() => {
  vi.clearAllMocks();
});

describe("ChannelsResource", () => {
  it("list(appId) invokes channelsList and unwraps the envelope", async () => {
    const { client, calls } = makeClient({ channels: [{ channelId: "c" }] });
    const res = await new ChannelsResource(client).list("app-1");
    expect(calls[0]?.op).toBe(ops.channelsList);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1" } });
    expect(res).toEqual([{ channelId: "c" }]);
  });

  it("get(appId, channelId) sends both path params", async () => {
    const { client, calls } = makeClient();
    await new ChannelsResource(client).get("app-1", "ch-id");
    expect(calls[0]?.op).toBe(ops.channelsGet);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1", channelId: "ch-id" } });
  });

  it("create(name, appId) packages path + body", async () => {
    const { client, calls } = makeClient();
    await new ChannelsResource(client).create("orders", "app-1");
    expect(calls[0]?.op).toBe(ops.channelsCreate);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1" }, body: { name: "orders" } });
  });

  it("update(appId, channelId, fields) sends path + body patch", async () => {
    const { client, calls } = makeClient();
    await new ChannelsResource(client).update("app-1", "ch", { name: "renamed" });
    expect(calls[0]?.op).toBe(ops.channelsUpdate);
    expect(calls[0]?.args).toEqual({
      path: { appId: "app-1", channelId: "ch" },
      body: { name: "renamed" },
    });
  });

  it("delete(appId, channelId) sends both path params", async () => {
    const { client, calls } = makeClient();
    await new ChannelsResource(client).delete("app-1", "ch");
    expect(calls[0]?.op).toBe(ops.channelsDelete);
    expect(calls[0]?.args).toEqual({ path: { appId: "app-1", channelId: "ch" } });
  });
});
