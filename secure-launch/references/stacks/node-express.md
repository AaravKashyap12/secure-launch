# Node / Express

Read date: 2026-09-27.

Inspect middleware order, body parsing and trust proxy before changes. Do not copy a trust-all proxy setting. Preserve raw request bytes before signature verification. Select an existing limiter or request permission for a new dependency; in-memory counters are not sufficient for multiple server instances.

Local proof: Run the project’s focused test command with a loopback HTTP server; check 429, headers, CORS and spoofed forwarding cases with a request cap.

Sources: [O18](../sources.md#o18), [P19](../sources.md#p19), [P15](../sources.md#p15), [O03](../sources.md#o03).
