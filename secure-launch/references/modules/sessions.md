# Sessions

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## A03 — Keep sessions scoped and revocable

- **Why:** Session scope and expiry limit how long stolen sessions remain useful.
- **Applies:** Session cookies or persistent login.
- **Default priority:** Before launch.
- **Who / approval:** Ask per semantic change.
- **Implementation:** Review cookie scope, flags, expiry and rotation without breaking expected login flows.
- **Local verification:** Inspect synthetic Set-Cookie flags and local logout/expiry behavior.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O08](../sources.md#o08), [S08](../sources.md#s08).

## W04 — Prevent cross-site state changes

- **Why:** A signed-in browser can otherwise submit an unwanted action from another site.
- **Applies:** Ambient browser credentials and write operations.
- **Default priority:** Before launch.
- **Who / approval:** Agent proposes; ask if session semantics change.
- **Implementation:** Use framework CSRF controls and appropriate cookie/Origin policy.
- **Local verification:** Missing/invalid CSRF proof fails; valid same-user request succeeds.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O11](../sources.md#o11), [O08](../sources.md#o08).
