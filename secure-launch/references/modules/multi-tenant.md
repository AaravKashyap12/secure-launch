# Multi Tenant

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## A05 — Keep tenant and user records separated

- **Why:** One customer must not read or change another customer’s records.
- **Applies:** Multi-user or multi-tenant records.
- **Default priority:** Before launch.
- **Who / approval:** Ask if auth, schema or policy changes.
- **Implementation:** Derive tenant scope from verified identity and enforce on every read/write path.
- **Local verification:** Two seeded tenants: cross-tenant access denied, same-tenant access succeeds.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O03](../sources.md#o03), [R01](../sources.md#r01), [S26](../sources.md#s26).

## A06 — Protect Supabase tables, views and privileged access

- **Why:** Database policies protect browser-facing data even when a client calls the API directly.
- **Applies:** Supabase detected.
- **Default priority:** Before launch.
- **Who / approval:** Ask per database/policy item.
- **Implementation:** Review grants/RLS and elevated key paths; avoid broad replacement policies.
- **Local verification:** Local nonprivileged users cannot cross tenants; privileged bypass paths audited separately.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P08](../sources.md#p08), [S28](../sources.md#s28).

## A07 — Limit Firebase access to the intended users

- **Why:** Broad rules can expose records without going through the app interface.
- **Applies:** Firebase data/storage products detected.
- **Default priority:** Before launch.
- **Who / approval:** Ask per data-policy item.
- **Implementation:** Review product-specific rules and server SDK authorization.
- **Local verification:** Emulator tests deny anonymous and cross-user access while allowing intended access.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P09](../sources.md#p09), [S29](../sources.md#s29).
