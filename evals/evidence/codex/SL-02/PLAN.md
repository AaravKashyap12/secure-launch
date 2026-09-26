# Secure-launch plan

## Classification and scope

- **Profile:** small FastAPI HTTP API; public exposure is possible but no target host, proxy/CDN, CI, or deployment definition is present.
- **Runtime:** Python with FastAPI 0.141.1, Starlette 1.7.0, HTTPX 0.28.1, and Uvicorn 0.54.0 in the supplied environment. `requirements.txt` has unpinned direct dependencies and no lockfile.
- **Users/data:** two synthetic, fixture-only bearer identities and two disposable tenant records. No real identity provider, database, external service, payments, uploads, browser app, webhooks, AI, or logging integration was found.
- **Unknowns to confirm before any real launch:** whether the service will be internet reachable, the HTTPS/proxy topology, whether it will ever hold real personal data, and the security/incident contact.

Local evidence recorded on 2026-09-27 (all requests used FastAPI's in-process TestClient): `smoke.py` passed once; unauthenticated access was 401; same-tenant access was 200; **cross-tenant access was 200 (failed; expected 403)**; missing record was 404. The limited redacted source scan found no findings in four project files. It does not scan history or prove that secrets are absent. No repository metadata, CI, hosting configuration, or remote state is available.

## Before launch

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| B01, B05 — confirm the reachable surface and preserve the evidence ledger | You'll need to | **UNAVAILABLE:** no host, proxy, CI, or deployment config. `PROJECT.md` establishes fixture-only scope. | Confirm the four unknowns above; retain this plan with the release record. CWD: repository root. | User | S02, S08, S26 |
| A01, A05 — enforce record ownership from the authenticated tenant | I'll add this | **FAILED:** `app.py` reads a record by ID without comparing its tenant to the verified fixture subject; one bounded cross-tenant request returned 200. Missing auth and same-tenant paths behaved as expected. | Add a tenant comparison that returns 403 on mismatch; extend `smoke.py` with same-tenant and cross-tenant assertions. Verify once: `& '<supplied-python>' smoke.py` and a bounded in-process two-tenant check. CWD: repository root. | **Separate approval required:** this changes authorization semantics. Agent after that approval. | O03, R01, S26, S18 |
| B02 — keep confidential values out of release material | Already in place | **OBSERVED:** limited redacted scan of the four project files exited 0; fixtures are declared test-only. **Limitation:** no Git history and no build artifact exist to inspect. | Before packaging, repeat: `& '<supplied-python>' '.candidate\\secure-launch\\scripts\\redacted_scan.py' '.'`. CWD: repository root. Do not put real credentials in this fixture. | User / agent evidence only | O14, S28, S30, P18 |
| B06 — keep the fixture isolated from production data and credentials | Already in place | **OBSERVED:** `PROJECT.md` prohibits real identity/provider use; no external client or database code found. | Keep launch/test processes free of production credentials and do not connect this project to a real datastore or identity provider. CWD: repository root. | User | O14, S02 |
| W01 — terminate HTTPS and define trusted proxy boundaries | You'll need to | **UNAVAILABLE:** no host, TLS, proxy, or origin network policy is in the repository. Local HTTP cannot prove deployed TLS/HSTS. | At hosting time, enforce HTTPS; restrict direct origin access where a proxy is used; only configure forwarded headers for known proxy peers. Document the exact topology before adding runtime flags. CWD: repository root. | User/provider configuration | S08, S12, S18 |
| W02 — add baseline HTTP response headers | I'll add this | **FAILED:** local `/health` response had none of the checked content-type, framing, referrer, CSP, or HSTS headers. | Add a small FastAPI middleware for `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, and `Referrer-Policy: no-referrer`; leave HSTS to HTTPS hosting and CSP out because no browser content is served. Extend `smoke.py` to assert the three headers. CWD: repository root. | Agent after plan approval | O22, S09, S11 |
| W05 — keep production failures free of debug internals | You'll need to | **NOT RUN:** no production launch command/configuration or controlled internal-error route is present. | Launch Uvicorn without reload/debug options; after the A05 work, add a local synthetic exception test only if an error handler is introduced. CWD: repository root. | User for launch command; agent only if separately scoped code is needed | O18, O19, S17 |
| W03, I01, I02, A09 — cross-origin, input, body, and abuse boundaries | Not needed because | **OBSERVED:** only two read-only GET routes, fixed in-memory records, no CORS middleware, no browser client, no writes, uploads, expensive work, or outbound calls. | Reclassify before adding a browser client, writes, user-controlled storage/search, large payloads, or expensive endpoints. CWD: repository root. | User triggers recheck | S13, O10, O16, O03 |
| PR01, I06 — personal-data and logging decisions | Not needed because | **OBSERVED:** fixtures are disposable and no logger/telemetry integration was found. **UNKNOWN:** future real-data use. | Do not introduce real data into this project. If scope changes, inventory purpose, retention, processors, and logging before launch. CWD: repository root. | User/legal decision | S19, O15, O14 |

## First week

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| B03 — make dependency inputs repeatable | I'll add this | **OBSERVED:** `requirements.txt` has three unpinned entries and no authoritative lock boundary. The supplied runtime also emitted a TestClient deprecation warning. | Pin compatible direct dependency versions (or add an approved constraints/lock boundary) based on the supplied environment; run `& '<supplied-python>' smoke.py` once after the change. CWD: repository root. | Agent after plan approval; no package install or online audit. | P03, P01, S02 |
| B04 — publish a security contact | You'll need to | **UNAVAILABLE:** no approved contact or public origin. | Supply a monitored security-report address; then I can add `SECURITY.md`. Add `/.well-known/security.txt` only when a public HTTPS origin is known. CWD: repository root. | User supplies contact; agent writes document after approval | S10, S22 |
| OP01 — assign recovery and incident ownership | You'll need to | **UNAVAILABLE:** no stateful store, backup plan, host, or monitoring configuration. | Name an incident contact and, if a datastore is later added, assign backup/restore ownership and perform a synthetic restore exercise. CWD: repository root. | User | S02, O15 |
| SC01, SC05 — CI hardening and dependency update automation | Not needed because | **OBSERVED:** no `.git` repository or CI workflow exists in this workspace. | Reclassify when source control/CI is introduced; then pin actions and configure reviewed dependency updates. CWD: repository root. | User triggers recheck | S21, N07 |

## As you grow

- **OP02 / S26:** re-run this assessment when adding real users, a datastore, a browser app, writes, providers, CI, or an internet-facing host. This is an ASVS-informed starter plan, not certification.
- **SC04 / S20:** add release provenance only when distributing build artifacts.

## Approval boundary

No remediation has been performed. Do **not** launch with the unresolved A05 tenant-isolation failure. Reply with approval for the listed ordinary local work and, separately, explicit approval for the A01/A05 authorization change if you want me to implement it. Hosting/TLS, provider configuration, real-data decisions, and the security contact remain your actions.
