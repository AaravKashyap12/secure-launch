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
