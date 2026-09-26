# Secure-launch plan

## Project classification

Next.js 16.3.6 App Router browser application with one same-origin `POST /api/chat` route. It is a synthetic, authenticated-demo chat surface: the route returns a local mock reply and no model SDK, database, uploads, webhooks, payments, email, telemetry, CI, Git repository, lockfile, hosting configuration, or provider account was found. The browser sends fixed fixture identity markers and a synthetic browser marker; neither is a production secret or real authentication mechanism.

Observed files: `app/page.jsx`, `app/api/chat/route.js`, `scripts/build.mjs`, `next.config.mjs`, and `package.json`. Hosting, launch domain/proxy topology, intended users, real-data handling, and whether a hosted model will replace the mock are **UNKNOWN**.

Evidence performed: `python .candidate/secure-launch/scripts/redacted_scan.py .` from this directory exited 0: 7 files scanned, 0 pattern findings. This local fallback does not inspect history or prove absence. No build, server, network audit, deployment, or external request was run.

## Before launch

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| B01, B05 — confirm the deployed surface and data boundary | You'll need to | **OBSERVED:** only the mock chat route and browser page above. **UNKNOWN:** host, users, data, and real-model intent. | Record answers in `PLAN.md`; no command. cwd: repository root. | User confirms launch facts. | S02, S08, S26 |
| A01 — replace the fixture identity boundary before private or billable use | I'll add this | **FAILED:** `app/api/chat/route.js` accepts fixed fixture bearer markers; `app/page.jsx` exposes one. They are unsuitable for real access control. | Change `app/page.jsx`, `app/api/chat/route.js`; test signed-out denial and an authorized synthetic user with bounded loopback requests. cwd: repository root. | **Separate approval required:** authentication/session semantics. User chooses public-demo versus real authenticated users. | O03, O07, R01, S26 |
| B02, AI01 — keep provider credentials server-only | I'll add this (conditional) | **OBSERVED:** the only browser marker is deliberately synthetic and is injected by `scripts/build.mjs`; route does not use it. **NOT RUN:** fresh production bundle scan. | If a real provider is added, remove the client header/public env reference; use a server-only environment variable in `app/api/chat/route.js`; build using a synthetic canary and redacted artifact search. cwd: repository root. | Plan approval for local code; user provisions/rotates any real credential. | O04, O14, S28, S30 |
| AI02, A09, I02 — bound chat cost and request work | I'll add this | **FAILED:** no payload shape/size, timeout, concurrency, or per-user/request budget appears in `app/api/chat/route.js`. | Change `app/api/chat/route.js`; local mocked test sends at most 20 loopback requests, stopping at 429/cap; verify another identity remains usable. cwd: repository root. | Plan approval; depends on the selected auth/public-demo model. | O03, O04, P19 |
| I01, W05 — validate malformed requests and return safe errors | I'll add this | **FAILED:** `await request.json()` has no malformed-JSON handling or message schema; no explicit safe error path. | Change `app/api/chat/route.js`; loopback checks for malformed JSON, non-string/oversize messages, and a valid request. cwd: repository root. | Plan approval. | O10, O16, O18, S01 |
| W02 — set baseline browser headers | I'll add this | **FAILED:** `next.config.mjs` only disables `X-Powered-By`; no baseline header policy is defined. | Change `next.config.mjs`; build/start locally on `127.0.0.1`, then inspect response header names only. cwd: repository root. | Plan approval. CSP enforcement is reserved separately. | O22, S09, S11 |
| W01 — make HTTPS and origin exposure intentional | You'll need to | **UNAVAILABLE:** no host, proxy, CDN, domain, or TLS configuration is in the repository. | Provider-side checklist: terminate HTTPS, redirect HTTP at the edge, scope HSTS only after domain/subdomain review, and restrict origin reachability to the intended edge where available. No local command can prove this. | User/provider action. | O22, S08, S12 |
| B06 — separate launch configuration from fixtures | I'll add this | **OBSERVED:** build injects only a synthetic marker. **UNKNOWN:** launch environment design. | Add an environment-variable template/documentation that names server-only versus public values without values; verify no real endpoint/credential is used by local tests. cwd: repository root. | Plan approval; user creates/provider-manages real values. | O14, S02 |
| W03 — restrict browser origins | Not needed because | **OBSERVED:** the sole client call is relative (`/api/chat`) and no CORS policy/external browser client is present. | Reassess if a separate frontend, mobile app, or public API client is added. | None now. | O16, S13 |
| AI03, AI04 — treat model/retrieval/tool content as data and scope it | Not needed because | **OBSERVED:** reply is a fixed local string; no model, retrieval, connector, tool, tenant record, or side effect exists. | Reclassify before adding a real model, RAG, tools, or user data. | None now. | O04, S15, S16 |
| PR01 — decide personal-data scope and retention | You'll need to | **UNKNOWN:** no storage exists, but a launched chat can collect personal information once requests are retained or sent to a provider. | Document whether messages are stored, sent to a processor, or discarded; define purpose/retention before enabling either. | User/legal/data owner. | O15, S19 |

## First week

| ID(s) / item / why | Action status | Evidence + file | Proposed files / local command + cwd | Approval / owner | Sources |
| --- | --- | --- | --- | --- | --- |
| B03 — make dependency inputs repeatable | I'll add this | **FAILED:** `package.json` uses version ranges and no lockfile was found. **NOT RUN:** audit; it may share package metadata externally. | Create the authoritative npm lockfile without installing/updating packages; then run the package manager's offline/locked verification if available. cwd: repository root. | Plan approval. Advisory audit requires a specific metadata-sharing exception. | P01, P03, S02 |
| B04 — publish a private vulnerability contact | I'll add this | **FAILED:** no `SECURITY.md` exists. | Add `SECURITY.md` after user supplies a real contact; validate contact/expiry format locally. cwd: repository root. | User supplies contact; plan approval for file. | S10, S22 |
| W06 — introduce CSP carefully | I'll add this | **FAILED:** no CSP is defined. | Add a local `Content-Security-Policy-Report-Only` policy after resource-origin inventory; local synthetic violation plus page check. cwd: repository root. | Plan approval for Report-Only. **Separate approval required** for enforcement. | O22, S11 |
| I06, OP01 — logging and recovery when state/integrations exist | Not needed because | **OBSERVED:** no logging, persistence, external integration, or operational configuration is present. | Reassess with telemetry, message storage, or an external model/provider. | None now. | O15, S02 |

## As you grow

- OP02 — rerun this classification when adding real auth, model providers, stored chats, tools/RAG, a separate client, CI, or hosting/IaC. Existing results are historical.
- SC01–SC04 — no CI, registry publishing, private packages, or release pipeline was found; introduce CI pinning and dependency update automation when one is added.
- GraphQL, uploads, webhooks, payments, multi-tenancy, and MCP controls are not applicable to the current codebase and must be assessed before those features launch.

## Approval boundary

Approve this plan to authorize only the ordinary local changes marked “I'll add this.” It does **not** authorize the reserved authentication/session decision (A01), CSP enforcement, provider configuration, credential provisioning/rotation, DNS/TLS changes, deployment, or external/network checks.

Before I remediate, please answer these material launch facts: (1) will the chat remain a public mock, or will real users authenticate; (2) will a hosted model or message storage be enabled at launch; and (3) what hosting/proxy/domain will front the app (and can only that proxy reach the origin)?
