import {
  channelsCreate,
  channelsDelete,
  channelsGet,
  channelsList,
  channelsUpdate,
} from "../_internal/api/sdk.gen.js";
import type { OkOutputBody } from "../_internal/api/types.gen.js";
import type { Channel } from "../models.js";
import type { ResourceClient } from "./_client.js";

/** Mutable channel fields accepted by {@link ChannelsResource.update}. */
export interface ChannelUpdateFields {
  name: string;
}

/**
 * Manage channels, the app-scoped fan-out unit that events and webhooks
 * hang off. All channel routes are nested under their parent app.
 */
export class ChannelsResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * List channels for an app. `GET /apps/{appId}/channels`
   *
   * @param appId - Parent app id.
   * @returns The channels, or `null` on fail-open error.
   */
  async list(appId: string): Promise<Channel[] | null> {
    const res = await this.client.invoke(channelsList, { path: { appId } });
    return res?.channels ?? null;
  }

  /**
   * Fetch a channel by id. `GET /apps/{appId}/channels/{channelId}`
   *
   * @param appId - Parent app id.
   * @param channelId - Channel id.
   * @returns The channel, or `null` on fail-open error.
   */
  async get(appId: string, channelId: string): Promise<Channel | null> {
    return this.client.invoke(channelsGet, { path: { appId, channelId } });
  }

  /**
   * Create a channel under the given app. `POST /apps/{appId}/channels`
   *
   * @param name - Human-readable channel name.
   * @param appId - Parent app id.
   * @returns The created channel, or `null` on fail-open error.
   */
  async create(name: string, appId: string): Promise<Channel | null> {
    return this.client.invoke(channelsCreate, { path: { appId }, body: { name } });
  }

  /**
   * Update mutable channel fields. `PUT /apps/{appId}/channels/{channelId}`
   *
   * @param appId - Parent app id.
   * @param channelId - Channel id.
   * @param fields - Patch object.
   * @returns The updated channel, or `null` on fail-open error.
   */
  async update(
    appId: string,
    channelId: string,
    fields: ChannelUpdateFields,
  ): Promise<Channel | null> {
    return this.client.invoke(channelsUpdate, { path: { appId, channelId }, body: fields });
  }

  /**
   * Delete a channel. `DELETE /apps/{appId}/channels/{channelId}`
   *
   * @param appId - Parent app id.
   * @param channelId - Channel id.
   * @returns Server ack, or `null` on fail-open error.
   */
  async delete(appId: string, channelId: string): Promise<OkOutputBody | null> {
    return this.client.invoke(channelsDelete, { path: { appId, channelId } });
  }
}
