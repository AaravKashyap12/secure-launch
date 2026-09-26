# Auth

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## A01 — Protect accounts and administrative actions

- **Why:** Knowing who signed in is different from checking what they may do.
- **Applies:** Private routes or management features.
- **Default priority:** Before launch.
- **Who / approval:** Ask per auth/session item.
- **Implementation:** Check server-side authentication plus role/resource authorization.
- **Local verification:** Signed-out request is denied; ordinary user cannot use admin action.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O07](../sources.md#o07), [O03](../sources.md#o03), [R01](../sources.md#r01), [S26](../sources.md#s26).

## A02 — Use appropriate password and recovery controls

- **Why:** Credential storage and recovery are common paths into accounts.
- **Applies:** Project owns password authentication.
- **Default priority:** Before launch.
- **Who / approval:** Ask per item.
- **Implementation:** Use current hash/policy guidance and bounded recovery flow; prefer maintained identity components.
- **Local verification:** Local policy/hash/recovery tests with fake accounts; no real-user resets.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S04](../sources.md#s04), [S05](../sources.md#s05), [O09](../sources.md#o09), [O07](../sources.md#o07).

## A04 — Bound login and recovery attempts

- **Why:** Repeated guesses and reset attempts should have a practical ceiling.
- **Applies:** Public auth endpoints.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan.
- **Implementation:** Apply endpoint/account-aware budgets without enabling trivial account lockout.
- **Local verification:** Bounded valid/invalid request sequence hits limit; unrelated local account can still authenticate.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O07](../sources.md#o07), [O03](../sources.md#o03), [P19](../sources.md#p19).

## A08 — Use the identity provider safely

- **Why:** A managed provider still needs the right application boundaries.
- **Applies:** Managed auth detected.
- **Default priority:** Before launch.
- **Who / approval:** User dashboard; ask per code item.
- **Implementation:** Read the actual provider/version docs for redirect, token and session settings.
- **Local verification:** Local token/redirect mocks; dashboard configuration remains unverified.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O07](../sources.md#o07), [S04](../sources.md#s04), [S34](../sources.md#s34).

## A09 — Limit public and write-endpoint abuse

- **Why:** Public actions can consume resources even without a login.
- **Applies:** Sign-up, contact, reset, API-key issuance or public writes.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; auth semantics require separate approval.
- **Implementation:** Set endpoint-specific network/user/API-client budgets, payload limits and timeouts; identify API clients without logging credential values. Preserve legitimate retries and webhooks.
- **Local verification:** A bounded local sequence reaches 429; a different permitted identity still works and spoofed forwarding headers cannot reset the budget.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O03](../sources.md#o03), [O07](../sources.md#o07), [P19](../sources.md#p19), [S18](../sources.md#s18).

## A10 — Make automated sign-up and form abuse harder

- **Why:** Forms and sign-up routes should not become spam or resource-amplification tools.
- **Applies:** Public sign-up, contact or costly forms.
- **Default priority:** Before launch.
- **Who / approval:** Agent existing local controls after plan; user enables new provider.
- **Implementation:** Combine endpoint limits with appropriate anti-automation controls. If a challenge provider is chosen, ask before adding the service and validate its result server-side before any side effect.
- **Local verification:** Mock accepted, rejected, expired and replayed challenge responses; rejected submissions send no email or create no account. No live challenge calls.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [N01](../sources.md#n01), [O07](../sources.md#o07), [O03](../sources.md#o03).

## I08 — Keep redirects on approved destinations

- **Why:** A trusted application link should not send someone to an unapproved destination.
- **Applies:** Return URLs, sign-in redirects or forwarding endpoints.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; auth-flow changes ask-first.
- **Implementation:** Use fixed destination IDs or allowlisted parsed URLs. Reject scheme-relative and encoded bypasses; preserve valid application-relative navigation.
- **Local verification:** Local benign redirect succeeds; external, //host and encoded attacker destinations cannot become Location targets.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [N03](../sources.md#n03), [O10](../sources.md#o10).
