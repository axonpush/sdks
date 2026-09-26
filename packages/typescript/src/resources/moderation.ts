import {
  moderationEfficacy,
  moderationRulesCreate,
  moderationRulesDelete,
  moderationRulesList,
  moderationViolationsList,
} from "../_internal/api/sdk.gen.js";
import type {
  CreateRuleInputBodyWritable,
  EfficacyOutputBody,
  ModerationEfficacyData,
  OkOutputBody,
  RuleDto,
  ViolationDto,
} from "../_internal/api/types.gen.js";
import type { ResourceClient } from "./_client.js";

export type ModerationRuleCreateInput = CreateRuleInputBodyWritable;
export type ModerationEfficacyParams = NonNullable<ModerationEfficacyData["query"]>;

/** Content-moderation rules and the violations they produce. */
export class ModerationResource {
  constructor(private readonly client: ResourceClient) {}

  /** List moderation rules. `GET /moderation/rules` */
  async listRules(): Promise<RuleDto[] | null> {
    const res = await this.client.invoke(moderationRulesList, {});
    return res?.rules ?? null;
  }

  /** Create a moderation rule. `POST /moderation/rules` */
  async createRule(input: ModerationRuleCreateInput): Promise<RuleDto | null> {
    return this.client.invoke(moderationRulesCreate, { body: input });
  }

  /** Delete a moderation rule. `DELETE /moderation/rules/{ruleId}` */
  async deleteRule(ruleId: string): Promise<OkOutputBody | null> {
    return this.client.invoke(moderationRulesDelete, { path: { ruleId } });
  }

  /** List recent violations. `GET /moderation/violations` */
  async listViolations(query: { limit?: number } = {}): Promise<ViolationDto[] | null> {
    const res = await this.client.invoke(moderationViolationsList, { query });
    return res?.violations ?? null;
  }

  /** Moderation efficacy over a window. `GET /moderation/efficacy` */
  async efficacy(query: ModerationEfficacyParams = {}): Promise<EfficacyOutputBody | null> {
    return this.client.invoke(moderationEfficacy, { query });
  }
}
