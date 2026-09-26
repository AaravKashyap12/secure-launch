# Payments

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## P01 — Verify incoming payment events

- **Why:** Only authentic provider events should change payment state.
- **Applies:** Payment webhooks.
- **Default priority:** Before launch.
- **Who / approval:** Ask per payment item.
- **Implementation:** Use provider SDK raw-body signature validation before side effects.
- **Local verification:** Local signed fixture accepted; altered body/signature rejected. No Stripe calls.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P15](../sources.md#p15), [O16](../sources.md#o16).

## P02 — Avoid processing the same payment twice

- **Why:** Retries should not create duplicate payment effects.
- **Applies:** Payment requests and event retries.
- **Default priority:** Before launch.
- **Who / approval:** Ask per payment/schema item.
- **Implementation:** Separate outgoing idempotency keys from incoming event deduplication.
- **Local verification:** Repeat local event/request fixture produces one intended effect.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S27](../sources.md#s27), [P15](../sources.md#p15).
