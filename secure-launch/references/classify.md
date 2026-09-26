# Read first, ask only what changes the plan

Start at the repository root and its governing instructions. Locate manifests and lockfile boundaries, runtime entry points, public/static build paths, server routes, auth middleware, data queries, admin features, uploads, webhooks, AI/model calls, email senders, CI workflows and infra manifests. Read only the relevant files. Do not dump `.env`, private keys, auth stores, token-bearing configs or runtime environment values. Use the redacted scanner and path-only Git inventory described in verification.

Record: project profiles; framework/runtime version from manifests; hosting/proxy topology from evidence; public/internal users; tenant model; personal/payment/health/children's data; browser versus server execution; external providers. A repo may have several profiles. A static frontend with a separate API needs both scopes identified, not assumptions about an unseen backend.

Evidence examples: Next.js routes and NEXT_PUBLIC_ references select web/client-secret checks; FastAPI plus tenant filters selects API/isolation checks; SKILL.md or MCP tool registration selects agent-tools; iOS/Android manifests select starter mobile checks. Publicly exposed health checks are not automatically unprotected admin routes. A documented publishable key is not a privileged secret.

Ask only missing material facts, such as whether real customer data will be stored, whether a listed host is the launch target, or whether only the proxy can reach the origin. Keep unanswered facts in the plan. Do not guess a database policy, production domain, email sender or CDN plan.

Sources: O01/O03/O04, S26, S28, P19; see sources.md. Protocol/application evidence overrides guesses from filenames.
