# Privacy

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## PR01 — Collect and retain only needed personal data

- **Why:** Keeping less personal data reduces what must be protected and managed.
- **Applies:** Personal or sensitive data.
- **Default priority:** Before launch.
- **Who / approval:** User legal/data decisions; ask per schema item.
- **Implementation:** Inventory purpose, processors, retention and applicable rights; do not assume consent is always the basis.
- **Local verification:** Synthetic export/delete checks only after approved data-model scope.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S19](../sources.md#s19), [S24](../sources.md#s24), [O15](../sources.md#o15).

## I06 — Keep sensitive records out of logs

- **Why:** Diagnostics should remain useful without collecting confidential content.
- **Applies:** Logging/telemetry exists.
- **Default priority:** First week.
- **Who / approval:** Agent after plan.
- **Implementation:** Redact at logging boundaries and retain only useful diagnostic fields.
- **Local verification:** Synthetic markers absent from captured local logs; no live secrets logged.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O15](../sources.md#o15), [O14](../sources.md#o14).
- **Exception:** active secret or personal-data leakage is a Before-launch item; redact before collecting any evidence.
