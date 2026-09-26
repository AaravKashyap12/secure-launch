# Native Apps

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## M01 — Protect mobile storage and platform entry points

- **Why:** Mobile data and entry points need platform-specific boundaries.
- **Applies:** Native mobile app.
- **Default priority:** Before launch.
- **Who / approval:** Agent proposes; ask per permissions/auth item.
- **Implementation:** Select current MASVS/MASTG controls for local storage, links, IPC, permissions and network use.
- **Local verification:** Use available simulator/device fixtures; unavailable platform tests explicitly NOT RUN.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O05](../sources.md#o05), [O06](../sources.md#o06), [S24](../sources.md#s24), [S25](../sources.md#s25).

## D01 — Separate desktop content from OS privileges

- **Why:** Untrusted desktop content should not inherit operating-system privileges.
- **Applies:** Desktop app; Electron when detected.
- **Default priority:** Before launch.
- **Who / approval:** Ask per privilege/auth item.
- **Implementation:** Review sandbox/renderer isolation, IPC validation and navigation boundaries.
- **Local verification:** Local renderer cannot invoke an unapproved privileged operation.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S14](../sources.md#s14), [O10](../sources.md#o10).
