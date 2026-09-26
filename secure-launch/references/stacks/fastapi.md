# FastAPI

Read date: 2026-09-27.

Read dependency-injected identity and tenant query scope. Derive tenant ownership from the verified subject, not a caller-supplied tenant header. Changes to auth/session semantics or schema remain ask-first. Only trust forwarded headers from enforced proxy peers.

Local proof: Use existing TestClient/ASGI fixtures and two fake identities; deny cross-tenant reads while retaining same-tenant access.

Sources: [S18](../sources.md#s18), [O03](../sources.md#o03), [O16](../sources.md#o16).
