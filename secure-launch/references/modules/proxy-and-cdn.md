# Proxy And Cdn

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## I03 — Trust forwarded addresses only through known proxies

- **Why:** An attacker-supplied address must not become a fresh rate-limit identity.
- **Applies:** Reverse proxy/CDN detected.
- **Default priority:** Before launch.
- **Who / approval:** Agent app settings; ask for network/IaC.
- **Implementation:** Model the allowed hop chain; do not trust arbitrary X-Forwarded-For.
- **Local verification:** Direct spoofed header cannot evade local limiter; approved proxy path preserves identity.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P19](../sources.md#p19), [S18](../sources.md#s18).

## C05 — Put an appropriate edge proxy in front of public services

- **Why:** An edge service can handle transport and some abuse before requests reach the app.
- **Applies:** Internet-exposed HTTP service.
- **Default priority:** Before launch.
- **Who / approval:** User provider/DNS action; ask per infrastructure configuration.
- **Implementation:** Prefer the hosting platform’s existing TLS/CDN/abuse layer where suitable. Verify origin bypass protection and trusted proxy addresses; do not buy or add another CDN without need and approval.
- **Local verification:** Local config and topology review; user verifies TLS, origin reachability and protection in provider settings. Local checks cannot prove edge protection.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [N02](../sources.md#n02), [S12](../sources.md#s12), [P19](../sources.md#p19), [S32](../sources.md#s32).
