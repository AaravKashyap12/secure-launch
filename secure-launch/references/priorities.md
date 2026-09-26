# A short launch list, with explicit exceptions

**Before launch:** include an applicable control here when the deployed surface can be misused on day one. Typical families: exposed server secrets/client bundles; signed-out/admin access; tenant checks; Supabase/Firebase rules; authentic and repeat-safe webhooks; auth, AI and public-write budgets; proxy identity; debug off; baseline headers/TLS; unsafe input, redirects or uploads; environment separation; bot-resistant forms; email-domain authentication; intended edge/origin protection.

Aim for 12–15 actionable groups in a typical SaaS plan. Combine overlapping controls, but retain their IDs, evidence and approvals. For example: (1) secrets/client boundary, (2) environment separation, (3) account/admin access, (4) tenancy/database rules, (5) session/CSRF boundaries, (6) public/auth budgets, (7) AI budget/tool boundaries if present, (8) trusted proxy/edge/TLS, (9) webhook/payment integrity, (10) debug/errors/baseline headers, (11) input/redirect/upload boundaries, (12) form automation resistance, (13) email sender authentication, (14) sensitive-data exposure decisions. Omit unused groups. Do not create risks merely to fill a quota.

**First week:** CSP monitoring followed by separately approved enforcement; routine log redaction; security contact/security.txt; CI action pinning; dependency update automation; normal dependency hygiene and operational recovery checks. Active secret leakage in logs, exploitable dependency code, or a CI path exposing publish/deploy privileges moves forward with a written reason.

**As you grow:** deeper ASVS L2 requirements, Kubernetes depth, SLSA provenance, GraphQL complexity and MCP transport depth. Promote specific checks if the project already exposes the relevant surface: an anonymously available costly GraphQL query or public unauthenticated MCP tool cannot wait merely because of its module default.

ASVS L1 informs the first applicable controls; L2 adds maturity and coverage, L3 is high-assurance specialist depth. Never assign an ASVS level from a risk adjective, label a subset compliant, or defer a reachable access-control defect because it appears in a deeper standard. Sources: S26, O03, O04, S20.

Priority is independent of approval: an urgent RLS/payment change still needs its item-specific approval. Keep unresolved Before-launch items visible; report conditional readiness, not an invented all-clear.
