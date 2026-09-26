# Supply Chain

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## SC01 — Pin and constrain CI execution

- **Why:** A workflow dependency or pull-request title should not take control of CI.
- **Applies:** CI workflows.
- **Default priority:** First week.
- **Who / approval:** Agent file edits after plan; remote permissions user.
- **Implementation:** Review full SHA action references, untrusted PR inputs and least token permission.
- **Local verification:** Static workflow assertions; no real publish/deploy job run.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S21](../sources.md#s21), [P01](../sources.md#p01).
- **Exception:** a reachable untrusted-code path with publish/deploy credentials is Before launch; routine pinning otherwise stays First week.

## SC02 — Keep private packages tied to their registry

- **Why:** A public package with the same name should not replace a private dependency.
- **Applies:** Mixed private/public packages.
- **Default priority:** First week.
- **Who / approval:** Agent proposes; registry settings user.
- **Implementation:** Inspect package scope, resolver sources and lockfile integrity without reading tokens.
- **Local verification:** Offline configuration checks; never publish or probe a collision package.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P03](../sources.md#p03), [P01](../sources.md#p01).

## SC03 — Protect package publishing identities

- **Why:** Publishing access can change every downstream installation.
- **Applies:** Published packages or distributed tooling.
- **Default priority:** First week.
- **Who / approval:** User registry/dashboard; ask per CI identity change.
- **Implementation:** Use supported 2FA/trusted publisher workflows and minimal credentials.
- **Local verification:** Review local workflow contract; registry configuration remains unverified until user confirms.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P06](../sources.md#p06), [P07](../sources.md#p07), [S23](../sources.md#s23).

## SC04 — Trace released artifacts to their source

- **Why:** Traceable artifacts make unexpected changes easier to investigate.
- **Applies:** Distributed releases.
- **Default priority:** As you grow.
- **Who / approval:** Agent proposes; user publishes.
- **Implementation:** Record release provenance and integrity metadata where supported.
- **Local verification:** Verify local artifact digests/attestations if present; absence is not proof of malware.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S20](../sources.md#s20), [P01](../sources.md#p01), [P03](../sources.md#p03).
- **Escalate earlier only when exposed:** identify the reachable path and day-one consequence; merely finding a manifest is not enough.

## SC05 — Keep dependency updates arriving automatically

- **Why:** Regular small updates reduce avoidable dependency drift.
- **Applies:** Managed dependencies.
- **Default priority:** First week.
- **Who / approval:** Agent config after plan; user enables remote features.
- **Implementation:** Configure the detected ecosystem’s supported update service and review cadence. Preserve lockfile boundaries and script policy; do not auto-merge major or untested changes.
- **Local verification:** Parse update config and check paths against manifests; local patch/minor updates pass relevant checks. Scheduling remotely stays unverified.
- **Stack pointers:** use the detected stack via [stack index](../stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [N07](../sources.md#n07), [P03](../sources.md#p03), [S21](../sources.md#s21).
