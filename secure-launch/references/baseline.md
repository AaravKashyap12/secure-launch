# Baseline

Load only controls selected for actual project features. Defaults below follow the approved priority policy; a demonstrated day-one exposure can move a later item forward. Record why.

## B01 — Know what is exposed and what data is held

- **Why:** A short inventory keeps irrelevant advice out of the launch list.
- **Applies:** Every project.
- **Default priority:** Before launch.
- **Who / approval:** Agent proposes; user confirms unknowns.
- **Implementation:** Inspect manifests, entry points, CI and data paths without opening secret values.
- **Local verification:** Cite evidence for each selected profile and module; record unknowns.
- **Stack pointers:** use the detected stack via [stack index](stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S02](sources.md#s02), [S08](sources.md#s08), [S26](sources.md#s26).

## B02 — Keep confidential values out of shipped files

- **Why:** Privileged values in public files can grant access immediately.
- **Applies:** Build, source and release material.
- **Default priority:** Before launch.
- **Who / approval:** Agent redacted checks; user rotates.
- **Implementation:** Inspect references to credentials; allowlist placeholders and documented public keys.
- **Local verification:** Redacted local scan plus built-artifact check; no online key validation.
- **Stack pointers:** use the detected stack via [stack index](stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O14](sources.md#o14), [S28](sources.md#s28), [S30](sources.md#s30), [P18](sources.md#p18).

## B03 — Keep builds repeatable and dependencies understood

- **Why:** Repeatable inputs make updates and advisory findings easier to assess.
- **Applies:** Where dependencies/build tools exist.
- **Default priority:** First week.
- **Who / approval:** Agent after plan.
- **Implementation:** Identify authoritative package manager/lock boundary; inspect scripts before execution.
- **Local verification:** Locked build/audit where installed and permitted; absent tools stay NOT RUN.
- **Stack pointers:** use the detected stack via [stack index](stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [P03](sources.md#p03), [P01](sources.md#p01), [S02](sources.md#s02).

## B04 — Choose a clear security contact

- **Why:** A working contact lets people report a problem privately.
- **Applies:** Public distribution or reachable service.
- **Default priority:** First week.
- **Who / approval:** User supplies contact; agent writes.
- **Implementation:** Draft SECURITY.md; add security.txt for a web origin when relevant.
- **Local verification:** Check usable approved contact and expiry format; no live submission.
- **Stack pointers:** use the detected stack via [stack index](stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S10](sources.md#s10), [S22](sources.md#s22).

## B05 — Record what was checked and what remains

- **Why:** Clear evidence prevents an unchecked setting from looking finished.
- **Applies:** Every project.
- **Default priority:** Before launch.
- **Who / approval:** Agent.
- **Implementation:** Separate planned action from observed behavior and unavailable environment evidence.
- **Local verification:** Each claimed pass has command, exit result and bounded evidence.
- **Stack pointers:** use the detected stack via [stack index](stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [S02](sources.md#s02), [S26](sources.md#s26).

## B06 — Separate development from production data and credentials

- **Why:** A local test should never spend production money or change real users’ data.
- **Applies:** Multiple environments or deployed integrations.
- **Default priority:** Before launch.
- **Who / approval:** Agent config references after plan; user provisions/rotates.
- **Implementation:** Use separate environment identifiers and least-privilege credentials; fixtures use synthetic data and mocked services. Do not copy production databases, credentials or environment files.
- **Local verification:** Inspect variable names and config references; local tests cannot reach production endpoints and use only synthetic records.
- **Stack pointers:** use the detected stack via [stack index](stacks/README.md); turn the proof above into a specific command and working directory before approval.
- **Sources:** [O14](sources.md#o14), [S02](sources.md#s02).
