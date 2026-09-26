# SL-03 — PARTIAL

Date: 2026-09-27. One initial trial; no independent rerun. One continuation of the same session after the real user approved the named fixture changes.

Approved source changes and direct route checks passed (401,400,200,429, separate-user 200); Next build failed with spawn EPERM. No fresh client bundle or served-header proof. No build retry. Summary initially grouped lockfile with launch gaps although table put it First week.

- Requested model/effort: gpt-5.6-terra / medium.
- Harness-confirmed model/effort: gpt-5.6-terra / medium.
- Confirmation source: `C:\Users\aarav\.codex\sessions\2026\09\27\rollout-2026-09-27T00-45-08-01a0df24-88ba-77e3-a54a-2714a7a538fa.jsonl`; fields `turn_context.payload.model` and `.effort`. Extract only those fields and sandbox/approval metadata; do not dump a rollout.
- Frozen runtime SHA-256: `bd99464798c2432ed16a2a1b16a23d46df24d9d83f5fd47be8034e62cce65443`. Current runtime matches the evaluated candidate.
- Original trial folder: `C:\Users\aarav\Desktop\agent skill library\.handoff-work\secure-launch-evals\trials\SL-03`.
- Plan/apply process exit: 0 / 0. A zero CLI exit is not a behavioral pass.
- Actual commands and their outputs: [commands.json](commands.json). Final report/plan and sanitized JSONL events are alongside this file.

No external application call, deployment or scanner install was observed in the inspected command trace. This is command/artifact evidence, not a packet capture or proof of every OS boundary. The CLI still emitted warnings about unrelated globally discovered skill files; only the copied candidate was explicitly requested. Counterexamples and environment failures are retained.

The original raw trace stays in the scratch workspace. Repository evidence redacts deliberately synthetic canary strings and records pre/post-sanitization hashes; those replacements are not hidden successful secret-scanner results. No real credential was used in the fixtures.

Owner correction: the successful direct-handler output has **eight** status lines, not the report’s “at most seven”: 401, 400, four 200s, 429, and a separate-user 200. The sequence stayed below the approved cap of 20.
