# Django

Read date: 2026-09-27.

Use documentation for the installed supported version. Inspect DEBUG, ALLOWED_HOSTS, security middleware and cookies; preserve framework CSRF controls. A production-settings check may touch external backends: review configuration and replace integrations first.

Local proof: Use the repo’s isolated test settings and local test client; inspect safe failure responses and applicable deployment checks without printing settings values.

Sources: [S17](../sources.md#s17), [O19](../sources.md#o19), [O08](../sources.md#o08).
