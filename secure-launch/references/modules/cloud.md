# Cloud

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## C01 — Make storage exposure deliberate

- **Why:** Private files should stay private even when their URLs are guessed.
- **Applies:** Cloud/object storage detected.
- **Default priority:** Before launch.
- **Who / approval:** User dashboard; ask per IaC item.
- **Implementation:** Separate intended public assets from private objects, policies and signed access.
- **Local verification:** Local config/policy tests; actual bucket state remains user-owned/unverified.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S31](../sources.md#s31), [P13](../sources.md#p13), [O01](../sources.md#o01).

## C02 — Protect preview and management surfaces

- **Why:** Preview and management surfaces may expose unfinished or internal functions.
- **Applies:** Hosted previews/admin consoles.
- **Default priority:** Before launch.
- **Who / approval:** User provider settings.
- **Implementation:** Select Vercel/Netlify/Cloudflare/AWS controls only for the detected host.
- **Local verification:** Read config evidence and provide exact user verification steps; no remote probes.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S32](../sources.md#s32), [S33](../sources.md#s33), [P11](../sources.md#p11), [P13](../sources.md#p13).

## C06 — Authenticate the domain used to send email

- **Why:** Receivers need a way to recognize mail sent for your domain.
- **Applies:** Application sends email from a custom domain.
- **Default priority:** Before launch.
- **Who / approval:** User DNS and mail provider actions.
- **Implementation:** Identify actual senders and existing records; propose SPF, provider-issued DKIM and staged DMARC alignment. Never invent DNS values or access signing keys; avoid duplicate SPF records or premature rejection.
- **Local verification:** User supplies redacted provider verification and a synthetic message’s authentication result. Agent does not change DNS or send email.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [N04](../sources.md#n04), [N05](../sources.md#n05), [N06](../sources.md#n06).
