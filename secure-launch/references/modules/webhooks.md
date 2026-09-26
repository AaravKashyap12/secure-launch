# Webhooks

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## P03 — Authenticate other incoming webhooks

- **Why:** External events need a verifiable sender and bounded processing.
- **Applies:** Nonpayment webhooks.
- **Default priority:** Before launch.
- **Who / approval:** Agent after plan; new auth scheme ask-first.
- **Implementation:** Follow the provider signature/replay contract and validate payloads.
- **Local verification:** Forged and replayed local messages denied; valid message succeeds.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O16](../sources.md#o16), [O10](../sources.md#o10).
