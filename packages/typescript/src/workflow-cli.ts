#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { resolveWorkflowBinary } from "./workflow.js";

const result = spawnSync(resolveWorkflowBinary(), process.argv.slice(2), { stdio: "inherit" });
if (result.error) throw result.error;
process.exitCode = result.status ?? 1;
