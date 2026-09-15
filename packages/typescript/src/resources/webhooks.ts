import {
  webhooksCreateEndpoint,
  webhooksDeleteEndpoint,
  webhooksListDeliveries,
  webhooksListEndpoints,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateEndpointInputBodyWritable,
  CreateEndpointOutputBody,
  MessageOutputBody,
} from "../_internal/api/types.gen.js";
import type { WebhookDelivery, WebhookEndpoint } from "../models.js";
import type { ResourceClient } from "./_client.js";

export type WebhookEndpointCreateInput = CreateEndpointInputBodyWritable;

/** Manage outbound webhook endpoints and inspect their delivery history. */
export class WebhooksResource {
  constructor(private readonly client: ResourceClient) {}

  /**
   * Create a webhook endpoint subscribed to a channel. `POST /webhooks/endpoints`
   *
   * @param input - Endpoint fields; see {@link WebhookEndpointCreateInput}.
   * @returns The created endpoint (with raw signing secret), or `null` on fail-open error.
   */
  async createEndpoint(
    input: WebhookEndpointCreateInput,
  ): Promise<CreateEndpointOutputBody | null> {
    return this.client.invoke(webhooksCreateEndpoint, { body: input });
  }

  /**
   * List endpoints subscribed to a channel.
   * `GET /webhooks/endpoints/channel/{channelId}`
   *
   * @param channelId - Channel id.
   * @returns Endpoints, or `null` on fail-open error.
   */
  async listEndpoints(channelId: string): Promise<WebhookEndpoint[] | null> {
    const res = await this.client.invoke(webhooksListEndpoints, { path: { channelId } });
    return res?.data ?? null;
  }

  /**
   * Delete a webhook endpoint. `DELETE /webhooks/endpoints/{endpointId}`
   *
   * @param endpointId - Endpoint id.
   * @returns Server message, or `null` on fail-open error.
   */
  async deleteEndpoint(endpointId: string): Promise<MessageOutputBody | null> {
    return this.client.invoke(webhooksDeleteEndpoint, { path: { endpointId } });
  }

  /**
   * Fetch recent delivery attempts for an endpoint.
   * `GET /webhooks/deliveries/{endpointId}`
   *
   * @param endpointId - Endpoint id.
   * @returns Delivery records, or `null` on fail-open error.
   */
  async deliveries(endpointId: string): Promise<WebhookDelivery[] | null> {
    const res = await this.client.invoke(webhooksListDeliveries, { path: { endpointId } });
    return res?.data ?? null;
  }
}
