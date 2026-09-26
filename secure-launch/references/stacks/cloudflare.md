# Cloudflare / edge proxy

Read date: 2026-09-27.

Map proxy-to-origin reachability before trusting provider client-IP headers. Prefer existing TLS/abuse infrastructure. A Turnstile widget needs server validation; challenge secrets and dashboard setup stay with the user.

Local proof: Review config and local proxy mocks; test challenge failure/replay with a mock verifier. No DNS, dashboard or real Siteverify requests.

Sources: [S33](../sources.md#s33), [N01](../sources.md#n01), [N02](../sources.md#n02), [P19](../sources.md#p19).
