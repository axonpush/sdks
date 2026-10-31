/**
 * Shared environment loader for the AxonPush SDK examples.
 *
 * The examples expect the standard `AXONPUSH_*` environment variables
 * resolved by `new AxonPush()` itself, plus a couple of extras that the
 * facade does not consume directly (channel id, etc.).
 *
 * Set what you need, then run any example with `bun run examples/<file>.ts`.
 */

export function requireEnv(name: string): string {
  const v = process.env[name];
  if (!v) {
    throw new Error(
      `Missing required env var ${name}. Set it in your shell or a .env file before running the examples.`,
    );
  }
  return v;
}

export const CHANNEL_ID = process.env.AXONPUSH_CHANNEL_ID ?? "";

export async function tryImport<T>(spec: string): Promise<T | null> {
  try {
    return (await import(spec)) as T;
  } catch {
    return null;
  }
}
