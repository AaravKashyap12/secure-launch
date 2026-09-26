# Next.js / Vercel

Read date: 2026-09-27.

Read the installed Next version and router. Treat NEXT_PUBLIC_ and Vite-style public exports as public; move privileged credentials to server-only code and remove them from serialized props/responses. A proxy file alone is not endpoint authorization. Verify the actual local production build, including client chunks; mock model/payment calls. Provider preview protection is a user dashboard task.

Local proof: Inspect package.json scripts; run its declared build with synthetic env only; use local request tests and scan the generated client directory.

Sources: [S30](../sources.md#s30), [S32](../sources.md#s32), [O18](../sources.md#o18).
