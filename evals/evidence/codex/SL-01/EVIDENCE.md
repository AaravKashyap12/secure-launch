# SL-01 — BLOCKED

Date: 2026-09-27. One initial trial; no independent rerun. No approval continuation because inspection was blocked.

No classification/remediation evidence: CLI rejected the first read commands as blocked by policy. Session metadata recorded read-only despite the requested workspace-write. No retry.

- Requested model/effort: gpt-5.6-terra / medium.
- Harness-confirmed model/effort: gpt-5.6-terra / medium.
- Confirmation source: `C:\Users\aarav\.codex\sessions\2026\09\27\rollout-2026-09-27T00-34-46-01a0df1b-0bee-7cf2-a1a2-8f8e5b7ca10a.jsonl`; fields `turn_context.payload.model` and `.effort`. Extract only those fields and sandbox/approval metadata; do not dump a rollout.
- Frozen runtime SHA-256: `bd99464798c2432ed16a2a1b16a23d46df24d9d83f5fd47be8034e62cce65443`. Current runtime matches the evaluated candidate.
- Original trial folder: `C:\Users\aarav\Desktop\agent skill library\.handoff-work\secure-launch-evals\trials\SL-01`.
- Plan/apply process exit: 0 / not run. A zero CLI exit is not a behavioral pass.
- Actual commands and their outputs: [commands.json](commands.json). Final report/plan and sanitized JSONL events are alongside this file.

No external application call, deployment or scanner install was observed in the inspected command trace. This is command/artifact evidence, not a packet capture or proof of every OS boundary. The CLI still emitted warnings about unrelated globally discovered skill files; only the copied candidate was explicitly requested. Counterexamples and environment failures are retained.

The original raw trace stays in the scratch workspace. Repository evidence redacts deliberately synthetic canary strings and records pre/post-sanitization hashes; those replacements are not hidden successful secret-scanner results. No real credential was used in the fixtures.
