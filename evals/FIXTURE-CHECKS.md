# Fixture setup checks — 2026-09-27

These verify that the deliberately vulnerable fixtures run. They are not secure-launch behavioral evaluations or remediation acceptance results.

| Fixture | Command in its scratch fixture-checks directory | Actual result |
| --- | --- | --- |
| Express | `node --test smoke.test.mjs` | Initial restricted run: spawn EPERM. One permission-corrected execution: 1 test passed, 0 failed, exit 0. |
| FastAPI | isolated venv Python, `smoke.py` | 1 test passed, exit 0. |
| Next.js | `node scripts/build.mjs` | Initial restricted run: spawn EPERM. One permission-corrected execution: compiled successfully; static / and /_not-found plus dynamic /api/chat; exit 0. |
| npm package | `node --test test.mjs` | Initial restricted run: spawn EPERM. One permission-corrected execution: 1 test passed, 0 failed, exit 0. |

Scratch root: `.handoff-work/secure-launch-evals/fixture-checks` in the skill-library workspace. Original restricted outputs are preserved there. Frameworks were installed separately with npm lifecycle scripts disabled, no npm audit, and no real provider integrations. See dependency-versions.json for versions read from installed package metadata. Next telemetry was disabled and the build used a noncredential canary. No behavioral case was rerun by these fixture checks.

Skill format: bundled quick_validate.py initially encountered a Windows cp1252 decode error; running it explicitly with Python UTF-8 mode returned `Skill is valid!`. Runtime links, canonical control paths and source-ID consistency passed. The pattern scanner detected a synthetic marker while keeping the matched value out of its output.

## 0.1.1 owner checks — 2026-09-27

These are the explicitly requested owner executions outside the actor sandbox against the **changed** SL-03/04 trial folders, not new actor trials. The historical PARTIAL outcomes remain unchanged. Each command below ran once. Raw output and working directories: [checks.json](evidence/owner-0.1.1/checks.json). Runner: `C:/Users/aarav/Desktop/agent skill library/.handoff-work/secure-launch-owner-checks.py`.

| Check | Command | Actual output / exit |
| --- | --- | --- |
| Scanner regression | `python -X utf8 evals/scanner-check.py` in secure-launch | PASS: 50 synthetic cases; all 5 rules fired; no generated values in output; exit 0 (internal scanner exit 1 expected). |
| Changed SL-03 build | `node scripts/build.mjs` in `.handoff-work/secure-launch-evals/trials/SL-03` | Next 16.3.6 compiled successfully; static `/` and `/_not-found`, dynamic `/api/chat`; exit 0. |
| Changed SL-03 client bundle grep | Python byte scan of fresh `.next/static` for the fixture canary and old public-key/header identifiers; see runner and checks.json | 21 files scanned; 0 matching files; exit 0. This proves bounded marker absence, not absence of all secrets or served-header behavior. |
| Changed SL-04 package | `node --test test.mjs` in `.handoff-work/secure-launch-evals/trials/SL-04` | 1 test passed, 0 failed; exit 0. |

Skill format command: `python -X utf8 C:/Users/aarav/.codex/skills/.system/skill-creator/scripts/quick_validate.py C:/Users/aarav/Desktop/secure-launch/secure-launch` returned `Skill is valid!`, exit 0. Local `validate_package.py` returned `PASS: 55 complete control records; 89 unique sources; runtime links; unpublished site-entry schema.`, exit 0. These ran in the patch session; no reviewer agent was used.
