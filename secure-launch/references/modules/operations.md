# Operations

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## OP01 — Plan recovery and watch for failed protections

- **Why:** A documented response and recovery path helps when something goes wrong.
- **Applies:** Stateful service or app operations.
- **Default priority:** First week.
- **Who / approval:** User operations; agent documented checks.
- **Implementation:** Assign incident contact, backup/restore responsibility and useful security-event monitoring.
- **Local verification:** Approved local restore exercise where available; distinguish plan from tested recovery.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S02](../sources.md#s02), [O15](../sources.md#o15).

## OP02 — Revisit sources and deeper assurance as the app grows

- **Why:** New features can make an earlier checklist incomplete.
- **Applies:** New integrations, data classes or scale.
- **Default priority:** As you grow.
- **Who / approval:** User selects depth; agent reclassifies.
- **Implementation:** Refresh source editions and module choices; escalate high-assurance work beyond this skill.
- **Local verification:** Changed project facts trigger new applicable checks; never re-use old passes as fresh evidence.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S02](../sources.md#s02), [S26](../sources.md#s26), [S20](../sources.md#s20).
