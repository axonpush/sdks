const DEFAULT_BASE_URL = "https://api.axonpush.xyz";

export interface GatewayOptions {
  apiKey: string;
  target?: string;
  app?: string;
  baseUrl?: string;
}

const root = (baseUrl?: string): string =>
  `${(baseUrl ?? DEFAULT_BASE_URL).replace(/\/+$/, "")}/gw`;

export const gatewayHeaders = (options: GatewayOptions): Record<string, string> => {
  const headers: Record<string, string> = { "x-axonpush-api-key": options.apiKey };
  if (options.target) headers["x-axonpush-target"] = options.target;
  if (options.app) headers["x-axonpush-app"] = options.app;
  return headers;
};

export const openaiGateway = (options: GatewayOptions) => ({
  baseURL: `${root(options.baseUrl)}/openai/v1`,
  defaultHeaders: gatewayHeaders({ target: "openai", ...options }),
});

export const anthropicGateway = (options: GatewayOptions) => ({
  baseURL: `${root(options.baseUrl)}/anthropic`,
  defaultHeaders: gatewayHeaders({ ...options, target: undefined }),
});
